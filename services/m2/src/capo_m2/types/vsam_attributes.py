"""Generated from Smithy shape ``com.amazonaws.m2#VsamAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.alternate_key_list
    import capo_m2.types.boolean
    import capo_m2.types.primary_key


class VsamAttributes(TypedDict, closed=True):
    format: "str"
    """<p>The record format of the data set.</p>"""
    encoding: NotRequired["str"]
    """<p>The character set used by the data set. Can be ASCII, EBCDIC, or unknown.</p>"""
    compressed: "capo_m2.types.boolean.Boolean"
    """<p>Indicates whether indexes for this dataset are stored as compressed values. If you have a large data set (typically &gt; 100 Mb), consider setting this flag to True.</p>"""
    primary_key: NotRequired["capo_m2.types.primary_key.PrimaryKey"]
    """<p>The primary key of the data set.</p>"""
    alternate_keys: NotRequired["capo_m2.types.alternate_key_list.AlternateKeyList"]
    """<p>The alternate key definitions, if any. A legacy dataset might not have any alternate key defined, but if those alternate keys definitions exist, provide them as some applications will make use of them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VsamAttributes) -> dict:
    out: dict = {}
    out["format"] = value["format"]
    if "encoding" in value:
        out["encoding"] = value["encoding"]
    out["compressed"] = value.get("compressed", False)
    if "primary_key" in value:
        import capo_m2.types.primary_key

        out["primaryKey"] = capo_m2.types.primary_key.serialize_json(
            value["primary_key"]
        )
    if "alternate_keys" in value:
        import capo_m2.types.alternate_key_list

        out["alternateKeys"] = capo_m2.types.alternate_key_list.serialize_json(
            value["alternate_keys"]
        )
    return out


def deserialize_json(data: dict) -> VsamAttributes:
    out: VsamAttributes = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        out["format"] = data["format"]
    else:
        out["format"] = ""
    if data.get("encoding") is not None:
        out["encoding"] = data["encoding"]
    if data.get("compressed") is not None:
        out["compressed"] = data["compressed"]
    else:
        out["compressed"] = False
    if data.get("primaryKey") is not None:
        import capo_m2.types.primary_key

        out["primary_key"] = capo_m2.types.primary_key.deserialize_json(
            data["primaryKey"]
        )
    if data.get("alternateKeys") is not None:
        import capo_m2.types.alternate_key_list

        out["alternate_keys"] = capo_m2.types.alternate_key_list.deserialize_json(
            data["alternateKeys"]
        )
    return out
