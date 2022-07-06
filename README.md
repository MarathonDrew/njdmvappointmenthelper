# njdmvappointmenthelper

Python script to check for NJ DMV appointments

## Background

I have been trying to get an appointment with the NJ DMV for over a month and they are booked out for several weeks around the greater NYC area.  They apparently changed over to this bullcrap during covid and you can't show up to get help anymore.  Gotta make an appointment 2 months in advance and hope that you have everything they need.  That being said, I realized that when someone cancels, their spot goes up for grabs.  

This is a dumb little python script that pings the relevant APIs for the locations I needed and checks if there are any earlier appointments to take from someone who cancels.  It is how I got an appointment around 5 weeks early.  I run Linux on my personal machines and utilized the `watch` command to run the script every 2 minutes.  If someone stumbles upon this repo and has some coding experience, but is running Windows or MacOS, there should equivalent commands you can run.  
