init python:
    menu_trans_time = 1
    company_name = "White Celebration Presents..."
    splash_message_default = [
    "This game contains themes that is not suitable for young audiences",
    "This game contains sensitive themes and mature content",
    "This game contains theme that is only suitable to Adult Audiences.\n Viewer's discretion is highly advice.",
    "This game is a work of fiction and does continue themes that is not suitable for certain audiences.\n You have been warned.",
    "You must be 18 and above to play this game. \n Contains sensitive themes and requires the player's discretion."
    ]

    splash_messages = [
    "You're missing the point.",
    "Have you tried risking your life for someone?",
    "Don't bother",
    "I'll just die anyways",
    "You can never save me",
    "I wish I could've been useful",
    "If only you were careful",
    "I don't know what to do now",
    "y hzrw lywnyvdz ev yvgvukjwpw lp jhho yosxr.\ny dnj'l oidnby jjgt akcj tn bwbp ewj i eawi plmu i'l wdoidfo czolbh rwj.",
    "Yf xkm xvh crld pg aifqte sdap wkkj, \ntgaf tldv qrd ugr hrkdg gajb rry?",
    "SSBsb3ZlIHlvdQ==",
    "If only Monika was here",
    "SSB3YW5uYSBraWxsIHlvdQ==",
    "Can you find me?",
    "This same is not cuitable for ghildren",
    "YOU FUCKINGGGGGGGGGGGGGGGGGGGGGGGGGGGGggGgGgGgGGgggggGgg",
    "Ha?",
    "Hakdog",
    "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA",
    "Be careful what you wish for...",
    "Promises are meant to be broken",
    "Reality is just an Illusion and some Illusion are fragments of reality.",
    "AUDIO LOG DECIPHERED: Every story has an ending. This is mine."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

default persistent.accepted_warning = False

##Menu Animations goes here##

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

transform rand_blink(img1, img2, size, pos):
    subpixel True
    anchor (0.5, 0.5)
    size size
    pos pos
    img1
    choice:
        pause 2.0
    choice:
        pause 4.0
    choice:
        pause 6.0
    img2
    pause 0.2
    repeat

image seika_anim = rand_blink("gui/Seika_1.png", "gui/Seika_2.png", (400, 700), (720, 550))
image iris_anim = rand_blink("gui/Iris_1.png", "gui/Iris_2.png", (450, 900), (350, 550))
image alice_anim = rand_blink("gui/Alice_1.png", "gui/Alice_2.png", (570, 1000), (1150, 450))

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    ease_cubic 1 xoffset 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_expo 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

##Actual Splash Screen##

label splashscreen:

    if not persistent.accepted_warning:
        "Warning:\nThis game contains scenes and topics that is not suitable for anyone under the age of 18."
        "If you are suffering from any mental illness, domestic violence and bullying, please seek do professional help and uninstall this game."
        menu:
            "If you agree with our terms, Please proceed with the game. Enjoy!"
            "Yes":
                scene black

                $ renpy.pause(1.6, hard=True)
                $ config.allow_skipping = False

                $ persistent.accepted_warning = True
                

            "No":

                "I see..."
                "If you cannot accept the terms then we cannot proceed."
                "Please uninstall the game and enjoy a fresh air"

                $ renpy.quit()

    $ config.main_menu_music = audio.menu1
    $ renpy.music.play(config.main_menu_music)

#Company Name
$ splash_message = company_name
show splash_warning "[splash_message]" with Dissolve(0.5)
$ renpy.pause(1.5, hard=True)
hide splash_warning with Dissolve(0.5)
$ renpy.pause(1.6, hard=True)

#Random splash
$ splash_message = renpy.random.choice(splash_message_default)
if persistent.chapter_rand == True and renpy.random.randint(0, 5) == 0:
    $ splash_message = renpy.random.choice(splash_messages)
show splash_warning "[splash_message]" with Dissolve(0.5)
$ renpy.pause(1.5, hard=True)
hide splash_warning with Dissolve(0.5)
$ renpy.pause(1, hard=True)

$ config.allow_skipping = True

return
