label ch2:

    scene bg vi living room
    with fade

    show mc neutral at left
    show vivian neutral at center
    show helio neutral at right

    v "Th... the food’s here..."

    v "Sorry I didn’t ask what you guys wanted, I, er, didn’t want to interrupt you guys, so..."

    v "I got some of their meal packages...?"

    h "This is fine."

    mc "Yeah, thanks! Let us repay you after this!"

    v "O-oh, no, that’s... it’s okay..."

    mc "You sure?"

    v "Yeah... it’s fine..."

    mc "Alright!"

    v "So, let’s start eating?"

    mc "Yeah!"

    h "Mmn."

    v "..."

    h "..."

    mc "..."

    v "......."

    h "......."

    mc "......."

    v "..................."

    h "..................."

    mc "..................."

    hide vivian
    hide helio
    hide mc
    "ARGHHHHHHH, this is so awkward!"

    "Vivi’s too shy to speak up, and Heli doesn’t give enough of a damn to talk! It’s up to me to start a conversation!"

    "But, how should I do it...!? Do I do polite small talk!? Or talk to Heli and hope Vivi just joins in!?"

    "I could start hitting on Vivi right away, but maybe that would scare them away...?"

    "Ah, whatever! I’ll just jump head-first! Heli says I’m really good at {i}‘diving into stupid situations with no thought or hesitation’!{/i}"

    menu:
        "So, Vivi, why’d you move here?":
            $ VP += 1
            jump ch2_c1
        "Heli! Why are you taking all the blood cakes?!":
            $ HP += 1
            jump ch2_c2
        "Heyyyy, Vivi, are you a construction worker?":
            $ BE += 1
            jump ch2_c3

label ch2_c1:
    show vivian neutral at midright
    show mc neutral at midleft
    v "Oh, um... the rent’s pretty cheap."

    mc "That so...? I’ve been living here forever, so I wouldn’t know."

    show mc at left
    show vivian at center
    show helio neutral at right
    h "It’s not like people are lining up to move {i}here{/i}."

    v "Y-yeah, the realtor was really surprised I wanted to move here..."

    v "There’s rumours that the house next door has been haunted by some Victorian noble..."

    mc "Eh...?! I’ve never seen a ghost in my house...! I wonder if I can do some sort of ritual to get them to talk to me...!"

    h "Isn’t it more likely that people just mistake you for a ghost...?"

    hide helio
    show mc surprised at midleft
    show vivian happy at midright

    mc "Huh!? Me!? A ghost?! Why would anyone think that?!"

    v "Pft... I guess the rumours were false, then..."

    v "There’s no way you could be a ghost when you’re so lively..."

    hide vivian
    hide mc

    mc "Vivi {i}smiled!!{/i} I must be doing something right!"

    jump ch2_2


label ch2_c2:
    show mc angry at midleft
    show helio neutral at midright
    h "The cakes are a bit underbaked. You hate the squishy ones anyways, so what’s the problem?"

    show mc happy
    mc "Oh, so that’s what it was... thanks, then, Heli! You saved me from a squishy cake shock!"

    show mc happy at left
    show vivian neutral at center
    show helio neutral at right

    v "You two... get along pretty well, huh?"

    mc "Yeah, of course! We’ve been together since forever, after all!"

    v "O-oh, so you two are, like, dating...?"

    mc "No, we aren’t! How’d you get that impression?! I’ve just been stuck with this guy since the past forever!"

    show helio angry
    h "...could you kindly shut up and eat your damn food?"

    mc "Eh!? Why are you mad at me all of a sudden?!"

    hide mc
    hide vivian
    hide helio

    "Even so... the atmosphere’s lightened up ! Thanks, Heli!"

    jump ch2_2

label ch2_c3:
    show mc happy at midleft
    show vivian neutral at midright
    v "....no?"

    mc "Because I can see you and I building a house together!"

    hide vivian
    hide mc
    "Wait, was the line supposed to be ‘building a future together’? Or does house still work? Uh..."

    show mc happy at midleft
    show vivian neutral at midright
    mc "Like, uh, wood!"

    v "What?"

    #sound effect of helios hitting Mc in the head

    show mc sad at left
    show vivian surprised at center
    show helio angry at right
    with vpunch
    
    mc "Ouchie!"

    h "I apologize for this rambunctious idiot’s foolish behaviour. They drank too much earlier in the evening and have no control over their mind, mouth, or motor skills."

    show vivian neutral 
    v "Ahaha... it’s, uh, fine..."

    hide helio
    hide vivian
    hide mc

    "It feels really awkward now..."

    "Pocket wine, save me from this terrible atmosphere...!!!"

    jump ch2_2


label ch2_2:
    menu:
        "Vivi, how are you liking the food?":
            $ VP += 1
            jump ch2_c4
        "Heli, can you spare me a bite~?":
            $ HP += 1
            jump ch2_c5
        "Heyyy, Vivi, has anyone ever told you that your teeth are like, so pretty?":
            $ BE += 1
            jump ch2_c6

label ch2_c4:
    show mc neutral at left
    show vivian neutral at center
    show helio neutral at right
    v "It’s... unique."

    h "In a bad way?"

    v "No, it’s... um, it’s more like, I’m not quite used to it, and it feels strange... but I don’t hate it."

    v "I feel like, if I got more used to it, I might start to like it..."

    hide helio
    show mc happy at midleft
    show vivian neutral at midright

    mc "Then, maybe I should bring you to visit the place in-person one day!"

    show vivian surprised
    v "H-huh?"

    mc "The food is really great! I get along great with the servers too, they’re all super nice and friendly!"

    mc "They’d be super happy to have you there!"

    show vivian flustered
    v "Th... then, maybe we can go together..."

    hide mc
    hide vivian

    "Vivi’s blushing! I’m totally on the right track!"

    jump ch2_3


label ch2_c5:
    show mc neutral at midleft
    show helio angry at midright
    h "Hahhh... what do you want?"

    mc "Some of the sausage bits!"

    show helio neutral
    h "Got it. Give me a moment to cut them up and they’re yours."

    show mc surprised
    mc "Wait a second, I only said I wanted a bite! I don’t want them all! Heli!"

    h "Shut up and eat."

    mc "Mmpf!?"

    mc "Don’t (chews) just (chews) shove food in my mouth!"

    h "Shouldn’t you be grateful that I’m even offering you my food?"

    show mc neutral at left
    show vivian neutral at center
    show helio neutral at right

    v "You two... are extremely close, huh..."

    show mc happy
    mc "Because we’re best friends!"

    v "...best friends, huh...?"

    v "...are they scared to come out to a stranger...? But, they’re being so blatant about it... are they normally so flirty that they don’t even know what they’re doing...?"

    hide mc
    hide vivian
    hide helio

    "I didn’t catch what Vivi said there... Oh well! At least the atmosphere seems more lively now!"

    jump ch2_3


label ch2_c6:
    show mc happy at midleft
    show vivian neutral at midright
    v "...uh, no?"

    mc "Well, they are!"

    v "...thank you?"

    mc "Like, they’re so sharp and shiny... Just a nick and I’d bleed!"

    mc "They could probably pierce right through skin so easily...!"

    show vivian sad
    v "Th... thanks...?"

    mc "Hey, have you ever tried to bite a squirrel–"

    show mc sad at left
    show helio angry at right
    show vivian surprised at center
    with vpunch 

    mc "Youchies...!"

    h "I apologize profusely for the inappropriate behaviour and stark rudeness of my companion."

    h "They’ve been afflicted with an unfortunate condition called {i}‘stupidity’{/i} since they were young. We’re still trying to find out who dropped them as a baby."

    v "Oh, okay... I see..."

    mc "Hey...!"

    hide helio
    hide vivian
    hide mc

    "It’s super awkward now..."

    "I gulp down some of my pocket beer stash just to avoid saying anything worse...!"

    jump ch2_3

label ch2_3:
    menu:
        "Vivi, do you want the last piece?":
            $ VP += 1
            jump ch2_c7
        "Heli, you’ve got some crumbs on your cheek...":
            $ HP += 1
            jump ch2_c8
        "Sooooo, Vivi, are you a recent convert or old blood?":
            $ BE += 1
            jump ch2_c9

label ch2_c7:
    show mc neutral at midleft
    show vivian surprised at midright
    
    v "No, no, it’s fine! You can have it!"

    mc "But, I can’t just steal food from the host! It’s discourteous of me!"

    v "Just consider this a host’s kindness and accept it!"

    mc "I could never! Please, you’re the host, so take it!"

    show mc neutral at left
    show vivian surprised at center
    show helio neutral at right

    h "You two... are going to get trapped in an endless loop if you keep this up..."

    show mc happy at midleft
    show vivian neutral at midright
    hide helio

    mc "Yeah! So, you should just accept it, Vivi!"

    v "No, wait... I think I have a better idea."

    show vivian flustered
    v "If you’d like... can we, er, maybe... share it?"

    mc "Ehehe, that works!"

    hide mc
    hide vivian

    "Vivi is blushing... how cute!"

    jump ch2_4


label ch2_c8:
    show mc neutral at midleft
    show helio neutral at midright

    h "Hm? Where?"

    mc "Let me get that for you..."

    show helio flustered
    h "O-oi!"

    mc "There! All done!"

    h "...nnrgh, seriously, you...! Consider the time and place, would you?!"

    mc "Hm? But it’s only in the here and now that you’ve got crumbs on your cheek?"

    h "Not what I meant!"

    show mc neutral at left
    show vivian neutral at center
    show helio neutral at right

    v "...p-pardon my asking, but... what, exactly, is the relationship between you two...?"

    mc "We’re best friends, why?"

    v "...no reason."

    show helio flustered
    h "Grgh...!"

    hide mc
    hide vivian
    hide helio

    "I don’t really get it, but whatever! At least Vivi’s participating in the conversation!"

    jump ch2_4


label ch2_c9:
    show mc neutral at midleft
    show vivian surprised at midright
    v "...what?"

    mc "Y’know! When’d you become a bloodsucker! From birth or later!"

    mc "Did you have to give up your crosses? Are you sad that you’re forbidden from eating Italian food? Stuff like that!"

    v "Er.... I... don’t... know?"

    show mc neutral at left
    show vivian surprised at center
    show helio neutral at right

    h "...let’s just leave these questions alone for now."

    mc "Ehhhh, but I’m curious!"

    h "Just drop it."

    mc "Jeez... fine."

    show vivian sad
    v "Oh god is this a cult town is this why the rent was so cheap are they going to do rituals on me–"

    hide mc
    hide vivian
    hide helio
    
    "Hm...? Vivi seems more tense now..."

    "I wonder if I should share some of my pocket beer to help Vivi relax..."

    "I gulp down a bit of it as I ponder over this. Or, well, it might be more than a bit..."

    jump ch2_4

label ch2_4:
     menu:
        "Vivi, I hope you like it here!":
            $ VP += 1
            jump ch2_c10
        "Heli, I’m tired~":
            $ HP += 1
            jump ch2_c11
        "Have you ever been psychic attacked by flaming rats during the middle ages?":
            $ BE += 1
            jump ch2_c12

label ch2_c10:
    show mc happy at midleft
    show vivian surprised at midright
    v "A-ah, thank you...!"

    mc "I really mean it, you know!"

    mc "If you need any help getting adjusted, if you ever get lost, or even if you just want to hang out, talk to me! We’re right next door to each other, after all!"

    show vivian flustered
    v "...alright. Thank you..."

    show mc neutral at left
    show vivian neutral at center
    show helio neutral at right

    h "I won’t do nearly as much as this idiot, but I can help if I feel like it."

    show vivian happy
    v "...thanks."

    mc "Heli, you have to make him feel welcome! Be nicer!"

    h "My kindness is a finite spring. They should be lucky I’m even giving him a drop."

    show mc angry
    mc "Heli!"

    show vivian neutral
    v "I-it’s fine!!"

    show mc neutral
    v "I...I really appreciate it. Really."

    v "I was scared of moving, and really anxious about meeting people, but..."

    show vivian happy
    v "If everyone’s as nice as you, maybe things will turn out okay..."

    hide mc
    hide vivian
    hide helio

    "Awawawawa...that smile’s so sweet, I want to frame it on my wall!"

    jump ch2_5

label ch2_c11:
    show mc neutral at midleft
    show helio angry at midright
    h "Hah? And what do you want me to do about it?"

    mc "This!"

    show helio flustered
    h "Get your head off my lap!"

    mc "But it’s so comfy!"

    h "You just ate! What if you vomit all over my legs!?"

    mc "It’ll be fine~!"

    show mc neutral at left
    show vivian neutral at center
    show helio neutral at right    
    
    v "...are you two... normally like this?"

    show mc happy
    mc "Yeah! All the time!"

    show helio angry
    h "It’s just because this idiot doesn’t have a concept of shame or decorum!"

    v "R-right... okay..."

    hide mc
    hide vivian
    hide helio

    "The atmosphere has gotten pretty lively!"

    jump ch2_5

label ch2_c12:
    show mc neutral at midleft
    show vivian surprised at midright
    v "What?"

    mc "Because I’m plagued by burning thoughts of you!"

    show mc neutral at left
    show vivian neutral at center
    show helio neutral at right

    v "..."

    h "..."

    show mc sad
    mc "...no good?"

    show vivian sad
    v "I’m... mostly just confused."

    h "I saw a copy of ‘How to Talk to Human Beings’ in the bookstore a few days ago. Would you like me to get it for you?"

    hide mc
    hide vivian    
    hide helio

    "The atmosphere here is subglacial!"

    "Pocket vodka, help warm me up...!"

    "..I forgot I ran out earlier."

    "Sorrows, sorrows."

    jump ch2_5

label ch2_5:
    show mc neutral at left
    show vivian neutral at center    
    show helio neutral at right
    
    mc "So..."

    show mc happy
    mc "Heli~ we’ve got a new neighbor...! Vivian...congratulations! You’ve successfully survived the long and hard journey of physical labour!"

    v "Mhm, thank you again for your help! ...I-I don’t think I could’ve finished it so quickly alone."

    h "Don’t ever mention it. Ever."

    show mc neutral
    mc "I say this calls for a celebration!"

    v "Oh! Um, well.. Do you drink?"

    mc "Oh, {i}do I?!{/i} I'd die for some good alcohol."

    h "Drink in moderation, [playername]. Moderation."

    hide mc
    hide vivian
    hide helio

    scene black
    with fade

    jump ch3
