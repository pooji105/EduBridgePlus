"""
AI Helper utilities for EduBridge+
This module contains AI-powered functions to assist with educational tasks focused on sustainability.
"""

import random
from typing import List, Dict, Any

def get_youtube_links(topic: str) -> List[Dict[str, str]]:
    """
    Get relevant YouTube video links for a given sustainability topic
    Returns a list of dictionaries with title and url
    """
    topic_lower = topic.lower()
    
    # Predefined video collections for different topics
    video_collections = {
        'climate': [
            {'title': 'Climate Change Explained in 5 Minutes', 'url': 'https://www.youtube.com/watch?v=G4H1N_yXBiA'},
            {'title': 'The Science of Climate Change', 'url': 'https://www.youtube.com/watch?v=EtW2rrLHs08'},
            {'title': 'How to Fight Climate Change', 'url': 'https://www.youtube.com/watch?v=0kL2hJ3n7sk'}
        ],
        'water': [
            {'title': 'Water Pollution: Causes and Solutions', 'url': 'https://www.youtube.com/watch?v=Om42Lppkd9w'},
            {'title': 'Ocean Plastic Pollution Explained', 'url': 'https://www.youtube.com/watch?v=HQTUWK7CM-Y'},
            {'title': 'How to Save Water at Home', 'url': 'https://www.youtube.com/watch?v=U6WqJ2Qj4cQ'}
        ],
        'energy': [
            {'title': 'Renewable Energy Explained', 'url': 'https://www.youtube.com/watch?v=1kUE0BZtTRc'},
            {'title': 'Solar Power: How It Works', 'url': 'https://www.youtube.com/watch?v=xKxrkht7CpY'},
            {'title': 'Wind Energy: The Future of Power', 'url': 'https://www.youtube.com/watch?v=QpViwKIwskE'}
        ],
        'education': [
            {'title': 'The Future of Education', 'url': 'https://www.youtube.com/watch?v=GEmuEWjHr5c'},
            {'title': 'Sustainable Development Goals Explained', 'url': 'https://www.youtube.com/watch?v=0XTBYMfZyrM'},
            {'title': 'Environmental Education for Kids', 'url': 'https://www.youtube.com/watch?v=WfGMYdalClU'}
        ],
        'default': [
            {'title': 'Sustainability: What It Means', 'url': 'https://www.youtube.com/watch?v=zx04Kl8y4dE'},
            {'title': 'How to Live More Sustainably', 'url': 'https://www.youtube.com/watch?v=V0lQ3ljjl40'},
            {'title': 'Environmental Protection Tips', 'url': 'https://www.youtube.com/watch?v=WmVLcj-XKnM'}
        ]
    }
    
    # Determine which collection to use based on topic
    if any(word in topic_lower for word in ['climate', 'carbon', 'warming', 'emission']):
        collection = 'climate'
    elif any(word in topic_lower for word in ['water', 'ocean', 'river', 'pollution']):
        collection = 'water'
    elif any(word in topic_lower for word in ['energy', 'solar', 'wind', 'renewable']):
        collection = 'energy'
    elif any(word in topic_lower for word in ['education', 'learning', 'school']):
        collection = 'education'
    else:
        collection = 'default'
    
    return video_collections[collection]

def get_daily_tip() -> str:
    """
    Get a random daily eco-friendly tip
    """
    eco_tips = [
        "💡 Turn off lights when leaving a room - it saves energy and reduces your carbon footprint!",
        "🌱 Use a reusable water bottle instead of plastic bottles - help reduce ocean pollution!",
        "🚶 Walk or bike for short trips - reduce emissions and stay healthy!",
        "♻️ Separate your recyclables - make sure paper, plastic, and glass go in the right bins!",
        "🌿 Plant a tree or start a small garden - every plant helps clean the air!",
        "💧 Take shorter showers - save water and energy used for heating!",
        "🛍️ Bring your own shopping bags - reduce plastic waste at stores!",
        "🌞 Use natural light during the day - open curtains instead of turning on lights!",
        "📱 Unplug electronics when not in use - they still consume energy when plugged in!",
        "🍎 Eat more plant-based meals - reduce your environmental impact through diet!",
        "🚗 Carpool or use public transport - reduce traffic and emissions!",
        "🌍 Support local businesses - reduce transportation emissions from shipping!",
        "📚 Borrow books from libraries - reduce paper consumption and save money!",
        "🔋 Use rechargeable batteries - reduce waste from disposable batteries!",
        "🌊 Participate in beach cleanups - help protect marine life!"
    ]
    
    return random.choice(eco_tips)

def generate_quiz(topic: str) -> List[Dict[str, Any]]:
    """
    Generate a 3-question multiple choice quiz for the given topic
    """
    topic_lower = topic.lower()
    
    # Predefined quiz questions for different topics
    quiz_templates = {
        'climate': [
            {
                'question': 'What is the primary cause of climate change?',
                'options': ['Solar radiation', 'Greenhouse gas emissions', 'Ocean currents', 'Volcanic activity'],
                'correct': 1,
                'explanation': 'Greenhouse gas emissions from human activities are the primary cause of climate change.'
            },
            {
                'question': 'Which gas is most responsible for global warming?',
                'options': ['Oxygen', 'Nitrogen', 'Carbon Dioxide', 'Argon'],
                'correct': 2,
                'explanation': 'Carbon dioxide (CO2) is the most significant greenhouse gas contributing to global warming.'
            },
            {
                'question': 'What is the Paris Agreement target for global temperature rise?',
                'options': ['1.5°C', '2°C', '3°C', '4°C'],
                'correct': 1,
                'explanation': 'The Paris Agreement aims to limit global temperature rise to well below 2°C, preferably 1.5°C.'
            }
        ],
        'water': [
            {
                'question': 'What percentage of Earth\'s water is freshwater?',
                'options': ['1%', '3%', '10%', '25%'],
                'correct': 1,
                'explanation': 'Only about 3% of Earth\'s water is freshwater, and most of it is frozen in glaciers.'
            },
            {
                'question': 'What is the main cause of ocean plastic pollution?',
                'options': ['Natural processes', 'Single-use plastics', 'Fish waste', 'Seaweed'],
                'correct': 1,
                'explanation': 'Single-use plastics are the main cause of ocean plastic pollution.'
            },
            {
                'question': 'How many people worldwide lack access to clean water?',
                'options': ['100 million', '500 million', '1 billion', '2 billion'],
                'correct': 3,
                'explanation': 'Approximately 2 billion people worldwide lack access to clean water.'
            }
        ],
        'energy': [
            {
                'question': 'What is the most abundant renewable energy source?',
                'options': ['Wind', 'Solar', 'Hydroelectric', 'Geothermal'],
                'correct': 1,
                'explanation': 'Solar energy is the most abundant renewable energy source on Earth.'
            },
            {
                'question': 'What percentage of global energy comes from renewables?',
                'options': ['10%', '20%', '30%', '50%'],
                'correct': 1,
                'explanation': 'About 20% of global energy comes from renewable sources.'
            },
            {
                'question': 'Which renewable energy source is most efficient?',
                'options': ['Solar panels', 'Wind turbines', 'Hydroelectric dams', 'Geothermal plants'],
                'correct': 2,
                'explanation': 'Hydroelectric dams are typically the most efficient renewable energy source.'
            }
        ],
        'default': [
            {
                'question': 'What does SDG stand for?',
                'options': ['Sustainable Development Goals', 'Social Development Group', 'Science Data Group', 'System Design Goals'],
                'correct': 0,
                'explanation': 'SDG stands for Sustainable Development Goals, set by the United Nations.'
            },
            {
                'question': 'How many Sustainable Development Goals are there?',
                'options': ['15', '17', '20', '25'],
                'correct': 1,
                'explanation': 'There are 17 Sustainable Development Goals.'
            },
            {
                'question': 'What is sustainability?',
                'options': ['Using all resources', 'Meeting present needs without compromising future', 'Growing economy only', 'Protecting environment only'],
                'correct': 1,
                'explanation': 'Sustainability means meeting present needs without compromising future generations\' ability to meet their needs.'
            }
        ]
    }
    
    # Determine which quiz template to use
    if any(word in topic_lower for word in ['climate', 'carbon', 'warming', 'emission']):
        quiz_type = 'climate'
    elif any(word in topic_lower for word in ['water', 'ocean', 'river', 'pollution']):
        quiz_type = 'water'
    elif any(word in topic_lower for word in ['energy', 'solar', 'wind', 'renewable']):
        quiz_type = 'energy'
    else:
        quiz_type = 'default'
    
    return quiz_templates[quiz_type]

def get_ai_response(topic: str, mode: str = 'basic') -> str:
    """
    Generate AI-powered educational explanation for sustainability topics
    aligned with SDG 4 (Quality Education), SDG 6 (Clean Water), and SDG 13 (Climate Action)
    
    Modes:
    - basic: Simple explanation
    - deep: In-depth technical content
    - action: Focus on practical steps
    """
    topic_lower = topic.lower()
    
    # Mode-specific content adjustments
    mode_prefixes = {
        'basic': '📚',
        'deep': '🔬',
        'action': '💪'
    }
    
    mode_descriptions = {
        'basic': 'Basic Learning Mode',
        'deep': 'Deep Dive Mode',
        'action': 'Action Mode'
    }
    
    # SDG 4: Quality Education responses
    if any(word in topic_lower for word in ['education', 'learning', 'school', 'student', 'teacher']):
        if mode == 'deep':
            return f"""
            <h3>{mode_prefixes[mode]} SDG 4: Quality Education - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>Advanced Understanding of {topic}:</strong></p>
            <p>{topic.title()} represents a complex intersection of pedagogical theory, cognitive science, and social development. Quality education systems integrate multiple learning modalities, including constructivist approaches, experiential learning frameworks, and technology-enhanced instruction methodologies.</p>
            
            <p><strong>Technical Implementation:</strong></p>
            <p>Modern educational frameworks utilize evidence-based practices including differentiated instruction, formative assessment protocols, and adaptive learning technologies. Research indicates that quality education requires systemic approaches encompassing curriculum design, teacher professional development, and infrastructure investment.</p>
            
            <p><strong>Global Impact Metrics:</strong></p>
            <ul>
                <li>Literacy rates and numeracy proficiency indicators</li>
                <li>Educational attainment levels across demographic groups</li>
                <li>Teacher-to-student ratios and classroom resource allocation</li>
                <li>Technology integration and digital literacy outcomes</li>
            </ul>
            """
        elif mode == 'action':
            return f"""
            <h3>{mode_prefixes[mode]} SDG 4: Quality Education - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>Immediate Action Steps for {topic}:</strong></p>
            <p>Take concrete steps to improve education quality in your community:</p>
            
            <p><strong>This Week:</strong></p>
            <ul>
                <li>Volunteer as a tutor or mentor in local schools</li>
                <li>Donate educational materials to underserved communities</li>
                <li>Advocate for increased education funding at local government meetings</li>
            </ul>
            
            <p><strong>This Month:</strong></p>
            <ul>
                <li>Organize a community education workshop</li>
                <li>Support teacher professional development initiatives</li>
                <li>Create educational content for online learning platforms</li>
            </ul>
            
            <p><strong>Long-term Commitment:</strong></p>
            <ul>
                <li>Join education policy advocacy groups</li>
                <li>Support scholarship programs for disadvantaged students</li>
                <li>Invest in educational technology for local schools</li>
            </ul>
            """
        else:  # basic mode
            return f"""
            <h3>{mode_prefixes[mode]} SDG 4: Quality Education - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>What is {topic}?</strong></p>
            <p>{topic.title()} is a fundamental aspect of quality education that empowers individuals and communities. Quality education ensures inclusive and equitable learning opportunities for all, promoting lifelong learning and sustainable development.</p>
            
            <p><strong>Why is it important?</strong></p>
            <p>Education is the foundation for sustainable development. It enables people to make informed decisions, develop critical thinking skills, and contribute meaningfully to society. Quality education reduces inequalities and promotes peace, justice, and strong institutions.</p>
            
            <p><strong>How can you take action?</strong></p>
            <ul>
                <li>Support educational initiatives in your community</li>
                <li>Advocate for equal access to quality education</li>
                <li>Engage in lifelong learning opportunities</li>
                <li>Share knowledge and mentor others</li>
            </ul>
            """
    
    # SDG 6: Clean Water responses
    elif any(word in topic_lower for word in ['water', 'pollution', 'sanitation', 'hygiene', 'ocean', 'river', 'lake']):
        if mode == 'deep':
            return f"""
            <h3>{mode_prefixes[mode]} SDG 6: Clean Water and Sanitation - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>Scientific Analysis of {topic}:</strong></p>
            <p>{topic.title()} involves complex hydrological, chemical, and biological processes. Water quality assessment requires understanding of pH levels, dissolved oxygen concentrations, microbial contamination indicators, and chemical pollutant thresholds established by WHO and EPA standards.</p>
            
            <p><strong>Technical Solutions:</strong></p>
            <p>Advanced water treatment technologies include reverse osmosis systems, UV disinfection protocols, membrane bioreactors, and advanced oxidation processes. Smart water management systems utilize IoT sensors, predictive analytics, and automated treatment controls.</p>
            
            <p><strong>Environmental Impact Assessment:</strong></p>
            <ul>
                <li>Aquatic ecosystem health indicators and biodiversity metrics</li>
                <li>Water cycle disruption patterns and climate change impacts</li>
                <li>Contaminant transport modeling and risk assessment protocols</li>
                <li>Sustainable water resource management frameworks</li>
            </ul>
            """
        elif mode == 'action':
            return f"""
            <h3>{mode_prefixes[mode]} SDG 6: Clean Water and Sanitation - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>Practical Water Conservation Actions:</strong></p>
            
            <p><strong>Home Water Management:</strong></p>
            <ul>
                <li>Install low-flow showerheads and faucet aerators</li>
                <li>Fix leaks immediately and monitor water usage</li>
                <li>Collect rainwater for garden irrigation</li>
                <li>Use greywater systems for non-potable applications</li>
            </ul>
            
            <p><strong>Community Water Protection:</strong></p>
            <ul>
                <li>Participate in local water quality monitoring programs</li>
                <li>Support watershed protection initiatives</li>
                <li>Advocate for sustainable water policies</li>
                <li>Organize community clean-up events</li>
            </ul>
            
            <p><strong>Global Water Advocacy:</strong></p>
            <ul>
                <li>Support organizations providing clean water access</li>
                <li>Educate others about water conservation techniques</li>
                <li>Promote sustainable agriculture practices</li>
                <li>Advocate for water rights and access policies</li>
            </ul>
            """
        else:  # basic mode
            return f"""
            <h3>{mode_prefixes[mode]} SDG 6: Clean Water and Sanitation - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>What is {topic}?</strong></p>
            <p>{topic.title()} directly impacts water quality and availability. Clean water and sanitation are essential for human health, environmental sustainability, and economic development. Water scarcity affects more than 40% of the global population.</p>
            
            <p><strong>Why is it important?</strong></p>
            <p>Access to clean water and sanitation is a basic human right. It prevents waterborne diseases, supports ecosystem health, and enables sustainable agriculture and industry. Water is crucial for achieving all other Sustainable Development Goals.</p>
            
            <p><strong>How can you take action?</strong></p>
            <ul>
                <li>Conserve water in daily activities</li>
                <li>Reduce water pollution by proper waste disposal</li>
                <li>Support water conservation projects</li>
                <li>Educate others about water importance</li>
            </ul>
            """
    
    # SDG 13: Climate Action responses
    elif any(word in topic_lower for word in ['climate', 'carbon', 'emission', 'global warming', 'greenhouse', 'renewable', 'energy', 'sustainability']):
        if mode == 'deep':
            return f"""
            <h3>{mode_prefixes[mode]} SDG 13: Climate Action - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>Climate Science Analysis:</strong></p>
            <p>{topic.title()} involves complex atmospheric physics, carbon cycle dynamics, and climate modeling. Understanding requires knowledge of radiative forcing, greenhouse gas concentrations (CO2, CH4, N2O), and climate sensitivity parameters. Current atmospheric CO2 levels exceed 420 ppm, significantly above pre-industrial levels of 280 ppm.</p>
            
            <p><strong>Advanced Mitigation Strategies:</strong></p>
            <p>Climate action encompasses carbon capture and storage (CCS) technologies, renewable energy grid integration, energy storage systems, and smart grid infrastructure. Adaptation strategies include nature-based solutions, climate-resilient infrastructure, and ecosystem-based adaptation approaches.</p>
            
            <p><strong>Climate Impact Modeling:</strong></p>
            <ul>
                <li>Temperature rise projections and regional climate variability</li>
                <li>Sea level rise scenarios and coastal vulnerability assessments</li>
                <li>Extreme weather event frequency and intensity modeling</li>
                <li>Ecosystem response patterns and biodiversity impact studies</li>
            </ul>
            """
        elif mode == 'action':
            return f"""
            <h3>{mode_prefixes[mode]} SDG 13: Climate Action - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>Immediate Climate Action Steps:</strong></p>
            
            <p><strong>Personal Carbon Reduction:</strong></p>
            <ul>
                <li>Calculate and track your carbon footprint monthly</li>
                <li>Switch to renewable energy sources for home and transportation</li>
                <li>Reduce meat consumption and adopt plant-based diets</li>
                <li>Minimize air travel and choose sustainable transportation</li>
            </ul>
            
            <p><strong>Community Climate Initiatives:</strong></p>
            <ul>
                <li>Join local climate action groups and environmental organizations</li>
                <li>Organize tree planting and urban greening projects</li>
                <li>Advocate for renewable energy policies at local government level</li>
                <li>Support climate education programs in schools</li>
            </ul>
            
            <p><strong>Global Climate Advocacy:</strong></p>
            <ul>
                <li>Participate in climate marches and environmental protests</li>
                <li>Support climate-friendly political candidates and policies</li>
                <li>Invest in sustainable and green technologies</li>
                <li>Promote climate awareness through social media and education</li>
            </ul>
            """
        else:  # basic mode
            return f"""
            <h3>{mode_prefixes[mode]} SDG 13: Climate Action - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>What is {topic}?</strong></p>
            <p>{topic.title()} is a critical component of climate action and environmental sustainability. Climate change affects every country and requires urgent action to limit global temperature rise and adapt to its impacts.</p>
            
            <p><strong>Why is it important?</strong></p>
            <p>Climate change threatens food security, water availability, and human health. Taking climate action helps protect ecosystems, reduce disaster risks, and create sustainable economic opportunities. Every degree of warming avoided makes a difference.</p>
            
            <p><strong>How can you take action?</strong></p>
            <ul>
                <li>Reduce your carbon footprint</li>
                <li>Use renewable energy sources</li>
                <li>Support climate-friendly policies</li>
                <li>Plant trees and support reforestation</li>
            </ul>
            """
    
    # General sustainability response
    else:
        if mode == 'deep':
            return f"""
            <h3>{mode_prefixes[mode]} Sustainability Focus - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>Comprehensive Analysis of {topic}:</strong></p>
            <p>{topic.title()} represents a complex intersection of environmental science, social systems, and economic frameworks. Understanding requires analysis of ecological footprints, life cycle assessments, and systems thinking approaches to sustainable development.</p>
            
            <p><strong>Interdisciplinary Connections:</strong></p>
            <p>Sustainability science integrates environmental chemistry, ecology, economics, sociology, and policy studies. Advanced frameworks include the Doughnut Economics model, Planetary Boundaries concept, and Social-Ecological Systems theory.</p>
            
            <p><strong>Research Methodologies:</strong></p>
            <ul>
                <li>Environmental impact assessment protocols</li>
                <li>Sustainability metrics and indicator frameworks</li>
                <li>Stakeholder engagement and participatory research methods</li>
                <li>Scenario planning and future studies approaches</li>
            </ul>
            """
        elif mode == 'action':
            return f"""
            <h3>{mode_prefixes[mode]} Sustainability Focus - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>Actionable Sustainability Steps:</strong></p>
            
            <p><strong>Individual Actions:</strong></p>
            <ul>
                <li>Audit your lifestyle for sustainability opportunities</li>
                <li>Adopt circular economy principles in daily consumption</li>
                <li>Support sustainable businesses and ethical products</li>
                <li>Reduce waste through mindful consumption patterns</li>
            </ul>
            
            <p><strong>Community Engagement:</strong></p>
            <ul>
                <li>Join sustainability-focused community groups</li>
                <li>Organize local environmental initiatives</li>
                <li>Promote sustainable practices in your workplace</li>
                <li>Educate others about sustainability principles</li>
            </ul>
            
            <p><strong>Systemic Change:</strong></p>
            <ul>
                <li>Advocate for sustainable policies and regulations</li>
                <li>Support research and innovation in sustainability</li>
                <li>Invest in sustainable technologies and solutions</li>
                <li>Promote sustainable development goals globally</li>
            </ul>
            """
        else:  # basic mode
            return f"""
            <h3>{mode_prefixes[mode]} Sustainability Focus - {topic.title()} ({mode_descriptions[mode]})</h3>
            <p><strong>What is {topic}?</strong></p>
            <p>{topic.title()} is an important aspect of sustainable development that connects to multiple Sustainable Development Goals. Understanding sustainability helps us create a better future for all.</p>
            
            <p><strong>Connection to SDGs:</strong></p>
            <ul>
                <li><strong>SDG 4 (Quality Education):</strong> Learning about {topic} promotes environmental literacy and critical thinking</li>
                <li><strong>SDG 6 (Clean Water):</strong> Many sustainability topics relate to water conservation and protection</li>
                <li><strong>SDG 13 (Climate Action):</strong> Most sustainability efforts contribute to climate change mitigation</li>
            </ul>
            
            <p><strong>How can you take action?</strong></p>
            <ul>
                <li>Research and learn more about {topic}</li>
                <li>Share your knowledge with others</li>
                <li>Look for local initiatives related to {topic}</li>
                <li>Make sustainable choices in your daily life</li>
            </ul>
            """

def get_action_plan(topic: str) -> str:
    """
    Generate a practical action plan for the given topic
    """
    topic_lower = topic.lower()
    
    # Action plans for different topics
    action_plans = {
        'climate': [
            "Calculate and reduce your carbon footprint using online calculators",
            "Switch to renewable energy sources for your home",
            "Participate in local climate action groups and tree planting events"
        ],
        'water': [
            "Install water-saving devices like low-flow showerheads",
            "Avoid dumping oils and chemicals down drains",
            "Support organizations working on water conservation projects"
        ],
        'energy': [
            "Audit your home's energy usage and identify savings opportunities",
            "Invest in energy-efficient appliances and LED lighting",
            "Consider installing solar panels or supporting renewable energy programs"
        ],
        'education': [
            "Volunteer to teach sustainability topics in your community",
            "Create educational content about environmental issues",
            "Support organizations providing education in underserved areas"
        ],
        'ocean': [
            "Participate in beach cleanup events",
            "Reduce single-use plastics in your daily life",
            "Support marine conservation organizations"
        ],
        'recycling': [
            "Set up a proper recycling system at home and workplace",
            "Learn about local recycling programs and guidelines",
            "Reduce waste by choosing products with minimal packaging"
        ],
        'default': [
            "Research local sustainability initiatives in your area",
            "Share your knowledge about this topic with friends and family",
            "Look for volunteer opportunities related to environmental protection"
        ]
    }
    
    # Determine which action plan to use
    if any(word in topic_lower for word in ['climate', 'carbon', 'warming', 'emission']):
        plan_type = 'climate'
    elif any(word in topic_lower for word in ['water', 'ocean', 'river', 'pollution']):
        plan_type = 'water'
    elif any(word in topic_lower for word in ['energy', 'solar', 'wind', 'renewable']):
        plan_type = 'energy'
    elif any(word in topic_lower for word in ['education', 'learning', 'school']):
        plan_type = 'education'
    elif any(word in topic_lower for word in ['ocean', 'marine', 'sea']):
        plan_type = 'ocean'
    elif any(word in topic_lower for word in ['recycling', 'waste', 'plastic']):
        plan_type = 'recycling'
    else:
        plan_type = 'default'
    
    actions = action_plans[plan_type]
    
    return f"""
    <div class="action-plan">
        <h4>💪 Action Plan</h4>
        <p><strong>Ready to make a difference? Here are 3 practical steps you can take:</strong></p>
        <ol>
            <li>{actions[0]}</li>
            <li>{actions[1]}</li>
            <li>{actions[2]}</li>
        </ol>
        <p class="action-note">💡 <em>Start with one action and build momentum. Every small step counts!</em></p>
    </div>
    """

class AIHelper:
    """AI Helper class for educational assistance"""
    
    def __init__(self):
        self.knowledge_base = {
            'mathematics': [
                'Basic arithmetic operations',
                'Algebraic equations',
                'Geometry concepts',
                'Calculus fundamentals'
            ],
            'science': [
                'Physics laws and principles',
                'Chemical reactions',
                'Biological processes',
                'Environmental science'
            ],
            'programming': [
                'Python fundamentals',
                'Data structures',
                'Algorithms',
                'Web development'
            ]
        }
    
    def get_learning_suggestions(self, subject: str) -> List[str]:
        """Get AI-powered learning suggestions for a given subject"""
        if subject.lower() in self.knowledge_base:
            return self.knowledge_base[subject.lower()]
        return ['General learning strategies', 'Study techniques', 'Time management']
    
    def generate_quiz_questions(self, topic: str, count: int = 5) -> List[Dict[str, Any]]:
        """Generate quiz questions for a given topic"""
        questions = []
        for i in range(count):
            questions.append({
                'id': i + 1,
                'question': f'What is the main concept of {topic}?',
                'options': ['Option A', 'Option B', 'Option C', 'Option D'],
                'correct_answer': random.randint(0, 3)
            })
        return questions
    
    def analyze_progress(self, scores: List[int]) -> Dict[str, Any]:
        """Analyze student progress based on scores"""
        if not scores:
            return {'status': 'No data available', 'recommendation': 'Start taking quizzes'}
        
        average_score = sum(scores) / len(scores)
        
        if average_score >= 80:
            status = 'Excellent'
            recommendation = 'Continue with advanced topics'
        elif average_score >= 60:
            status = 'Good'
            recommendation = 'Review weak areas and practice more'
        else:
            status = 'Needs Improvement'
            recommendation = 'Focus on fundamentals and seek help'
        
        return {
            'status': status,
            'average_score': round(average_score, 2),
            'recommendation': recommendation,
            'total_quizzes': len(scores)
        }

# Example usage
if __name__ == "__main__":
    ai_helper = AIHelper()
    
    # Test learning suggestions
    suggestions = ai_helper.get_learning_suggestions('mathematics')
    print("Mathematics suggestions:", suggestions)
    
    # Test quiz generation
    quiz = ai_helper.generate_quiz_questions('algebra', 3)
    print("Generated quiz:", quiz)
    
    # Test progress analysis
    progress = ai_helper.analyze_progress([85, 92, 78, 88])
    print("Progress analysis:", progress)
