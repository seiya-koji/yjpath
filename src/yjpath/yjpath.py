"""CLI tool to extract JSONPath from YAML files."""

from typing import Any, List

import click
import yaml


def yaml_to_jsonpath(data: Any, prefix: str = "") -> List[str]:
    """
    Converts YAML data into JSONPath format.

    Args:
        data (Any): YAML data (dictionary or list).
        prefix (str, optional): Current JSONPath. Defaults to an empty string.

    Returns:
        List[str]: A list of JSONPaths.
    """
    paths = []
    if isinstance(data, dict):
        for key, value in data.items():
            new_prefix = f"{prefix}.{key}" if prefix else key
            paths.append(new_prefix)
            paths.extend(yaml_to_jsonpath(value, new_prefix))
    elif isinstance(data, list):
        for i, value in enumerate(data):
            new_prefix = f"{prefix}[{i}]" if prefix else f"[{i}]"
            paths.append(new_prefix)
            paths.extend(yaml_to_jsonpath(value, new_prefix))
    return paths


@click.command()
@click.argument("yaml_file", type=click.File("r"))
@click.option("--slash", is_flag=True, help="Use slash-separated JSONPath")
def main(yaml_file, slash: bool) -> None:
    """Extract JSONPath from a YAML file."""
    yaml_data = yaml.safe_load(yaml_file)
    json_paths = yaml_to_jsonpath(yaml_data)

    if slash:
        json_paths = [path.replace(".", "/") for path in json_paths]

    for path in json_paths:
        click.echo(path)


if __name__ == "__main__":
    main()
