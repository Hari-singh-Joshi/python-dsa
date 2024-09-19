class OTTSubscription:
    def __init__(self,subscription_id,plan,total_payment):
        self.id=subscription_id
        self.plan=plan
        self.total_payment=total_payment
        
    def subscribe(self):
        print(f"subscription with {self.id} id subscribed to the{self.plan} plan")
        
    def unsubscribe(self):
        print(f'unsubscribe with {self.id} is unsubscribed to the {self.plan} plan')

netflix=OTTSubscription(121212,'monthly',100)
#accessing through method 

netflix.subscribe()
netflix.unsubscribe()
        
class PremiumSubscription(OTTSubscription):
    def __init__(self, subscription_id, plan, total_payment,screens):
        super().__init__(subscription_id,plan,total_payment)
        self.max_screens=screens
    
    def set_max_screens(self,screens):
        self.max_screens=screens
        print(f'maximum screen set to {self.max_screens} in the premium')
netflix=PremiumSubscription(454545,'year',1,8500)
netflix.subscribe()
netflix.unsubscribe()
netflix.set_max_screens(4)
        
       
            
            