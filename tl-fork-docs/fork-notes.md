# Notes on Tim Littlefair's fork of alesisysysex

## Background to this fork

I have forked this project from @tmick0's original GitHub project.

As at the time of writing (July 2026), the original repository had
been forked 8 times before I created this fork:

![tree view of forks](./alesisvsysex-forks-as-at-260718.png)

My (initial) personal motivation for adding yet a further fork is to 
see if I can add support for the Alesis V61 (original, not mkII) keyboard
which I own.

Before working on the changes I want for my own sake, I merged the 
following features implemented in prior forks on top of the latest 
commit in @tmick0's repo:

* work in the forks created by @Baggypants and @abridgewater to add 
  support for the following models:
  + VMini added by @Baggypants
  + VI49 and (possibly?) VI61 added by @abridgewater
  + VI25 added by @wimcoelus

This work is merged in a branch named wimcoelus-master as wimcoelus's
fork supporting the VI25 includes all commits in the prior forks from 
@Baggypants and @abridgewater.

I've looked at the commits in the other forks belonging to @alextld, 
@bennylangston, @ColdyESP, @nicolalandro and @pgaudillere.  For the 
moment I don't see anything in any of these which looks of immediate 
value to merge, but I'd be happy to merge future work from any of 
those contributors if they are prepared to rebase against the tip of 
my repo.

In the event that I am able to successfully add support for my V61 
model, I will try to generate a useable pull request for consumption
by @tmick0 should he choose to accept it and bring support for the
widest range of devices possible back to the root of the tree 
of forks.

I may also consider whether it is possible to continue and add 
support for the Akai MPK Mini (original) model, as I own this, and 
the excellent reverse engineering documentation generated and linked
by earlier contributors to this tree of forks would appear to make
this extension beyond the Alesis brand feasible. 

## Random useful pages:

https://github.com/tmick0/alesisvsysex/issues/2
https://lo.calho.st/posts/alesis-v-config-gui/
https://lo.calho.st/posts/reverse-engineering-sysex/
https://github.com/tmick0/alesisvsysex/issues/6
https://www.untergeek.de/2014/11/taming-arturias-beatstep-sysex-codes-for-programming-via-ipad/
https://github.com/tsmetana/mpk3-settings
https://github.com/tsmetana/mpk3-settings/issues/21


https://support.spectrasonics.net/manual/Omnisphere3HW/3/en/topic/setting-up-the-v61-mk1
https://support.spectrasonics.net/manual/Omnisphere3HW/3/en/topic/setting-up-the-mpk-mini-mk1

https://www.akaipro.com/downloads-and-support/downloads/?legacy=true
NB: The material related to MPK Mini original version is titled "MPK MINI CLASSIC"
and the associated product picture does not look at all like my MPK mini.  
The Quickstart user manual in this section does contain a picture which looks 
like my model and the software works with it.





