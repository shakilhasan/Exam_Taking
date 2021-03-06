============
Exam_Taking
============
This is a simple Online Exam Taking Application. I am doing this project using the Python Django framework.

Features
---------
* The exam paper will have multiple-choice Questions.
* Admins can create Questions with Choices.
* Students can view the exam paper and submit Answers.
* Every Question will have 5 Choices.
* Each set of Questions will have shuffling Questions as well as shuffling Choices.
* There will be a large number of Questions on the list. Admins choose Questions from these for specific Subjects. They can also search for Questions with text.
* Students are assigned with Exam papers by Admin.
* Admin will be emailed with submitted Answers.
* Application manages permission for Admin and Students.
* Login Form Validation using AngularJs.

Questions
^^^^^^^^^^
Shuffling Questions, as well as shuffling Choices, are ready for Students for an Exam that is selected by Admin. Students get only selected Questions.

Submit Questions:
*****************
Students submit Question's Answer that emailed to Admin.

Add Questions:
**************
Admin can add new Questions with Choices. 5th No. The choice is count as an Answer. but they become shuffled to the Student.

Edit Questions:
***************
Admin can edit existing Questions and Choices.

Delete Questions:
*****************
Admin can delete existing Questions also.

Subject
^^^^^^^^
Admin can add the Subject, the Question is arranged Subjectwise.

Search
^^^^^^^^
Admin/Student can Search for specific Questions. The search result also shuffled.

Submission
^^^^^^^^^^^
Admin access the Submission home that is a collection of all Student's Submission with the varified correct Answer. Admin can delete the Submission.

Users
^^^^^^^
Superusers are count as Admin/Teacher. And the normal User is counts as Students. Login Form Validation using AngularJs.

* To create a **superuser account**, use this command::

    $ python manage.py createsuperuser

settings:
***********
In settings.py replace this with your (`Less secure app access <https://myaccount.google.com/lesssecureapps>`_
) Gmail and Password: ::

    EMAIL_HOST_USER = 'your@gmail.com'
    EMAIL_HOST_PASSWORD = 'password'

APIs
^^^^
* **Api_v1_Question** is a REST API endpoint to get and create questions, create is not work properly.
* **Question_Api** implement API calls using AJAX.

Unit test cases
^^^^^^^^^^^^^^^^
Implement simple Unit test cases.

* Run them using the test command of your project’s manage.py utility::

     $ ./manage.py test

Deployment
^^^^^^^^^^^^^^^^
The application is deployed on the **Heroku server**.

* superuser username and password for checking::

      username: admin
      password: admin

* `Live Link <https://examtaking.herokuapp.com/>`_::

      https://examtaking.herokuapp.com/
