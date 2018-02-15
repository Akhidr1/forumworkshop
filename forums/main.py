import models

member1 = models.Member("Ahmed", 20)

member2 = models.Member("Nesma", 25)

post1 = models.Post("Hello!", "Happy to join your community!")

post2 = models.Post("Hi!", "First time for me here!")

post3 = models.Post("Howdy!", "Glad to be on of your community!")


print post3.body

print post1.title

print member1.age

print member2.name
