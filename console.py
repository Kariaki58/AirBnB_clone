#!/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = {
            "BaseModel": BaseModel, "Amenity": Amenity,
            "User": User, "City": City,
            "State": State, "Place": Place, "Review": Review
            }
    load_data = storage.all()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, end):
        """exit the program"""
        return True
    
    def emptyline(self):
        """emptyline print nothing"""
        pass

    def is_valid_line(self, line):
        if not line:
            print("** class name missing **")
            return False
        linex = line.split()
        if linex[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return False
        return True
    
    def do_create(self, line):
        """creates a new instance of class"""
        if self.is_valid_line(line):
            instance = HBNBCommand.valid_classes[f"{line}"]()
            storage.save()
            print(instance.id)
    
    def do_show(self, line):
        line = line.split()
        if not line:
            print("** class name missing **")
            return
        elif line[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(line) > 1:
            text = f'{line[0]}.{line[1]}'
            if text not in HBNBCommand.load_data:
                print("** no instance found **")
            else:
                print(HBNBCommand.load_data[text])
        else:
            print("** instance id missing **")
    
    def do_destroy(self, line):
        line = line.split()
        if not line:
            print("** class name missing **")
            return
        elif line[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(line) > 1:
            text = f'{line[0]}.{line[1]}'
            if text not in HBNBCommand.load_data:
                print("** no instance found **")
            else:
                del HBNBCommand.load_data[text]
                storage.save()
        else:
            print("** instance id missing **")

    def get_all(self, line):
        ...
    
    def do_all(self, line):
        line = line.split()
        content = []
        for key, value in HBNBCommand.load_data.items():
            content.append(f"{value}")
        if len(line) > 0:
            if line[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            else:
                for key, value in HBNBCommand.load_data.items():
                    if line[0] in key:
                        content.append(f"{value}")
                print(content)
        else:
            print(content)
    
    def do_update(self, line):
        line = line.split()
        if not line:
            print("** class name missing **")
            return
        elif line[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        text = f'{line[0]}.{line[1]}'
        if text not in HBNBCommand.load_data:
            print("** no instance found **")
        elif len(line) < 3:
            print("** attribute name missing **")
        elif len(line) < 4:
            print("** value missing **")
        else:
            for key, value in HBNBCommand.load_data.items():
                if key == text:
                    remove_quote = line[3].replace('"', "")
                    setattr(value, line[2], remove_quote)
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

