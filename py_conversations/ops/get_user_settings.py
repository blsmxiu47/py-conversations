from dagster import op

@op
def get_user_settings():
    return {
        'language': 'en-US',
        'topic': 'wildfires'
    }
