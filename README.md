<h1 align="center">Airbnb Clone</h1>
<img src="https://user-images.githubusercontent.com/105363918/196176491-6fd1077d-6d2a-446c-9a6b-04cbae6f448f.png">
<h2>Description</h2>

This is the first step towards building the AirBnB clone and it's very important because it will be the basis for the following.<br>
<br>
We will create a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances. The other classes will be based on BaseModel and will help in the web funcionality, which are: User, State, City, Place, Amenity and Review.<br>
<br>
Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file. Serialization refers to the process of converting a data object into a format that allows us to store or transmit the data and then recreate the object when needed using the reverse process of deserialization.<br>
<br>
Create the first abstracted storage engine of the project: File storage. There are different formats for the serialization of data in this case we will use Json and it will be save in the File storage.<br>
<br>


<h2>Files and short description about them</h2>

- <b>/models/base_model.py</b>:  contains the parent class (BaseModel)
- <b>/models/engine/file_storage.py</b>:  contains the methods to serializate and deserializate a JSON file (class FileStorage)
- <b>/models/user.py</b>:	class User that inherits from BaseModel
- <b>/models/state.py</b>:  class State inherits from BaseModel
- <b>/models/city.py</b>:	class City inherits from BaseModel
- <b>/models/amenity.py</b>:  class Amenity inherits from BaseModel
- <b>/models/place.py</b>:  class Place inherits from BaseModel
- <b>/models/review.py</b>: 	class Review inherits from BaseModel
- <b>/tests</b>:  directory containing all the unittest
- <b>console.py</b>:	Conmmand interpeter
- <b>README.md</b>:	readme file
- <b>AUTHORS</b>: contributors


<h2>Usage</h2>
Before starting, it's necessary to have installed python3 (version 3.8.5) locally <br>
<h3>Clone this repo:</h3>

`https://github.com/gasstin/holbertonschool-AirBnB_clone.git`

Make sure that the execution permissions are enabled. Now you should be able to execute the console and see the next prompt `(hbnb)`<br>
<br>
<h3>Commands and usage examples</h3>

- `help` will show the available commands and if you run help followed by the name of a command will display a short description of what that command does.
- `quit` and `EOF` to exit the program.
- `create` creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.

      create 'Class name'
      
- `show` Prints the string representation of an instance based on the class name and id.

      (hbnb) show 'Class name' 'id'      

- `destroy` Deletes an instance based on the class name and id (save the change into the JSON file)

      (hbnb) destroy 'Class name' 'id'

- `all` Prints all string representation of all instances based or not on the class name

      (hbnb) all || all 'Class name'

- `update` Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)

      (hbnb) update 'Class name' 'id' 'attribute_name'  'attribute_value'
      


<h2>Examples</h2>

      
     root@f576c3df40fe:/holbertonschool-AirBnB_clone# ./console.py
     (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

    (hbnb) help create

            Creates a new instance, saves it (to the JSON file)
            and prints the id. Example: (hbnb) create User

    (hbnb) create User
    14df5fcd-80e5-4efb-8adb-47a6aec8f174
    
    (hbnb) show User 14df5fcd-80e5-4efb-8adb-47a6aec8f174
    [User] (14df5fcd-80e5-4efb-8adb-47a6aec8f174) {'id': '14df5fcd-80e5-4efb-8adb-47a6aec8f174', 'created_at': datetime.datetime(2022, 10, 16, 9, 49, 53, 860345),    'updated_at': datetime.datetime(2022, 10, 16, 9, 49, 53, 860358)}
    
    (hbnb) create Place
    0a8e4be0-2ece-4114-a1cc-b7eb643b7cb5
    
    (hbnb) all Place
    ["[Place] (0a8e4be0-2ece-4114-a1cc-b7eb643b7cb5) {'id': '0a8e4be0-2ece-4114-a1cc-b7eb643b7cb5', 'created_at': datetime.datetime(2022, 10, 16, 9, 50, 25, 164060),     'updated_at': datetime.datetime(2022, 10, 16, 9, 50, 25, 164082)}"]
    
    (hbnb) all
    ["[User] (24938b8d-ee47-4b11-9e34-c0629064c8f5) {'id': '24938b8d-ee47-4b11-9e34-c0629064c8f5', 'created_at': datetime.datetime(2022, 10, 16, 9, 47, 54, 56446),     'updated_at': datetime.datetime(2022, 10, 16, 9, 47, 54, 56460)}", "[User] (14df5fcd-80e5-4efb-8adb-47a6aec8f174) {'id': '14df5fcd-80e5-4efb-8adb-47a6aec8f174',    'created_at': datetime.datetime(2022, 10, 16, 9, 49, 53, 860345), 'updated_at': datetime.datetime(2022, 10, 16, 9, 49, 53, 860358)}", "[Place] (0a8e4be0-2ece-  4114-a1cc-b7eb643b7cb5) {'id': '0a8e4be0-2ece-4114-a1cc-b7eb643b7cb5', 'created_at': datetime.datetime(2022, 10, 16, 9, 50, 25, 164060), 'updated_at': datetime.datetime(2022, 10, 16, 9, 50, 25, 164082)}"]
    
    (hbnb) destroy User 14df5fcd-80e5-4efb-8adb-47a6aec8f174
    
    (hbnb) show User 14df5fcd-80e5-4efb-8adb-47a6aec8f174
    ** no instance found **
    
    (hbnb) update Place 0a8e4be0-2ece-4114-a1cc-b7eb643b7cb5 name "Stonehenge"
    
    (hbnb) show Place 0a8e4be0-2ece-4114-a1cc-b7eb643b7cb5
    [Place] (0a8e4be0-2ece-4114-a1cc-b7eb643b7cb5) {'id': '0a8e4be0-2ece-4114-a1cc-b7eb643b7cb5', 'created_at': datetime.datetime(2022, 10, 16, 9, 50, 25, 164060), 'updated_at': datetime.datetime(2022, 10, 16, 9, 50, 25, 164082), 'name': 'Stonehenge'}
    
    (hbnb) quit
    root@f576c3df40fe:/holbertonschool-AirBnB_clone#

<h2>Tests</h2>
Our packages and modules were tested with <b>unittest</b> as can you see below:

      ~/holbertonschool-AirBnB_clone$python3 -m unittest discover tests -v
      test_amenity_name (test_models.test_amenity.TestBaseModel_Amenity) ... ok
      test_created (test_models.test_base_model.TestBaseModel) ... ok
      test_id (test_models.test_base_model.TestBaseModel) ... ok
      test_save (test_models.test_base_model.TestBaseModel) ... ok
      test_str (test_models.test_base_model.TestBaseModel) ... ok
      test_to_dict (test_models.test_base_model.TestBaseModel) ... ok
      test_update (test_models.test_base_model.TestBaseModel) ... ok
      test_city (test_models.test_city.TestBaseModel) ... ok
      test_file_storage_all (test_models.test_engine.test_file_storage.TestFileStorage) ... ok
      test_file_storage_new (test_models.test_engine.test_file_storage.TestFileStorage) ... ok
      test_file_storage_reload (test_models.test_engine.test_file_storage.TestFileStorage) ... ok
      test_file_storage_save (test_models.test_engine.test_file_storage.TestFileStorage) ... ok
      test_place_name (test_models.test_place.TestBaseModel_Place) ... ok
      test_review_text (test_models.test_review.TestBaseModel) ... ok
      test_state (test_models.test_state.TestBaseModel) ... ok
      test_user_email (test_models.test_user.TestBaseModel) ... ok
      test_user_first_name (test_models.test_user.TestBaseModel) ... ok
      test_user_last_name (test_models.test_user.TestBaseModel) ... ok
      test_user_password (test_models.test_user.TestBaseModel) ... ok

      ----------------------------------------------------------------------
      Ran 19 tests in 0.021s

      OK      
with the objetive to see the correct performance of the files. For more information about the tests, go in 'tests' folder.

<h2>Links to Resources</h2>

- [cmd module](https://docs.python.org/3.4/library/cmd.html)
- [uuid module](https://docs.python.org/3.4/library/uuid.html)
- [datetime](https://docs.python.org/3.4/library/datetime.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

<h2>Authors</h2>

- Gastón Larroque     - [gasstin](https://github.com/gasstin)
- Ignacio Capezzolo   - [NachoCape](https://github.com/NachoCape)
