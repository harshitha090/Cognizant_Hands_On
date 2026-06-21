class SingleObject:
    shared_obj = None

    def __new__(current_class):
        if current_class.shared_obj is None:
            current_class.shared_obj = super().__new__(current_class)
        return current_class.shared_obj

first_instance = SingleObject()
second_instance = SingleObject()

print(first_instance is second_instance)