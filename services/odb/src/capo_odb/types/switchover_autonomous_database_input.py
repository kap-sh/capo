"""Generated from Smithy shape ``com.amazonaws.odb#SwitchoverAutonomousDatabaseInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_arn
    import capo_odb.types.resource_id_or_arn


class SwitchoverAutonomousDatabaseInput(TypedDict, closed=True):
    autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to switch over.</p>"""
    peer_db_arn: NotRequired["capo_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the peer Autonomous Database to switch over to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SwitchoverAutonomousDatabaseInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "peer_db_arn" in value:
        out["peerDbArn"] = value["peer_db_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SwitchoverAutonomousDatabaseInput:
    out: SwitchoverAutonomousDatabaseInput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseId") is not None:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        out["autonomous_database_id"] = ""
    if data.get("peerDbArn") is not None:
        out["peer_db_arn"] = data["peerDbArn"]
    return out
