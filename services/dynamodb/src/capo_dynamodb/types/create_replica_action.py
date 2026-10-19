"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateReplicaAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.region_name


class CreateReplicaAction(TypedDict, closed=True):
    region_name: "capo_dynamodb.types.region_name.RegionName"
    """<p>The Region of the replica to be added.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateReplicaAction) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateReplicaAction:
    out: CreateReplicaAction = {}  # type: ignore[typeddict-item]
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    else:
        out["region_name"] = ""
    return out
