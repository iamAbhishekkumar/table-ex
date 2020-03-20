import click
import tabula


@click.command()
@click.option('--dirt',is_flag = True, help="Conversion of all pdf in the directory.")
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--p', help="Enter number of pages : Eg('1-2,3', 'all', [1,2])", show_default=True)
@click.argument('frt')
def convert(file_path, frt, p, dirt):

    try:
        if dirt:
            wholedir(file_path, frt, p)
        else:
            tabula.convert_into(file_path, output_path=f"{file_path[0:len(file_path) - 4]}.{frt}", output_format=frt,
                                pages=p)
        converted()
    except FileNotFoundError:
        click.echo("Sorry,File not Found.Please check the path.")
    except ValueError:
        click.echo("Please enter a valid conversion format. ")


def converted():
    click.echo("Successfully Converted")


def wholedir(dir_path, frt, p):
    tabula.convert_into_by_batch(input_dir=dir_path, output_format=frt, pages=p)


if __name__ == '__main__':
    convert()