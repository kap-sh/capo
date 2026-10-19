"""Generated from Smithy shape ``com.amazonaws.m2#PsAttributes``."""

from typing_extensions import NotRequired, TypedDict


class PsAttributes(TypedDict, closed=True):
    format: "str"
    """<p>The format of the data set records.</p>"""
    encoding: NotRequired["str"]
    """<p>The character set encoding of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PsAttributes) -> dict:
    out: dict = {}
    out["format"] = value["format"]
    if "encoding" in value:
        out["encoding"] = value["encoding"]
    return out


def deserialize_json(data: dict) -> PsAttributes:
    out: PsAttributes = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        out["format"] = data["format"]
    else:
        out["format"] = ""
    if data.get("encoding") is not None:
        out["encoding"] = data["encoding"]
    return out
