"""Generated from Smithy shape ``com.amazonaws.m2#PsDetailAttributes``."""

from typing_extensions import TypedDict


class PsDetailAttributes(TypedDict, closed=True):
    format: "str"
    """<p>The format of the data set records.</p>"""
    encoding: "str"
    """<p>The character set encoding of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PsDetailAttributes) -> dict:
    out: dict = {}
    out["format"] = value["format"]
    out["encoding"] = value["encoding"]
    return out


def deserialize_json(data: dict) -> PsDetailAttributes:
    out: PsDetailAttributes = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        out["format"] = data["format"]
    else:
        out["format"] = ""
    if data.get("encoding") is not None:
        out["encoding"] = data["encoding"]
    else:
        out["encoding"] = ""
    return out
