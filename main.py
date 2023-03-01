import cat
from ninebandedarmadillo import NinebandedArmadilo as Armadillo

def main():

    # Create Cat.
    # This code imported the cat module, Cat class is a name in the cat module 
    kitten = cat.Cat('Kitty')
    kitten.make_sound()


    
    armadillo = Armadillo('Armadillo')
    armadillo.make_sound()


if __name__ == '__main__':
    main()