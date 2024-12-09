#Characters
define mc = Character("[playername]")
define v = Character("Vivian")
define h = Character("Helio")

#Character Variables
#HP stands for Helio Points, VP stands for Vivian Points
default HP = 0
default VP = 0

#Route Variables
#BE Stands for bad end
default BE = 0

default playername = "Silas"

#Layered Images

layeredimage mc:
    zoom 0.425
    always:
        "mc_base"

    group expressions:
        attribute angry:
            "mc_angry"

        attribute flustered:
            "mc_flustered"

        attribute happy:
            "mc_happy"

        attribute neutral:
            "mc_neutral"

        attribute sad:
            "mc_sad"

        attribute surprised:
            "mc_shocked"

layeredimage helio:
    zoom 0.425
    always:
        "heli_base"

    group expressions:
        attribute angry:
            "heli_angry"

        attribute flustered:
            "heli_flustered"

        attribute happy:
            "heli_happy"

        attribute neutral:
            "heli_neutral"

        attribute sad:
            "heli_sad"

        attribute surprised:
            "heli_surprised"

layeredimage vivian:
    zoom 0.425
    always:
        "vi_base"

    group expressions:
        attribute angry:
            "vi_angry"

        attribute flustered:
            "vi_flustered"

        attribute happy:
            "vi_happy"

        attribute neutral:
            "vi_neutral"

        attribute sad:
            "vi_sad"

        attribute surprised:
            "vi_surprised"

#Sprite Placements
transform midleft:
    xcenter 0.31
    yalign 1.0

transform midright:
    xcenter 0.70
    yalign 1.0