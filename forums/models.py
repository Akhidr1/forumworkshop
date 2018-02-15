class Member():

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Post():

    def __init__(self, title, body):
        self.title = title
        self.body = body

class MemberStore:

  members = []

  def get_all(self):
      # get all members

      for member in MemberStore.members:

            print(member)

  def add(self, member):
      # append member

     MemberStore.members = MemberStore.members.append(self.name)


class PostStore:

  posts = []

  def get_all(self):
      # get all posts

      for post in PostStore.posts:

            print(post)

  def add(self, post):
      # append post

     PostStore.posts = PostStore.posts.append(self.post)

