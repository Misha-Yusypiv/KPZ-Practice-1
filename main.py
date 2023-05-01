import csv
import os
import requests
import string


def get_text_info(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        for c in string.punctuation:
            text = text.replace(c, ' ')
        words = text.split()
        word_count = {}
        for word in words:
            if word.isalpha():
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
        for word, count in sorted(word_count.items()):
            print(f'{word} - {count}')


get_text_info('arctical.txt.txt')


def download_csv(urlpath):
    filename = 'username.csv'
    filepath = os.path.join('source_data', filename)
    with requests.get(urlpath) as r:
        with open(filepath, 'wb') as f:
            f.write(r.content)
    with open(filepath, 'r') as f:
        lines = f.readlines()
    with open(filepath, 'w') as f:
        f.writelines(lines[:-1])
    print('Completed!')


download_csv('https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv')
