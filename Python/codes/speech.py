import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)
engine.say("People of Reddit, What is the crazies thing that happened to you while being a fucking idiot?.....")
engine.say("""My friend and I were racing home from a restaurant about an hour away from his house. I had a head start on him, and I was going a consistent 90 on a 75, so I was sure that I was gonna beat him.

Anyways, after an hour on the highway, I finally got into our town and got onto the country road that leads to his house. I was in the home stretch.

Suddenly, his car pulls out right in front of me from this random-ass road and starts speeding away. I could hear his music through my rolled-up windows. If I had just gone a little faster on the country road (I was going the speed limit), I would have beat him…""")
engine.runAndWait()