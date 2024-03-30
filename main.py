#artwork class
class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        #initialize Artwork object with attributes
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.exhibition_location = exhibition_location

    def display_details(self):
        #method to display details of the artwork
        print("Artwork Details:")
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Date of Creation: {self.date_of_creation}")
        print(f"Historical Significance: {self.historical_significance}")
        print(f"Exhibition Location: {self.exhibition_location}")


# exhibition class
class Exhibition:
    def __init__(self, location, duration):
        #initialize Exhibition object with attributes
        self.location = location
        self.duration = duration

    def display_details(self):
        #method to display details of the exhibition
        print("Exhibition Details:")
        print(f"Location: {self.location}")
        print(f"Duration: {self.duration}")


# visitor class
class Visitor:
    def __init__(self, name, age, nationality):
        # initialize Visitor object with attributes
        self.name = name
        self.age = age
        self.nationality = nationality

    def purchase_ticket(self, ticket):
        #method for a visitor to purchase a ticket
        print(f"{self.name} purchased a ticket for {ticket.price} AED.")


# ticket class
class Ticket:
    def __init__(self, price, ticket_type):
        ##initialize Ticket object with attributes
        self.price = price
        self.ticket_type = ticket_type

    def calculate_price(self):
        # calculate the ticket price
        return self.price


# ticket type class
class TicketType:
    def __init__(self, type):
        # initialize TicketType object with attributes
        self.type = type


# special event class
class SpecialEvent:
    def __init__(self, event_type, location, duration):
        # initialize SpecialEvent object with attributes
        self.event_type = event_type
        self.location = location
        self.duration = duration


# museum class
class Museum:
    def __init__(self):
        # initialize Museum object with attributes with an empty lists for artworks, exhibitions, special events,and visitors
        self.artworks = []
        self.exhibitions = []
        self.special_events = []
        self.visitors = []

    def add_artwork(self, artwork):
        # Method to add artwork to the museum
        self.artworks.append(artwork)

    def add_exhibition(self, exhibition):
        # Method to add exhibition to the museum
        self.exhibitions.append(exhibition)

    def add_special_event(self, special_event):
        # Method to add special event to the museum
        self.special_events.append(special_event)

    def add_visitor(self, visitor):
        # Method to add visitor to the museum
        self.visitors.append(visitor)


#test cases

# 1. Adding new art to the museum
def test_add_artwork():
    # Creating artwork
    artwork = Artwork("Starry Night", "Vincent van Gogh", "1889", "Post-Impressionist masterpiece", "Permanent Gallery")

    # Creating museum instance
    museum = Museum()

    # Adding artwork to the museum
    museum.add_artwork(artwork)

    # Displaying added artwork
    print("Artwork added to the museum:")
    artwork.display_details()


# 2. Opening a new exhibition or event at the museum
def test_open_exhibition():
    # Creating exhibition
    exhibition = Exhibition("Gallery 2", "2 months")

    # Creating museum instance
    museum = Museum()

    # Opening exhibition at the museum
    museum.add_exhibition(exhibition)

    # Displaying opened exhibition
    print("Exhibition opened at the museum:")
    exhibition.display_details()


# 3. Purchasing tickets by an individual or tour group for an event
def test_purchase_ticket():
    # Creating visitor
    visitor = Visitor("Salama Naser", 21, "Emirati")

    # Creating ticket type
    ticket_type = TicketType("Adult")

    # Creating ticket
    ticket = Ticket(63, ticket_type)

    # Creating museum instance
    museum = Museum()

    # Visitor purchasing ticket
    visitor.purchase_ticket(ticket)


# 4. Displaying payment receipts for purchasing tickets
def test_display_payment_receipt():
    # Creating visitor
    visitor = Visitor("Salem Ahmed", 30, "Saudi")

    # Creating ticket type
    ticket_type = TicketType("Adult")

    # Creating ticket
    ticket = Ticket(63, ticket_type)

    # Creating museum instance
    museum = Museum()

    # Visitor purchasing ticket
    visitor.purchase_ticket(ticket)

    # Displaying payment receipt
    print("Payment Receipt:")
    print(f"Visitor: {visitor.name}")
    print(f"Ticket Price: {ticket.price} AED")


# 5. Adding special events to the museum
def test_add_special_event():
    # Creating special event
    special_event = SpecialEvent("Concert", "Outdoor Space", "2 hours")

    # Creating museum instance
    museum = Museum()

    # Adding special event to the museum
    museum.add_special_event(special_event)

    # Displaying added special event
    print("Special event added to the museum:")
    print(f"Type: {special_event.event_type}")
    print(f"Location: {special_event.location}")
    print(f"Duration: {special_event.duration}")


# 6. Adding visitors to the museum
def test_add_visitor():
    # Creating visitor
    visitor = Visitor("Charlie Brown", 27, "Canadian")

    # Creating museum instance
    museum = Museum()

    # Adding visitor to the museum
    museum.add_visitor(visitor)

    # Displaying added visitor
    print("Visitor added to the museum:")
    print(f"Name: {visitor.name}")
    print(f"Age: {visitor.age}")
    print(f"Nationality: {visitor.nationality}")


# Running test cases
if __name__ == "__main__":
    print("Adding New Artwork to the Museum")
    test_add_artwork()
    print("Opening a New Exhibition or Event at the Museum")
    test_open_exhibition()
    print("Purchasing Tickets by an Individual or Tour Group for an Event")
    test_purchase_ticket()
    print("Displaying Payment Receipts for Purchasing Tickets")
    test_display_payment_receipt()
    print("Adding Special Events to the Museum")
    test_add_special_event()
    print("Adding Visitors to the Museum")
    test_add_visitor()

