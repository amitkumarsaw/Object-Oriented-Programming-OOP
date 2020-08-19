class Bird:
    def fly(self):
        print("bird can fly")


class Frog(Bird):
    def fly(self, name):
        print('{} Can\'t Fly'.format(name))    


f = Frog()            # the user will only get the insatance and not the classes - Abstraction
f.fly('parrot')
