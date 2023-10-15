#!/usr/bin/python3
"""importing useful model"""
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
    """AirBnB console"""
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

    def show_content(self, line):
        """show content of json file

        Args:
            line (str): the string formate of class name to print
        """
        if self.is_valid_line(line):
            line = line.split()
            if len(line) > 1:
                text = f'{line[0]}.{line[1]}'
                if text not in HBNBCommand.load_data:
                    print("** no instance found **")
                else:
                    print(HBNBCommand.load_data[text])
            else:
                print("** instance id missing **")

    def do_show(self, line):
        """show content of class name from file storage"""
        self.show_content(line)

    def destroy_content(self, line):
        """destroy content of class name from file storage"""
        if self.is_valid_line(line):
            line = line.split()
            if len(line) > 1:
                text = f'{line[0]}.{line[1]}'
                if text not in HBNBCommand.load_data:
                    print("** no instance found **")
                else:
                    del HBNBCommand.load_data[text]
                    storage.save()
            else:
                print("** instance id missing **")

    def do_destroy(self, line):
        """destroy content from file

        Args:
            line (str): string representation of class to destroy
        """
        self.destroy_content(line)

    def get_all(self, line):
        """get all data of class if exist else get all class data"""
        content = []
        if line[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in HBNBCommand.load_data.items():
                if line[0] in key:
                    content.append(f"{value}")
            print(content)

    def do_all(self, line):
        """get all data from class

        Args:
            line (str): str formate of class to display
        """
        line = line.split()
        content = []
        if len(line) > 0:
            self.get_all(line)
        else:
            for key, value in HBNBCommand.load_data.items():
                content.append(f"{value}")
            print(content)

    def set_update(self, line):
        """update data in file storage"""
        if self.is_valid_line(line):
            line = line.split()
            if len(line) == 1:
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

    def do_update(self, line):
        """update function"""
        self.set_update(line)

    def get_id(self, linex):
        """get the id from linex str"""
        other_split = linex[1].split('"')[1]
        text = f"{linex[0]} {other_split}"
        return text

    def default(self, line: str):
        """what can't be done will be done here"""
        if "." in line:
            linex = line.split(".")
        if '"' in line:
            text = self.get_id(linex)
        if "all()" in line:
            self.get_all(linex)
        elif "count()" in line:
            count = 0
            for key, value in HBNBCommand.load_data.items():
                if line[0] in key:
                    count += 1
            print(count)
        elif 'show("' in line and '")':
            self.show_content(text)
        elif 'destroy("' in line and '")':
            self.destroy_content(text)
        elif 'update("' in line and ')' in line and "{" not in line:
            get_attr_value = line.split(',')
            get_attr = get_attr_value[1].split('"')[1]
            get_valuex = get_attr_value[2].split(")")[0]
            get_value = get_valuex.split(" ")[1].replace('"', '')
            text += " " + get_attr + " " + get_value
            self.set_update(text)
        elif 'update(' in line and ')' in line and "{" in line and "}" in line:
            dict_rep = linex[1].split("{")[1].split('}')[0].split(",")
            string_text = text.replace(" ", ".")
            if string_text not in HBNBCommand.load_data:
                print("** no instance found **")
                return
            for data in dict_rep:
                key_datax = data.split(":")[0].replace("'", "")
                key_data = key_datax.replace('"', "").replace(" ", "")
                value_datax = data.split(":")[1].replace("'", "")
                value_data = value_datax.replace('"', "").replace(" ", "")
                textx = text + " " + key_data + " " + value_data
                self.set_update(textx)


if __name__ == "__main__":
    """entry point of the program"""
    HBNBCommand().cmdloop()
