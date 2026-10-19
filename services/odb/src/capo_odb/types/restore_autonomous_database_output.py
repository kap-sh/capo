"""Generated from Smithy shape ``com.amazonaws.odb#RestoreAutonomousDatabaseOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_resource_status


class RestoreAutonomousDatabaseOutput(TypedDict, closed=True):
    autonomous_database_id: "str"
    """<p>The unique identifier of the Autonomous Database that was restored.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the Autonomous Database.</p>"""
    status: NotRequired[
        "capo_odb.types.autonomous_database_resource_status.AutonomousDatabaseResourceStatus"
    ]
    """<p>The current status of the Autonomous Database after the restore operation.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the Autonomous Database after the restore operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreAutonomousDatabaseOutput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_odb.types.autonomous_database_resource_status

        out["status"] = (
            capo_odb.types.autonomous_database_resource_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreAutonomousDatabaseOutput:
    out: RestoreAutonomousDatabaseOutput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseId") is not None:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        out["autonomous_database_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.autonomous_database_resource_status

        out["status"] = (
            capo_odb.types.autonomous_database_resource_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
