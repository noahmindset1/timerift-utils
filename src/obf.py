import pickle
import json

# Your embed data
embed_data = {
    "title": "timerift utils",
    "description": "This is a test embed for the bot timerift utils.",
    "image": {"url": "https://private-user-images.githubusercontent.com/157752909/302306572-92218147-7845-4346-948e-a7874f596d18.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcxNDMyODUsIm5iZiI6MTcwNzE0Mjk4NSwicGF0aCI6Ii8xNTc3NTI5MDkvMzAyMzA2NTcyLTkyMjE4MTQ3LTc4NDUtNDM0Ni05NDhlLWE3ODc0ZjU5NmQxOC5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIwNVQxNDIzMDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02ZmY5ZWRiODE3MjYxMjEwOTZkN2FkMzEwZTRmNmI0M2M4NGFmYjNkNmM0ZmI2MTdiZDg3ODdjZTVkZmZkOTk1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.R5dLccpJTtkn4htZsT4TFlYWYfdzkVMuI-NMZ593Dqs"},
    "footer": {"text": "requested by {user}", "icon_url": "{user.avatar}"},
    "author": {"name": "timerift utils", "icon_url": "https://private-user-images.githubusercontent.com/157752909/302306572-92218147-7845-4346-948e-a7874f596d18.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcxNDMyODUsIm5iZiI6MTcwNzE0Mjk4NSwicGF0aCI6Ii8xNTc3NTI5MDkvMzAyMzA2NTcyLTkyMjE4MTQ3LTc4NDUtNDM0Ni05NDhlLWE3ODc0ZjU5NmQxOC5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIwNVQxNDIzMDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02ZmY5ZWRiODE3MjYxMjEwOTZkN2FkMzEwZTRmNmI0M2M4NGFmYjNkNmM0ZmI2MTdiZDg3ODdjZTVkZmZkOTk1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.R5dLccpJTtkn4htZsT4TFlYWYfdzkVMuI-NMZ593Dqs"},
    "timestamp": True
}

# Obfuscate the JSON data and save it to a .bin file
obfuscated_data = pickle.dumps(json.dumps(embed_data))
with open('embed_data.bin', 'wb') as f:
    f.write(obfuscated_data)
