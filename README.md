# Larissa's Adventures Blog (Backend)

Tech Stack: Python (Flask), PostgreSQL, LargeBinary database storage for images

### Routes
1. GET `https://larissas-adventures-backend-180179e43c72.herokuapp.com/adventures`
- Returns array of all active records from the adventure table ordered by id, which includes: id, name, alt_name, img, and public.
- Public (boolean) serves as a blog feature-flag and allows navigation to the /blog endpoint once publication is ready. Imgs are stored as large binary and converted to base64 in an effort to reduce space complexity.
- Ability to provide query params for filtering adventures by alt_name e.g. `adventures?name={alt_name}`

2. GET `https://larissas-adventures-backend-180179e43c72.herokuapp.com/blogs`
- Requires header --> `Adventure-ID`
- Returns object of blog data associated with the provided adventure_id. The blog data object includes: title, publication_date (from blog table) and array of content objects (from content table): id, text, figure, caption.
- Content arrays are variable in size as a blog can have several iterations of text-figure-caption with any being nullable.
- Ability to provide query params for filtering blog by adventure alt_name e.g. `blogs?name={alt_name}`

## Database Schema
[Database_Scheme.pdf](https://github.com/user-attachments/files/19146177/Database_Scheme.pdf)
