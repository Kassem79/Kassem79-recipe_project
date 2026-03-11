# Kassem79-recipe_project

User Stories for Django Full-Stack Web Application
1. User Registration

User Story:
As a new user, I want to create an account, so that I can access the web application and its services.

Acceptance Criteria

User can register with username, email, and password.

Password must meet security requirements.

User receives confirmation after registration.

2. User Login

User Story:
As a registered user, I want to log into the system, so that I can access my personal dashboard.

Acceptance Criteria

User enters valid username/email and password.

System authenticates credentials.

User is redirected to their dashboard.

3. User Logout

User Story:
As a logged-in user, I want to log out of the system, so that my account remains secure when I leave the platform.

Acceptance Criteria

Logout button is available.

Session is terminated after logout.

User is redirected to the home/login page.

4. Profile Management

User Story:
As a registered user, I want to view and update my profile information, so that my personal details stay current.

Acceptance Criteria

User can edit name, email, and other profile data.

Changes are saved in the database.

Confirmation message is displayed.

5. Create Data Entry (Core Feature)

User Story:
As a user, I want to create new records in the system, so that I can store relevant information.

Acceptance Criteria

Form allows users to input data.

Data is validated before saving.

Record is stored in the database.

6. View Data

User Story:
As a user, I want to view stored records, so that I can see the information I have added.

Acceptance Criteria

Records appear in a list/table format.

Only authorized users can view certain data.

7. Update Data

User Story:
As a user, I want to edit existing records, so that I can correct or update information.

Acceptance Criteria

Edit option is available.

Changes update the database.

8. Delete Data

User Story:
As a user, I want to delete records, so that I can remove outdated or incorrect information.

Acceptance Criteria

Delete button available.

Confirmation prompt before deletion.

Record is removed from the database.

9. Admin Management

User Story:
As an administrator, I want to manage users and application data, so that the system operates correctly.

Acceptance Criteria

Admin can view all users.

Admin can delete or modify user accounts.

Admin has access to admin dashboard.

10. Application Testing

User Story:
As a developer, I want to run automated tests, so that I can ensure the application works correctly after changes.

Acceptance Criteria

Unit tests exist for models and views.

Tests run successfully.

11. Version Control

User Story:
As a developer, I want to store project code in a version control system, so that changes can be tracked and collaborated on.

Acceptance Criteria

Project hosted in Git repository.

Commits documented with messages.

12. Deployment

User Story:
As a user, I want to access the application online, so that I can use it from anywhere.

Acceptance Criteria

Application deployed on a cloud platform.

Website is publicly accessible.

Security settings are configured.

## Keys views

Home Page (home)

Displays recipes categorized by meals (Hot Dishes, Salads, Desserts).

Recipe List (recipe_list)

Shows all recipes in one page.

Recipe Detail (recipe_detail)

Shows full details of a selected recipe.

Category List (category_list)

Displays all categories and recipes filtered by category.

Buttons allow filtering recipes dynamically.

CRUD Views

recipe_create – Add new recipe.

recipe_update – Edit existing recipe.

recipe_delete – Delete a recipe.

Authentication

login_view – User login.

logout_view – User logout.

signup_view – User signup.


## Wireframe Layout (Recipe Website)

## Pages Structure

------------------------------------------------
| Logo | Home | Recipes | Categories | Login   |
------------------------------------------------
|                Hero Section                  |
|         "Discover Delicious Recipes"         |
|             [Search Recipes]                 |
------------------------------------------------
| Featured Recipes                             |
|  [Recipe Card] [Recipe Card] [Recipe Card]   |
------------------------------------------------
| Categories                                   |
| Breakfast | Lunch | Dinner | Desserts        |
------------------------------------------------
| Footer                                       |
| About | Contact | Social Links               |
------------------------------------------------

## Django Project Structure

recipe_project/
│
├── recipe_project/
│     settings.py
│     urls.py
│
├── recipes/
│     models.py
│     views.py
│     urls.py
│
├── templates/
│     base.html
│     home.html
│     recipes.html
│     recipe_detail.html
│
├── static/
│     css/style.css
│     js/script.js



## HTML templates define what users see:

base.html – main layout, includes header, nav, footer.

home.html – shows featured recipes.

recipes.html – lists all recipes.

categories.html – shows categories with buttons to filter recipes.

recipe_detail.html – detailed view of one recipe.

recipe_form.html – form for creating/updating a recipe.

recipe_confirm_delete.html – confirms deletion.