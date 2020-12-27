import datetime
import pandas as pd

def get_timestamp() -> str:
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def get_hero_details(df:pd.DataFrame, hero_name:str) -> dict:
    hero_name = ' '.join([x.capitalize() for x in hero_name.split('_')])
    try:
        result = df[df.HERO==hero_name].iloc[0].to_dict()
    except IndexError as ierr:
        return {'MSG': f'Invalid hero name {hero_name}'}
    except Exception as err:
        return {'MSG': str(err)}
    else:
        return result

def get_attr_desc(df:pd.DataFrame, attr_desc:list) -> dict:
    return dict(zip(df.columns, attr_desc))

def get_all_hero_details(df:pd.DataFrame) -> list:
    data = []
    for _, hero in df.iterrows():
        data.append(hero.to_dict())
    return data

def get_all_hero_names(df:pd.DataFrame) -> list:
    return list(df.HERO.values)

def order_by_attr(df:pd.DataFrame, request_body:dict) -> list:
    data = []
    attr = request_body.get('attr')
    desc = request_body.get('desc')
    print(request_body)
    print(df[df[attr]==2])
    try:
        for _, hero in df.sort_values(
            by=attr,
            ascending=False if desc else True
        ).iterrows():
            data.append(hero.to_dict())
        return data
    except Exception as err:
        return [{'ERR': str(err)}]