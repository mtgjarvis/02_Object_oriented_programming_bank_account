class PaperBoy:

    def __init__(self, name, experience, earnings,):
        self.name = name
        self.experience = experience
        self.earnings = earnings


    def __str__(self):
        return ('')

    def quota(self):
        new_quota = 50
        new_quota = self.experience / 2 + new_quota
        return new_quota

    def deliver(self, start_address, end_address):
        delivered = (end_address - start_address)
        self.experience = delivered
        if delivered < self.quota():
            self.earnings = delivered * 0.25 
            delivered -= 2.00
        elif delivered > self.quota():
            over_quota = delivered - self.quota()
            self.earnings = over_quota * 0.50
            self.earnings = self.earnings + (self.quota() * 0.25)
        return delivered

    def report(self):
        return (f"I'm {self.name} and I delivered {self.experience} and I earned ${self.earnings}")


paper_boy1 = PaperBoy('Mark', 0, 0,)
paper_boy1.deliver(1, 200)
print(paper_boy1.report())
print(f'My new quota is {paper_boy1.quota()}')

paper_boy1 = PaperBoy('Tommy', 50, 0,)
paper_boy1.deliver(1, 100)
print(paper_boy1.report())
print(f'My new quota is {paper_boy1.quota()}')