# python-selenium-test-framework

Clone the project

Download Chrome and other drivers. Place them inside src/main/script/drivers. If need give executable permissions to the driver

Update the test.ini file under src/main/resources and add the browser drivers paths

Open a terminal window, navigate to the project root directory

Issue tox command - This will build the project download all dependencies from the requirements file and run the tests

To rebuild the project, for e.g if you added new dependencies in requirements file, then issue tox -r command. This will download new dependencies, rebuild the project and run the tests.

HTMLTest Runner gives a nice html report. This is located under target folder that gets generated after running the "tox" command
