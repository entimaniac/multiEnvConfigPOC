# generic __str__ method to print instance variables for a class. Should be default python behavior IMO
def to_string(the_class):
    def __str__(self):
        class_name = type(self).__name__
        instance_variables_string = ', '.join('%s=%s' % item for item in vars(self).items())
        return '%s(%s)' % (class_name, instance_variables_string)

    the_class.__str__ = __str__
    return the_class
