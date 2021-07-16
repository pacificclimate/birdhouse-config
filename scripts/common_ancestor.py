import click
import yaml


def filter_file(file):
    paths = []
    with open(file, "r") as infile:
        contents = yaml.load(infile)["services"]["thredds"]["volumes"]
        for content in contents:
            path, _ = content.split(":")
            paths.append(path)

    return paths

        

@click.command()
@click.option('--file', help="Feeder file with paths")
def find_common(file):
    filtered = filter_file(file)

    common = {}

    for path in filtered: 
        def check_filetype(sections):
            for suffix in [".txt", ".md", ".csv", ".nc"]:
                if suffix in sections:
                    return sections[:-1]

            return sections
                   
        sections = check_filetype(path.split("/"))

        # 3 because we want to avoid the empty str and we know /storage will have everything
        for i in range(3, len(sections)):
            tmp_sections = sections[0:i]
            tmp_path = "/".join(tmp_sections)

            if tmp_path in common.keys():
                common[tmp_path] += 1

            else:
                common[tmp_path] = 1
            
    for root in sorted(common, key=common.get, reverse=True):
        print(f"{root}, {common[root]}")
            

if __name__ == "__main__":
    find_common()