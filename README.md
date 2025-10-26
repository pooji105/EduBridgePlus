# EduBridge+ - AI-Powered Learning for a Sustainable Future

![EduBridge+ Logo](https://img.shields.io/badge/EduBridge+-AI%20Learning-green?style=for-the-badge&logo=education)

A comprehensive sustainability learning platform aligned with SDG 4 (Quality Education), SDG 6 (Clean Water), and SDG 13 (Climate Action). Built with Flask, featuring AI-powered explanations, gamification, community features, and PWA capabilities.

## 🌟 Features

### 🧠 AI-Powered Learning
- **Smart Explanations**: AI-generated content for sustainability topics
- **Multiple Learning Modes**: Basic, Deep Dive, and Action-focused learning
- **Voice Interaction**: Speech-to-text input and text-to-speech output
- **Dynamic Quizzes**: 3-question multiple-choice quizzes with instant feedback

### 🎯 SDG-Focused Content
- **SDG 4**: Quality Education topics and resources
- **SDG 6**: Clean Water and Sanitation learning materials
- **SDG 13**: Climate Action and environmental sustainability

### 🏆 Gamification System
- **Progress Tracking**: Track learning across all SDGs
- **Achievement Badges**: 
  - 🌱 Eco Starter (3 topics)
  - 💧 Water Warrior (5 topics)
  - 🌞 Climate Champion (10 topics)
- **Interactive Dashboard**: Visual progress with Chart.js

### 🌍 Community Features
- **Action Sharing**: Post sustainability actions and inspire others
- **Social Engagement**: Like and interact with community posts
- **Real-time Updates**: Database-backed community interactions

### 📊 Analytics & Insights
- **Platform Analytics**: Comprehensive statistics and trends
- **Leaderboard**: Top performers and community champions
- **Topic Popularity**: Most engaging sustainability topics
- **SDG Impact Tracking**: Visual representation of learning distribution

### 📱 Progressive Web App (PWA)
- **Offline Support**: Service worker for offline functionality
- **Installable**: Add to home screen on mobile and desktop
- **Responsive Design**: Optimized for all device sizes
- **App-like Experience**: Native app feel in the browser

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd EduBridgePlus
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **SQLite**: Database for user progress and community posts

### Frontend
- **HTML5/CSS3**: Modern web standards
- **JavaScript**: Interactive features and API calls
- **Chart.js**: Data visualization
- **Web Speech API**: Voice interaction

### AI Integration
- **Custom AI Helper**: Topic-specific content generation
- **Smart Categorization**: Automatic SDG classification
- **Dynamic Content**: Mode-based learning adaptation

## 📁 Project Structure

```
EduBridgePlus/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── manifest.json      # PWA manifest
│   └── service-worker.js  # PWA service worker
├── templates/
│   ├── index.html         # Homepage
│   ├── learn.html         # Learning center
│   ├── dashboard.html     # User dashboard
│   ├── community.html     # Community page
│   ├── leaderboard.html   # Leaderboard
│   └── analytics.html     # Analytics page
└── utils/
    └── ai_helper.py       # AI content generation
```

## 🎮 How to Use

### Learning Journey
1. **Start Learning**: Choose from 12+ sustainability topics
2. **Select Mode**: Pick Basic, Deep Dive, or Action mode
3. **AI Explanation**: Get comprehensive topic coverage
4. **Take Quiz**: Test your knowledge with interactive quizzes
5. **Action Plan**: Get practical steps to make a difference
6. **Track Progress**: Monitor your SDG learning journey

### Community Engagement
1. **Share Actions**: Post your sustainability efforts
2. **Inspire Others**: Like and engage with community posts
3. **Build Momentum**: See collective impact through analytics

### Voice Features
1. **Voice Input**: Click microphone to speak topic names
2. **Voice Output**: Listen to AI explanations with text-to-speech
3. **Accessibility**: Enhanced learning experience for all users

## 🌱 Sustainability Impact

### Educational Impact
- **Knowledge Building**: Comprehensive sustainability education
- **Skill Development**: Critical thinking and environmental awareness
- **Behavioral Change**: Action-oriented learning approach

### Community Impact
- **Collective Action**: Shared sustainability efforts
- **Social Learning**: Peer-to-peer knowledge sharing
- **Motivation**: Gamified progress tracking

### Technical Impact
- **Accessibility**: PWA ensures wide device compatibility
- **Performance**: Optimized for low-bandwidth environments
- **Scalability**: Database-backed architecture for growth

## 🔧 Configuration

### Environment Variables
- `FLASK_ENV`: Set to `development` for debug mode
- `SECRET_KEY`: Flask secret key for sessions

### Database
- SQLite database automatically created on first run
- Sample community posts included for demonstration

## 📈 Future Enhancements

### Planned Features
- **Multi-language Support**: Expand to global audiences
- **Advanced AI**: Integration with external AI APIs
- **Mobile App**: Native iOS/Android applications
- **Certification System**: Digital badges and certificates
- **Teacher Dashboard**: Classroom management features

### Technical Improvements
- **Performance Optimization**: Caching and CDN integration
- **Security Enhancements**: Authentication and authorization
- **API Development**: RESTful API for third-party integrations
- **Analytics Enhancement**: Advanced data visualization

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **UN Sustainable Development Goals**: Framework for content alignment
- **Flask Community**: Excellent web framework
- **Chart.js**: Beautiful data visualization
- **Web Standards**: PWA and accessibility features

## 📞 Support

For support, questions, or feedback:
- Create an issue in the repository
- Contact the development team
- Check the documentation

---

**EduBridge+** - Empowering learners to tackle global challenges through AI-driven education. 🌍📚✨
