import models
import stores

member1 = models.Member("Ahmed", 20)

member2 = models.Member("Nesma", 25)

post1 = models.Post("Hello!", "Happy to join your community!")

post2 = models.Post("Hi!", "First time for me here!")

post3 = models.Post("Howdy!", "Glad to be on of your community!")

print(post1)

member_store = stores.MemberStore()
post_store = stores.PostStore()

member_store.add(member1)
member_store.add(member2)

print member_store.get_all()


post_store.add(post1)
post_store.add(post2)

print post_store.get_all()







#print post3.body
#print post1.title
#print member1.age
#print member2.name
