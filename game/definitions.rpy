## All Definition goes here

## Image Files ##

## Seika

#Placeholders
image seika nml1 = "images/seika/001.png"
image seika nml2 = "images/seika/002.png"
image seika narm1 = "images/seika/003.png"
image seika narm2 = "images/seika/004.png"
image seika ahh1 = "images/seika/005.png"
image seika smug1 = "images/seika/006.png"
image seika smug2 = "images/seika/007.png"
image seika smug3 = "images/seika/008.png"
image seika sad1 = "images/seika/009.png"
image seika sad2 = "images/seika/010.png"
image seika sad3 = "images/seika/011.png"
image seika cry1 = "images/seika/012.png"
image seika cry2 = "images/seika/013.png"
image seika cry3 = "images/seika/014.png"
image seika grr1 = "images/seika/015.png"
image seika grr2 = "images/seika/016.png"
image seika grr3 = "images/seika/017.png"
image seika grr4 = "images/seika/018.png"
image seika yan1 = "images/seika/019.png"
image seika yan2 = "images/seika/020.png"
image seika yan3 = "images/seika/021.png"
image seika yan4 = "images/seika/022.png"
image seika yan5 = "images/seika/023.png"
image seika yan6 = "images/seika/024.png"

## Alice

##Placeholder
image alice nml1 = "images/alice/001.png"
image alice hap1 = "images/alice/002.png"
image alice hap2 = "images/alice/003.png"
image alice sad1 = "images/alice/004.png"
image alice cfs1 = "images/alice/005.png"


## Iris

##Placeholder
image iris nml1 = "images/iris/001.png"
image iris nml2 = "images/iris/002.png"
image iris hap1 = "images/iris/003.png"
image iris hap2 = "images/iris/004.png"

## Backgrounds ##

image roomdark = "images/bg/room_dark.png"
image roomlight = "images/bg/room_light.png"
image outside_m = "images/bg/outside_morning.png"
image c_day = "images/bg/classroom_day.png"
image corridor_d = "images/bg/corridor_morning.png"
image council_d = "images/bg/council_day.png"

## Main Characters ##

define mc = Character("[player]")
define u = Character("???")
define s = Character("Seika")
define a = Character("Alice")
define i = Character("Iris")

## Minor Characters ##

define t = Character("Teacher")
define b2 = Character("Both")
define sc = Character("Secretary")
define vp = Character("Vice President")
define n = Character("Nurse")
define m1 = Character("Member 1")
define m2 = Character("Member 2")
define m3 = Character("Member 3")
define m4 = Character("Member 4")
define amem = Character("All")

## Music ##

## BGM Placeholder ##

define audio.menu1 = "audio/continue-life-by-kevin-macleod-from-filmmusic-io.mp3"

## Sound Effects ##

define audio.m1 = "<loop 1.000>audio/sfx/morning_1.mp3"
define audio.bb1 = "audio/sfx/baseball_1.mp3"
define audio.whoosh = "audio/sfx/whoosh.mp3"
define audio.body1 = "audio/sfx/body_1.mp3"

## All append/remove ##

init:

    # Hide Windows
    $ config.keymap['hide_windows'].append('mouseup_3')
    $ config.keymap['hide_windows'].remove('mouseup_2')
    $ config.keymap['hide_windows'].remove('h')

    # Disable Game Menu
    $ config.keymap['game_menu'].remove('mouseup_3')

    # Disable Scrolls
    $ config.keymap['rollback'].remove('mousedown_4')
    $ config.keymap['rollforward'].remove('mousedown_5')

    # Disable Skips
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['toggle_skip'].remove('K_TAB')

## Persistent Data ##

default persistent.playername = ""
default player = persistent.playername

## Controller ##
define config.mouse =  None
default allow_skipping = True
