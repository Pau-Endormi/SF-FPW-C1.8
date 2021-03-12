class Cat:
  def __init__(self, name=None, sex=None, age=None):
    self.name = name
    self.sex = sex
    self.age = age

  def show_cat(self):
    print(f'Cat "{self.name}",\n Sex: {self.sex},\n Age: {self.age}')

  def get_name(self):
    return self.name

  def get_sex(self):
    return self.sex

  def get_age(self):
    return self.age

  def set_name(self, name):
    if isinstance(name, str):
      self.name = name

  def set_sex(self, sex):
    if isinstance(sex, str):
      self.sex = sex

  def set_age(self, age):
    if age > 0 and isinstance(age, int):
      self.age = age
