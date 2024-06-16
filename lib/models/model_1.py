import sqlite3

class DonationManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect('donation_management.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

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

    def write_review(self, user_id, campaign_id, review):
        self.cursor.execute('''INSERT INTO Reviews (user_id, campaign_id, review) VALUES (?, ?, ?)''', (user_id, campaign_id, review))
        self.conn.commit()

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
def main():
    dms = DonationManagementSystem()
    
    print("Welcome to Donation Management System!")

    while True:
        print("\nMain Menu:")
        print("1. Register as a user")
        print("2. View available campaigns")
        print("3. Donate to a campaign")
        print("4. View donation history")
        print("5. Add a beneficiary")
        print("6. View beneficiary details")
        print("7. Write a review for a campaign")
        print("8. View reviews for a campaign")
        print("9. Add new campaign (admin)")
        print("10. Remove campaign (admin)")
        print("11. Update campaign details (admin)")
        print("12. Generate donation report (admin)")
        print("13. View all donations for a campaign")
        print("14. Search for campaigns by name")
        print("15. Search for beneficiaries by name")
        print("16. View most donated campaigns")
        print("17. View highest-rated campaigns")
        print("18. Update user profile")
        print("19. Generate campaign statistics report (admin)")
        print("20. View all users")
        print("21. View campaign details")
        print("22. Exit")

        choice = input("Enter your choice (1-22): ")

        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            dms.register_user(username, email, password)
            print("User registered successfully!")
        elif choice == '2':
            campaigns = dms.view_available_campaigns()
            print("Available Campaigns:")
            for campaign in campaigns:
                print(campaign)
        elif choice == '3':
            # Donate to a campaign
            campaign_id = int(input("Enter the campaign ID you want to donate to: "))
            amount = float(input("Enter the amount you want to donate: "))
            
            user_id = 1  
            dms.donate_to_campaign(user_id, campaign_id, amount)
            print("Donation successful!")
        elif choice == '4':
            # View donation history
            user_id = int(input("Enter your user ID: "))
            donations = dms.view_donation_history(user_id)
            print("Donation History:")
            for donation in donations:
                print(donation)
        elif choice == '5':
            # Add a beneficiary
            name = input("Enter beneficiary name: ")
            description = input("Enter beneficiary description: ")
            dms.add_beneficiary(name, description)
            print("Beneficiary added successfully!")
        elif choice == '6':
            # View beneficiary details
            beneficiaries = dms.view_beneficiary_details()
            print("Beneficiary Details:")
            for beneficiary in beneficiaries:
                print(beneficiary)
        elif choice == '7':
            # Write a review for a campaign
            campaign_id = int(input("Enter the campaign ID you want to review: "))
            review = input("Write your review: ")
            # Assuming user_id is obtained from user authentication
            user_id = 1  # Example user_id
            dms.write_review(user_id, campaign_id, review)
            print("Review submitted successfully!")
        elif choice == '8':
            # View reviews for a campaign
            campaign_id = int(input("Enter the campaign ID to view reviews: "))
            reviews = dms.view_reviews_for_campaign(campaign_id)
            print("Reviews for Campaign:")
            for review in reviews:
                print(review)
        elif choice == '9':
            # Add new campaign (admin)
            name = input("Enter campaign name: ")
            description = input("Enter campaign description: ")
            target_amount = float(input("Enter target amount: "))
            dms.add_campaign(name, description, target_amount)
            print("Campaign added successfully!")
        elif choice == '10':
            # Remove campaign (admin)
            campaign_id = int(input("Enter the campaign ID to remove: "))
            dms.remove_campaign(campaign_id)
            print("Campaign removed successfully!")
        elif choice == '11':
            # Update campaign details (admin)
            campaign_id = int(input("Enter the campaign ID to update: "))
            new_description = input("Enter new campaign description: ")
            new_target_amount = float(input("Enter new target amount: "))
            dms.update_campaign_details(campaign_id, new_description, new_target_amount)
            print("Campaign details updated successfully!")
        elif choice == '12':
            # Generate donation report (admin)
            report = dms.generate_donation_report()
            print("Donation Report:")
            for item in report:
                print(item)
        elif choice == '13':
            # View all donations for a campaign
            campaign_id = int(input("Enter the campaign ID to view donations: "))
            donations = dms.view_all_donations_for_campaign(campaign_id)
            print("All Donations for Campaign:")
            for donation in donations:
                print(donation)
        elif choice == '14':
            # Search for campaigns by name
            name = input("Enter campaign name to search: ")
            campaigns = dms.search_campaign_by_name(name)
            print("Search Results:")
            for campaign in campaigns:
                print(campaign)
        elif choice == '15':
            # Search for beneficiaries by name
            name = input("Enter beneficiary name to search: ")
            beneficiaries = dms.search_beneficiary_by_name(name)
            print("Search Results:")
            for beneficiary in beneficiaries:
                print(beneficiary)
        elif choice == '16':
            # View most donated campaigns
            most_donated = dms.view_most_donated_campaigns()
            print("Most Donated Campaigns:")
            for campaign in most_donated:
                print(campaign)
        elif choice == '17':
            # View highest-rated campaigns
            highest_rated = dms.view_highest_rated_campaigns()
            print("Highest Rated Campaigns:")
            for campaign in highest_rated:
                print(campaign)
        elif choice == '18':
            # Update user profile
            user_id = int(input("Enter your user ID: "))
            new_email = input("Enter new email: ")
            new_password = input("Enter new password: ")
            dms.update_user_profile(user_id, new_email, new_password)
            print("User profile updated successfully!")
        elif choice == '19':
            # Generate campaign statistics report (admin)
            report = dms.generate_campaign_statistics_report()
            print("Campaign Statistics Report:")
            for item in report:
                print(item)
        elif choice == '20':
            # View all users
            users = dms.view_all_users()
            print("All Users:")
            for user in users:
                print(user)
        elif choice == '21':
            # View campaign details
            campaign_id = int(input("Enter the campaign ID to view details: "))
            campaign = dms.view_campaign_details(campaign_id)
            print("Campaign Details:")
            print(campaign)
        elif choice == '22':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 22.")

if __name__ == "__main__":
    main()


