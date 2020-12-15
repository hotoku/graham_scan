#!/usr/bin/env python

import logging
import json
import re
import click
import base64

LOGGER = logging.getLogger(__file__)
IMG_NUM = 0


def process_md(cell):
    return "".join(cell["source"])


def process_code(cell):
    global IMG_NUM
    ret = ""
    if not re.match(".*__NOT_RENDER_SOURCE__", cell["source"][0]):
        ret += "\n\n```python\n" + "".join(cell["source"]) + "\n```\n"
    if len(cell["outputs"]) > 0:
        for output in cell["outputs"]:
            if output["output_type"] == "stream":
                ret += "\n" + "".join(output["text"])
            if output["output_type"] == "display_data":
                fname = f"{IMG_NUM}.png"
                ret += f"\n![{fname}]({fname})\n"
                with open(fname, "bw") as f:
                    f.write(base64.b64decode(output["data"]["image/png"]))
                IMG_NUM += 1
    return ret


@click.command()
@click.argument("fpath")
def main(fpath):
    contents = json.load(open(fpath))
    cells = contents["cells"]
    ret = ""
    for cell in cells:
        if cell["cell_type"] == "markdown":
            ret += "\n" + process_md(cell)
        if cell["cell_type"] == "code":
            ret += "\n" + process_code(cell)
    print(ret)


if __name__ == "__main__":
    main()
