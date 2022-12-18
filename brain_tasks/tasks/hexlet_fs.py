from hexlet.fs import mkdir, mkfile, get_children, get_name
from hexlet.fs import get_meta, is_file, is_directory, flatten
import os


def downcase_file_names(node):
    name = get_name(node)
    meta = get_meta(node)
    name = name.lower()

    if is_file(node):
        return mkfile(name, meta)

    children = get_children(node)
    new_children = list(map(downcase_file_names, children))
    new_tree = mkdir(name, new_children, meta)

    return new_tree


def get_hidden_files_count(node):
    name = get_name(node)

    if is_file(node) and name[0] == '.':
        return 1

    children = get_children(node)
    hidden_files = list(map(get_hidden_files_count, children))

    return sum(hidden_files)


def get_files_count(node):
    if is_file(node):
        return 1
    children = get_children(node)
    descendant_counts = list(map(get_files_count, children))
    return sum(descendant_counts)


def get_subdirectories_info(node):
    children = get_children(node)
    filtered = filter(is_directory, children)
    result = map(
        lambda child: (get_name(child), get_files_count(child)),
        filtered,
    )
    return list(result)


def get_files_size(node):
    if is_file(node):
        meta = get_meta(node)
        return meta['size']
    children = get_children(node)
    descendant_size = list(map(get_files_size, children))
    return sum(descendant_size)


def du(node):
    children = get_children(node)
    result = list(map(
        lambda child: (get_name(child), get_files_size(child)),
        children))
    return sorted(result, key=lambda r: r[1], reverse=True)


def find_files_by_name(tree, string):
    def walk(node, ancestry):
        name = get_name(node)
        new_ancestry = os.path.join(ancestry, name)
        if is_file(node):
            return [] if name.find(string) < 0 else new_ancestry
        children = get_children(node)
        output = map(lambda child: walk(child, new_ancestry), children)
        return list(output)

    return walk(tree, '')


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkdir('a', [
                mkdir('b')
            ]),
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
print(find_files_by_name(tree, 'co'))
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
