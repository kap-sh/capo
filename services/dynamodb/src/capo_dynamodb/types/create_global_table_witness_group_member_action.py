"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateGlobalTableWitnessGroupMemberAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.region_name


class CreateGlobalTableWitnessGroupMemberAction(TypedDict, closed=True):
    region_name: "capo_dynamodb.types.region_name.RegionName"
    """<p>The Amazon Web Services Region name to be added as a witness Region for the MRSC global table. The witness must be in a different Region than the replicas and within the same Region set:</p> <ul> <li> <p>US Region set: US East (N. Virginia), US East (Ohio), US West (Oregon)</p> </li> <li> <p>EU Region set: Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt)</p> </li> <li> <p>AP Region set: Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka)</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateGlobalTableWitnessGroupMemberAction) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateGlobalTableWitnessGroupMemberAction:
    out: CreateGlobalTableWitnessGroupMemberAction = {}  # type: ignore[typeddict-item]
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    else:
        out["region_name"] = ""
    return out
