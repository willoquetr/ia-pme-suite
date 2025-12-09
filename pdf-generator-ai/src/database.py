import sqlite3
import os
from pathlib import Path
from typing import Optional, Dict, List, Any
from src.config import settings
from src.logger import app_logger


class Database:
    """Gestion de la base de données SQLite."""
    
    def __init__(self, db_path: str = None):
        self.db_path = db_path or settings.db_path
        self.connection = None
        self.init_db()
    
    def connect(self) -> sqlite3.Connection:
        """Établir la connexion."""
        if self.connection is None:
            Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
        return self.connection
    
    def init_db(self) -> None:
        """Créer les tables si elles n'existent pas."""
        conn = self.connect()
        cursor = conn.cursor()
        
        # Table users
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                company_name TEXT,
                is_admin BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Table document types
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS document_types (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT,
                template_file TEXT,
                required_fields TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Table generated documents
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS generated_documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                document_type TEXT NOT NULL,
                title TEXT NOT NULL,
                content TEXT,
                pdf_path TEXT,
                file_size INTEGER,
                status TEXT DEFAULT 'completed',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        
        # Table document templates
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS document_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                document_type TEXT NOT NULL,
                template_name TEXT NOT NULL,
                template_content TEXT NOT NULL,
                is_default BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        
        # Table audit logs
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                action TEXT NOT NULL,
                details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        
        conn.commit()
        app_logger.info("Database initialized successfully")
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """Exécuter une requête SELECT."""
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            app_logger.error(f"Database query error: {e}")
            raise
    
    def execute_insert(self, query: str, params: tuple = ()) -> int:
        """Exécuter une insertion."""
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            app_logger.error(f"Database insert error: {e}")
            raise
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """Exécuter une mise à jour."""
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount
        except sqlite3.Error as e:
            app_logger.error(f"Database update error: {e}")
            raise
    
    def close(self) -> None:
        """Fermer la connexion."""
        if self.connection:
            self.connection.close()
            self.connection = None


db = Database()
