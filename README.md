# BE Capstone Project: Inventory Management API

This API has been successfully deployed. You can access it at [derileeinventory.pythonanywhere.com](https://derileeinventory.pythonanywhere.com)

## How to Use on Postman

1. **Register a User**
   - Go to [derileeinventory.pythonanywhere.com/register/](https://derileeinventory.pythonanywhere.com/register/) to create a user.
   - **Using Postman**: 
     - Enter the URL `https://derileeinventory.pythonanywhere.com/register/` and choose `POST` as the HTTP request.
     - In the `Body` tab, choose `raw`, then `JSON`, and input the following:
       ```json
       {
         "username": "your_username",
         "first_name": "your_firstName",
         "last_name": "your_lastName",
         "email": "your_email",
         "password": "your_password"
       }
       ```
     - Click **Send**.

2. **Login**
   - **Using Postman**:
     - Enter `https://derileeinventory.pythonanywhere.com/login/` as the URL with a `POST` request.
     - Input the following in `Body`:
       ```json
       {
         "username": "your_username",
         "password": "your_password"
       }
       ```
     - Click **Send**. A refresh token and access token will be provided in the response.

3. **Authorization**
   - Copy the `access_token` and go to the `Authorization` tab in Postman.
   - Select `Bearer Token` and paste the token.
   - **Note**: Keep your `refresh_token` commented in your JSON body for easy access when trying to get a new access token:
     ```json
     //  {  
     "refresh_token": "your_refresh_token"
     }
     ```

4. **Access and Update Profile**
   - **GET** your profile at `https://derileeinventory.pythonanywhere.com/profile/`.
   - Change the HTTP request to `PUT` or `PATCH` to update profile details:
     ```json
     {
       "username": "your_username",
       "first_name": "your_firstName",
       "last_name": "your_lastName",
       "email": "your_email",
       "staff_id": "your_staffId",
       "position": "your_position",
       "profile_picture": null
     }
     ```

5. **Create an Inventory Item**
   - **POST** at `https://derileeinventory.pythonanywhere.com/inventory/create/`:
     ```json
     {
       "name": "Water",
       "description": "a pack of Bottle water(50cl)",
       "quantity": 20,
       "price": 2500.00,
       "category": "Beverages"
     }
     ```

6. **View Inventory Items**
   - **GET** all items at `https://derileeinventory.pythonanywhere.com/inventory/`.

7. **Update, View, or Delete an Item**
   - Use `https://derileeinventory.pythonanywhere.com/inventory/id/` with appropriate HTTP methods:
     - `PUT` or `PATCH` to update.
     - `GET` for detailed view.
     - `DELETE` to remove an item.

8. **View Inventory Change History**
   - **GET** at `https://derileeinventory.pythonanywhere.com/inventory/history/`.

9. **View Current Inventory Levels**
   - **GET** at `https://derileeinventory.pythonanywhere.com/inventory/current-levels/`.

10. **Sorting and Filtering**
    - **Sort** by price: 
      - Ascending: `https://derileeinventory.pythonanywhere.com/inventory/?ordering=price`
      - Descending: `https://derileeinventory.pythonanywhere.com/inventory/?ordering=-price`
    - **Filter** by category: 
      - Example: `https://derileeinventory.pythonanywhere.com/inventory/?category=Beverages`
    - **Filter by price range**: 
      - Example: `https://derileeinventory.pythonanywhere.com/inventory/?price__gte=1000&price__lte=5000`
    - **Fetch Low Stock Items**: 
      - **GET** at `https://derileeinventory.pythonanywhere.com/inventory/?low_stock=True`.

11. **Logout**
    -  **POST** at `https://derileeinventory.pythonanywhere.com/logout/`.
  
12. **Get New Access Token if the current expires**
    - Uncomment your `refresh_token` in the JSON body
    - **POST** `https://derileeinventory.pythonanywhere.com/api/token/refresh/`
    - if the refresh token is valid, the server will respond with a new access token `"access": "new_access_token_generated_by_the_server"`
    - Note: The access token remains valid until it expires, which is currently set to 120 minutes
