#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

ticket_dict = {}

def reconstruct_trip(tickets, length):
    route = []
    global ticket_dict

    #insert tickets into dict (source: destination)
    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    #append the first flight
    first_flight = ticket_dict['NONE']
    route.append(first_flight)

    #lookup the next flight by using the previous flights value 
    for i in range(1, len(tickets)):
        route.append(ticket_dict[route[i-1]])

    return route

