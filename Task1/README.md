🏔️ Operation: CloudScale Nepal Rescue Mission
📉 The Situation
It is 4:30 PM on a Friday. You just received an urgent Slack message from the CTO.

One of our junior developers, Ramesh, has just left the company for a "better opportunity." He was working on our core Nepal Weather Utility, which is supposed to provide live data for our high-end trekking agency partners.

The problem? Ramesh wrote the code as a single, messy "spaghetti" script. Everest Treks Ltd. wants to import our weather logic into their new mobile app today, but they can't because:

The code starts an infinite loop and asks for user input immediately—you can't use it as a library.

The API URL is hardcoded directly in the logic.

The logic and the UI are so tangled that you can't get the temperature calculation without the script printing a bunch of unorganized text to the console.

🎯 Your Mission
You have been tasked to "clean the mess." You need to take Ramesh's weather_script.py and turn it into a professional, modular Python package that a high-end client would actually trust.

🛠️ The Technical "Orders"
To satisfy the CTO and keep our clients happy, your refactored solution must meet these professional standards:

The "Safety Net" (Enums): CloudScale only has a license to provide data for 8 specific cities. You must use a Python Enum to store these cities and their coordinates. If a user asks for a city we don't own, reject it immediately with a clean error message.

The "Secret Box" (.env): Remove all hardcoded URLs. Use a .env file and python-dotenv. We don't want our infrastructure details leaked!

The "Surgical Split" (Modularity): Break the script into a package named weather/:

models.py: The Enums and city data structures.

client.py: The logic for handling network requests.

processor.py: The pure logic (C to F conversion) and report data formatting.

The "Bridge" (main.py): This is your entry point. It should use argparse to handle inputs.

No More Talking Back: Replace all input() calls. Our partners want to run this from a terminal command or a script, not an interactive chat box.



🏆 Scoring Rubric (20 Points)
<img width="921" height="495" alt="image" src="https://github.com/user-attachments/assets/2cb02bd5-e399-4eaa-a1a8-ef187cfce32a" />


🚀 Getting Started
Review the "Legacy" code in weather_script.py.

Install requirements: pip install requests python-dotenv.

Start splitting the logic. Remember: Ramesh is gone, the clock is ticking, and the CTO is watching!

💡 Pro-Tip for Success
A good engineer builds code that other engineers love to use. If I run from weather.processor import convert_c_to_f, I should be able to convert temperatures in my own script without your whole program running.

🛑 Appendix: The Legacy Code (weather_script.py)
For reference, this is the code you are destroying to build something better.

Python

import requests

# ⚠️ WARNING: Ramesh's Spaghetti Code Below
🏁 One last thing:
How do you want to handle the Bonus Challenge for the students who finish early? I can add a section for "Automated Testing" or "JSON Output Mode" if you like!
