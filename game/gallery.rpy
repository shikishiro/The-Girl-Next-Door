#########Gallery#########


init python:

    g = Gallery()

    #Room
    g.button("roomdark")
    g.image("roomdark")
    g.condition("persistent.unlock_roomdark")
    g.image("roomlight")
    g.condition("persistent.unlock_roomlight")

    #Outside
    g.button("outside_m")
    g.image("outside_m")
    g.condition("persistent.unlock_outside_m")

    #Classroom
    g.button("c_day")
    g.image("c_day")
    g.condition("persistent.unlock_c_day")
    
    #transition
    g.transition = dissolve

screen gallery:

    #style_prefix "gallery"

    tag menu

    use game_menu("Gallery"):

        grid 3 2:

            xfill True
            yfill True

            spacing 0.5

            add g.make_button("roomdark", "images/bg/room_dark_button.png", xalign=0.5, yalign=0.5, locked="images/bg/button_locked.png")
            add g.make_button("outside_m", "images/bg/outside_morning_button.png", xalign=0.5, yalign=0.5, locked="images/bg/button_locked.png")
            add g.make_button("c_day", "images/bg/c_day_button.png", xalign=0.5, yalign=0.5, locked="images/bg/button_locked.png")

            add g.make_button("roomdark", "images/bg/room_dark_button.png", xalign=0.5, yalign=0.5, locked="images/bg/button_locked.png")
            add g.make_button("outside_m", "images/bg/outside_morning_button.png", xalign=0.5, yalign=0.5, locked="images/bg/button_locked.png")
            add g.make_button("c_day", "images/bg/c_day_button.png", xalign=0.5, yalign=0.5, locked="images/bg/button_locked.png")
            

        hbox:
            align (0.5, 0.0)
            spacing 50
            textbutton "Gallery" action ShowMenu("gallery") xalign 0.3 yalign 1
            textbutton "Music" action ShowMenu("music_room") xalign 0.5 yalign 1
            textbutton "H-Scene" action Return() xalign 0.7 yalign 1

# style gallery_button_text is gui_button
# style gallery_text is gui_button_text

# style gallery_button_text is gui_button_text:
#     font "gui/fonts/Spring Holiday.ttf"
#     size gui.title_text_size
#     color gui.accent_color
#     yalign 0.5

#########Music Room#########
#########
init python:
    
    mr = MusicRoom(fadeout=1.0)

    mr.add("audio/continue-life-by-kevin-macleod-from-filmmusic-io.mp3", always_unlocked=True)

screen music_room:

    #style_prefix "music"

    tag menu

    use game_menu("Music"):
        vbox:
            hbox:
                box_wrap True
                vbox:

                    null height 50

                    textbutton "Sunshine and Sleep"
                    textbutton "The Girl and the Bear"
                    textbutton "Flightless Bird"
                    textbutton "Continued Life" action mr.Play("audio/continue-life-by-kevin-macleod-from-filmmusic-io.mp3")
                    textbutton "The Girl's resolved"

                vbox:

                    null height 50

                    textbutton "Flames of Resolution"
                    textbutton "The boss of the family"
                    textbutton "Clearing the hedge"
                    textbutton "The Girl"
                    textbutton "The Girl Next Door"
        hbox:

            align (0.5, 0.5)
            spacing 50
            textbutton "Next" action mr.Next()
            textbutton "Stop" action mr.Stop()
            textbutton "Previous" action mr.Previous()

        hbox:

            align (0.5, 0.0)
            spacing 50
            textbutton "Gallery" action ShowMenu("gallery") xalign 0.3 yalign 1
            textbutton "Music" action ShowMenu("music_room") xalign 0.5 yalign 1
            textbutton "H-Scene" action Return() xalign 0.7 yalign 1

    on "replace" action mr.Stop()

    on "replaced" action mr.Play(audio.menu1)

# style music_button_text is gui_button
# style music_text is gui_button_text

# style music_button_text is gui_button_text:
#     font "gui/fonts/Spring Holiday.ttf"
#     size gui.title_text_size
#     color gui.accent_color
#     yalign 0.5

# Conditions

default persistent.unlock_roomdark = False
default persistent.unlock_roomlight = False
default persistent.unlock_outside_m = False
default persistent.unlock_c_day = False
