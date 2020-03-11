# krr_final_project

## **Project Documentation**

Group Members: \
Irinel Bandas, Chloe Brown, Kartik Kesavabhotla, and Jack Warshaw

[Slides from our final presentation can be found here.](https://docs.google.com/presentation/d/1I3tvXqGooKNRNcl3zhcLqX70YVkzf8nX0Mz07U5MxSE/edit?usp=sharing)

Our project is a character generator for the tabletop roleplaying game Dungeons & Dragons (5th edition).  To run this project, load the file `project_mt.krf` into Companions as a flatfile. Then, go to Browse KB, and in the query tab, enter a query of this format: `(getCharacter ?race ?class ?str ?dex ?con ?int ?wis ?cha <term1> <term2> <term3> <term4>)`. The query takes about 10-15 seconds to run. The terms can be any of the terms in our word bank, which is as follows:

| Word | Term in MT (enter this) |
| --- | --- |
| scary | Scary |
| hearty | Hearty |
| supernatural | Supernatural |
| acute | Acute |
| aware | Aware |
| quiet | Quiet |
| shadowy | Shadowy |
| Bear Grylls | BearGrylls |
| theology | Theology |
| magic | Magic |
| outdoorsy | Outdoorsy |
| silver tongue | SilverTongue |
| tradition | Tradition |
| beefy | Beefy |
| nimble | Nimble |
| lithe | Lithe |
| good liar | GoodLiar |
| finesse | Finesse |
| intuit | Intuit |
| storyteller | StoryTeller |
| strong | Strong |
| rune | Rune |
| charm | Charm |
| farm | Farm |
| edgy | Edgy |
| worldly | Worldy |
| wild | Wild |
| lie detector | LieDetector |
| doctor | Doctor |
| pick pocket | PickPocket |
| occult | Occult |
| muscular | Muscular |
| healer | Healer |
| tanky | Tanky |
| Sherlock Holmes | SherlockHolmes |
| Steve Irwin | SteveIrwin |
| politician | Politician |
| music | Music |
| old | Old |
| eagle eyed | EagleEyed |
| hippie | Hippie |


## **Representation**

Our microtheory contains representations for the following entity categories: Class, Race, PlayableRace, Stat, Skill, and Term. They are as follows:

**Terms** are the words in the word bank listed above. Two terms are associated with each Skill via the `associatedTerm` predicate.

**Skills** are the activities in D&D which a player character can roll for. These include things like Stealth, Investigation, Arcana, etc. We also added the Constitution and Caster skills, which are not official D&D skills, but which help us to determine a character's class. Each skill is associated with each class via the `ClassSkillValue` predicate. The value argument in this predicate ranges from -20 to 100 and represents how much a certain class is associated with a certain skill. Skills are also associated with Stats via the `associatedStat` predicate. This helps us to determine a character's race.

**Stats** are the broad categories in which a character can be gifted. The six stats in D&D are Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma. Stats are associated with classes via the `ClassStatValue` predicate. The value argument in this predicate ranges from -1 to 2 and represents how much a certain class is associated with a certain stat. Stats are also associated with Races via the `PrimaryStat` predicate. The value argument in this predicate ranges from 0 to 2 and represents how much a certain race is associated with a certain stat.

**Race** is the category for races found in D&D. **PlayableRace** is a subset of Race: Some races cannot be used for player characters themselves, but have subcategories which can be used for player characters. An example of this is the Elf race, which has the three subraces High Elf, Wood Elf, and Drow. A player can't choose to be just an Elf; they must choose to be one of the three elf subraces.

**Class** is most closely described as a character's profession. Classes include things like Wizard, Rogue, and Cleric.

## **Reasoning**

To determine a character's class from the four input terms, our microtheory has defined horn clauses which first find the four skills associated with the input terms, then find the sum of the ClassSkillValues for each class, and finally pick the highest summed value as the character's class.

To determine a character's stats, we first find the class. Then, we use ClassStatValues summed with the number of terms associated with each stat (via associatedTerm and associatedStat) to generate six stat "weights". These weights are not the exact stat values that would go on a D&D character sheet, but they do accurately represent which stats should be higher and which should be lower for a character.

To determine a character's race, we find the four stats associated with the input terms, then find the sum of the PrimaryStat values for each race, picking the highest valued race as the character's race. Because PrimaryStat values are less variable then ClassSkillValues, it is possible that you will get multiple possible Races in your query results.
