import models
import stores

member1 = models.Member("Ahmed", 20)

member2 = models.Member("Nesma", 25)

post1 = models.Post("Hello!", "Happy to join your community!")

post2 = models.Post("Hi!", "First time for me here!")

post3 = models.Post("Howdy!", "Glad to be on of your community!")



models.MemberStore.add(member1)
models.MemberStore.add(member2)

print(models.MemberStore.get_all())

models.PostrStore.add(post1)
models.PostStore.add(post2)
models.PostStore.add(post3)

print(models.PostStore.get_all())







#print post3.body
#print post1.title
#print member1.age
#print member2.name
