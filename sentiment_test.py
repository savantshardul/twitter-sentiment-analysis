import sentiment_mod as s
import tweetProcess as ts

testing1="It is very sad that nike hiked prices of jogging shoes."
testing2="#Nike got the amazing range of soccer shoes.#FCBarca"
print(testing1,s.sentiment(testing1))
print(testing2,s.sentiment(testing2))