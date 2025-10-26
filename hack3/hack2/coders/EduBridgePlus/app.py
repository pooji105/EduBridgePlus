from flask import Flask, render_template, request, session, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from utils.ai_helper import get_ai_response, get_youtube_links, get_daily_tip, generate_quiz, get_action_plan
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'edubridge_plus_secret_key_2024'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edubridge.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), unique=True, nullable=False)
    topics_learned = db.Column(db.Integer, default=0)
    quizzes_completed = db.Column(db.Integer, default=0)
    sdg_4_topics = db.Column(db.Integer, default=0)
    sdg_6_topics = db.Column(db.Integer, default=0)
    sdg_13_topics = db.Column(db.Integer, default=0)
    total_score = db.Column(db.Integer, default=0)
    badges = db.Column(db.Text, default='[]')  # JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CommunityPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    action = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(200), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialize user progress if not exists
def init_user_progress():
    if current_user.is_authenticated:
        # Use user ID for authenticated users
        session_id = f"user_{current_user.id}"
    else:
        # Use session ID for anonymous users
        session_id = session.get('session_id')
        if not session_id:
            session_id = f"session_{datetime.utcnow().timestamp()}"
            session['session_id'] = session_id
    
    # Check if user progress exists in database
    user_progress = UserProgress.query.filter_by(session_id=session_id).first()
    
    if not user_progress:
        # Create new user progress record
        user_progress = UserProgress(
            session_id=session_id,
            topics_learned=0,
            quizzes_completed=0,
            sdg_4_topics=0,
            sdg_6_topics=0,
            sdg_13_topics=0,
            total_score=0,
            badges='[]'
        )
        db.session.add(user_progress)
        db.session.commit()
    
    # Update session with database data
    session['progress'] = {
        'topics_learned': user_progress.topics_learned,
        'quizzes_completed': user_progress.quizzes_completed,
        'sdg_4_topics': user_progress.sdg_4_topics,
        'sdg_6_topics': user_progress.sdg_6_topics,
        'sdg_13_topics': user_progress.sdg_13_topics,
        'badges': json.loads(user_progress.badges),
        'total_score': user_progress.total_score
    }
    
    return user_progress

def update_user_progress():
    """Update user progress in database"""
    if current_user.is_authenticated:
        session_id = f"user_{current_user.id}"
    else:
        session_id = session.get('session_id')
        if not session_id:
            return
    
    user_progress = UserProgress.query.filter_by(session_id=session_id).first()
    if user_progress:
        user_progress.topics_learned = session['progress']['topics_learned']
        user_progress.quizzes_completed = session['progress']['quizzes_completed']
        user_progress.sdg_4_topics = session['progress']['sdg_4_topics']
        user_progress.sdg_6_topics = session['progress']['sdg_6_topics']
        user_progress.sdg_13_topics = session['progress']['sdg_13_topics']
        user_progress.total_score = session['progress']['total_score']
        user_progress.badges = json.dumps(session['progress']['badges'])
        user_progress.updated_at = datetime.utcnow()
        db.session.commit()

def check_badge_achievements():
    """Check and award badges based on progress"""
    badges = session['progress']['badges']
    topics_learned = session['progress']['topics_learned']
    
    # Eco Starter badge
    if topics_learned >= 3 and 'eco_starter' not in badges:
        badges.append('eco_starter')
    
    # Water Warrior badge
    if topics_learned >= 5 and 'water_warrior' not in badges:
        badges.append('water_warrior')
    
    # Climate Champion badge
    if topics_learned >= 10 and 'climate_champion' not in badges:
        badges.append('climate_champion')
    
    session['progress']['badges'] = badges

# Authentication routes
@app.route('/auth')
def auth():
    """Landing page with login and register options"""
    return render_template('auth.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Validation
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return render_template('register.html')
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('auth'))

@app.route('/topic/<topic_name>')
@login_required
def show_topic(topic_name):
    """Display topic details page"""
    return render_template('topic.html', topic_name=topic_name)

@app.route('/')
@login_required
def index():
    """Homepage route that renders the index.html template"""
    init_user_progress()
    return render_template('index.html')

@app.route('/learn', methods=['GET', 'POST'])
@login_required
def learn():
    """Learning center route with AI integration"""
    init_user_progress()
    
    if request.method == 'POST':
        topic = request.form['topic']
        mode = request.form.get('mode', 'basic')
        ai_output = get_ai_response(topic, mode)
        youtube_videos = get_youtube_links(topic)
        daily_tip = get_daily_tip()
        quiz_questions = generate_quiz(topic)
        action_plan = get_action_plan(topic)
        
        # Update progress
        session['progress']['topics_learned'] += 1
        
        # Determine SDG category
        topic_lower = topic.lower()
        if any(word in topic_lower for word in ['education', 'learning', 'school']):
            session['progress']['sdg_4_topics'] += 1
        elif any(word in topic_lower for word in ['water', 'ocean', 'river', 'pollution']):
            session['progress']['sdg_6_topics'] += 1
        elif any(word in topic_lower for word in ['climate', 'carbon', 'energy', 'renewable']):
            session['progress']['sdg_13_topics'] += 1
        
        # Check for badge achievements
        check_badge_achievements()
        update_user_progress()
        
        return render_template('learn.html', 
                             topic=topic, 
                             ai_output=ai_output,
                             youtube_videos=youtube_videos,
                             daily_tip=daily_tip,
                             quiz_questions=quiz_questions,
                             action_plan=action_plan)
    elif request.method == 'GET' and request.args.get('topic'):
        topic = request.args.get('topic')
        mode = request.args.get('mode', 'basic')
        ai_output = get_ai_response(topic, mode)
        youtube_videos = get_youtube_links(topic)
        daily_tip = get_daily_tip()
        quiz_questions = generate_quiz(topic)
        action_plan = get_action_plan(topic)
        
        # Update progress
        session['progress']['topics_learned'] += 1
        
        # Determine SDG category
        topic_lower = topic.lower()
        if any(word in topic_lower for word in ['education', 'learning', 'school']):
            session['progress']['sdg_4_topics'] += 1
        elif any(word in topic_lower for word in ['water', 'ocean', 'river', 'pollution']):
            session['progress']['sdg_6_topics'] += 1
        elif any(word in topic_lower for word in ['climate', 'carbon', 'energy', 'renewable']):
            session['progress']['sdg_13_topics'] += 1
        
        # Check for badge achievements
        check_badge_achievements()
        update_user_progress()
        
        return render_template('learn.html', 
                             topic=topic, 
                             ai_output=ai_output,
                             youtube_videos=youtube_videos,
                             daily_tip=daily_tip,
                             quiz_questions=quiz_questions,
                             action_plan=action_plan)
    return render_template('learn.html', 
                         topic=None, 
                         ai_output=None,
                         youtube_videos=None,
                         daily_tip=None,
                         quiz_questions=[],
                         action_plan=None)

@app.route('/dashboard')
@login_required
def dashboard():
    """SDG Dashboard showing user progress and achievements"""
    init_user_progress()
    return render_template('dashboard.html', progress=session['progress'])

@app.route('/community')
@login_required
def community():
    """Community page for sharing sustainability actions"""
    init_user_progress()
    posts = CommunityPost.query.order_by(CommunityPost.created_at.desc()).limit(20).all()
    return render_template('community.html', posts=posts)

@app.route('/api/posts', methods=['GET', 'POST'])
def api_posts():
    """API endpoint for community posts"""
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username', '').strip()
        action = data.get('action', '').strip()
        
        if username and action:
            post = CommunityPost(username=username, action=action)
            db.session.add(post)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Post created successfully!'})
        else:
            return jsonify({'success': False, 'message': 'Username and action are required'}), 400
    
    elif request.method == 'GET':
        posts = CommunityPost.query.order_by(CommunityPost.created_at.desc()).limit(20).all()
        return jsonify([{
            'id': post.id,
            'username': post.username,
            'action': post.action,
            'likes': post.likes,
            'created_at': post.created_at.isoformat()
        } for post in posts])

@app.route('/api/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    """Like a community post"""
    post = CommunityPost.query.get_or_404(post_id)
    post.likes += 1
    db.session.commit()
    return jsonify({'success': True, 'likes': post.likes})

@app.route('/leaderboard')
@login_required
def leaderboard():
    """Leaderboard showing top performers"""
    init_user_progress()
    
    # Get top users by total score
    top_users = db.session.query(
        UserProgress.session_id,
        UserProgress.topics_learned,
        UserProgress.quizzes_completed,
        UserProgress.total_score,
        UserProgress.sdg_4_topics,
        UserProgress.sdg_6_topics,
        UserProgress.sdg_13_topics
    ).order_by(UserProgress.total_score.desc()).limit(10).all()
    
    # Get most active community members
    top_contributors = db.session.query(
        CommunityPost.username,
        db.func.count(CommunityPost.id).label('post_count'),
        db.func.sum(CommunityPost.likes).label('total_likes')
    ).group_by(CommunityPost.username).order_by(db.func.sum(CommunityPost.likes).desc()).limit(10).all()
    
    return render_template('leaderboard.html', 
                         top_users=top_users, 
                         top_contributors=top_contributors,
                         progress=session['progress'])

@app.route('/analytics')
@login_required
def analytics():
    """Analytics page showing platform statistics"""
    init_user_progress()
    
    # Platform statistics
    total_users = UserProgress.query.count()
    total_posts = CommunityPost.query.count()
    total_quiz_attempts = QuizAttempt.query.count()
    total_likes = db.session.query(db.func.sum(CommunityPost.likes)).scalar() or 0
    
    # Topic popularity
    topic_stats = db.session.query(
        QuizAttempt.topic,
        db.func.count(QuizAttempt.id).label('attempts'),
        db.func.avg(QuizAttempt.percentage).label('avg_score')
    ).group_by(QuizAttempt.topic).order_by(db.func.count(QuizAttempt.id).desc()).limit(10).all()
    
    # SDG distribution
    sdg_stats = {
        'sdg_4': UserProgress.query.with_entities(db.func.sum(UserProgress.sdg_4_topics)).scalar() or 0,
        'sdg_6': UserProgress.query.with_entities(db.func.sum(UserProgress.sdg_6_topics)).scalar() or 0,
        'sdg_13': UserProgress.query.with_entities(db.func.sum(UserProgress.sdg_13_topics)).scalar() or 0
    }
    
    return render_template('analytics.html',
                         total_users=total_users,
                         total_posts=total_posts,
                         total_quiz_attempts=total_quiz_attempts,
                         total_likes=total_likes,
                         topic_stats=topic_stats,
                         sdg_stats=sdg_stats,
                         progress=session['progress'])

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    """Handle quiz submission and return score"""
    data = request.get_json()
    answers = data.get('answers', [])
    quiz_questions = data.get('questions', [])
    topic = data.get('topic', 'Unknown')
    
    correct = 0
    total = len(quiz_questions)
    
    for i, question in enumerate(quiz_questions):
        if i < len(answers) and answers[i] == question['correct']:
            correct += 1
    
    percentage = round((correct / total) * 100) if total > 0 else 0
    
    # Update progress
    session['progress']['quizzes_completed'] += 1
    session['progress']['total_score'] += correct
    
    # Save quiz attempt to database
    session_id = session.get('session_id')
    if session_id:
        quiz_attempt = QuizAttempt(
            session_id=session_id,
            topic=topic,
            score=correct,
            total_questions=total,
            percentage=percentage
        )
        db.session.add(quiz_attempt)
        db.session.commit()
    
    # Check for badge achievements
    check_badge_achievements()
    update_user_progress()
    
    return jsonify({
        'score': correct,
        'total': total,
        'percentage': percentage
    })

# Initialize database
with app.app_context():
    db.create_all()
    
    # Add some sample community posts if none exist
    if CommunityPost.query.count() == 0:
        sample_posts = [
            CommunityPost(username="EcoWarrior", action="Planted 10 trees in my neighborhood today 🌳", likes=5),
            CommunityPost(username="GreenThumb", action="Started composting kitchen waste - already reduced my trash by 30%! ♻️", likes=8),
            CommunityPost(username="WaterSaver", action="Installed low-flow showerheads and saved 50 gallons this week 💧", likes=12),
            CommunityPost(username="SolarFan", action="Switched to solar panels - my electricity bill is now $0! ☀️", likes=15),
            CommunityPost(username="BikeCommuter", action="Biked to work every day this month instead of driving 🚴‍♀️", likes=7)
        ]
        for post in sample_posts:
            db.session.add(post)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
