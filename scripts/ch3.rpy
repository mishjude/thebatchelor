#ROUTE TITLES

#ch3_H = Helios Route
#ch3_V = Vivian Route
#ch3_P = Poly Route
#ch3_BE = Bad End

label ch3:

  scene bg vi living room
  with fade

  if HP >= 3:
    jump ch3_H

  if VP >= 3:
    jump ch3_V

  if HP & VP >= 2:
    jump ch3_P

  if BE >= 4:
    jump ch3_BE

label ch3_BE:

  show helio neutral at center

  h "Now then, it’s late. I should bring this idiot home now."

  show mc happy at left

  mc "Ehehe~! Byeeeee, Vivi!"

  show vivian surprised at right
  with vpunch

  v "Whoa, are you okay?!"

  mc "Okay…? Of coursseee I’m okay!"

  h "Shit, [they_re] drunk…!"

  hide mc
  hide vivian
  hide helio

  "Hmmm…? Drunk… But it’s not my head that’s spinning…it’s the room, isn’t it?"
  
  "Ahhh…who cares..? This place feels nice…!"

  show mc happy at left
  show vivian sad at center
  show helio angry at right  
  
  mc "Huhh, what are you saying, Heli~? I’m to… *hic* totally fine!"

  h "{i}You are obviously not!{/i}"

  v "D-don’t yell…!"

  play music "bgm sad spooky track.ogg"

  show mc happy at midleft
  show vivian happy at midright
  hide helio

  v "Here, [playername], let me help you up…"

  "All of a sudden, I’m held by these warm and comfy arms…"

  "Whoa… it’s so comfy, I just want to lay down and take a nap…!"

  show vivian surprised

  v "H-huh?! You okay…!? You just slumped against me…!"

  show mc at left
  show vivian at center
  show helio angry at right

  h "Oi, get off of that guy! [playername]!!!"

  hide mc
  hide vivian
  hide helio

  "Ack…! It’s…so noisy…"

  "But, something smells… really good…"

  "A warm…heady scent…something that curls around something in my brain? Or is it my throat? It’s potent…so potent…and {i}so good.{/i}"

  "Ah…I can feel myself salivating…"

  "Somehow, it’s like there’s a cake in front of me, or maybe a marshmallow…!"

  "{i}...I want a bite!{/i}"

  show mc happy at left
  show vivian surprised at center
  show helio angry at right

  v "OW?! DID YOU JUST {i}BITE ME?!{/i}"
  with vpunch

  h "[playername]! Off!!! Get {i}off{/i}!!! Let him go!!! {i}Stop biting!!!!{/i}"

  "Ohhh, the jam inside tastes delicious! It’s so delicious, {i}it’s addicting~~!!{/i}"

  show vivian sad
  v "I, I’m getting… lightheaded…."

  h "Oh, suns and stars, you idiot…! I told you to drop him, didn’t I?!"

  mc "Oh, Heli… did you want to have some too…? The jam’s great!"

  h "Urgh…stars above, no–"

  h "...and I’m not helping you clean this up either, okay?!"

  mc "Okay~! More for me~!"

  scene black
  with fade

  "I ended up crashing for a week, waking up with a massive hangover, no calls from Heli, and the decomposing corpse of the guy I was hoping to invite to the festival…"
    
  "And that’s the story of how my attempt at asking Vivi out ended so badly, it had a body count."

  "If only I was smarter during that dinner date…!"

  "BAD END"

  jump demo_text

label ch3_H:

  show mc neutral at midleft
  show helio neutral at midright
  
  h "(yawn) Argh… I’m tired…" 

  mc "Oh! Should I bring you home?!"

  "I start to stand instantly, but Helios pushes my shoulder down before I even leave my chair. Ack! I forgot how strong he was…!"

  "I pout indignantly up at him, just to make sure my disapproval is known! Take that, you sunfish!"

  "Before I can ask what’s going on, he hisses a secret message to me–"

  h "Idiot, I’m {i}giving you an opportunity!{/i} You actually seem to be {i}getting along{/i} with this guy, so ask him to the ball while I’m gone!"

  mc "Oh… {i}Oh{/i}! Right!"

  "Whoopsies…false alarm."

  "Heli, my most beloved friend…how could I ever have doubted your boundless loyalty! I will make sure to take this dream you have entrusted to me and make it a reality!"

  "Heli gives me a withering look like he doesn't like what I’m thinking."

  "...sometimes I think he can read my mind. Sorry, Heli."

  show mc at left
  show vivian neutral at center
  show helio at right

  h "So, anyways, I’m going."

  v "Ah, bye…"

  h "My sincerest thanks for permitting my stay for so long. I must ask that you continue caring for my companion."

  v "R-right! Yeah!"

  hide helio
  show mc at midleft
  show vivian at midright
  
  "Heli gives a short nod of his head, before heading out the door."

  "His exit is nothing short of plain— which is funny, because usually Heli can be pretty dramatic about leaving me!"

  "It’s just me and Vivi now… I gotta ask them now or never…! But, how do I do that…!?"

  "Even though I can already hear Heli’s voice yelling that I always jump into things without thinking, I blurt out the first thing that comes to mind."
    
  mc "You’re really hot!"

  v "Uh, thanks?"

  "...this may have been a mistake."

  "Come on, [playername]! You gotta salvage this somehow! What's something about your hot neighbor— {i}other{/i} than their face— that you think is cool."

  mc "Er, well, I mean… you look really good in that outfit! I love the ribbons! Adds some flair to the Victorian aesthetic!"

  v "Oh, thanks."

  mc "Say, do you like dressing in fancy formalwear a lot?"

  v "I… guess?"

  show mc happy
  mc "Then, I’ve got an opportunity for you! My family’s throwing this get-together later this week, it’s the perfect chance to wear a fancy outfit and show off!"

  show vivian surprised
  show mc sad
  v "U-um, I don’t really know…"

  show vivian neutral
  v "Not that I’m saying I wouldn’t love to go, but…! My hand-me-downs would probably be really out of place in that kind of party…!"

  "Hand-me-downs…?! Vivian thinks their style is hand-me-down’s?"
  
  "Vivian’s soft hair frames their face like a baroque portrait— the dark and dramatic shadow bringing out the beautifully bright light— and their gentle lips are purses in something between contemplation and something akin to worry. All in all, they’re beyond picturesque."
  
  "I step towards them, quickly grasping their hands in mine. Words come quickly to me— they need to know!"

  show mc happy
  mc "Don’t be silly! You’re like, ‘hwa-BAM!’ and ‘ba-BOOM!’, looks-wise {i}and{/i} personality-wise!"

  mc "You could go in your curtains and still have hordes of admirers!"

  show vivian flustered

  "Vivian’s face blooms into a stunning shade of scarlet as his eyes flutter wide with surprise. He looks at me with doe-like eyes, then blinks all-too-eager quickly and looks away, like he can't meet my gaze."

  v "Th-that’s going too far, isn’t it?!"

  "They’re sweet, so sweet. He’s kind and thoughtful— and I can't help but want to make it clear how lovely he is."

  "I wrap my arms around him and pull him into a gentle hug. Vivian seems stunned for a moment, before laughing lightly, hugging back."

  show mc neutral
  mc "You're cool, you know! Like, seriously cool!"

  show vivian sad
  v "...ah, man…you don't mean that…!"

  mc "Jeez, I mean it, y’know?! If you keep denying my praise, I’ll bite you!"

  v "But, I’m not actually that–"

  "Honestly! If he's not gonna take me seriously, then I suppose I have to follow through, don't I?"
  
  "I lean my head on Vivian’s shoulder, light and comfy, and gently nip at the nape of his neck, fangs grazing skin and—"

  show vivian surprised
  v "-OW?! YOU ACTUALLY BIT ME?!"
  with vpunch

  mc "Because you wouldn’t stop being self-depreciating!"

  "There's nothing wrong with a little affection between friends, right? Besides, it's not like I can do it with Heli without burning the inside of my mouth. There's nothing harmful about it—"

  v "I think I’m actually bleeding!?"

  mc "Eh, you’ll be fine after drinking some blood."

  "There’s nothing harmful about it…"

  "...for vampires."

  "My heart sinks in my chest. I stare at Vivian, the loud thumping reverberating in my ears— and there it is, a little rivulet of blood trickling down his neck. His neck is untouched, unblemished, unmarried by anything but that scarlet streak…"

  "...and a fresh puncture wound."

  mc "...wait, did you say you’re bleeding?"

  show vivian angry
  v "{i}{b}YES?!{/b}{/i}"

  mc "Oh, that… that means that you were… oh."

  v "Oh?!?!"

  mc "..That’s probably bad!"

  v "Probably? It hurts…! Why does it hurt so much, wasn't it just a scratch?"

  mc "So…uhm…quick crash course!"

  mc "...have you ever heard of…vampires?"

  v "Yes, I have heard of vampires, but is now really the time to—"

  mc "So, about that…"

  show vivian sad
  v "...no. {i}They're not real.{/i}"

  mc "...I mean…"

  v "...oh no."

  show mc sad
  mc "...kinda hard to argue that one…when…you…uhhhh…"

  mc "...when you might be turning into one."

  v "...please tell me you're joking."

  "I since, watching Vivian bring one hand up to his neck to stem the bleeding. Not that it'll do anything…"

  "I can feel my head spin— the scene unfolding in front of me right now absolutely, definitely, most certainly wasn't supposed to happen!"

  jump demo_text


label ch3_V:

  show mc neutral at midleft
  show helio neutral at midright
  
  mc "Shoo! Shoo! Heli, let me talk to them one-on-one, won't ya?"

  h "...If you do {i}anything{/i} inappropriate, I'll personally give you a one way ticket to the afterlife."

  mc "I've escaped death once, I can do it again!"

  mc "...ah, maybe that isn't something I should joke about...anyways!"

  "Heli opens his mouth to argue but is swiftly ushered outside the door."

  mc "Bye-bye Heli~! I'll talk to you when the sun rises."

  h "{i}You've got to be kidding–{/i}"

  show mc at center
  hide helio

  "The door slams shut, effectively cutting off any scolding Heli might have been about to launch into. Oops!"

  mc "Now, where were we?"

  show mc neutral at midleft
  show vivian neutral at midright

  v "...uhm? We were…at…the dinner table?"

  show mc happy
  mc "That we were! But I’m also interested in where we’re going…"

  show vivian flustered
  v "...going?"

  "Vivian looks a little flustered and a touch sheepish at the fact that they don’t seem to be fully getting what’s going on here. Everything about him seems…so adorable, doesn’t it?"

  "In the dark cover of the night, there’s only the fixtures we’ve managed to set up within this room, and the pale light of the moon that filters through the half-open curtains."

  "Vivian fidgets with his shirt, looking at me and then looking away. He looks like he wants to say something, but has nothing to say– and to answer him I take quick steps from the door to the dining table to stand next to Vivian again."

  show mc neutral
  mc "{i}Hello{/i}, you."

  show vivian neutral
  v "...uhm...hi?"

  mc "It’s been a long day, hasn’t it? With, y’know, packing and unpacking and all that?"

  "I take one of Vivian’s hands in mine. Their eyes flutter down to the unexpected gesture, and then back up to settle on my face."

  mc "C’mon, let’s rest for a bit! There’s nothing like a little bit of downtime to get your spirits lifted right up!"

  "With a light tug, Vivian seems to follow through, and we both end up on the couch. Perhaps to give him courage, Vivian drags the bottle along with him."

  mc "I've been meaning to ask— that painting we put up over there—"

  v "—ah, uhm…that's…!"

  mc "—it’s totally avant-garde! I mean, like, is the artist a genius or what! Ooooh, I just love the composition, you know!"

  mc "It's impeccably bold! That splatter! The vacant scribbles! The swirls of color! The handprints!"

  "Vivian looks a touch stunned at my statement, before a fond smile comes across his face."

  show vivian happy
  v "...ahaha, thank you…! It's…well…my siblings and I made it together before I moved out."

  v "They said, and I quote, that I would ‘wither away without their delightful presences’...and so, we sat down one afternoon and…well…there you have it."

  mc "And here I thought this painting couldn't get more fascinating…"

  mc "It's beautiful, Vivian…"

  v "...it…it really is."

  "For a moment, I'm too caught up in the beautifully somber look on Vivian's face as he seems to grapple with the idea of what to say."

  "Just as I remember to tear my eyes away from that beautiful face…Vivian suddenly reaches for the bottle to take a big gulp before turning around to look at me!"

  show vivian neutral
  v "...hey, [playername]..."

  v "...thanks for…coming over tonight…and…you know…being there."

  show mc happy
  mc "...! It was my pleasure! Although, you know, we basically invited ourselves in, hehe!"

  v "...and I’m glad you did."

  v "I…uhm…well…there's no easy way to say this…but…I was kinda dreading being alone tonight."

  v "I dunno…I've just spent all my life with my siblings and…well…the quiet is a little…"

  v "...well, I suppose it would remind me that…I was well and truly on my own."

  v "...but…you know…I wasn't…"

  v "...so…thank you, [playername]."

  show mc sad
  "I can feel my eyes welling up with tears…what the heck! Vivian…if you make a face like that…I…"

  "I surge forward, wrapping Vivian in a tight hug. He stiffens, surprised, for a second— but then slowly relaxes, letting out a soft chuckle as his arms wrap around me in turn."

  mc "Oh, Vivian…!"

  show mc happy
  mc "Hear, hear! A toast! To my {i}dashing{/i} new neighbor!"

  v "...! Do I…really…have to say that….?"

  mc "Hmmm, not really? But it would be fun, wouldn't it! Maybe you'd even laugh at something so ridiculous…"

  show mc neutral
  mc "You'd look pretty when you laugh…but you look pretty now, so that's a total no-brainer!"

  show vivian flustered
  v "...ah— I mean— uhm…thank you…?"

  v "...I don't really know what to say to these sorts of things."

  mc "Really? I figured you were the type that totally got fawned over, you know? I mean— the Victorian look is to {i}die{/i} for, right? And who {i}doesn’t{/i} love a charming personality?"

  v "...we’ve only just met, you know."

  mc "I know! But I also know that I’m having so much fun— and that's because I’m with you!"

  "...oh my goodness, is he just naturally this charming?"

  "My heart is beating so fast— this night is so beautiful, isn't it? The way Vivian smiles at me…the way the brilliant light of the moon flickers across his features…"

  v "...and, you know…I’m grateful to be here…with you."

  "Vivian tilts his head away from me, cheeks flushed. I lean forward, gently steadying a hand against the nape of his neck."
  
  show mc flustered
  mc "...Vivian…I'm…grateful to be here…too…"

  "With a gentle touch, I let my lips press against his neck, fangs scraping into the soft skin, right where…"
  
  show vivian surprised
  v "...?!"

  "Wait…"

  v "...did you just…?"

  show mc surprised
  "There's blood in my mouth. Vivian is bleeding."

  "As I stare, horrified, at Vivian’s neck— it's true. There's no mark there."

  "The taste of blood— sweet, oh so sweet— is acrid in my mouth. Vivian holds one hand to his neck in shock."

  mc "...I…you're…you're not…?"

  v "...?! It stings…?"

  mc "...you're…you’re not a vampire?"

  v "What? No! That's ridiculous…! Vampires aren't real!"

  mc "...uhm…so…"

  v "...oh."

  mc "...about that…"

  show vivian sad
  v "...oh no."

  show mc sad
  mc "I…may have {i}something{/i} to tell you."

  v "...you {i}bit{/i} me."

  "I did…and now…"

  "My heart thrums against my guilty ribcage, and I can feel my head swim. There’s so much to fix here…like, seriously…"

  "...this wasn't how this night was supposed to go at all!"

  jump demo_text

label ch3_P:

  show helio neutral

  h "It’s getting pretty late… I’ve probably overstayed my welcome."

  "When Heli mentions that, I realise that the moon’s pretty much overhead! It is pretty late…for him, at least."

  "It's basically like midday for me, but a sun elf is a sun elf! It's a wonder he’s awake, actually. He mentioned it to me once. Something about a rhythm of cicadas, or circuses, or something like that…"

  "Anyways! Vivian shakes his head, smiling at us gently; the previous train of though is unimportant in the face of this smile."

  show mc neutral at left
  show vivian happy at center
  show helio neutral at right

  v "N-no! The two of you, you’re both welcome to stay as long as you like!"

  show mc happy
  mc "Eh~? What if we said we wanted to stay all night, then?"

  h "Then I’ll drag you to your house by the hair."

  show vivian neutral
  v "You don’t have to do that…! I, um,  if you’re okay with the couch…"

  show mc neutral
  v "No, I’ll just sleep on the couch! You guys can take the bed!"

  h "No. I refuse to impose on the host, that's entirely impolite. I’ll take the couch…"

  "Heli shakes his head firmly, refusing to abandon his principles. He's always like that— when he figured out his rules for things, he basically sticks to them forever. He's always a good host and a great guest— super polite! That's my Heli!"

  h "... and [playername] can sleep on the floor."

  "Nevermind! He's also a meanie!"

  show mc sad
  mc "Huh!? Why should I sleep on the floor?!"

  h "Since you’re so low to the ground already, shouldn’t it feel like home?"

  show mc angry
  mc "Maybe Vivi should make you sleep on the roof, then! Since you're so full of hot air!"

  show vivian sad
  "Vivian seems a little bit frantic, his eyes darting around the room and his fidgeting hands as he tries to iron out the details while he watches us row. Oopsies…! His thumb worries over the skin by cuticles as he thinks."

  v "I-I wouldn’t make either of you sleep there! Please, take the bed!"

  h "Absolutely not. It’s rude to force the host out of their own bed."

  show mc happy
  mc "Yeah! I’ll take the couch, and Heli can sleep in a tree!"

  h "I’ll take the couch."

  show vivian neutral
  v "Er, well, you could always… share?"

  show helio angry
  h "...hah?"

  show mc sad
  mc "No way~! Heli would set me on fire! We need a barrier between us!!"

  v "I have, uh, like two pillows? If that works for you?"

  show mc neutral
  show helio neutral
  mc "..."

  h "..."

  mc "There’s no way that’d work…"

  "But then, I get a new idea."

  mc "Buuuuut, I just spotted something that could work as a great barrier!"

  v "...?"

  show helio angry
  "Looking at me with mild irritation, Heli’s eyes follow my gaze, only to pause. He gives me a look like he can't believe the stuff I’m saying. Which is a very common look, unfortunately."

  h "...wait, are you serious?"

  show mc happy
  mc "Ehehe, of course!!"

  show vivian surprised
  v "H-huh? What?"

  mc "Let’s go!!"

  hide mc
  hide vivian
  hide helio
  
  "Looping one hand around Vivian and using the other to grab Heli’s hand, I pull the two of them onto the couch. Newly unpacked!"

  "Helio takes the right arm of the chair— as he always does— and Vivian sits down by him. Nice! Now I’m safe from a fiery attack, and Heli would never attack anyone else. He's just nice like that."

  "As I talk to Vivian about the latest issue of my favourite fashion magazine, Heli’s quips get increasing smaller and more infrequent…until they finally disappear."

  "Peering over Vivian’s shoulder, I can see that Heli’s fallen fast asleep! Somehow, while we were talking, he'd managed to curl into a ball and end up with his head on Vivian’s lap."

  "Most of the lights are turned down pretty low, and…man…I know elves are pretty ethereal, but sometimes I forget just how beautiful my best friend is."

  "Combined with Vivian, who reflexively runs a gentle hand through Heli’s long blonde hair, it's a wonderful sight…almost too perfect!"

  show mc neutral at midleft
  show vivian neutral at midright
  v "Heli… er, Lord Helios… he sure fell asleep fast."

  mc "Ehehe, when the sun goes down, so do his energy levels. He was bound to crash sooner than later."

  "I’m so tempted to poke and tease Heli, but that’d ruin the moment."

  "He’s normally so serious and angry, so ruining his cuteness is forbidden! Especially since it’s a rare shot of him sleeping on Vivi’s lap!"

  mc "That said… you’re really, really sure about letting me and Heli stay over? I can drag Heli home if you want us to leave you in peace."

  v "N-no, um… Actually, I really wanted you two to stay."

  v "My family home, it’s a lot livelier, so I’m not really used to an empty house…"

  show vivian happy
  v "Having both of you over… it made me feel really happy…"

  v "A-and, well, I know it’s stupid, but…"

  show vivian neutral
  v "...never mind."

  mc "Hey, that’s unfair~ Tell me…!"

  show vivian flustered
  v "It’s embarrassing…!"

  show mc happy
  mc "Even so, I wanna know~"

  v "...I just… wanted the night to last a bit longer…"

  show mc neutral
  show vivian neutral
  mc "Oh…! I get it…!!"

  v "You do…?"

  mc "It’s like when you’re a kid at a sleepover, right? Staying up later than you’re supposed to is forbidden excitement…!"

  v "...um. I don’t think that’s… actually, that’s close enough, I think."

  mc "Then, let’s fulfill our childhood fantasies and chat all night~! If you drift off, I’ll bite ya~!"

  show vivian happy
  v "Ahaha… sure."

  hide mc
  hide vivian

  "For what feels like a long while, we exchange hushed whispers and giggles under a shared blanket."

  "We hold our breath whenever it feels like we’re going to wake Heli up, but it’s still tempting to wake him up so he can join in on our fun…"

  "Even though it’s so fun, eventually, Vivi starts getting more and more sluggish."

  "He looks so sweet drifting off like this— the moonlight is kind to his pretty features. Though, I suppose this is just how it is for handsome dudes…so lucky! I wanna caress that pretty face too, moonlight!"

  "Still, I know I ought to let him sleep soon, but… my mischievous heart can’t resist!"

  show mc neutral at midleft
  show vivian neutral at midright

  mc "You’re falling asleep, aren’t you?"

  v "E-eh? No, I’m not… I can still keep going…"

  show mc happy
  mc "Li~aaaar. I can see your eyelids drooping, you know?"

  "I lean in close, pressing a finger to Vivi’s lips. They're soft to the touch— and the way his eyes flutter open with sudden surprise, I can't help the grin that grows on my face."

  mc "You’re so defenseless, I could probably get a sneak attack in and you wouldn’t be able to stop me~!"

  show vivian flustered
  v "E-eh? What kind of sneak attack…!?"

  show mc neutral
  mc "What kind~? This one, obviously!"

  "I wrap my arms around Vivian, tugging him close in a tight hug, nuzzling my face against his comfy shoulder. I can't help the little giggle that slips past my lips."

  "With a gentle touch, I let my lips press against his neck, fangs scraping into the soft skin, right where…)"

  show vivian surprised
  v "Ah?! You bit me!?"

  show mc happy
  mc "I warned you, didn’t I~? If you drift off, I’ll bite you!"

  show vivian angry
  v "I thought that was a joke! That actually hurt!?"

  show mc neutral
  mc "Ehhh, even though I bit you so gently?"

  v "Your teeth are so sharp…!?"

  show mc happy
  mc "Obviously~! They’re a vampire’s pride and joy, after all!"

  show vivian surprised
  v "...eh? Vampire?"

  show mc neutral
  mc "Yeah? Did you think I was a fairy or elf like Heli or something?"

  v "N-no! I thought you were a human, like me!"

  mc "Ahaha, don’t be silly! Humans haven’t lived in this town in decades other than granny Maggie, the most recent one was like, er, how long ago was it, actually…?"

  show vivian sad
  v "...today. When I moved in."

  mc "...eh? Seriously?"

  v "...yeah."

  mc "And I, uh, bit you?"

  v "You did."

  show mc sad
  mc "...oh no. Heli’s going to kill me."

  hide mc
  hide vivian  
  
  "I can feel my head spin— the scene unfolding in front of me right now absolutely, definitely, most certainly wasn't supposed to happen!"

  show helio surprised

  "And it is at that precise moment that, even though he slept through hours of gossiping and screaming, Heli suddenly jolts up."

  "He takes one look at me, then at the blood dripping down Vivi’s neck, and lets out a deep, deep, deep sigh."

  h "I woke up because I suddenly felt like you fucked up, but I didn’t think it’d be that bad!"

  jump demo_text

label demo_text:
  
  scene black
  with fade
  
  "Thanks for playing, you've reached the end of the demo! Stay tuned for the full release of The Batchelor coming soon!"

  return