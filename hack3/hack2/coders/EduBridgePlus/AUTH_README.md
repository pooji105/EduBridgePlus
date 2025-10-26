# EduBridge+ Authentication System

This document describes the authentication system implemented for EduBridge+, a Flask-based learning platform.

## Features

### 🔐 Authentication Features
- **User Registration**: New users can create accounts with username, email, and password
- **Secure Login**: Password-based authentication with secure password hashing
- **Session Management**: Flask-Login integration for session handling
- **Route Protection**: All main application routes require authentication
- **Logout Functionality**: Secure logout with session cleanup

### 🎨 User Interface
- **Landing Page**: Clean welcome page with login/register options
- **Bootstrap Styling**: Modern, responsive design
- **Password Strength**: Real-time password strength indicator
- **Flash Messages**: User feedback for all authentication actions
- **Mobile Responsive**: Works on all device sizes

## File Structure

```
templates/
├── auth.html          # Landing page with login/register options
├── login.html         # User login form
├── register.html      # User registration form
└── index.html         # Main application (updated with user info)

app.py                 # Main Flask application with authentication
requirements.txt       # Updated with Flask-Login dependency
```

## Database Schema

### User Model
```python
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

## Routes

### Authentication Routes
- `GET /auth` - Landing page with login/register options
- `GET/POST /login` - User login form and processing
- `GET/POST /register` - User registration form and processing
- `GET /logout` - User logout (requires authentication)

### Protected Routes
All main application routes now require authentication:
- `GET /` - Main application homepage
- `GET/POST /learn` - Learning center
- `GET /dashboard` - User dashboard
- `GET /community` - Community page
- `GET /leaderboard` - Leaderboard
- `GET /analytics` - Analytics page

## Security Features

### Password Security
- **Hashing**: Passwords are hashed using Werkzeug's `generate_password_hash`
- **Verification**: Password verification using `check_password_hash`
- **Strength Indicator**: Real-time password strength feedback during registration

### Session Security
- **Flask-Login**: Secure session management
- **User Loading**: Automatic user loading from session
- **Login Required**: Decorator-based route protection
- **Logout**: Secure session cleanup

### Input Validation
- **Username**: 3-20 characters, unique
- **Email**: Valid email format, unique
- **Password**: Minimum 6 characters, strength validation
- **Confirmation**: Password confirmation matching

## Usage

### 1. Start the Application
```bash
cd coders/EduBridgePlus
python app.py
```

### 2. Access the Application
- Visit `http://localhost:5000/auth` to see the landing page
- Click "Register" to create a new account
- Click "Login" to sign in with existing credentials

### 3. User Flow
1. **First Visit**: Redirected to `/auth` landing page
2. **Registration**: Fill out registration form with username, email, password
3. **Login**: Use credentials to access the application
4. **Main App**: Full access to all learning features
5. **Logout**: Click logout button to return to landing page

## Testing

### Manual Testing
1. Start the application: `python app.py`
2. Visit `http://localhost:5000/auth`
3. Test registration with new user
4. Test login with created user
5. Test logout functionality
6. Test direct access to protected routes

### Automated Testing
Run the test script:
```bash
python test_auth.py
```

## Dependencies

### New Dependencies
- `Flask-Login==0.6.3` - User session management
- `Werkzeug` - Password hashing (already included)

### Updated Files
- `requirements.txt` - Added Flask-Login
- `app.py` - Added authentication routes and models
- `templates/` - New authentication templates

## Configuration

### Environment Variables
- `SECRET_KEY` - Flask secret key for session security
- `SQLALCHEMY_DATABASE_URI` - Database connection string

### Database
- SQLite database (`edubridge.db`)
- Automatic table creation on first run
- User table with authentication fields

## Error Handling

### Registration Errors
- Username already exists
- Email already registered
- Password confirmation mismatch
- Weak password strength

### Login Errors
- Invalid username or password
- Account not found

### Session Errors
- Unauthenticated access to protected routes
- Session timeout handling

## Future Enhancements

### Potential Improvements
- Email verification for registration
- Password reset functionality
- Remember me option
- Two-factor authentication
- Social login integration
- User profile management

## Troubleshooting

### Common Issues
1. **Database not found**: Run the app once to create the database
2. **Import errors**: Install Flask-Login: `pip install Flask-Login==0.6.3`
3. **Template not found**: Ensure all template files are in the `templates/` directory
4. **Session issues**: Clear browser cookies and restart the application

### Debug Mode
Run with debug mode for detailed error messages:
```python
app.run(debug=True)
```

## Support

For issues or questions about the authentication system, check:
1. Flask-Login documentation
2. Werkzeug security documentation
3. Bootstrap documentation for UI issues
4. Application logs for debugging information

