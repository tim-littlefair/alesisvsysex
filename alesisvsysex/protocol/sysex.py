from .model import AlesisV

__all__ = ['SysexMessage']

class SysexMessage (object):
    
    _TYPES = {
        'update': [0x61],
        'query':  [0x62],
        'reply':  [0x63]
    }
    
    # 0xff at last byte of _HEADER_START is a placeholder for the product id
    _HEADER_START = [0x00, 0x00, 0x0e, 0x00, 0xff] 
    _HEADER_END   = [0x00, 0x5d]
    
    _START_BYTE = [0xf0]
    _END_BYTE   = [0xf7]
    
    def __init__(self, msg_type, product_id, model=None):
        self.type       = msg_type
        self.product_id = product_id
        self.model      = model
    
    def serialize(self):
        product_header_start = self._HEADER_START
        product_header_start[4] = self.product_id
        if self.type == 'query':
            return bytes(self._START_BYTE + product_header_start + self._TYPES[self.type]
                         + self._HEADER_END + self._END_BYTE)
        else:
            return bytes(self._START_BYTE + product_header_start + self._TYPES[self.type]
                         + self._HEADER_END) + self.model.serialize() + bytes(self._END_BYTE)
                     
        
    @classmethod
    def deserialize(cls, b):
        i = 0
        
        start_byte = b[i : i+1]
        if start_byte != bytes(cls._START_BYTE):
            raise ValueError("Invalid start byte '0x%02x'" % start_byte[0])
        i += 1
        
        header_start = b[i : i + len(cls._HEADER_START)]
        if header_start != bytes(cls._HEADER_START):
            raise ValueError("Invalid message header")
        product_id = header_start[4]
        i += len(cls._HEADER_START)
        
        t = b[i : i + 1]
        for k, v in cls._TYPES.items():
            if t == bytes(v):
                msg_type = k
                break
        else:
            raise ValueError("Unknown message type '0x%02x'" % t[0])
        i += 1
        
        header_end = b[i : i + len(cls._HEADER_END)]
        if header_end != bytes(cls._HEADER_END):
            raise ValueError("Invalid message header")
        i += len(cls._HEADER_END)
        
        if msg_type == "query":
            model = None
        else:
            model = AlesisV.deserialize(b[i : i + AlesisV.num_bytes()])
            i += AlesisV.num_bytes()
        
        end_byte = b[i : i+1]
        if end_byte != bytes(cls._END_BYTE):
            raise ValueError("Invalid end byte '0x%02x'" % end_byte[0])
        i += 1
        
        return SysexMessage(msg_type, product_id, model)
    
    @classmethod
    def num_bytes(cls, msg_type):
        if msg_type == 'query':
            return (len(cls._START_BYTE) + len(cls._HEADER_START) + 1
                    + len(cls._HEADER_END) + len(cls._END_BYTE))
        else:
            return (len(cls._START_BYTE) + len(cls._HEADER_START) + 1
                    + len(cls._HEADER_END) + AlesisV.num_bytes()
                    + len(cls._END_BYTE))
        
