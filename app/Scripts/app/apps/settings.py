DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            'host': 'mongodb+srv://sauravshinde900:<password>@pbl.4ef4odp.mongodb.net/?retryWrites=true&w=majority&appName=PBL', # Replace with your MongoDB server address
            'port': 27017,               # Replace with your MongoDB port if different
            'username': 'sauravshinde900', # Replace with your MongoDB username (optional)
            'password': 'D6fE-!TZj5xgVAv', # Replace with your MongoDB password (optional)
            'authSource': 'admin', # Replace with your MongoDB authentication database (optional)
        },
        'NAME': 'EHR',
    }
}