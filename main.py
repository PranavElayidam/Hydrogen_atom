import argparse
import sys

'''The Path Hack.
   Python is stupid sometimes(So am I , i will be more than python is though .·°՞(˃ ᗜ ˂)՞°·.(Laughing)). It doesn't always know that the folders 
   'visualization' and 'physics' are right here.
   sys.path.append('.') tells Python: "Hey, look in the current folder too!"
   Without this, 'from visualization import...' might fail.
   P.S : I'm new to using argparse , i haven't had that amount of practice to make optimized code,]. Forgive me
         And also there are few thiings i don't understand completely in here(argparse fucntions), i asked help from
         Gemini AI , subreddit r/python and stackoverflow. kindly forgive me for mistakes and errors'''
sys.path.append('.')

from Visualization import plot_3d, plot_density, plot_radial

def main():
    '''Setting up the Argument Parser.
       Think of 'parser' as a robot waiter. Its job is to listen to what the user types
       in the terminal, figure out what they want, and reject bad orders.'''
    parser = argparse.ArgumentParser(description="Hydrogen Atom Physics Engine")

    '''The Subparsers.
       This is like the main menu. The user has to pick ONE mode.
       dest='command' means: "Whatever the user types (shape/density/radial), 
       save it in a variable called 'args.command' so I can check it later."'''
    subparsers = parser.add_subparsers(dest='command', help='Select Visualization Mode')

    # ==========================================
    # MODE 1: 3D Shape
    # ==========================================
    # This creates the command: python main.py shape ...
    shape_parser = subparsers.add_parser('shape', help='3D Orbital Shape')
    
    # Adding ingredients (Arguments) to the 'shape' command.
    # type=int: If user types "apple", crash and tell them we need a number.
    # default=1: If user forgets -n, just assume n=1.
    shape_parser.add_argument('-n', type=int, default=1, help='Principal Quantum Number')
    
    # required=True: If user forgets -l, the robot yells at them and stops.
    shape_parser.add_argument('-l', type=int, required=True, help='Azimuthal Quantum Number')
    shape_parser.add_argument('-m', type=int, required=True, help='Magnetic Quantum Number')

    # ==========================================
    # MODE 2: 2D Density
    # ==========================================
    # This creates the command: python main.py density ...
    density_parser = subparsers.add_parser('density', help='2D Probability Density Map')
    density_parser.add_argument('-n', type=int, required=True)
    density_parser.add_argument('-l', type=int, required=True)
    density_parser.add_argument('-m', type=int, required=True)

    # ==========================================
    # MODE 3: Radial Graph
    # ==========================================
    # This creates the command: python main.py radial ...
    radial_parser = subparsers.add_parser('radial', help='1D Radial Distribution')
    radial_parser.add_argument('-n', type=int, required=True)
    radial_parser.add_argument('-l', type=int, required=True)

    '''The Processing Step.
       This line actually reads the command line.
       It takes "python main.py shape -n 2 -l 1 -m 0"
       and converts it into an object 'args' where:
       args.command = 'shape'
       args.n = 2
       args.l = 1
       etc.'''
    args = parser.parse_args()

    # If the user just ran 'python main.py' with nothing, print help and exit.
    if not args.command:
        parser.print_help()
        return

    '''The Execution Logic.
       Now we look at what the waiter wrote down (args.command)
       and send the order to the kitchen (the visualization modules).
       
       I added a try/except block here. 
       Because if the user asks for n=1, l=2, the physics engine will raise a ValueError.
       We want to catch that error and print a nice message, not show a scary stack trace.'''
    try:
        if args.command == 'shape':
            plot_3d.render(args.n, args.l, args.m)
            
        elif args.command == 'density':
            plot_density.render(args.n, args.l, args.m)
            
        elif args.command == 'radial':
            plot_radial.render(args.n, args.l)
            
    except ValueError as e:
        print(f"\n❌ PHYSICS ERROR: {e}")
        print("Tip: Remember that l must be less than n, and |m| must be less than or equal to l.\n")
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}\n")

if __name__ == "__main__":
    main()