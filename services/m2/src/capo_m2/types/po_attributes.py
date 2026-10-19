"""Generated from Smithy shape ``com.amazonaws.m2#PoAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.string20_list


class PoAttributes(TypedDict, closed=True):
    format: "str"
    """<p>The format of the data set records.</p>"""
    encoding: NotRequired["str"]
    """<p>The character set encoding of the data set.</p>"""
    member_file_extensions: "capo_m2.types.string20_list.String20List"
    """<p>An array containing one or more filename extensions, allowing you to specify which files to be included as PDS member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PoAttributes) -> dict:
    out: dict = {}
    out["format"] = value["format"]
    if "encoding" in value:
        out["encoding"] = value["encoding"]
    import capo_m2.types.string20_list

    out["memberFileExtensions"] = capo_m2.types.string20_list.serialize_json(
        value["member_file_extensions"]
    )
    return out


def deserialize_json(data: dict) -> PoAttributes:
    out: PoAttributes = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        out["format"] = data["format"]
    else:
        out["format"] = ""
    if data.get("encoding") is not None:
        out["encoding"] = data["encoding"]
    if data.get("memberFileExtensions") is not None:
        import capo_m2.types.string20_list

        out["member_file_extensions"] = capo_m2.types.string20_list.deserialize_json(
            data["memberFileExtensions"]
        )
    else:
        out["member_file_extensions"] = []
    return out
