class BarbershopChatbot:
    def __init__(self):
        self.services = []
        self.appointments = []
        self.promotions = []
        self.reviews = []
        self.payment_methods = ['Credit Card', 'Cash', 'Digital Wallet']

    def show_menu(self):
        print("--- Barbershop Chatbot Menu ---")
        print("1. View Services")
        print("2. Book Appointment")
        print("3. Promotions")
        print("4. Leave a Review")
        print("5. View Payment Methods")
        print("6. Cancellation Policy")
        print("7. Exit")

    def add_service(self, service_name):
        self.services.append(service_name)

    def view_services(self):
        return self.services

    def book_appointment(self, customer_name, service_name, appointment_time):
        appointment = {'customer_name': customer_name, 'service_name': service_name, 'appointment_time': appointment_time}
        self.appointments.append(appointment)
        return appointment

    def add_promotion(self, promotion):
        self.promotions.append(promotion)

    def view_promotions(self):
        return self.promotions

    def leave_review(self, review):
        self.reviews.append(review)

    def view_reviews(self):
        return self.reviews

    def show_payment_methods(self):
        return self.payment_methods

    def show_cancellation_policy(self):
        return "You can cancel your appointment 24 hours in advance for a full refund."

    def run(self):
        while True:
            self.show_menu()
            choice = input("Select an option: ")
            if choice == '1':
                print(self.view_services())
            elif choice == '2':
                customer_name = input("Enter your name: ")
                service_name = input("Enter service name: ")
                appointment_time = input("Enter appointment time: ")
                print(self.book_appointment(customer_name, service_name, appointment_time))
            elif choice == '3':
                print(self.view_promotions())
            elif choice == '4':
                review = input("Enter your review: ")
                self.leave_review(review)
            elif choice == '5':
                print(self.show_payment_methods())
            elif choice == '6':
                print(self.show_cancellation_policy())
            elif choice == '7':
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    chatbot = BarbershopChatbot()
    chatbot.run()