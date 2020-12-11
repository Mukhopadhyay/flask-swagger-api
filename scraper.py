import bs4
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import configs as cfg
from utils.utils import save_as_pkl

def get_html() -> BeautifulSoup:
    html = requests.get(cfg.URL).text
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_wikitable(soup, table_class) -> bs4.element.Tag:
    return soup.find('table', class_=table_class)

def get_headers(table) -> tuple:
    rows = table.find_all('tr')

    # table headers
    attrs = []
    # attribute descriptions
    attrs_desc = []

    for header in rows[0].find_all('th'):
        is_span = header.span
        attrs_desc.append(
            header.span['title'] if is_span else None
        )
        attrs.append(header.text)
    return (attrs, attrs_desc)


def process_attrs(attrs, attrs_desc) -> tuple:
    attrs = list(map(lambda x: x.strip(), attrs))
    attrs_desc = list(map(
        lambda x: '' if not x else x,
        attrs_desc
    ))
    return (attrs, attrs_desc)

def generate_dataframe(table, attrs) -> pd.DataFrame:
    rows = table.find_all('tr')
    all_attributes = []
    for hero in rows[1:]:
        attribute = []
        for x in hero.find_all('td'):
            try:
                attribute.append(
                    x.a['title'] if len(x.text.strip()) == 0 else x.text
                )
            except TypeError as err:
                attribute.append(np.nan)
        all_attributes.append(
            [y.strip() for y in attribute if isinstance(y, str)]
        )
    # Creating the dataframe
    hero_stats = pd.DataFrame(data=all_attributes, columns=attrs)
    return hero_stats


def main():
    soup = get_html()
    table = get_wikitable(soup, 'wikitable')

    # attributes and descriptions
    attrs, attrs_desc = get_headers(table)
    attrs, attrs_desc = process_attrs(attrs, attrs_desc)

    hero_stats = generate_dataframe(table, attrs)
    save_as_pkl(hero_stats, [cfg.DATA_DIR, cfg.DATA_FILE])


# Driver code
if __name__ == '__main__':
    main()