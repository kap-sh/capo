"""Generated from Smithy shape ``com.amazonaws.keyspaces#PartitionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.generic_string


class PartitionKey(TypedDict, closed=True):
    name: "capo_keyspaces.types.generic_string.GenericString"
    """<p>The name(s) of the partition key column(s).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartitionKey) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PartitionKey:
    out: PartitionKey = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
