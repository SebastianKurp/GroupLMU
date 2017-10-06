from search import *
from report_by_symbol import *
from topological_sort import *

def showResult(info,result):
    print('\n>>>> ' + info + ' <<<<\n')
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j])

def main():
    fileContents = ["""
!cousin
Dear Merrys:--As a subject appropriate to the season, I want to tell you about a New Year's breakfast which I had when I was a little girl. What do you think it was? A slice of dry bread and an apple. This is how it happened, and it is a true story, every word.
As we came down to breakfast that morning, with very shiny faces and spandy clean aprons, we found father alone in the dining-room.
"Happy New Year, papa! Where is mother?" we cried.
"A little boy came begging and said they were starving at home, so your mother went to see and--ah, here she is."
As papa spoke, in came mamma, looking very cold, rather sad, and very much excited. #excited
"Children, don't begin till you hear what I have to say," she cried; and we sat staring at her, with the breakfast untouched before us.
"Not far away from here, lies a poor woman with a little new-born baby. Six children are huddled into one bed to keep from freezing, for they have no fire. There is nothing to eat over there; and the oldest boy came here to tell me they were starving this bitter cold day. My little girls, will you give them your breakfast, as a New Year's gift?"
We sat silent a minute, and looked at the nice, hot porridge, creamy milk, and good bread and butter; for we were brought up like English children, and never drank tea or coffee, or ate anything but porridge for our breakfast.
"I wish we'd eaten it up," thought I, for I was rather a selfish child, and very hungry.
"I'm so glad you come before we began," said Nan, cheerfully. ^hour
"May I go and help carry it to the poor, little children?" asked Beth, who had the tenderest heart that ever beat under a pinafore.
"I can carry the lassy pot," said little May, proudly giving the thing she loved best.
"And I shall take all the porridge," I burst in, heartily ashamed of my first feeling. #porridge
"You shall put on your things and help me, and when we come back, we'll get something to eat," said mother, beginning to pile the bread and butter into a big basket.
We were soon ready, and the procession set out. First, papa, with a basket of wood on one arm and coal on the other; mamma next, with a bundle of warm things and the teapot; Nan and I carried a pail of hot porridge between us, and each a pitcher of milk; Beth brought some cold meat, May the "lassy pot," and her old hood and boots; and Betsey, the girl, brought up the rear with a bag of potatoes and some meal.
Fortunately it was early, and we went along back streets, so few people saw us, and no one laughed at the funny party.
What a poor, bare, miserable place it was, to be sure,--broken windows, no fire, ragged clothes, wailing baby, sick mother, and a pile of pale, hungry children cuddled under one quilt, trying to keep warm. How the big eyes stared and the blue lips smiled as we came in!
"Ah, mein Gott! it is the good angels that come to us!" cried the poor woman, with tears of joy.
"Funny angels, in woollen hoods and red mittens," said I; and they all laughed. ^camel
Then we fell to work, and in fifteen minutes, it really did seem as if fairies had been at work there. Papa made a splendid fire in the old fireplace and stopped up the broken window with his own hat and coat. Mamma set the shivering children round the fire, and wrapped the poor woman in warm things. Betsey and the rest of us spread the table, and fed the starving little ones.
"Das ist gute!" "Oh, nice!" "Der angel--Kinder!" cried the poor things as they ate and smiled and basked in the warm blaze. We had never been called "angel-children" before, and we thought it very charming, especially I who had often been told I was "a regular Sancho." What fun it was! Papa, with a towel for an apron, fed the smallest child; mamma dressed the poor little new-born baby as tenderly as if it had been her own. Betsey gave the mother gruel and tea, and comforted her with assurance of better days for all. Nan, Lu, Beth, and May flew about among the seven children, talking and laughing and trying to understand their funny, broken English. It was a very happy breakfast, though we didn't get any of it; and when we came away, leaving them all so comfortable, and promising to bring clothes and food by and by, I think there were not in all the hungry little girls who gave away their breakfast, and contented themselves with a bit of bread and an apple of New Year's day.
Testing the search for when, let's see
    """,
    """
!hour
Knowing that Mrs. Mallard was afflicted with a heart trouble, great care was taken to break to her as gently as possible the news of her husband's death. @mallard
It was her sister Josephine who told her, in broken sentences; veiled hints that revealed in half concealing. Her husband's friend Richards was there, too, near her. It was he who had been in the newspaper office when intelligence of the railroad disaster was received, with Brently Mallard's name leading the list of "killed." He had only taken the time to assure himself of its truth by a second telegram, and had hastened to forestall any less careful, less tender friend in bearing the sad message. ^time
She did not hear the story as many women have heard the same, with a paralyzed inability to accept its significance. She wept at once, with sudden, wild abandonment, in her sister's arms. When the storm of grief had spent itself she went away to her room alone. She would have no one follow her.
There stood, facing the open window, a comfortable, roomy armchair. Into this she sank, pressed down by a physical exhaustion that haunted her body and seemed to reach into her soul.
She could see in the open square before her house the tops of trees that were all aquiver with the new spring life. The delicious breath of rain was in the air. In the street below a peddler was crying his wares. The notes of a distant song which someone was singing reached her faintly, and countless sparrows were twittering in the eaves.
There were patches of blue sky showing here and there through the clouds that had met and piled one above the other in the west facing her window.
She sat with her head thrown back upon the cushion of the chair, quite motionless, except when a sob came up into her throat and shook her, as a child who has cried itself to sleep continues to sob in its dreams.
She was young, with a fair, calm face, whose lines bespoke repression and even a certain strength. But now there was a dull stare in her eyes, whose gaze was fixed away off yonder on one of those patches of blue sky. It was not a glance of reflection, but rather indicated a suspension of intelligent thought.
There was something coming to her and she was waiting for it, fearfully. What was it? She did not know; it was too subtle and elusive to name. But she felt it, creeping out of the sky, reaching toward her through the sounds, the scents, the color that filled the air.
Now her bosom rose and fell tumultuously. She was beginning to recognize this thing that was approaching to possess her, and she was striving to beat it back with her will--as powerless as her two white slender hands would have been. When she abandoned herself a little whispered word escaped her slightly parted lips. She said it over and over under the breath: "free, free, free!" The vacant stare and the look of terror that had followed it went from her eyes. They stayed keen and bright. Her pulses beat fast, and the coursing blood warmed and relaxed every inch of her body.
She did not stop to ask if it were or were not a monstrous joy that held her. A clear and exalted perception enabled her to dismiss the suggestion as trivial. She knew that she would weep again when she saw the kind, tender hands folded in death; the face that had never looked save with love upon her, fixed and gray and dead. But she saw beyond that bitter moment a long procession of years to come that would belong to her absolutely. And she opened and spread her arms out to them in welcome.
There would be no one to live for during those coming years; she would live for herself. There would be no powerful will bending hers in that blind persistence with which men and women believe they have a right to impose a private will upon a fellow-creature. A kind intention or a cruel intention made the act seem no less a crime as she looked upon it in that brief moment of illumination.
And yet she had loved him--sometimes. Often she had not. What did it matter! What could love, the unsolved mystery, count for in the face of this possession of self-assertion which she suddenly recognized as the strongest impulse of her being!
"Free! Body and soul free!" she kept whispering. #quiet
Josephine was kneeling before the closed door with her lips to the keyhole, imploring for admission. "Louise, open the door! I beg; open the door--you will make yourself ill. What are you doing, Louise? For heaven's sake open the door."
"Go away. I am not making myself ill." No; she was drinking in a very elixir of life through that open window.
Her fancy was running riot along those days ahead of her. Spring days, and summer days, and all sorts of days that would be her own. She breathed a quick prayer that life might be long. It was only yesterday she had thought with a shudder that life might be long.
She arose at length and opened the door to her sister's importunities. There was a feverish triumph in her eyes, and she carried herself unwittingly like a goddess of Victory. She clasped her sister's waist, and together they descended the stairs. Richards stood waiting for them at the bottom.
Someone was opening the front door with a latchkey. It was Brently Mallard who entered, a little travel-stained, composedly carrying his grip-sack and umbrella. He had been far from the scene of the accident, and did not even know there had been one. He stood amazed at Josephine's piercing cry; at Richards' quick motion to screen him from the view of his wife.
When the doctors came they said she had died of heart disease--of the joy that kills. #medicine
    """,
    """
!camel
NOW this is the next tale, and it tells how the Camel got his big hump.
In the beginning of years, when the world was so new and all, and the Animals were just beginning to work for Man, there was a Camel, and he lived in the middle of a Howling Desert because he did not want to work; and besides, he was a Howler himself. So he ate sticks and thorns and tamarisks and milkweed and prickles, most 'scruciating idle; and when anybody spoke to him he said 'Humph!' Just 'Humph!' and no more.
Presently the Horse came to him on Monday morning, with a saddle on his back and a bit in his mouth, and said, 'Camel, O Camel, come out and trot like the rest of us.'
'Humph!' said the Camel; and the Horse went away and told the Man. @camel
Presently the Dog came to him, with a stick in his mouth, and said, 'Camel, O Camel, come and fetch and carry like the rest of us.'
'Humph!' said the Camel; and the Dog went away and told the Man. @man
Presently the Ox came to him, with the yoke on his neck and said, 'Camel, O Camel, come and plough like the rest of us.'
'Humph!' said the Camel; and the Ox went away and told the Man.
At the end of the day the Man called the Horse and the Dog and the Ox together, and said, 'Three, O Three, I'm very sorry for you (with the world so new-and-all); but that Humph-thing in the Desert can't work, or he would have been here by now, so I am going to leave him alone, and you must work double-time to make up for it.' ^time
That made the Three very angry (with the world so new-and-all), and they held a palaver, and an indaba, and a punchayet, and a pow-wow on the edge of the Desert; and the Camel came chewing on milkweed most 'scruciating idle, and laughed at them. Then he said 'Humph!' and went away again.
Presently there came along the Djinn in charge of All Deserts, rolling in a cloud of dust (Djinns always travel that way because it is Magic), and he stopped to palaver and pow-pow with the Three.
'Djinn of All Deserts,' said the Horse, 'is it right for any one to be idle, with the world so new-and-all?'
'Certainly not,' said the Djinn.
'Well,' said the Horse, 'there's a thing in the middle of your Howling Desert (and he's a Howler himself) with a long neck and long legs, and he hasn't done a stroke of work since Monday morning. He won't trot.'
'Whew!' said the Djinn, whistling, 'that's my Camel, for all the gold in Arabia! What does he say about it?'
'He says "Humph!"' said the Dog; 'and he won't fetch and carry.'
'Does he say anything else?'
'Only "Humph!"; and he won't plough,' said the Ox.
'Very good,' said the Djinn. 'I'll humph him if you will kindly wait a minute.' #excited
The Djinn rolled himself up in his dust-cloak, and took a bearing across the desert, and found the Camel most 'scruciatingly idle, looking at his own reflection in a pool of water.
'My long and bubbling friend,' said the Djinn, 'what's this I hear of your doing no work, with the world so new-and-all?'
'Humph!' said the Camel.
The Djinn sat down, with his chin in his hand, and began to think a Great Magic, while the Camel looked at his own reflection in the pool of water.
'You've given the Three extra work ever since Monday morning, all on account of your 'scruciating idleness,' said the Djinn; and he went on thinking Magics, with his chin in his hand.
'Humph!' said the Camel.
'I shouldn't say that again if I were you,' said the Djinn; you might say it once too often. Bubbles, I want you to work.'
And the Camel said 'Humph!' again; but no sooner had he said it than he saw his back, that he was so proud of, puffing up and puffing up into a great big lolloping humph.
'Do you see that?' said the Djinn. 'That's your very own humph that you've brought upon your very own self by not working. To-day is Thursday, and you've done no work since Monday, when the work began. Now you are going to work.'
'How can I,' said the Camel, 'with this humph on my back?'
'That's made a-purpose,' said the Djinn, 'all because you missed those three days. You will be able to work now for three days without eating, because you can live on your humph; and don't you ever say I never did anything for you. Come out of the Desert and go to the Three, and behave. Humph yourself!'
And the Camel humphed himself, humph and all, and went away to join the Three. And from that day to this the Camel always wears a humph (we call it 'hump' now, not to hurt his feelings); but he has never yet caught up with the three days that he missed at the beginning of the world, and he has never yet learned how to behave.
    """,
    """
!time
The most notable thing about Time is that it is so purely relative. A large amount of reminiscence is, by common consent, conceded to the drowning man; and it is not past belief that one may review an entire courtship while removing one's gloves.
That is what Trysdale was doing, standing by a table in his bachelor apartments. On the table stood a singular-looking green plant in a red earthen jar. The plant was one of the species of cacti, and was provided with long, tentacular leaves that perpetually swayed with the slightest breeze with a peculiar beckoning motion.
Trysdale's friend, the brother of the bride, stood at a sideboard complaining at being allowed to drink alone. Both men were in evening dress. White favors like stars upon their coats shone through the gloom of the apartment.
As he slowly unbuttoned his gloves, there passed through Trysdale's mind a swift @trysdale, scarifying retrospect of the last few hours. It seemed that in his nostrils was still the scent of the flowers that had been banked in odorous masses about the church, and in his ears the lowpitched hum of a thousand well-bred voices, the rustle of crisp garments, and, most insistently recurring, the drawling words of the minister irrevocably binding her to another.
From this last hopeless point of view he still strove, as if it had become a habit of his mind, to reach some conjecture as to why and how he had lost her. Shaken rudely by the uncompromising fact, he had suddenly found himself confronted by a thing he had never before faced --his own innermost, unmitigated, arid unbedecked self. He saw all the garbs of pretence and egoism that he had worn now turn to rags of folly. He shuddered at the thought that to others, before now, the garments of his soul must have appeared sorry and threadbare. Vanity and conceit? These were the joints in his armor. And how free from either she had always been--But why--
As she had slowly moved up the aisle toward the altar he had felt an unworthy, sullen exultation that had served to support him. He had told himself that her paleness was from thoughts of another than the man to whom she was about to give herself. But even that poor consolation had been wrenched from him. For, when he saw that swift, limpid, upward look that she gave the man when he took her hand, he knew himself to be forgotten. Once that same look had been raised to him, and he had gauged its meaning. Indeed, his conceit had crumbled; its last prop was gone. Why had it ended thus? There had been no quarrel between them, nothing--
For the thousandth time he remarshalled in his mind the events of those last few days before the tide had so suddenly turned.
She had always insisted upon placing him upon a pedestal, and he had accepted her homage with royal grandeur. It had been a very sweet incense that she had burned before him; so modest (he told himself); so childlike and worshipful, and (he would once have sworn) so sincere. She had invested him with an almost supernatural number of high attributes and excellencies and talents, and he had absorbed the oblation as a desert drinks the rain that can coax from it no promise of blossom or fruit.
As Trysdale grimly wrenched apart the seam of his last glove, the crowning instance of his fatuous and tardily mourned egoism came vividly back to him. The scene was the night when he had asked her to come up on his pedestal with him and share his greatness. He could not, now, for the pain of it, allow his mind to dwell upon the memory of her convincing beauty that night--the careless wave of her hair, the tenderness and virginal charm of her looks and words. But they had been enough, and they had brought him to speak. During their conversation she had said:
"And Captain Carruthers tells me that you speak the Spanish language like a native. Why have you hidden this accomplishment from me? Is there anything you do not know?"
Now, Carruthers was an idiot. No doubt he (Trysdale) had been guilty (he sometimes did such things) of airing at the club some old, canting Castilian proverb dug from the hotchpotch at the back of dictionaries. Carruthers, who was one of his incontinent admirers, was the very man to have magnified this exhibition of doubtful erudition. @carruthers
But, alas! the incense of her admiration had been so sweet and flattering. He allowed the imputation to pass without denial. Without protest, he allowed her to twine about his brow this spurious bay of Spanish scholarship. He let it grace his conquering head, and, among its soft convolutions, he did not feel the prick of the thorn that was to pierce him later.
How glad, how shy, how tremulous she was! How she fluttered like a snared bird when he laid his mightiness at her feet! He could have sworn, and he could swear now, that unmistakable consent was in her eyes, but, coyly, she would give him no direct answer. "I will send you my answer to-morrow," she said; and he, the indulgent, confident victor, smilingly granted the delay. The next day he waited, impatient, in his rooms for the word. At noon her groom came to the door and left the strange cactus in the red earthen jar. There was no note, no message, merely a tag upon the plant bearing a barbarous foreign or botanical name. He waited until night, but her answer did not come. His large pride and hurt vanity kept him from seeking her. Two evenings later they met at a dinner. Their greetings were conventional, but she looked at him, breathless, wondering, eager. He was courteous, adamant, waiting her explanation. With womanly swiftness she took her cue from his manner, and turned to snow and ice. Thus, and wider from this on, they had drifted apart. Where was his fault? Who had been to blame? Humbled now, he sought the answer amid the ruins of his self-conceit. If--
The voice of the other man in the room, querulously intruding upon his thoughts, aroused him.
"I say, Trysdale, what the deuce is the matter with you? You look unhappy as if you yourself had been married instead of having acted merely as an accomplice. Look at me, another accessory, come two thousand miles on a garlicky, cockroachy banana steamer all the way from South America to connive at the sacrifice--please to observe how lightly my guilt rests upon my shoulders. Only little sister I had, too, and now she's gone. Come now! take something to ease your conscience."
"I don't drink just now, thanks," said Trysdale.
"Your brandy," resumed the other, coming over and joining him, "is abominable. Run down to see me some time at Punta Redonda, and try some of our stuff that old Garcia smuggles in. It's worth the, trip. Hallo! here's an old acquaintance. Wherever did you rake up this cactus, Trysdale?"
"A present," said Trysdale, "from a friend. Know the species?"
"Very well. It's a tropical concern. See hundreds of 'em around Punta every day. Here's the name on this tag tied to it. Know any Spanish, Trysdale?"
"No," said Trysdale, with the bitter wraith of a smile--"Is it Spanish?"
"Yes. The natives imagine the leaves are reaching out and beckoning to you. They call it by this name--Ventomarme. Name means in English, 'Come and take me.'"
    """]
    fileNames = ["Cousin Tribulation's Story", "The Story of An Hour", "How the Camel Got His Hump", "The Cactus"]



    searchResults = search(fileContents, fileNames, "when", 60)
    mentionsByNote = reportBySymbol(fileContents, fileNames, '@', 60, style = 'by note')
    keywordsBySymbol = reportBySymbol(fileContents, fileNames, '#', style = 'by symbol')
    sort = topologicalSort(fileContents, fileNames)


    showResult('search results for [when]:',searchResults)
    showResult('mentions found (by note):',mentionsByNote)
    showResult('keywords found (by symbol):',keywordsBySymbol)
    showResult('Topological sort:',sort)

main()

#need to add
#   the max len should still matter for notes with really long titles when sorting by symbol
#   need to explain that when sorting by symbol, the front end can let the user click on a note title, 
#       which will trigger the search function just for that note they clicked on,
#       so they get that nice report that the search function gives.
