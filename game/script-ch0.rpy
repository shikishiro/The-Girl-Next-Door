## This is the start of the Main Game ##
label ch0_main_a:
    stop music fadeout 2.0
    with dissolve
    pause (2.0)

    "What's your ideal girl?"
    "Is it her sweet smile?"
    "Her dazzling appearance?"
    "The kind, caring aura she emits?"
    "Or perhaps..."
    "Her personality attracts you? Her mind and soul unveiled to the one she loves--that being you."
    "A cold embrace envelops your body as you slowly drift into the sleepy darkness."
    u "Hehehe~"
    "That... sounds like giggling but... who's giggling?"
    "..."
    "..."
    "..."

label ch0_main_b:
    $ quick_menu = True
    scene roomdark with dissolve
    $ persistent.unlock_roomdark = True

    play music m1

    u "...he..."
    u "...hey..."
    u "Hello...?"
    "A faint voice tries to wake you up from your deep slumber..."
    "I wonder who could it be?"
    "..."
    "It's gone...?"
    "I guess it was just my dreams speaking to me..."
    "Dismissing the matter, I fell asleep once again."

    scene black with dissolve

    "Heeding no mind to it."
    u "...?"
    u "Hmph..."
    "Just as I was about to drift away into dreamland, I hear some clothes rustling and some soft footsteps... Odd."
    "I guess it was no one..."
    "Well, off to dreamland I go."
    
    stop music fadeout 1.0

    u "Big brother...?"
    u "WAAAAAAAAAKE UP!" with vpunch

    play sound [ whoosh, bb1 ]

    "A loud yell pierces my ears; along with a swift swing of a rubber baseball bat."
    "Hitting me in the gut, which is enough to startle me awake."

    scene roomlight with vpunch
    $ persistent.unlock_roomlight = True

    play sound body1
    mc "WHAT THE--?!" 
    "I woke with a start and fell off of my bed."
    "I'm glad that whatever hit me didn't hurt as much as falling off my bed."
    "But boy, did that scared the life out of me..."
    mc "...Ugh."
    u "So..."
    u "You finally decided to wake up!"
    "As I groggily open my eyes,"
    "I see the small, slender figure of my little sister."
    "Her favorite pink rubber baseball bat is propped up against her shoulder. It's something she cherishes quite a lot."
    "I bet she used that to wake me up."
    show seika smug1 zorder 2 at t33
    u "Shaking you awake isn't enough as always..."
    show seika smug3 zorder 2 at t33
    u "So, I resorted to this instead!"
    "Seika smiles smugly as she shows me her favorite toy bat."
    mc "Yeah..."
    mc "But next time, go soft on me please."
    show seika narm1 zorder 2 at t11
    "This is my little sister, Seika."
    "She's an energetic ball of sunshine but she can be shy at times."
    "She's a bit boyish too but not that I mind. As long as she's happy, I'm happy."
    show seika smug2 zorder 2 at t11
    s "Yeah, I would."
    show seika smug1 zorder 2 at t11
    s "But you didn't wake up, did you?"
    show seika grr3 zorder 2 at s11
    s "Hmph."
    show seika grr1 zorder 2 at t11
    mc "Fine, fine..."
    mc "I'll get up and get ready."
    mc "After I get ready⁠—let me guess⁠, you want me to cook breakfast?"
    show seika smug3 zorder 2 at s11
    pause (0.5)
    show seika smug2 zorder 2 at t11
    s "Yes! I’m starving!"

label ch0_main_c:

    scene outside_m with wipeleft_scene
    $ persistent.unlock_outside_m = True

    show seika grr1 zorder 2 at t11

    s "Come on, brother!"
    s "We need to go now or we’ll be late!"
    mc "Yeah, yeah."
    mc "I'm coming, Seika."
    show seika grr1 at thide zorder 1
    hide seika
    "As Seika and I were about to leave our house, I'd noticed that there were some trucks parked next door."
    "I think we might be getting a new neighbor soon."
    mc "Hey, Seika."
    show seika narm1 zorder 2 at s11
    s "Hm?"
    mc "Look! It seems that we'll be having a new neighbor soon."
    hide seika
    "I pointed to one of the trucks parked near our home."
    "Some of the movers were carrying boxes of various sizes into the person's home."
    show seika narm2 zorder 2 at t11
    s "Oh yeah, huh!"
    show seika smug2 zorder 2 at t11
    s "I wonder who he or she is?"
    mc "I don't know to be honest."
    mc "Guess we'll have to find out ourselves after class."
    show seika smug2 at thide zorder 1
    hide seika
    "While passing by the neighboring houses on our way to school, a young lady rushes by."
    "She seems to be hurrying to school and she couldn't afford to be late."
    show alice hap1 zorder 2 at  h21
    show seika sad1 zorder 2 at h22
    u "Good morning, you two!"
    show alice hap2 zorder 2 at t21
    u "Make sure to be early to your classes!"
    show seika sad1 at thide zorder 1
    show alice hap2 at thide zorder 1
    hide alice
    hide seika
    "And the young lady hurries off without waiting for a reply."
    mc "Huh?"
    mc "I was going to greet her a 'good morning.'"
    mc "But I guess I missed the chance to do so."
    show seika yan4 zorder 2 at t22
    s "{cps=*2.5}Hmph! Brother is mine! Not some random chick who decides to bump into us. {/cps}{nw}"
    show seika grr2 zorder 2 at t22
    $ _history_list.pop()
    mc "Hm?"
    mc "Seika?"
    mc "Did you say anything?"
    show seika ahh1 zorder 2 at h11
    s "Hm? Nothing at all, Brother."
    s "I was rambling to myself. Nothing to be concerned about!"
    show seika smug2 zorder 2 at h11
    s "Hahaha~"
    mc "Well, if you say so."
    hide seika

    scene black with dissolve

    "With that being said, Seika and I continued our path towards school."
    "And from there, we went to our respective classrooms."
    "Seika heads to the 3rd floor as all of the freshmen classrooms are located there."
    "And I went to the 2nd floor as my classroom was located here."
    "As I entered the classroom, I went straight to my assigned seat and sat down."
    "And my class begun and went on according to schedule."

label ch0_main_d:

    "Ding...{w} Dong...{w} Ding...{w} Dong..."

    scene c_day with wipeleft_scene
    $ persistent.unlock_c_day = True

    t "The bell has rung and that's concludes our lesson for today, class."
    t "Be sure to head home right after your club activities. Dismissed."
    mc "Ahh... Finally!"
    mc "Class is over! Boy, am I beat."
    "I stretched out my arms and let out a sigh of relief."
    "It hurts to sit for hours on end without budging an inch."
    mc "I guess I should pack up and start heading home then."
    "In a rush, I stuffed my books, notebooks, and pencil case inside my bag, zipped it closed, and slung it over my shoulder."
    "Right after that, I got up and went to the door, placing my hand on the sliding door to open it, and walked out."

    scene corridor_d with wipeleft_scene

    "As soon as I left the room,"
    "I failed to notice someone passing by and we bumped into each other."

    with vpunch

    mc "Oof..."
    u "Kyah!"
    mc "Ah! Sorry for bumping into you. Are you alright? Here, take my hand."
    show alice nml1 zorder 2 at t11
    u "Yes, I'm fine. Thank you so much."
    show alice cfs1 zorder 2 at t11
    u "I'm sorry, I wasn't paying attention to my surroundings."
    show alice nml1 zorder 2 at t11
    "Stunned by her beauty and her troubled face, I couldn't help but stop Alice from hurrying off again."
    "Alice has been my childhood friend and she's also in the same year as I am, second year. The only difference is that..."
    "Well, there's a lot of differences. Currently, she's the student council president."
    "And to add to that, everyone in the entire school admires her."
    "Long story short, she's the perfect girl that everyone wants but also out of everyone's league."
    show alice nml1 at thide zorder 1
    hide alice
    mc "Alice, are you really alright?"
    mc "You really look like you're in a pinch right now..."
    mc "Is something the matter?"
    show alice cfs1 zorder 2 at t11
    a "I'm really sorry."
    show alice sad1 zorder 2 at t11
    a "I'm just feeling a bit...{w}off right now."
    show alice sad1 at thide zorder 1
    hide alice
    "I know for a fact that there must be something wrong. My gut just says so."
    "And I just can't stand around and do nothing."
    mc "Well..."
    mc "If you need some help, {w}I'd be glad to offer a hand."
    show alice cfs1 zorder 2 at t11
    a "Hmm..."
    "By the looks of it, it seems she has something on her mind."
    show alice hap1 zorder 2 at t11
    a "Well..."
    a "If you aren't busy, can you swing by the Student Council room?"
    mc "Sure! I've got nothing to do anyway."
    show alice hap2 zorder 2 at h11
    a "Perfect! Shall we go then?"
    show alice hap2 at thide zorder 1
    hide alice
    scene black with wipeleft_scene

    "Without a word spoken, Alice and I head towards the Student Council Room."
    "As we arrived, Alice swung the door open gently."

    scene council_d with wipeleft_scene

    "Upon entering the Student Council room, a girl with short bobbed hair and round-rimmed glasses, bigger than her own face, immediately approaches us."
    show sec zorder 2 at t11
    sc "President Alice! Welcome back!"
    sc "Did you manage to convince the faculty to increase the budget for the school's festival?"
    hide sec
    "She was followed by another student, also sporting the same get-up."
    show sec zorder 2 at t21
    show vp zorder 2 at t22
    vp "Prez!"
    vp "We still have to file all of our papers by the end of the day!"
    hide sec
    hide vp
    "From just entering the room,"
    "It was way more chaotic than I had anticipated."
    "Questions barraging from her members here and there nonstop even I would be overwhelmed if I was in Alice's situation."
    mc "So..."
    mc "Has it always been like this or...?"
    "Alice lets out a long sigh, in which I found kind of cute."
    show alice cfs1 zorder 2 at s11
    a "It's always been like this."
    show alice sad1 zorder 2 at t11
    a "It's just a bit more hectic due to the Cultural Festival coming up soon."
    mc "I see..."
    hide alice
    "So, they've been this chaotic every since?"
    show sec zorder 2 at t11
    sc "Oh, President Alice!"
    sc "I didn't know that we were expecting a guest today."
    show sec zorder 2 at t21
    show vp zorder 2 at t22
    vp "Uuu... {w}But we don't have any extra cash to treat our guest with."
    mc "Ah! You don't have to, seriously."
    mc "It's fine! I'm just here to help, really."
    mc "In any case, I think I can help out."
    hide sec
    hide vp

    scene black with wipeleft_scene

    "Immediately diffusing the situation before everything goes out-of-hand,"
    "It does make me wonder...{w}Is the school's budget really that bad?"
    "The student council's secretary showed me all the necessary papers and documents."
    "I quickly scanned and analyzed all the data and the time stamps on each individual ins and outs."
    "Problem solving and financial matters like these aren't much of a bother to me since my parents are usually away."
    "So, analyzing and budgeting stuff like this isn't a big deal for me at all."

    scene council_d with wipeleft_scene

    mc "And that's that!"
    "With that, I managed to re-evaluate all the numbers in the documents."
    show sec zorder 2 at t11
    sc "W-w-WHAT?!"
    sc "YOU MANAGE TO SOLVE THAT IN JUST MINUTES?!"
    show sec zorder 2 at t21
    show vp zorder 2 at t22
    vp "We've had this problem for almost a month now and you just solved it like it was nothing?!"
    show alice cfs1 zorder 2 at t11
    a "I-{w}I-{w}I'm at a lost for words...{w}How'd you manage to do that?!"
    show alice hap2 zorder 2 at t11
    a "[player], thank you so much!"
    show alice hap1 zorder 2 at t11
    a "I'll go on and hand these re-evaluated budget logs to the faculty."
    show alice nml1 zorder 2 at t11
    a "Vice President, you can handle the remaining paperworks. Thank you!"
    show alice nml1 at thide zorder 1
    hide alice
    hide sec
    hide vp
    "I handed Alice the re-evaluated documents and she immediately left the room."
    mc "Well...{w} I guess I'll be taking my leave then."
    vp "Thank you so much for helping us out today!"
    "He says gratefully as he bows his head down."
    vp "We really thought we had to limit the festival's activities due to the budget cuts."
    sc "Not only that... {w}You just prevented a school-wide crisis!"
    "Uhm... Isn't that a bit exaggerating?"
    mc "It was nothing at all, I just wanted to help Alice out."
    vp "Speaking of Alice..."
    mc "What about her?"
    vp "Actually, {w}nevermind."
    "The Vice President abruptly stopped what he was going to say and hastily shifted the subject."
    vp "Anyway, thank you so much for your hardwork and providing us with your assistance."
    "Not prying into the details, I dismissed the matter."
    mc "It's the least of what I can do to help."
    "I gently opened the door and waved my hand as I left the Student Council room."

    scene corridor_d with wipeleft_scene

    "With my business done at the Student Council room, I decided to take a little stroll on the second floor."
    
    scene black with dissolve
    # add CG with Alice

    "As I was roaming through the corridor, I saw Alice from afar."
    "She was gazing out of the window, her binder in hand but her thoughts were elsewhere."
    "And all of a sudden-"
    "She dropped all of her papers on the ground, tears brimming in her eyes and a look of defeat upon her face."
    "Her fists clenching, nails digging into her palms and knuckles turning white all while Alice berates herself."
    a "Why can't I do anything right?"
    a "Why am I such a failure to everyone?"
    a "Just...{w} why?!"
    "Then she falls. Her conflicting emotions of fear, anger, and hate directed at herself bested her."
    "She couldn't do more but weep and bury her face in her palms."

    scene corridor_d with wipeleft_scene

    "From where I'm currently standing, I could barely hear what Alice is saying."
    "But there's no mistaking it that the tears trickling down Alice's face means she isn't okay."
    "And out of the blue, I lightly called out her name."


    mc "Alice?"

    show alice sad1 zorder 2 at h11

    "Alice looked at me, a mix of surprise, defeat, and hope shown on her face."
    "Though... I didn't know if she actually knew it was me she was looking at."

    show alice at thide zorder 1
    hide alice

    "Fearing that more people would see her like this, she immediately wiped her tears and tried to calm herself while hurriedly collecting all the documents she dropped."
    "I made my way to Alice to help out but by the time I got there, she had already picked up everything."
    mc "Hey...{w} Are you okay?"
    show alice cfs1 zorder 2 at t11
    a "Yeah..."
    show alice nml1 zorder 2 at t11
    a "I'm fine."
    show alice at thide zorder 1
    hide alice
    "Trying her best to keep her emotions in check, she lets out a smile. A smile so hollow that I knew I was powerless to do anything... yet."
    "She used to vent all of her problems to me back when we were close but now... she's keeping to herself."
    "I wonder what had happened to the Alice I used to know."
    "In return, I sheepishly smiled."
    "I calmly lent a hand to Alice, helping her get back up but trying not to show my worry for her."
    "Her normal expression soon returns to her face but I knew she was toughing it out."
    show alice cfs1 zorder 2 at t11
    a "Anyway..."
    show alice sad1 zorder 2 at t11
    a "Did you see that?"
    "I knew Alice was aware that I was there during that time."
    "But it's best to ignore that matter for now."
    mc "See what exactly?"
    "I raised an eyebrow, feigning ignorance."
    show alice csf1 zorder 2 at s11
    a "Oh... it was nothing."
    show alice nml1 zorder 2 at t11
    "She smiles as if nothing happened."
    "But nothing hides her slightly puffy, reddish eyes, the tear stains that dampen her sleeves, and the occasional sniffle I hear from time to time."
    show alice sad1 zorder 2 at t11
    mc "Anyway Alice, if you ever need someone to talk to or just have a casual talk,"
    mc "I'm here to listen."
    show alice at thide zorder 1
    "As those words reached Alice's ears, her eyes widened. It seems I struck something quite deep."

    scene black with dissolve
    #cg alice hug

    "She slowly breaks down and starts crying as she gives me a tight embrace."
    "Dropping all of her documents once again as tears streamed down her face."
    "I decided to stay silent and lend her a crying shoulder."
    "I guess she must've been going through a lot recently."
    "And after a good minute or so,"
    "Alice finally calmed down and let go of me."
    "I tried my best to wipe some stray tears on her cheek."
    mc "Hey...{w} Are you feeling better now?"
    a "Yeah."
    a "I'm feeling a bit better now.{w} Thank you."
    "Alice knelt down and retrieved the documents from the floor."
    a "Well, I should hand in these budget logs to the faculty now."
    a "I guess{w} I'll be seeing you around?"
    mc "Yeah, I'll see you around."
    "She smiled sweetly as she continued her way to the faculty's office."

label ch0_main_e:

    with wipeleft_scene
    "Parting ways with Alice, I made my way towards the staircase so I can head to my locker downstairs."
    "Nearing the stairs, I couldn't help but hear someone grunting. Are they struggling with something?"
    u "Argh...{w} So heavy..."
    u "Ugh...{w} Just a few more steps..."
    "Peeking by the corner, I see a slender girl wearing a simple but cute cardigan dragging a sack of, what seems to be, plant fertilizer."
    "Choosing to help her out, I immediately approached her and offered my assistance."
    mc "Hey, let me carry that for you."
    u "Oh, no need to worry. I can handle this on my own."
    "The girl hesitates as she rejects my offer, briefing looking away and focusing on her task. I knew that she was struggling, judging by the sweat on her forehead and clothes."
    mc "It's fine. Let me help you out."
    mc "It'll be a lot faster and more effcient if I carry that for you."
    "I reasoned with her so that I'll be able to provide help on carrying such heavy material."
    u "Hmm...{w} Yeah, you got a point there."
    u "There isn't enough time for me to carry this weighty sack and I still need to tend to my plants."
    u "Alright then, I accept your offer. The garden is on the rooftop of this building."
    u "I'll be going on ahead first, okay?"
    "She turns around and walks up the set of stairs, leaving me with the sack of fertilizer behind."
    "I picked up the sack and surprisingly it wasn't that heavy, so I carried it on my shoulder."
    "After adjusting the sack on my shoulder to prevent it from falling, I made my way upstairs, heading to the rooftop."

    with wipeleft_scene

    "Opening the doors to the rooftop, I was in awe to see a beautiful garden, hidden from view and isolated from everyone else."
    "The clean, crisp air from various greens, alongside the alluring scent from different types of flowers, made it feel like I was in paradise."
    mc "Whoa!"
    mc "Th-{w}This place is beautiful!"
    u "Thank you so much! I've really worked hard on this garden and it took me quite a while to grow this garden from ground up."
    u "Just place the sack near my tool shed please and I'll handle the rest."
    "I was still in awe, but I placed the sack of fertilizer on a small makeshift shed that sheltered all of her gardening tools."
    u "Thank you so much for helping me out, {w}uhm...?"
    mc "Oh!"
    mc "My name is [player]. {w}Nice to meet you, Iris."
    i "Oh! You know my name."
    mc "Well, of course, you're the former student council president and you're quite popular around the school."
    "As far as I know, Iris is in her senior year. Despite being timid and shy, she's quite passionate if she sets her mind on something."
    "Plus, she's one of the smartest and good-looking students alongside Alice."
    "But I wonder what made her retire as student council president?"
    i "Hmm...{w}Well, I supposed that is true."
    i "After all, my student ranking is a bit too much. Hehehe~"
    "When I mentioned her former role and her popularity, Iris looked reluctant; shying away from the said topic and obviously not comfortable talking about it."
    "Deciding not pry on that matter, I simply asked her a question about her garden."
    mc "By that way, when did you start this garden?"
    i "Oh! Let's see..."
    i "I started around the time when I was still the president of the student council."
    i "This is my go-to hobby as it helps me calm down and destress from time to time."
    "As she saunters about, Iris halts suddenly, caressing the orchids mounted upon the wall."
    "Iris's facial expression softens, a delicate, sweet smile appears. Would such a smile like that be given to me someday?"
    i "The reason why being in nature helps us feel good is because of phytoncides."
    i "It's literally the fragrance of the forest and it is known to lower stress levels, help us concentrate, and strengthen our immune systems!"
    i "... {w}Oh, I'm sorry! There I go spouting out random facts again."
    mc "Oh, don't be sorry. Honestly, I didn't even know what phytoncides are, so it's great to learn that from you!"
    i "R-Really? Th-thanks I guess."
    "Iris hastily looked away, a slight blush apparent on her face. Was it something I said?"
    mc "Now I see why gardening helps clear your mind."
    i "It also gives me great produce! Here, take a look a these eggplants."
    i "They're coming along nice and healthy."
    "Iris lead me to one of the growing plants nearby. She picked a healthy, girthy eggplant and handed it to me so I can inspect it."
    mc "Hey, you're right. They're growing quite plump it seems."
    i "Go ahead and take some home. It's my thanks for your help earlier."
    "I can't say no to a such a generous offer; especially if it involves food."
    mc "Seriously? Thank you! I can't wait to prepare some dishes using these eggplants tonight."
    "Iris proceeds to pick a few more eggplants, cut off the stems from them, wraps it in some old, outdated newspaper, and puts them inside a paper bag."
    "In my case, my head starts brainstorming on what to cook for dinner later on. Oh, the amount of dishes I can make with these eggplants."
    i "Here you go. Please, do enjoy them."
    "She handed me the paper bag, containing the freshly picked eggplants."
    mc "Thank you. I'll enjoy these greatly."
    mc "Anyway, do you still need help with anything else?"
    "As the sun sets and the twilight approaches, I await an answer from Iris."
    i "Well, I could use some extra hands in tending my garden. But for today, I can manage on my own."
    mc "Are you sure? I still have a lot of free time on my hands right now."
    i "No, it's okay. I got this."
    i "If you want to help out, I'll be either here or on the building behind this one as I have another garden situated there."
    i "I'll be in either garden tomorrow and I'll be waiting."
    "Iris smiles sweetly and waves goodbye as I leave the secret rooftop garden."

label ch0_main_f:

    with wipeleft_scene

    "As I descend from the rooftop to the ground floor, I head to the shoe locker area to wait for my little sister, Seika."
    "It's likely that most of the students, with or without extra-curricular activities, had already left the school premises."
    "So where did Seika wander off to?"
    "I was about to reach for my shoes, but then I suddenly felt a chill crawl up my spine."
    "A familiar aura of anger coming from someone I certainly know..."
    show seika grr2 zorder 2 at t11
    s "Oh, brooooother.{w}.{w}."
    "Oh, crap..."
    "I'm so screwed..."
    show seika grr1 zorder 2 at t11
    s "Where have you been, {w}big brother?"
    s "Did you forget that I'd been waiting for you since the bell rung?"
    hide seika
    "I'd totally forgot that she hated waiting."
    "I timidly faced Seika and gave her a wary smile; topping it off with a white lie."
    mc "Well...{w}I just lazed around inside the classroom for a bit."
    show seika grr4 zorder 2 at t11
    s "Uh-huh..."
    hide seika
    "Crap...{w} She's not buying it."
    mc "And then I strolled around the campus too..."
    mc "You know...{w} Just to stretch out my muscles after sitting for a while. Hahaha~"
    show seika yan4 zorder 2 at t11
    s "{cps=*2}Lies, I saw you with someone...{/cps}{nw}"
    $ _history_list.pop()
    show seika grr4 zorder 2 at t11
    mc "Hmm? {w}What was that?"
    show seika ahh1 zorder 2 at t11
    s "Hmm? What?"
    mc "Did you just say something?"
    show seika grr2 zorder 2 at f11
    s "Hmph... I didn't say anything...{w}Stupid!"
    show seika grr3 zorder 2 at t11
    mc "Well... okay."
    mc "Shall we head home then?"
    show seika grr4 zorder 2 at f11
    s "Hmph!"
    show seika grr3 zorder 2 at t11
    "Seika crossed her arms and walked out of the locker room, not even bothering to wait for me."
    "Ah, it looks like I really pissed her off this time."
    "After putting on my shoes and tying them in a hurry, I left the locker room and made my way outside."
    "I quickly looked around for Seika, hoping she didn't leave me behind. But luckily, she was standing by the school gate."
    "Suddenly, I remembered that I had the eggplants that Iris gave me. An idea popped into my mind."
    "Since Seika loves my cooking, maybe she'll dismiss this matter if I mention some food to her."
    "As I approached her, I cleared my throat so she'd be aware that I'm here."
    mc "Seika?"
    s "..."
    "Ah, still pissed. I feel the cold shoulder already. Good thing I have a trick up my sleeve."
    mc "Hmm, I think I'll make some parmigiana tonight."
    show seika narm1 zorder 2 at f11
    "Seika's eyes suddenly gleamed at the mention of food. I think she's curious about the dish I'll be making."
    show seika smug2 zorder 2 at t11
    s "Oh! What's that?"
    "Bingo. I knew she'd be swayed easily by food."
    mc "You'll see, it'll be delicious. Trust me."
    s "Can't wait then!"
    "Seika buzzed with happiness, excited at the dish I'll be making for our dinner."
    show seika smug3 zorder 2 at t11
    "I smiled softly at Seika and she smiled back at me, successfully diffusing the tense atmosphere from earlier."
    "I offered to carry her bag and she gave it to me without hesitating. And then we made our way home."
    hide seika


    with wipeleft_scene


    "Walking through our neighborhood, I have noticed that the movers and their trucks had already left."
    "However, I still have no clue as to who's our new neighbor."
    "The lights are on but I barely hear anything nor do I see any silhouettes inside the house."
    mc "Hey, Seika."
    show seika smug3 zorder 2 at t11
    "Seika turned to look at me, eyebrow raised."
    s "Hmm?"
    mc "Looks like our neighbor has already moved in now, huh?"
    mc "Why don't we welcome them to the neighborhood?"
    show seika ahh1 zorder 2 at f11
    s "I would love to...{w}but..."
    "Seika looks away shyly, her hands clutching her stomach."
    hide seika
    "{i}*Tummy growls*{/i}"
    "That sound..."
    show seika ahh1 zorder 2 at t11
    mc "Well...{w} I guess that could wait 'til tomorrow."
    mc "For now, I need to prepare and cook our dinner."
    hide seika

label ch0_main_g:

    with wipeleft_scene

    "Arriving home, Seika heads to her room, grabbing a towel and her pajamas, and makes her way to the bathroom to shower."
    "In the meantime, I set our stuff down in the living room and went to the kitchen to prepare and cook our dinner."
    "These eggplants that Iris gave me are really glossy and big. I think I might have double the servings."
    "Not that I'm complaining though; the more, the merrier."
    "Guess it's time to start cooking!"
    "Moments later.{w}.{w}."
    "The smell of parmigiana fanned out throughout the kitchen and dining table."
    "It was still in the oven but it's almost thoroughly cooked. Just standing here and waiting for it while I scroll through social media is making me hungry."
    "Deciding to put down my phone, especially after seeing some pictures of tasty food, I glanced at the oven."
    "The parmigiana looks well baked and is most likely finished by now. With a oven mitts on, I opened the oven and the fragrance of the food hit me like a truck."
    "Ahh, I can't wait to eat. I'm getting hungry by just getting the pan out of the oven."
    "As soon as I took out the pan of parmigiana, Seika came out of the bathroom; her towel hanging around her shoulders."
    "I turned to Seika and asked her to set some plates for us on the table."
    mc "Perfect Timing! Can you set the plates on the table?"
    show seika narm1 zorder 2 at t11
    s "Sure thing~"
    hide seika
    "As Seika brought some plates and utensils to our table, I picked up and brought the pan of freshly cooked parmigiana."
    "Seika took a seat, spoon and fork in her hands as she eyes me bringing the pan over to the table."
    "As I set the pan onto the table, I grasped the handle of the cover."
    mc "Alright, are you ready?"
    "With Seika eying the platter, drooling at how fragrant the food is, she nodded at me."
    "I swiftly lifted the lid and carefully unveiled our meal for tonight."
    mc "TA-{w=1.0}DA!"
    show seika smug2 zorder 2 at h11
    s "WHOA!"
    mc "I present to you, eggplant parmigiana!"
    mc "Be careful though, it's-"
    hide seika
    "I was going to warn Seika about the food being hot but she quickly stabbed her fork into the dish."
    s "TIME TO DIG IN!"
    "And then took a huge bite of piping hot parmigiana..."
    "..."
    s "IT BURNS!"
    mc "-hot."
    "I dragged my hand across my face. It's common sense that the food is hot but I guess I can't blame her for being hungry."
    mc "You do realize that cheese conducts heat a lot better than the eggplant, right?"
    "Regardless, I got a glass from the cupboard and poured some cold water in it."
    mc "Here, have some water to cool down your mouth but don't swallow it just yet."
    "I handed the glass of water to her and she took a few sips, cooling her burnt mouth."
    mc "So..."
    mc "Are you okay now?"
    s "Yeah, I feel better now."
    s "But still, it tastes SOOOO GOOD!"
    "Seika went to get another serving but this time, after learning her lesson, she blew a few puffs of air onto her food to cool it down before taking another bite."
    mc "I'm glad that you liked it."
    "I sat down just across from Seika's seat and grabbed my serving of parmigiana."
    "I took a bite and the flavor of the eggplant really bursts throughout every bite."
    "The parmesan cheese holds all of the flavor together too."
    mc "Ah~"
    mc "Cheese heaven and a mix of wonderful flavors~"
    "I am in heaven."
    s "By the way, big brother?"
    mc "Hmm? {w}What is it?"
    "Waiting for Seika to speak up, I noticed her expression suddenly changed as she put down her spoon."
    s "Well..."
    s "Do you think mom and dad would be here for your birthday?"
    "After hearing that, I felt a bit down. And come to think of it..."
    "Ever since my parents started working abroad, they kept missing out on our birthdays."
    "Though, they do send some birthday gifts over to compensate."
    "But... {w}even though they send gifts to compensate, it doesn't feel the same as celebrating with them in person."
    "And I kind of miss celebrating with the whole family to be honest."
    mc "I don't think they'll be here on my birthday though. They're busy in Macau, you know."
    mc "Remember? They're getting a promotion and they'll be extending their stay there just to further work."
    s "Yeah, I know."
    s "But, don't you feel sad when they aren't around?"
    s "I mean, it's been two years since they left and they already missed out on me entering high school."
    "Seika looked at me in the eye as she spoke those words. I could see how saddened she is and honestly, I feel the same way."
    "Yeah, it is sad that our parents aren't usually around."
    "And it's hard to manage the house by myself."
    "But I have to be strong and be the head of this house while my parents are away."
    "And it's my duty to keep my little sister happy and supported."
    mc "It's sad, I know but don't worry, I'll be here for you."
    mc "And hey, don't you like your present?"
    "Seika's birthday was a month ago. We celebrated it together, just us."
    "And speaking of present, I bought her a shiny, metal baseball bat."
    s "Yup! {w}I love it so much!"
    mc "Strange though, I never saw you use that bat at all."
    mc "Did you break it or something?"
    s "No, it's just in my room."
    s "I just cherish it so much that I don't want it to be dented is all."
    "Seika smiles, happy about the gift I gave her last month."
    mc "Oh! Well okay then. I'm glad that you liked it."
    s "Speaking of bats..."
    s "Uhm...{w} Hey, big brother..."
    s "..."
    "Seika lowers her head, the atmosphere suddenly heavy as if she has a problem."
    mc "Yeah, what's wrong? You suddenly went quiet."
    s "Well..."
    s "This afternoon, I finally decided to open up a club."
    mc "Oh? {w}A club?{w} That's great! Did you finally start a softball club?"
    "It's been months since Seika found out that there wasn't a single softball club in our school."
    "She was eager to make it a reality but she also feared that no one would join."
    s "Yeah..."
    mc "But?"
    s "I CAN'T BARE THE PRESSURE OF BEING THE SELF-APPOINTED PRESIDENT!"
    s "Ugh...{w} I'm starting to regret my decision."
    "I stood up from my chair and took a seat beside Seika."
    "Gently patting her head, I came to realize how she's becoming more independent."
    "It's almost as if she doesn't need a big brother for guidance anymore, which is a good but sad thing."
    mc "You're doing great. Just keep it up and I'll be by your side, supporting you as I've always been."
    s "No matter what?"
    mc "Yeah..."
    mc "No matter what."
    s "Even though I slipped your name into the club's membership form without you knowing?"
    "Our tender and sentimental moment vanished as fast as a finger snap."
    mc "..."
    mc "YOU DID WHAT?!"
    s "Well..."
    s "I don't know how to start a club and I need someone to help me set it up."
    s "And besides...{w} You already said that you'll be by my side no matter what... Hmph!"
    "Such a cunning, clever girl. I was baffled by how she used my own methods against me but I like it."
    "Yeah, she's surely maturing now and I'm proud of her."
    mc "Fine, it's not like I have a choice or anything."
    s "Alright! Let's celebrate our softball club!"
    s "YEAH!"
    mc "Uh...Yeah."
    "And with that, my tiresome day has ended."
    "Today was such a delight and I was glad to be able to help people."
    show alice nml1 at t21 zorder 2
    "Alice,"
    show iris nml1 at t11 zorder 2
    extend " Iris,"
    show seika nml1 at t22 zorder 2
    extend " and Seika."
    hide alice
    hide iris
    hide seika
    "I promise to help you guys with everything I've got!"

call ch1_main_a

return
