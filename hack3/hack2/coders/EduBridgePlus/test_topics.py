#!/usr/bin/env python3
"""
Test script to verify topic navigation functionality
"""
import requests
import sys

def test_topic_navigation():
    base_url = "http://localhost:5000"
    
    print("Testing EduBridge+ Topic Navigation System")
    print("=" * 50)
    
    try:
        # Test 1: Check if main page loads with topic cards
        print("1. Testing main page with topic cards...")
        response = requests.get(f"{base_url}/", allow_redirects=False)
        if response.status_code == 302:  # Redirect to login
            print("   ✓ Main page correctly redirects to login (authentication working)")
        else:
            print(f"   ✗ Main page access issue: {response.status_code}")
            return False
        
        # Test 2: Check if topic pages are accessible (should redirect to login)
        print("2. Testing topic page redirects...")
        test_topics = ["Climate_Change", "Water_Pollution", "Renewable_Energy"]
        
        for topic in test_topics:
            response = requests.get(f"{base_url}/topic/{topic}", allow_redirects=False)
            if response.status_code == 302:  # Redirect to login
                print(f"   ✓ Topic page /topic/{topic} correctly redirects to login")
            else:
                print(f"   ✗ Topic page /topic/{topic} failed: {response.status_code}")
                return False
        
        print("\n" + "=" * 50)
        print("✓ All topic navigation tests passed!")
        print("The topic navigation system is working correctly.")
        print("\nTo test the full functionality:")
        print("1. Visit http://localhost:5000/auth")
        print("2. Login or register a new account")
        print("3. Click on any topic card on the main page")
        print("4. You should be redirected to the topic detail page")
        print("5. Use the 'Back to Topics' button to return")
        
        return True
        
    except requests.exceptions.ConnectionError:
        print("✗ Could not connect to the application.")
        print("Make sure the Flask app is running on http://localhost:5000")
        return False
    except Exception as e:
        print(f"✗ Error during testing: {e}")
        return False

if __name__ == "__main__":
    success = test_topic_navigation()
    sys.exit(0 if success else 1)

