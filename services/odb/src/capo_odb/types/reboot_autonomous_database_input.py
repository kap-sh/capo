"""Generated from Smithy shape ``com.amazonaws.odb#RebootAutonomousDatabaseInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class RebootAutonomousDatabaseInput(TypedDict, closed=True):
    autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to reboot.</p>"""
    is_online_reboot: NotRequired["bool"]
    """<p>Specifies whether to perform an online reboot of the Autonomous Database without interrupting active connections.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RebootAutonomousDatabaseInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "is_online_reboot" in value:
        out["isOnlineReboot"] = value["is_online_reboot"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RebootAutonomousDatabaseInput:
    out: RebootAutonomousDatabaseInput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseId") is not None:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        out["autonomous_database_id"] = ""
    if data.get("isOnlineReboot") is not None:
        out["is_online_reboot"] = data["isOnlineReboot"]
    return out
