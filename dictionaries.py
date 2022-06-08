monthConversions = {
    "jan":"january",
    "feb":"february",
    "mar":"march",
    "apr":"april",
    "jun":"may"
}

print(monthConversions["jan"])
print(monthConversions.get("feb"))
print(monthConversions.get("liv","not a valid key"))