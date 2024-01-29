# instance/config.py

# Flask Configuration
DEBUG = True  # Enable debugging in development mode
SECRET_KEY = 'your_secret_key_here'

# Database Configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'

# HeroPower Validations
HERO_POWER_STRENGTH_MIN = 1  # Minimum allowed strength value
HERO_POWER_STRENGTH_MAX = 100  # Maximum allowed strength value

# Routes Configuration
HEROES_PER_PAGE = 10  # Number of heroes to display per page in the /heroes route
POWERS_PER_PAGE = 10  # Number of powers to display per page in the /powers route
