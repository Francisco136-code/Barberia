class BarberShopChatBot:
    def __init__(self):
        self.services = self.load_services()
        self.staff = self.load_staff()
        self.promotions = self.load_promotions()
        self.reviews = self.load_reviews()
        
    def load_services(self):
        return {
            "haircut": {"price": 20, "duration": "30 minutes"},
            "shave": {"price": 15, "duration": "20 minutes"},
            "coloring": {"price": 40, "duration": "60 minutes"},
            # Add more services as needed
        }

    def load_staff(self):
        return {
            "John": {"role": "Barber", "experience": "5 years"},
            "Emily": {"role": "Barber", "experience": "3 years"},
            # Add more staff profiles as needed
        }

    def load_promotions(self):
        return [
            {"description": "10% off on Tuesdays", "valid_until": "2026-12-31"},
            # Add more promotions as needed
        ]

    def load_reviews(self):
        return [
            {"reviewer": "Alice", "rating": 5, "comment": "Great service!"},
            # Add more reviews as needed
        ]

    def manage_appointment(self, date_time, service, staff_member):
        # Logic for managing appointments (creation, cancellation, etc.)
        pass

    def get_interactive_menu(self):
        return {
            "Services": self.services,
            "Staff Profiles": self.staff,
            "Promotions": self.promotions,
            "Reviews": self.reviews,
            # Add interactive options as needed
        }

    # Add more methods to handle user inquiries
