
import model_1
from model_1 import User
from model_1 import Campaign
from model_1 import Donation
from model_1 import Beneficiary
import sqlite3



def main():
    print("Welcome to Donation Management System!")
    while True:
        print("\nMain Menu:")
        print("1. Register as a user")
        print("2. View available campaigns")
        print("3. Donate to a campaign")
        print("4. View donation history")
        print("5. View beneficiary details")
        print("6. Write a review for a campaign")
        print("7. View reviews for a campaign")
        print("8. Add new campaigns ")
        print("9. Remove campaigns ")
        print("10. Update campaign details ")
        print("11. Generate donation report ")
        print("12. View all donations for a campaign")
        print("13. Search for campaigns by name")
        print("14. Search for beneficiaries by name")
        print("15. View most donated campaigns")
        print("16. View highest-rated campaigns")
        print("17. Update user profile")
        print("18. Generate campaign statistics report ")
        print("19. View all users")
        print("20. View campaign details")
        print("21. Exit")
        break
choice = input("Enter your choice: ")

if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            new_user = User(username, email, password)
            new_user.save()
            
elif choice == '2':
            # View available campaigns
            campaigns = Campaign.display_all()
            for campaign in campaigns:
             print(campaign)
            
elif choice == '3':
            # Donate to a campaign
              campaign_name = input("Enter the name of the campaign you want to donate to: ")
              amount = float(input("Enter the amount you want to donate: "))
              
              
elif choice == '4':
            # View donation history
             user_donations = Donation.display_all_for_user()
             for donation in user_donations:
              print(donation)
             pass
elif choice == '5':
            # View beneficiary details
            beneficiaries = Beneficiary.display_all()
            for beneficiary in beneficiaries:
             print(beneficiary)
            pass
elif choice == '6':
            campaign_name = input("Enter the name of the campaign you want to review: ")
            review = input("Write your review: ")
            ( campaign_name, review)
            pass
elif choice == '7':
            # View reviews for a campaign
            pass
elif choice == '8':
            # Add new campaigns (admin)
            admin_key = input("Enter admin key: ")
            
            name = input("Enter campaign name: ")
            description = input("Enter campaign description: ")
            target_amount = float(input("Enter target amount: "))
            
            
            
            pass
elif choice == '9':
            # Remove campaigns (admin)
              
              campaign_name = input("Enter the name of the campaign you want to remove: ")
              del(campaign_name)
              print("deleted")
              
elif choice == '10':
            # Update campaign details (admin)
            pass
elif choice == '11':
            # Generate donation report (admin)
            pass
elif choice == '12':
            # View all donations for a campaign
            pass
elif choice == '13':
            # Search for campaigns by name
            pass
elif choice == '14':
            # Search for beneficiaries by name
            pass
elif choice == '15':
            # View most donated campaigns
            pass
elif choice == '16':
            # View highest-rated campaigns
            pass
elif choice == '17':
    # Update user profile
    username = input("Enter your username: ")
    new_email = input("Enter your new email: ")
    new_password = input("Enter your new password: ")

    # Find the user by username
    user = User.find_by_username(username)
    if user:
        # Update the user's email and password
        user.update_profile(new_email, new_password)
        print("User profile updated successfully!")
    else:
        print("User not found. Please enter a valid username.")

        pass
elif choice == '18':
            # Generate campaign statistics report (admin)
            pass
elif choice == '19':
            # View all users
            pass
elif choice == '20':
            # View campaign details
            pass
elif choice == '21':
            print("Exiting...")
            
else:
            print("Invalid choice. Please enter a number between 1 and 21.")

if __name__ == "__main__":
    main()
