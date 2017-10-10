from .search import search
from .report_by_symbol import reportBySymbol


def showResult(info,result):
    print('\n>>>> ' + info + ' <<<<\n')
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j])

def main():
    fileContents = ["""
Since cats first got their adorable claws into us about 9,500 years ago, humans have had a love affair with felines.

Today more than 80 million cats reside in U.S. homes, with an estimated three cats for every dog on the planet. (Watch a video about the secret lives of cats.) Yet there's still a lot we don't know about our feline friends—including what they think of their owners.

John Bradshaw is a cat-behavior expert at the University of Bristol and the author of the new book Cat Sense. After observing pet cats for several years, he's come to an intriguing conclusion: They don't really understand us the way dogs do.

Bradshaw recently shared some of his insights with National Geographic.

How did you get into cat behavior?

For the first 20 years of my career I studied olfactory [smell] behavior in invertebrates. I've always been fascinated by this other world that animals live in—primarily of odor, which is dogs' primary sense. So in the early 1980s I started working on dog behavior. [Later] I very quickly became fascinated with cats, and what their idea of the world is compared to the one we have.

What do you do in your research?

A lot of observation—watching groups of cats to see how they interact with one another and deducing their social structure. [I watch] cats in colonies that are free-ranging, and in animal shelters where quite a number will be housed together—you get interesting dynamics [when new cats are introduced].

I've also done slightly more manipulative things, such as studying the way cats play with toys, or testing cat [behaviors] at different times of the day. [I also observe] relationships with owners, interviewing them and giving them questionnaires to find out how they perceive their cats.

Why did you conclude that cats don't "get us" the way dogs do?

There's been a lot of research with dogs and how dogs interact with people. [It's] become very clear that dogs perceive us as being different than themselves: As soon as they see a human, they change their behavior. The way a dog plays with a human is completely different from [the way it plays] with a dog.

We've yet to discover anything about cat behavior that suggests they have a separate box they put us in when they're socializing with us. They obviously know we're bigger than them, but they don't seem to have adapted their social behavior much. Putting their tails up in the air, rubbing around our legs, and sitting beside us and grooming us are exactly what cats do to each other. (Also see "How Cats and People Grew to Love Each Other.")

I've read articles where you've said cats think of us as big, stupid cats. Is that accurate?

No. In the book [I say] that cats behave toward us in a way that's indistinguishable from [how] they would act toward other cats. They do think we're clumsy: Not many cats trip over people, but we trip over cats.

But I don't think they think of us as being dumb and stupid, since cats don't rub on another cat that's inferior to them. (See "Cats Use 'Irresistible' Purr-Whine to Get Their Way.")

Can we discover what cats really think about us?

More research needs to be done. [It's] not an area that's received sufficient attention. [Cats are] not wild animals, so ecologists [might think], 'Well they're not really animals at all.'

What has been most surprising to you in your research?

How stressed a lot of pet cats can be without their owners realizing it, and how much it affects the quality of their mental lives and their health. Cats don't [always] get on with other cats, [and people don't realize] how much that can stress them out. Other than routine visits, the most common reason cats are taken to vets is because of a wound sustained in a fight with another cat.

[More cats are mysteriously getting] dermatitis and cystitis [inflammation of the bladder] and it's becoming abundantly clear that these medical problems are made worse by psychological stress. [For instance], inflammation of the bladder wall is linked to stress hormones in the blood.

One solution is to examine the cat's social lifestyle, instead of pumping it full of drugs. [For example, that could mean making sure] two cats that [don't get along] live at opposite ends of the house. Quite often the whole problem goes away.

I have a few questions from cat owners on Facebook. First, why might a cat yowl when it's by itself in a room?

Cats learn specifically how their owners react when they make particular noises. So if the cat thinks, 'I want to get my owner from the other room,' it works to vocalize. They use straightforward learning. (Learn about National Geographic's Little Kitties for Big Cats initiative.)
    """]
    fileNames = ["Nat Geo"]



    searchResults = search(fileContents, fileNames, "you", 60)
    mentionsByNote = reportBySymbol(fileContents, fileNames, '@', 60, style = 'by note')
    keywordsBySymbol = reportBySymbol(fileContents, fileNames, '#', style = 'by symbol')

    showResult('search results for [you]:',searchResults)
    showResult('mentions found (by note):',mentionsByNote)
    showResult('keywords found (by symbol):',keywordsBySymbol)

main()

#need to add
#   the max len should still matter for notes with really long titles when sorting by symbol
#   need to explain that when sorting by symbol, the front end can let the user click on a note title,
#       which will trigger the search function just for that note they clicked on,
#       so they get that nice report that the search function gives.
