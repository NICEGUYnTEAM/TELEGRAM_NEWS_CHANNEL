import feedparser

def parse_rss(url):
    # Создаем объект feedparser для работы с RSS лентой
    feed = feedparser.parse(url)
    
    # Проверяем успешность загрузки RSS ленты
    if feed.status != 200:
        print("Ошибка загрузки RSS ленты")
        return
    
    # Если загрузка RSS ленты прошла успешно, выводим заголовок
    print(feed.feed.title)
    
    # Перебираем элементы в RSS ленте (обычно это новости или статьи)
    for item in feed.entries:
        # Выводим заголовок элемента
        print(item.title)
        
        # Если доступны, выводим описание и ссылку на элемент
        if 'description' in item:
            print(item.description)
            
        if 'link' in item:
            print(item.link)
        
        # Выводим разделитель между элементами
        print('---'*30)

# Парсим ленту с сайта MOTOR.ru
parse_rss("https://motor.ru/exports/rss")
