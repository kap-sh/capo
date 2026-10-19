"""Generated from Smithy shape ``com.amazonaws.transfer#HomeDirectoryMapEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.map_entry
    import capo_transfer.types.map_target
    import capo_transfer.types.map_type


class HomeDirectoryMapEntry(TypedDict, closed=True):
    entry: "capo_transfer.types.map_entry.MapEntry"
    """<p>Represents an entry for <code>HomeDirectoryMappings</code>.</p>"""
    target: "capo_transfer.types.map_target.MapTarget"
    """<p>Represents the map target that is used in a <code>HomeDirectoryMapEntry</code>.</p>"""
    type: NotRequired["capo_transfer.types.map_type.MapType"]
    """<p>Specifies the type of mapping. Set the type to <code>FILE</code> if you want the mapping to point to a file, or <code>DIRECTORY</code> for the directory to point to a directory.</p> <note> <p>By default, home directory mappings have a <code>Type</code> of <code>DIRECTORY</code> when you create a Transfer Family server. You would need to explicitly set <code>Type</code> to <code>FILE</code> if you want a mapping to have a file target.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HomeDirectoryMapEntry) -> dict:
    out: dict = {}
    out["Entry"] = value["entry"]
    out["Target"] = value["target"]
    if "type" in value:
        import capo_transfer.types.map_type

        out["Type"] = capo_transfer.types.map_type.serialize_aws_json_1_1(value["type"])
    return out


def deserialize_aws_json_1_1(data: dict) -> HomeDirectoryMapEntry:
    out: HomeDirectoryMapEntry = {}  # type: ignore[typeddict-item]
    if data.get("Entry") is not None:
        out["entry"] = data["Entry"]
    else:
        out["entry"] = ""
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    else:
        out["target"] = ""
    if data.get("Type") is not None:
        import capo_transfer.types.map_type

        out["type"] = capo_transfer.types.map_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
