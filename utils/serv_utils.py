import datetime

def get_timestamp() -> str:
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def get_hero_details(df, hero_name) -> dict:
    hero_name = ' '.join([x.capitalize() for x in hero_name.split('_')])
    try:
        result = df[df.HERO==hero_name].iloc[0].to_dict()
    except IndexError as ierr:
        return {'MSG': f'Invalid hero name {hero_name}'}
    except Exception as err:
        return {'MSG': str(err)}
    else:
        return result