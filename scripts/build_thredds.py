import click
import yaml


def collect_paths(filename):
    """Collect filepaths from file"""
    with open(filename, "r") as f:
        paths = set()
        for line in f.readlines():
            paths.add(line.strip("\n"))

    return paths


def process_paths(existing, new):
    """Combine and format filepaths"""
    existing = {path for volume in existing for path, _ in [volume.split(":")]}
    union = new.union(existing)

    return sorted([f"{path}:/pavics-ncml{path}" for path in union])


def generate_thredds_paths(override, paths):
    """Update thredds volumes in docker override given paths"""
    with open(override) as f:
        configs = yaml.load(f, Loader=yaml.FullLoader)

    try:
        existing = configs["services"]["thredds"]["volumes"]
    except Exception as e:
        raise e

    configs["services"]["thredds"]["volumes"] = process_paths(existing, paths)

    with open(override, "w") as f:
        yaml.dump(configs, f)


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.argument("override", type=click.Path(exists=True))
def build_thredds(filename, override):
    """Apply given filepaths to the docker override file"""
    paths = collect_paths(filename)
    thredds_paths = generate_thredds_paths(override, paths)


if __name__ == "__main__":
    build_thredds()
