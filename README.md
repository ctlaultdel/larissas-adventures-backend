# Larissa's Adventures Blog (Backend)

Tech Stack: Python (Flask), PostgreSQL, LargeBinary database storage for images

### Routes
1. GET `https://larissas-adventures-backend-180179e43c72.herokuapp.com/adventures`
- Returns array of all adventures data (object) from the adventure table, which includes columns: id, name, url, img, and public. public (boolean) serves as a blog feature-flag and allows navigation to the blog url once publication is ready. Imgs are stored as large binary and converted to base64 in an effort to reduce space complexity.

## Database Schema
![Database_scheme](https://github.com/user-attachments/assets/7b462e57-ad5e-4b5a-8183-dc8aaf04de40)
