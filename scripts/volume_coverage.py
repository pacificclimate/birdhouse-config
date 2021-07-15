import click
import yaml

@click.command()
@click.option('--docker')
@click.option('--pathfile')
def volume_coverage(docker, pathfile):
    def filter_file(file):
        paths = set()
        with open(file, "r") as infile:
            contents = yaml.load(infile)["services"]["thredds"]["volumes"]
            for content in contents:
                path, _ = content.split(":")
                paths.add(path.strip())

        return paths

    paths_to_cover = filter_file(docker)
    
    def get_used_paths(pathfile):
        with open(pathfile, "r") as pfile:
            return {path.strip() for path in pfile}
    
    paths_covered = get_used_paths(pathfile)

    covered = set()

    for path_covered in paths_covered:
        for path_to_cover in paths_to_cover:
            if path_covered in path_to_cover:
                covered.add(path_to_cover)

    missing = paths_to_cover - covered
    print(f"Num volumes missing: {len(missing)}")
    for miss in missing:
        print(miss)
    
if __name__ == "__main__":
    volume_coverage()