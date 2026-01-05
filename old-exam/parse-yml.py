import sys
import yaml
import jinja2
import git

from babel.dates import format_date

assert(len(sys.argv) > 1)

with open(sys.argv[1], 'r') as f:
    yml = yaml.safe_load(f)

# Format date
yml['exam']['date'] = {
    'iso': yml['exam']['date'],
    'full': format_date(yml['exam']['date'], 'full', locale='fr_CH')
}

repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha

yml['git'] = {
    'sha': sha,
    'url': 'https://github.com/' + repo.remotes.origin.url.split(':')[1].replace('.git','') + '/tree/' + sha
}

print(
    jinja2.Template(
        sys.stdin.read(),
        block_start_string = r'\BLOCK{',
        block_end_string = r'}',
        variable_start_string = r'\VAR{',
        variable_end_string = r'}',
        comment_start_string = r'\#{',
        comment_end_string = r'}',
        line_statement_prefix = r'%%',
        line_comment_prefix = r'%#',
        trim_blocks = False,
        autoescape = False
    ).render(data=yml)
)
