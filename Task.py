import click
@click.command()
@click.argument('name')

def greet(name):
    click.echo(f'こんにちは、{name}さん')

if __name__ == '__main__':
    greet()