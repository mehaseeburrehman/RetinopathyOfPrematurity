import sqlite3
import json
from datetime import datetime
import base64
from PIL import Image
from io import BytesIO

class DatabaseManager:
    def __init__(self, db_path="predictions.db"):
        self.db_path = db_path
    
    def init_db(self):
        """Initialize predictions database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                image_data TEXT NOT NULL,
                prediction TEXT NOT NULL,
                confidence REAL NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
        print("✅ Database initialized successfully")
    
    def save_prediction(self, username, image_data, prediction, confidence):
        """Save prediction to database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO predictions (username, image_data, prediction, confidence)
                VALUES (?, ?, ?, ?)
            ''', (username, image_data, prediction, confidence))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            print(f"Error saving prediction: {e}")
            return False
    
    def get_user_history(self, username, limit=50):
        """Get user's prediction history"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, image_data, prediction, confidence, timestamp
                FROM predictions
                WHERE username = ?
                ORDER BY timestamp DESC
                LIMIT ?
            ''', (username, limit))
            
            results = cursor.fetchall()
            conn.close()
            
            # Format results
            history = []
            for row in results:
                history.append({
                    'id': row[0],
                    'image_data': row[1],
                    'prediction': row[2],
                    'confidence': row[3],
                    'timestamp': row[4]
                })
            
            return history
            
        except Exception as e:
            print(f"Error getting user history: {e}")
            return []
    
    def get_prediction_stats(self, username):
        """Get prediction statistics for user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT prediction, COUNT(*) as count
                FROM predictions
                WHERE username = ?
                GROUP BY prediction
            ''', (username,))
            
            results = cursor.fetchall()
            conn.close()
            
            return dict(results)
            
        except Exception as e:
            print(f"Error getting prediction stats: {e}")
            return {}
    
    def delete_user_data(self, username):
        """Delete all user data (for privacy compliance)"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM predictions WHERE username = ?', (username,))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            print(f"Error deleting user data: {e}")
            return False
