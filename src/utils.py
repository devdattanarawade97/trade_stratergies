from datetime import datetime

def days_to_expiry(expiry_date: str, current_date: str) -> int:
    """
    Calculate the number of days remaining until expiry.

    :param expiry_date: Expiry date in 'YYYY-MM-DD' format
    :param current_date: Current date in 'YYYY-MM-DD' format
    :return: Number of days to expiry
    """
    expiry = datetime.strptime(expiry_date, "%Y-%m-%d")
    current = datetime.strptime(current_date, "%Y-%m-%d")
    
    # Calculate the difference in days
    delta = expiry - current
    return delta.days

# Example usage:
# days = days_to_expiry("2024-12-31", "2024-11-28")
# print(days)  # Output: 33
