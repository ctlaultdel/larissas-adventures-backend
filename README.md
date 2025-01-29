# Larissa's Adventures Blog (Backend)

Tech Stack: Python (Flask), PostgreSQL, LargeBinary database storage for images

### Routes
GET `https://larissas-adventures-backend-180179e43c72.herokuapp.com/adventures`
- Returns array of data from adventure table, which includes adventure columns id, name, url, img, and public. Public (boolean) serves as a blog feature-flag and allows navigation to blog url once publication is ready. Imgs are stored as large binary and converted to base64 in an effort to reduce space complexity.

## Database Schema
![Database_scheme](https://github.com/user-attachments/assets/25e585e5-a106-4fc7-ac62-5f2c2a25de8d)
