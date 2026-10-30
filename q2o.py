
session_1 = ['Asha', 'Kabir', 'Meera', 'Dev']
session_2 = ['Meera', 'Dev', 'Zoya', 'Aman']

both = set(session_1) & set(session_2)
all_attendees = set(session_1) | set(session_2)

sessions = {
    'Session 1': session_1,
    'Session 2': session_2
}

print("Attendees in both sessions:", both)
print("All unique attendees:", all_attendees)
print("Session details:", sessions)
print("Number of unique attendees:", len(all_attendees))
