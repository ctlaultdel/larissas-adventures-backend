# Larissa's Adventures Blog (Backend)

Tech Stack: Python (Flask), PostgreSQL, LargeBinary database storage for images

### Routes
1. GET `https://larissas-adventures-backend-180179e43c72.herokuapp.com/adventures`
- Returns array of data from adventure table, which includes adventure columns id, name, url, img, and public. Public (boolean) serves as a blog feature-flag and allows navigation to blog url once publication is ready. Imgs are stored as large binary and converted to base64 in an effort to reduce space complexity.

## Database Schema
![Database_scheme](https://github.com/user-attachments/assets/7b462e57-ad5e-4b5a-8183-dc8aaf04de40)
