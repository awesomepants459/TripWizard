Hello, and thank you for downloading TripWizard!

As you know, TripWizard revolutionizes the way people plan trips. Here's what you need to do to utilize it:

1. Install the latest version of the requirements file with the following command:
	Windows: pip install -r requirements.txt
	Linux: $ pip install -r requirements.txt

2. Initialize the databases
	Windows: flask init-db
	Linux: $ flask init-db

3. Run the application
	Windows: flask run --debug
	Linux: $ flask run --debug

That will be everything you need to install to run this application. Enjoy your trip, and consider sending us an email about your journey!

Here are some things to note about the programming of our application:

1. Because there is something in an existing Python library called Site, we have not been able to put the site, day, and itinerary classes into their own files. 
2. There are not as many family and nature sites in every city as there are historical. Be aware of this during testing, and when you create an itinerary with only family or nature sites, make it a very short trip. 
3. The reason we wanted in the survey to have light, moderate, and heavy selection instead of asking the user how many sites they would like to see, is because sometimmes, people don't know exactly how long they will spend at sites. They might be overwhelmed or underwhelmed by the itinerary if they don't understand how heavy their day is. 

Best Regards,
The TripWizard Team