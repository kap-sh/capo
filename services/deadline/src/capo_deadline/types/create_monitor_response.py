"""Generated from Smithy shape ``com.amazonaws.deadline#CreateMonitorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.identity_center_application_arn
    import capo_deadline.types.monitor_id


class CreateMonitorResponse(TypedDict, closed=True):
    monitor_id: "capo_deadline.types.monitor_id.MonitorId"
    """The unique identifier of the monitor."""
    identity_center_application_arn: "capo_deadline.types.identity_center_application_arn.IdentityCenterApplicationArn"
    """The Amazon Resource Name that IAM Identity Center assigns to the monitor."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorResponse) -> dict:
    out: dict = {}
    out["monitorId"] = value["monitor_id"]
    out["identityCenterApplicationArn"] = value["identity_center_application_arn"]
    return out


def deserialize_json(data: dict) -> CreateMonitorResponse:
    out: CreateMonitorResponse = {}  # type: ignore[typeddict-item]
    if data.get("monitorId") is not None:
        out["monitor_id"] = data["monitorId"]
    else:
        out["monitor_id"] = ""
    if data.get("identityCenterApplicationArn") is not None:
        out["identity_center_application_arn"] = data["identityCenterApplicationArn"]
    else:
        out["identity_center_application_arn"] = ""
    return out
