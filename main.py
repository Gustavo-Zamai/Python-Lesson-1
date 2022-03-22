class Clients:
  def __init__(self, name, email, payment, plan):
    self.name = name
    self.email = email
    self.payment = payment
    self.plans_lists = ["Basic", "Plus", "Premium"]
    if plan in self.plans_lists:
      self.plan = plan
    else:
      raise Exception("Invalid Plan")
    
  def change_plan(self, new_plan):
    if new_plan in self.plans_lists:
      self.plan = new_plan
    else:
      print ("Invalid Plan")

client = Clients("Gus","gus@gmail.com", "Credit Card", "Basic")
client.change_plan("Premium")
print(client.name, client.email, client.payment, client.plan)   


