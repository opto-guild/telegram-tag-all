import yaml

with open('config.yaml', 'rb') as f_handler:
    yaml_file = yaml.safe_load(f_handler)
    
    TELEGRAM_API_KEY = yaml_file["telegram"]["api_key"]
    OPTO_GROUP_ID = yaml_file["telegram"]["opto_group_id"]
    TAGS_PER_MESSAGE = yaml_file["telegram"]["tags_per_message"]