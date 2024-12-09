# The game starts here.

label start:
    $ playername = renpy.input("What is your name?", default = "Silas")
    $ playername = playername.strip()
    if playername == "":
        $ playername = "Silas"

    menu pick_pronouns:
        "Which pronouns do you use?"
        "They/Them":
            $ pronoun = "they/them"
        "She/Her":
            $ pronoun = "she/her"
        "He/Him":
            $ pronoun = "he/him"

    menu:
        "So your pronouns are [they]/[them]?"
        "Yes":
            pass
        "No":
            jump pick_pronouns

    jump ch1

label ch1:

    play music "bgm sad spooky track.ogg"
    
    scene bg forest
    with fade

    show mc angry
    mc "I knew I should have never agreed to go home for the holidays."

    mc "It's all, “oh, when are you going to get married” this and “isn't it time you settled down” that!"

    mc "And now I'm stuck in the great outdoors while my folks eat a feast by the fire, freezing my ass off tryin' to bury this fucking body!"

    "Granted, I did sneak out to enjoy the carny-fest... but the corpse wasn’t my fault! Mostly!"

    "This whole mess started a week ago, when I was hanging out in my room with my best friend. Like most of my headaches, it involved my parents and three bottles of alcohol."

    "{i}One week ago...{/i}" 

    play music "bgm main track.ogg" 
    
    scene bg mc bedroom
    with fade

    show mc sad
    mc "And you know what they said to me?! *hic*"

    show mc sad at midleft
    show helio neutral at midright
    h "That you need to stop spilling your bloody beer over the rug before I disintegrate you?"

    "Even though Helios keeps on saying stuff like that, I know he’d never actually do it. He’s way too nice!"

    "Any other sun elf would have disintegrated me for being annoying a long time ago, but he lets me just flop over his lap and keep complaining."

    mc "Nooo, that’s nowhere even close to what they said, Heli! They were all like, {i}“the DeVille’s daughter has already found NINE husbands!”{/i} and asked when I’d find {i}ONE!{/i}"

    mc "{i}“You’re already two centuries old, I got married when I was 14,”{/i} FUCK, dad, it’s not the 1300s anymore!"

    mc "You’d think they’d quit nagging, but no! They’re even more annoying than usual this time!"

    h "Hmm... Is there any reason in particular, or are vampires just prone to making messes of themselves this time of year?"

    show mc neutral
    mc "They want me to bring a partner to the Autumn Equinox ball they’re throwing!"

    h "And? You {i}have{/i} a partner. Can’t you go together with me like usual?"

    mc "No, no, no, like... a {i}partner{/i}-partner."

    h "I’m aware."

    hide helio
    hide mc

    "Helios isn’t getting it at all... what should I say?"

    menu:
        "As in, a {i}not-you{/i} partner.":
            jump ch1_c1
        "As in, like, someone I’m dating, y’know?":
            $ HP += 1
            jump ch1_c2

label ch1_c1:
    show mc neutral at midleft
    show helio neutral at midright
    h "...excuse me?"

    mc "Not that you’re not like, mega hot and super boyfriend material, but they want me to bring home someone I’m dating!"

    h "And the problem is...?"

    mc "We’ve been besties for {i}forever{/i}. I can’t just date you after you’ve been like, a little bro to me for a century!"

    h "{i}*sigh*{/i}"

    h "If anything, I’ve been the one taking care of you. Shouldn’t you be the one calling me big brother?"

    mc "What?! But, I’m older!"

    h "And you’ve got nothing to show for it."

    show helio sad
    h "...seriously, you’d think you’d notice after so long..."

    mc "Did you just say something?"

    show helio angry
    h "I asked what your brilliant plan is, since you’re not bringing your only option to the ball."

    mc "Oh, I’ll just find a partner!"

    jump ch1_2

label ch1_c2:
    show mc neutral at midleft
    show helio flustered at midright
    h "...and? You can still bring me, can’t you? Your parents like me, they won’t kick up a fuss if you say you’re dating me."

    mc "That {i}is{/i} true..."

    h "Right?"

    mc "But, won’t it be too awkward if they ask if we broke up after we’re done fake dating?"

    h "...fake...?"

    mc "If only there was someone I could just drop after the ball’s done with..."

    mc "Oh! That’s it! I’ll just find someone else for the fake dating!"

    jump ch1_2

label ch1_2:
    show helio neutral
    h "You... what?"

    mc "I’ll just {i}find{/i} a partner!"

    h "...you’re going to find someone, just like that?"

    mc "How hard can it be? There are people everywhere!"

    h "You can’t be serious. You can’t just go out into public and ask people to fake-date you for your parents’ ball."

    mc "...ask?"

    h "...why are you confused?"

    mc "I mean, like, there’s people everywhere. Can’t I just grab one?"

    h "I am {i}very{/i} hesitant to ask this, but when you say {i}‘just grab one,’{/i} what do you mean, exactly?"

    mc "What’s so complicated about it? Just grab someone and drag them back home."

    h "...oh suns and stars, this idiot spent too long rotting in the coffin this morning."

    mc "Huh?!"

    h "You are describing kidnapping! The thing you are planning to do is called kidnapping, and if word gets out that there is a {i}vampire{/i} who is {i}kidnapping{/i} people off the streets, you’re going to get a stake to the heart!"

    mc "Sweet! Win-win, either I get a fake date or a hundred year nap while I’m regenerating!"

    h "{i}{b}NO!{/b}{/i}"

    mc "Thanks for the info, Heli~! I’ll go carry out the plan now~!"

    hide mc
    show helio angry at center

    h "GET BACK HERE YOU FUCKING MORON–"

    scene bg outside
    with fade

    "I almost made it back to my house to get the rope and room ready, when all of a sudden, I crashed into him."
    with vpunch

    mc "Oh no, I’m sorry, I wasn’t looking where I was going at all, are you–"

    show vivian surprised

    mc "...fiiiiineeeeee as hellll?!!?"

    show mc neutral at midleft
    show vivian surprised at midright

    v "Uh... probably...?"

    mc "O-oh, let me give you a hand!" 

    show vivian neutral
    v "...thanks."

    mc "No problem...!!"

    hide mc
    hide vivian
    
    "This guy is..."

    "EXACTLY MY TYPE."

    "Those piercing blood-red eyes, those shining fangs...!"

    "This guy isn’t just the prettiest vampire I’ve ever seen, he’s like the posterboy of Fangs Weekly...!"

    "No, this guy might even beat all those models in model vampire-ness!"

    show mc neutral at midleft
    show vivian neutral at midright
    v "...you okay? You’ve been kinda quiet?"

    mc "You’re fine! I mean, I’m fine!" 

    mc "And, uh, you come here often?!"

    v "...not... really?"

    v "I just moved next door, so... haven’t been here a lot... but, er, that might change, I guess...?"

    mc "Oh! So we’re, like, neighbours!"

    v "Huh? So the person who lives in the rumoured haunted house is...?"

    show mc neutral at left
    show vivian surprised at center
    show helio angry at right

    h "OI YOU STUPID BATTY MORON YOU BETTER NOT BE FUCKING UP AGAIN!"

    v "?!"

    mc "Oh, hey Heli. You took a while."

    h "Because {i}you{/i} fly too fast!"

    v "...fly?"

    h "Yeah, fly–"

    h "Wait, who the hell are you."

    v "Um. Hi. I, uh, moved next door... the name’s Vivian..."

    mc "Nice to meet you! I’m [playername] and this is Heli!"

    v "R-right... hi..."

    h "Right, right, I’m charmed, spellbound, and ensorcelled or whatever, now could you give me a moment alone with this moron?"

    v "...sure?"

    hide vivian

    show mc neutral at midleft
    show helio angry at midright
    with vpunch

    mc "I don’t wanna– Ow! Don’t grab me like that! Heli!!"

    h "I know you were already stupid and your drinking cannot possibly be helping, but {i}please{/i}, for my own sanity, swear to me this..."

    h "Please, just swear that you were not trying to kidnap your neighbour to be your fake date."

    mc "No, I didn’t do that..."

    h "Oh, praise the stars— you’ve finally learned some self-restraint–"

    mc "But, that’s a great idea! Thanks, Heli!"

    h "OI HOLD ON–"

    "Honestly, Heli’s always the bearer of great ideas like this! I mean, he's the one who suggested bringing him to the ball for the last few decades, y’know, to leverage the fact that my parents basically LOVEEEE him."

    "He's basically a genius like that! It almost makes me wonder why he's still single...but then again, if I had to compete with Heli...ooooooh, boy. Maybe I should be glad he's just mysteriously out of commision! More of the hot new neighbor for me!"

    show mc happy at left
    show vivian surprised at center
    show helio neutral at right

    mc "Heyyyy, Vivi!"

    v "O-oh, you’re... talking to me again. I, uh, thought you were gonna leave."

    v "Was it rude of me to keep unpacking...?"

    show mc neutral
    mc "No way! Hey, why don’t we help you?"

    h "...we?"

    mc "We!"

    v "Uh, if you want to, I guess it’s fine...?"

    v "But, does Heli want to...?"

    h "Don’t call me that."

    h "You will refer to me as Lord Heliodoros."

    v "U-uh..."

    mc "Calm down, Heli! I need your help carrying this big box!"

    #Slow down the next text

    show helio angry
    h "{cps=2}...{/cps}"

    h "{cps=2}...{/cps}"

    h "I am helping entirely because I do not trust you not to fuck up immeasurably."

    v "...thanks... I... guess...?"

    "Sweet! Heli’s being nicer than usual. I thought he was gonna cuss me out again for sure...thank you, wingman Heli!"

    hide mc
    hide helio
    hide vivian

    scene bg vi living room
    with fade

    show mc neutral at left
    show vivian neutral at center
    show helio neutral at right

    "After a long evening of hauling boxes off the sidewalk and into the house...we’re finally done! Vivian’s house is pretty neat— and they have some fascinating decor"

    "I mean, who doesn't love a bat-shaped lamp!"

    "Even Helios is surprisingly compliant...though I suppose that might be more because he doesn't want to talk to anyone rather than him actually enjoying himself...anyway, all’s well that ends well, right?"

    "He {i}did{/i} save me from nearly tripping over a stack of boxes once...or twice...or thrice...but the point is— he {i}did{/i} help."

    "And Vivian even cracked a smile at our antics once or twice, so! Score!"

    h "Are we {i}finally{/i} done...?"

    v "Y-yeah. That’s everything. Thank you for, uh, your help."

    v "Uh, you hungry? I can order take-out for us..."

    h "Actually, we really should be go–"

    mc "That would be so so so great! Thanks a ton, Vivi!"

    v "Alright, then, I’ll... go look for good food nearby, yeah."

    hide vivian
    show mc neutral at midleft
    show helio neutral at midright

    h "Okay, genius. I admit, getting dinner in this guy’s house is a lot further than I thought you’d ever get."

    h "Is it possible that you... actually have a plan?"

    mc "I am going to charm the pants off that handsome motherfucker so hard he will {i}instantly{/i} agree to go to the ball with me."

    h "...I’m not sure why I expected anything resembling sense from you."

    v "so, uh, you guys are fine with... Love Bites?"

    mc "Ohh!!!! I {i}love{/i} Love Bites!"

    h "...it’s fine."

    v "R-right, okay, I’ll call them."

    mc "Wow...! Maybe it’s fate that I ran into a guy who also loves my favourite restaurant...!"

    h "It is literally the closest place that does delivery in the area."

    mc "To think that I ran into another guy who loves the same blood bank/maid cafe I do!"

    show helio angry
    h "...oi, are you too far in your own dream land to hear me? Should I knock you back to earth with my polite and considerate fist?"

    mc "W-wait, no, Heli, mercy–!!"

    scene black
    with fade
    jump ch2
