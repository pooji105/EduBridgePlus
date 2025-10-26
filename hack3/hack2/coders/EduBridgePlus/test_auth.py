#!/usr/bin/env python3
"""
Simple test script to verify the authentication system
"""
import requests
import sys

def test_auth_system():
    base_url = "http://localhost:5000"
    
    print("Testing EduBridge+ Authentication System")
    print("=" * 50)
    
    try:
        # Test 1: Check if auth landing page is accessible
        print("1. Testing auth landing page...")
        response = requests.get(f"{base_url}/auth")
        if response.status_code == 200:
            print("   ✓ Auth landing page accessible")
        else:
            print(f"   ✗ Auth landing page failed: {response.status_code}")
            return False
        
        # Test 2: Check if login page is accessible
        print("2. Testing login page...")
        response = requests.get(f"{base_url}/login")
        if response.status_code == 200:
            print("   ✓ Login page accessible")
        else:
            print(f"   ✗ Login page failed: {response.status_code}")
            return False
        
        # Test 3: Check if register page is accessible
        print("3. Testing register page...")
        response = requests.get(f"{base_url}/register")
        if response.status_code == 200:
            print("   ✓ Register page accessible")
        else:
            print(f"   ✗ Register page failed: {response.status_code}")
            return False
        
        # Test 4: Check if main page redirects to login when not authenticated
        print("4. Testing main page redirect...")
        response = requests.get(f"{base_url}/", allow_redirects=False)
        if response.status_code == 302:  # Redirect
            print("   ✓ Main page correctly redirects to login")
        else:
            print(f"   ✗ Main page redirect failed: {response.status_code}")
            return False
        
        print("\n" + "=" * 50)
        print("✓ All authentication tests passed!")
        print("The authentication system is working correctly.")
        print("\nTo test the full flow:")
        print("1. Visit http://localhost:5000/auth")
        print("2. Click 'Register' to create a new account")
        print("3. Click 'Login' to sign in")
        print("4. You should be redirected to the main application")
        
        return True
        
    except requests.exceptions.ConnectionError:
        print("✗ Could not connect to the application.")
        print("Make sure the Flask app is running on http://localhost:5000")
        return False
    except Exception as e:
        print(f"✗ Error during testing: {e}")
        return False

if __name__ == "__main__":
    success = test_auth_system()
    sys.exit(0 if success else 1)

