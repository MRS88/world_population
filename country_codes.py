from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    '''Возвращает для заданной страны ее 2-буквенный код'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        if country_name == "Yemen, Rep.": return 'ye'
        if country_name == "Iran, Islamic Rep.": return 'ir'
        if country_name == "Kyrgyz Republic": return 'kg'
        if country_name == 'Moldova': return 'md'
        if country_name == 'Slovak Republic': return 'sk'
        if country_name == 'Venezuela, RB': return 've'
        if country_name == 'Bolivia': return 'bo'

    # Если страна не найдена, вернуть None
    return None
