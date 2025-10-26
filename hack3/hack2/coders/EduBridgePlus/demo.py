#!/usr/bin/env python3
"""
EduBridge+ - AI-Powered Learning for a Sustainable Future
Demo and Setup Script

This script demonstrates the key features of EduBridge+ and provides
instructions for running the application.
"""

import os
import sys
import subprocess

def print_banner():
    """Print the EduBridge+ banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    🌍 EduBridge+ - AI-Powered Learning Platform 🌍         ║
    ║                                                              ║
    ║    📚 Learn. Act. Impact.                                   ║
    ║                                                              ║
    ║    Aligned with SDG 4, 6, and 13                            ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_requirements():
    """Check if required packages are installed"""
    print("🔍 Checking requirements...")
    
    try:
        import flask
        import flask_sqlalchemy
        print("✅ Flask and Flask-SQLAlchemy are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("📦 Please install requirements: pip install -r requirements.txt")
        return False

def show_features():
    """Display the key features of EduBridge+"""
    features = """
    🚀 Key Features:
    
    🧠 AI-Powered Learning
    ├── Smart explanations for sustainability topics
    ├── Multiple learning modes (Basic, Deep Dive, Action)
    ├── Voice input/output with Web Speech API
    └── Dynamic 3-question quizzes with instant feedback
    
    🎯 SDG-Focused Content
    ├── SDG 4: Quality Education
    ├── SDG 6: Clean Water and Sanitation
    └── SDG 13: Climate Action
    
    🏆 Gamification System
    ├── Progress tracking across all SDGs
    ├── Achievement badges (Eco Starter, Water Warrior, Climate Champion)
    └── Interactive dashboard with Chart.js visualizations
    
    🌍 Community Features
    ├── Share sustainability actions
    ├── Like and interact with posts
    └── Real-time database-backed interactions
    
    📊 Analytics & Insights
    ├── Platform statistics and trends
    ├── Leaderboard with top performers
    ├── Topic popularity analysis
    └── SDG impact tracking
    
    📱 Progressive Web App (PWA)
    ├── Offline support with service worker
    ├── Installable on mobile and desktop
    ├── Responsive design for all devices
    └── App-like experience in the browser
    """
    print(features)

def run_application():
    """Run the EduBridge+ application"""
    print("\n🚀 Starting EduBridge+...")
    print("📱 The application will be available at: http://localhost:5000")
    print("🌐 Open your browser and navigate to the URL above")
    print("📱 On mobile, you can install it as a PWA!")
    print("\n" + "="*60)
    
    try:
        # Change to the EduBridgePlus directory
        os.chdir('EduBridgePlus')
        
        # Run the Flask application
        subprocess.run([sys.executable, 'app.py'], check=True)
    except subprocess.CalledProcessError:
        print("❌ Error running the application")
        print("💡 Make sure you're in the correct directory and all dependencies are installed")
    except KeyboardInterrupt:
        print("\n👋 Thanks for using EduBridge+!")

def show_demo_instructions():
    """Show instructions for exploring the demo"""
    instructions = """
    🎮 Demo Exploration Guide:
    
    1. 🏠 Homepage
       ├── Click "Start Learning" to begin
       ├── Try the "Install App" button for PWA features
       └── Explore navigation to different sections
    
    2. 📚 Learning Center
       ├── Select different AI modes (Basic, Deep Dive, Action)
       ├── Try voice input: Click microphone and say "Climate Change"
       ├── Use voice output: Click speaker to hear AI explanations
       ├── Take quizzes and see instant feedback
       └── Check out the action plans for practical steps
    
    3. 📊 Dashboard
       ├── View your learning progress
       ├── See SDG distribution charts
       ├── Check badge achievements
       └── Monitor quiz scores and topics learned
    
    4. 🌍 Community
       ├── Post your sustainability actions
       ├── Like community posts
       ├── See real-time interactions
       └── Get inspired by others' efforts
    
    5. 🏆 Leaderboard
       ├── See top learners by score
       ├── Check community champions
       └── Track your ranking
    
    6. 📈 Analytics
       ├── View platform statistics
       ├── See topic popularity trends
       ├── Check SDG impact distribution
       └── Monitor your personal progress
    
    💡 Pro Tips:
    - Try different topics to see varied AI responses
    - Use voice features for accessibility
    - Install as PWA for offline access
    - Share actions in community to inspire others
    """
    print(instructions)

def main():
    """Main function to run the demo"""
    print_banner()
    
    if not check_requirements():
        return
    
    show_features()
    
    print("\n" + "="*60)
    choice = input("🎯 Would you like to:\n1. Run the application now\n2. See demo instructions\n3. Exit\n\nEnter your choice (1-3): ")
    
    if choice == "1":
        run_application()
    elif choice == "2":
        show_demo_instructions()
        print("\n" + "="*60)
        run_choice = input("🚀 Ready to run the application? (y/n): ")
        if run_choice.lower() == 'y':
            run_application()
    else:
        print("👋 Thanks for exploring EduBridge+!")
        print("🌱 Remember: Every small step towards sustainability counts!")

if __name__ == "__main__":
    main()
