import bcrypt
import sqlite3
from datetime import datetime

class AuthManager:
    def __init__(self, db_path="users.db"):
        self.db_path = db_path
        self.init_users_db()
    
    def init_users_db(self):
        """Initialize users database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def hash_password(self, password):
        """Hash password using bcrypt"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def verify_password(self, password, hashed):
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    
    def create_user(self, username, password):
        """Create new user account"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Check if username already exists
            cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
            if cursor.fetchone():
                conn.close()
                return False
            
            # Hash password and create user
            password_hash = self.hash_password(password)
            cursor.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
    
    def verify_user(self, username, password):
        """Verify user credentials"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute(
                "SELECT password_hash FROM users WHERE username = ?",
                (username,)
            )
            
            result = cursor.fetchone()
            conn.close()
            
            if result and self.verify_password(password, result[0]):
                return True
            return False
            
        except Exception as e:
            print(f"Error verifying user: {e}")
            return False
    
    def user_exists(self, username):
        """Check if user exists"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            conn.close()
            
            return result is not None
            
        except Exception as e:
            print(f"Error checking user existence: {e}")
            return False
