"""Generated from Smithy shape ``com.amazonaws.migrationhub#NotifyApplicationStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub.types.application_id
    import capo_migration_hub.types.application_status
    import capo_migration_hub.types.dry_run
    import capo_migration_hub.types.update_date_time


class NotifyApplicationStateRequest(TypedDict, closed=True):
    application_id: "capo_migration_hub.types.application_id.ApplicationId"
    """<p>The configurationId in Application Discovery Service that uniquely identifies the grouped application.</p>"""
    status: "capo_migration_hub.types.application_status.ApplicationStatus"
    """<p>Status of the application - Not Started, In-Progress, Complete.</p>"""
    update_date_time: NotRequired[
        "capo_migration_hub.types.update_date_time.UpdateDateTime"
    ]
    """<p>The timestamp when the application state changed.</p>"""
    dry_run: NotRequired["capo_migration_hub.types.dry_run.DryRun"]
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyApplicationStateRequest) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    import capo_migration_hub.types.application_status

    out["Status"] = capo_migration_hub.types.application_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "update_date_time" in value:
        import capo_migration_hub.types.update_date_time

        out["UpdateDateTime"] = (
            capo_migration_hub.types.update_date_time.serialize_aws_json_1_1(
                value["update_date_time"]
            )
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyApplicationStateRequest:
    out: NotifyApplicationStateRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError(
            "NotifyApplicationStateRequest.application_id required"
        )
    if data.get("Status") is not None:
        import capo_migration_hub.types.application_status

        out["status"] = (
            capo_migration_hub.types.application_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("NotifyApplicationStateRequest.status required")
    if data.get("UpdateDateTime") is not None:
        import capo_migration_hub.types.update_date_time

        out["update_date_time"] = (
            capo_migration_hub.types.update_date_time.deserialize_aws_json_1_1(
                data["UpdateDateTime"]
            )
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
