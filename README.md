# Python Reference Application

This is a reference web application for python. 
It is in draft status and there is plenty missing from this application.
This application is a FastAPI instance with Flask mounted on it.

## Application Structure

```
{APP}
|- resources
    |- static
		|- js
		|- css
		|- images
	|- book_list.json
|- src
	|- app
		|- controllers
		|- service
		|- gateway
		|- repository
		|- model
		|- core
	|- templates
	|- tests
	|- main.py
	|- setup-python-venv.sh
```

## The Application Folder

The application is in `src/app/...`

### Controllers

Any URL that is invoked in the application
Only the service layer can be called from a controller
The responsibility of a controller is only to verify the parameters
No business logic should be included in controllers

### Services

The business logic layer is applied to here and services can be either simple or compound.
Compound services can call multiple simple services.

### Gateways

These should be wrapped into a simple service for use by compound services

### Repository

All persisted data is accessed from a repository and these can only be called by services.

### Model

The data model is the DTO from the persistence all the way through to the Controllers

### Core

The application logic is in the core where general processing such as schedulers etc.

## Static

 * js - All javascript including third party libraries are served from this folder
 * css - All sylesheets including third party styles are served from this folder
 * images - All images are served from this folder
 
## Templates
 
 All HTML files are served from here and referenced from the controllers.
 Templates should be structured in a logical manner according to the application requirements
 
## Resources

Any application resources that are needed by a developer.
These files are not bundled into the deployed application

## Tests

Unit tests required in the build step

## main.py

The applications main entry point
The UI is a flask application and mounted onto a fast API application to serve the applications REST API
