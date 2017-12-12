# intucompass
locational site, user intuition reviews 

#Chloe's Capstone:
##Project Name: 
intucompass

##Project Overview: 

**Users of this mapping app will be able to:**

 - Create user profile
 - Use mapping system to pin locations
 - Add 'review' content to pinned locations
 - Have access to the community content.
 - Access location oriented data maps 

##Functionality:

 - First page will be a Login/Registration page (login_reg.html)-page with explanation of site purpose and mission (Login will be required to see data)
 - User will be sent an validation email to complete Registration and User Profile.
 - OnClick (email validation)- user will be routed back to Login page for login.
 - Once logged in, user will come to Main Landing page, (main.html) - will show where user is located. 
 - Search bar at top to search for business names or places (Google Places API)
 - Submit the place, pin appears in correct location, open location in Pin_detail url.
 - Pin_detail.html shows Place with address - Previous comments will be available with comment box for current user to review as well. 
 - Possible hard coded checkboxes for trackable data points which can be populated into map overlays specific to event type and/or resources.
 
 
##Data Model:
Users:
 - email
 - username
 - event tag
 - reviews
 
Map:
 - event tag
 - review

 
 
##Schedule:
Want to get the general skeleton of a locational and event review app for now and then fill in with the actual infrastructure and mission at another date. So this project will start out really generic in scope using the Google Places and Google Maps Embed API's.
