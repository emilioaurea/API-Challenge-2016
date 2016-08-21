# API-Challenge-2016
Repo for CODE2040 Fellow's Program API Challenge.

I learned a lot from this challenge. Although I had never created an API or used HTTP before, I was able to comlete the challenge in a resonable amount of time. 

Step one was not too bad. I knew this had to do somethin with HTTP so I started looking for HTTP libraries for Python. This brought me to the Requests library, which is totally awesome. Once I took a look at the documentation, I was able to figure out the right methods to get the job done. 

Steps 2-4 were not very algorithmically challenging -- I had already seen these problems in my CS classes. However, I got stuck on step 4. 

I had no idea what was wrong because I was doing the challenge correctly. I reached out to CODE2040 thinking there might have been a bug in their system. Alex very kindly suggested I look at how the request should be formated based on the specs. I had no idea what she was talking about, so I moved on to step 5. 

This is not my proudest moment. I looked at what the date looked like. Then I pretty much hard-coded it and assumed the time-zone thing would always be "Z". I got pretty lucky. 

Then, after banging my head for a day, I went back to search for an answer to step 4. After frantically searching other HTTP libraries, I came across this wierd json encoding thing. So then, like any real programmer, I googled Stack Overflow. Turns out, the list I was returning was encoded in json! That's what Alex meant. So I fixed it and vuala, it worked!

In the end, it was a great experience learning about HTTP Requests and making an API.
