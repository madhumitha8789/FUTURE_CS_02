Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
... 
... print("=== PHISHING EMAIL DETECTOR ===")
... 
... subject = input("Enter email subject: ")
... message = input("Enter email message: ")
... 
... text = (subject + " " + message).lower()
... warnings = []
... 
... urgent_words = [
...     "urgent",
...     "immediately",
...     "action required",
...     "account suspended",
...     "password expire"
... ]
... 
... if any(word in text for word in urgent_words):
...     warnings.append("Urgent or threatening language detected")
... 
... if re.search(r"https?://|www\.", text):
...     warnings.append("Email contains a link; verify it safely")
... 
... if any(word in text for word in ["password", "otp", "credit card"]):
...     warnings.append("Sensitive information is mentioned")
... 
... print("\n=== ANALYSIS RESULT ===")
... 
... if warnings:
...     print("Potential phishing indicators found:")
...     for warning in warnings:
...         print("-", warning)
... else:
...     print("No obvious phishing indicators found.")
... 
... print("\nNote: This is a basic educational detector.")
