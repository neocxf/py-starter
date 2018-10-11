monthConversions = {
    "Jan": "January",
    "Feb": "Feburary",
    "Mar": "March"
}
print(monthConversions["Jan"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Dec", "December"))
