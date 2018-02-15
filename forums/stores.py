
class MemberStore:

  members = []

  def get_all(self):
      # get all members

      for member in MemberStore.members:

            return member

  def add(self, member):
      # append member

     MemberStore.members.append(member)


class PostStore:

  posts = []

  def get_all(self):
      # get all posts

      for post in PostStore.posts:

            return post

  def add(self, post):
      # append post

     PostStore.posts.append(post)

