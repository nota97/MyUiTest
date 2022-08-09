import yaml


def yamlload(filename):
    files = open(filename, 'r', encoding='utf-8')
    data = yaml.load(files, Loader=yaml.FullLoader)
    return data

