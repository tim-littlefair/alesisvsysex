import mido
from alesisvsysex.protocol.sysex import SysexMessage

__all__ = ['AlesisDevice']

class AlesisDevice (object):
    
    
    @staticmethod 
    def device_factory():
        _PRODUCT_PREFIXES_AND_IDS = {
            "V25:": 0x41,
            "V49:": 0x42,
            "V61:": 0x43
        }
        ioport_names = mido.get_ioport_names()
        for product_prefix in _PRODUCT_PREFIXES_AND_IDS:
            ioports_for_product = [
                n for n in ioport_names if n.startswith(product_prefix)
            ]
            if len(ioports_for_product)>0:
                # if multiple matching port names are found 
                # (e.g for V61 at least)
                # we expect that the editor port will be last
                # in the sequence
                return AlesisDevice(
                    ioports_for_product[-1], 
                    _PRODUCT_PREFIXES_AND_IDS[product_prefix]
                )
        # If we get here, no supported port names were found
        target_prefix_list = "','".join(_PRODUCT_PREFIXES_AND_IDS.keys())
        raise RuntimeError("Could not find a port with prefix in '%s'" % target_prefix_list)

    def __init__(self, ioport_name, product_id):
        self.ioport_name = ioport_name
        self.product_id = product_id
        self._port = mido.open_ioport(self.ioport_name)
    
    def __del__(self):
        try:
            self._port.close()
        except:
            pass

    def _send(self, message):
        if not isinstance(message, SysexMessage):
            raise ValueError("Can only send a SysexMessage")
        p = mido.Parser()
        p.feed(message.serialize())
        self._port.send(p.get_message())

    def _recv(self):
        while True:
            r = self._port.receive()
            if r.type == 'sysex':
                break
        return SysexMessage.deserialize(r.bin())

    def get_config(self):
        self._send(SysexMessage('query', self.product_id))
        return self._recv().model
    
    def set_config(self, model):
        model_bin = model.serialize()
        self._send(SysexMessage('update', self.product_id, model))
        if self.get_config().serialize() != model_bin:
            raise RuntimeError('Failed to update configuration')

