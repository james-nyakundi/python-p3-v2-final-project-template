import sqlite3

class DonationManagementSystem:


    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                target_amount REAL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                campaign_id INTEGER,
                amount REAL,
                FOREIGN KEY (user_id) REFERENCES Users(id),
                FOREIGN KEY (campaign_id) REFERENCES Campaigns(id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Beneficiaries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                campaign_id INTEGER,
                review TEXT,
                rating INTEGER,  -- Add rating column
                FOREIGN KEY (user_id) REFERENCES Users(id),
                FOREIGN KEY (campaign_id) REFERENCES Campaigns(id)
            )
        ''')

        self.conn.commit()

    def register_user(self, username, email, password):
        self.cursor.execute('''INSERT INTO Users (username, email, password) VALUES (?, ?, ?)''', (username, email, password))
        self.conn.commit()

    def view_available_campaigns(self):
        self.cursor.execute('''SELECT * FROM Campaigns''')
        return self.cursor.fetchall()

    def donate_to_campaign(self, user_id, campaign_id, amount):
        self.cursor.execute('''INSERT INTO Donations (user_id, campaign_id, amount) VALUES (?, ?, ?)''', (user_id, campaign_id, amount))
        self.conn.commit()

    def view_donation_history(self, user_id):
        self.cursor.execute('''SELECT * FROM Donations WHERE user_id = ?''', (user_id,))
        return self.cursor.fetchall()

    def add_beneficiary(self, name, description):
        self.cursor.execute('''INSERT INTO Beneficiaries (name, description) VALUES (?, ?)''', (name, description))
        self.conn.commit()

    def view_beneficiary_details(self):
        self.cursor.execute('''SELECT * FROM Beneficiaries''')
        return self.cursor.fetchall()

    def write_review(self, user_id, campaign_id, review, rating):
        self.cursor.execute('''INSERT INTO Reviews (user_id, campaign_id, review, rating) VALUES (?, ?, ?, ?)''', (user_id, campaign_id, review, rating))
        self.conn.commit()

    def view_reviews_for_campaign(self, campaign_id):
        self.cursor.execute('''SELECT * FROM Reviews WHERE campaign_id = ?''', (campaign_id,))
        return self.cursor.fetchall()

    def view_highest_rated_campaigns(self):
        self.cursor.execute('''SELECT campaign_id, AVG(rating) AS avg_rating FROM Reviews GROUP BY campaign_id ORDER BY avg_rating DESC''')
        return self.cursor.fetchall()

    def update_user_profile(self, user_id, new_email, new_password):
        self.cursor.execute('''UPDATE Users SET email = ?, password = ? WHERE id = ?''', (new_email, new_password, user_id))
        self.conn.commit()

    def view_all_users(self):
        self.cursor.execute('''SELECT * FROM Users''')
        return self.cursor.fetchall()

    def add_campaign(self, name, description, target_amount):
        self.cursor.execute('''INSERT INTO Campaigns (name, description, target_amount) VALUES (?, ?, ?)''', (name, description, target_amount))
        self.conn.commit()

    def remove_campaign(self, campaign_id):
        self.cursor.execute('''DELETE FROM Campaigns WHERE id = ?''', (campaign_id,))
        self.conn.commit()

    def update_campaign_details(self, campaign_id, new_description, new_target_amount):
        self.cursor.execute('''UPDATE Campaigns SET description = ?, target_amount = ? WHERE id = ?''', (new_description, new_target_amount, campaign_id))
        self.conn.commit()

    def generate_donation_report(self):
        self.cursor.execute('''SELECT campaign_id, SUM(amount) AS total_donations FROM Donations GROUP BY campaign_id''')
        return self.cursor.fetchall()

    def view_all_donations_for_campaign(self, campaign_id):
        self.cursor.execute('''SELECT * FROM Donations WHERE campaign_id = ?''', (campaign_id,))
        return self.cursor.fetchall()

    def search_campaign_by_name(self, name):
        self.cursor.execute('''SELECT * FROM Campaigns WHERE name = ?''', (name,))
        return self.cursor.fetchall()

    def search_beneficiary_by_name(self, name):
        self.cursor.execute('''SELECT * FROM Beneficiaries WHERE name = ?''', (name,))
        return self.cursor.fetchall()

    def view_most_donated_campaigns(self):
        self.cursor.execute('''SELECT campaign_id, SUM(amount) AS total_donations FROM Donations GROUP BY campaign_id ORDER BY total_donations DESC''')
        return self.cursor.fetchall()

    def view_highest_rated_campaigns(self):
        self.cursor.execute('''SELECT campaign_id, AVG(rating) AS avg_rating FROM Reviews GROUP BY campaign_id ORDER BY avg_rating DESC''')
        return self.cursor.fetchall()

    def update_user_profile(self, user_id, new_email, new_password):
        self.cursor.execute('''UPDATE Users SET email = ?, password = ? WHERE id = ?''', (new_email, new_password, user_id))
        self.conn.commit()

    def generate_campaign_statistics_report(self):
        self.cursor.execute('''SELECT campaign_id, COUNT(*) AS num_reviews, AVG(rating) AS avg_rating FROM Reviews GROUP BY campaign_id''')
        return self.cursor.fetchall()

    def view_all_users(self):
        self.cursor.execute('''SELECT * FROM Users''')
        return self.cursor.fetchall()

    def view_campaign_details(self, campaign_id):
        self.cursor.execute('''SELECT * FROM Campaigns WHERE id = ?''', (campaign_id,))
        return self.cursor.fetchone()

    def __del__(self):
        self.conn.close()

# User interface
