"""Generated from Smithy shape ``com.amazonaws.glue#PartitionIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.key_list
    import capo_glue.types.name_string


class PartitionIndex(TypedDict, closed=True):
    keys: "capo_glue.types.key_list.KeyList"
    """<p>The keys for the partition index.</p>"""
    index_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the partition index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionIndex) -> dict:
    out: dict = {}
    import capo_glue.types.key_list

    out["Keys"] = capo_glue.types.key_list.serialize_aws_json_1_1(value["keys"])
    out["IndexName"] = value["index_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionIndex:
    out: PartitionIndex = {}  # type: ignore[typeddict-item]
    if data.get("Keys") is not None:
        import capo_glue.types.key_list

        out["keys"] = capo_glue.types.key_list.deserialize_aws_json_1_1(data["Keys"])
    else:
        out["keys"] = []
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        out["index_name"] = ""
    return out
