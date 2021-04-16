class budget:
    def __init__(self,food,clothing,entertainment):
        self.food=food
        self.clothing=clothing
        self.entertainment=entertainment

        

    @classmethod
    def from_input(cls):
        return cls(
            int(input('food budget:')),
            int(input('clothing budget:')),
            int(input('entertainment budget:')),
            
                  )
                


    @classmethod
    def with_draw_funds(cls):
        return cls(
            int(input('Food: ')),
            int(input('Clothing: ')),
            int(input('Entertainment: '))
        )


    @classmethod
    def compute_balance(cls):
        return cls(
            int(input('Food: ')),
            int(input('Clothing: ')),
            int(input('Entertainment: '))
        ) 
        

print('Budget--------------------------------------------------------')        
budget.from_input()
print('Withdraw Funds from ------------------------------------------')
budget.with_draw_funds()
print('Compute balance -----------------------------------------------')
budget.compute_balance()