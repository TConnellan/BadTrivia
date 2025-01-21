# Very small app for reading through a general trivia question bank I found on /r/trivia
- Question bank is a decade old and not very clean
- App cycles through questions by naively linking to the next ID
- Models set up for more complex relations concerning topics and subjects but not populated
- Basic, unconfigured caching set up with redis

## Potential Improvements
- Look into cache configuring, eviction strategies (for if a question becomes outdated)
- Better traversal of the question list
    - have user select a number of questions then randomly retrieve those, then display them
- Recieving answers as input, matching against the answer
    - some kind of way to remember users, track correct/false answers, no point doing full auth, maybe just store some cookies

## Ideas
- relational mapping I've set up for topics/subjects could be viewed as a graph. If subjects are nodes and edges describe relationships betweent them then Questions would be paths within the graph with edges givning info to formulate the question and one of the subjects being the answer. Would be interesting to set up in graph db, see if questions could be constructed
- It would make for boring questions but could scrape wikipedia or other sites for simple things (e.g. this person is married to who?) to generate more questions.