# Database
Here we outline and build the database that we will use to save what we do with our bot. Note that this database tries to differentiate between the platforms as little as possible.

## Tables

### Users
Save basic information on user

* Id
* Creation date

### Platform users
Save basic platform specific information on the users

* Id
* Platform name
* Creation date
* Platform id

### Content
Save information on content

* Id
* Content type
* Creation date
* Description
* URL

### Content recommendations
Save the recommendations for content

* Id
* User id
* Content id
* Recommendation date

#### Other tables that haven't decided on

* Sent / received messages
* User settings (i.e. some settings that we might give them at some point)