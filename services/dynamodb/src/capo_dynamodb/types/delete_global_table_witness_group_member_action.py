"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteGlobalTableWitnessGroupMemberAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.region_name


class DeleteGlobalTableWitnessGroupMemberAction(TypedDict, closed=True):
    region_name: "capo_dynamodb.types.region_name.RegionName"
    """<p>The witness Region name to be removed from the MRSC global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteGlobalTableWitnessGroupMemberAction) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteGlobalTableWitnessGroupMemberAction:
    out: DeleteGlobalTableWitnessGroupMemberAction = {}  # type: ignore[typeddict-item]
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    else:
        out["region_name"] = ""
    return out
