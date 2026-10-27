"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.iam_role_arn
    import capo_deadline.types.monitor_id
    import capo_deadline.types.resource_name
    import capo_deadline.types.subdomain


class UpdateMonitorRequest(TypedDict, closed=True):
    monitor_id: "capo_deadline.types.monitor_id.MonitorId"
    """The unique identifier of the monitor to update."""
    subdomain: NotRequired["capo_deadline.types.subdomain.Subdomain"]
    """The new value of the subdomain to use when forming the monitor URL."""
    display_name: NotRequired["capo_deadline.types.resource_name.ResourceName"]
    """<p>The new value to use for the monitor's display name.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    role_arn: NotRequired["capo_deadline.types.iam_role_arn.IamRoleArn"]
    """The Amazon Resource Name of the new IAM role to use with the monitor."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitorRequest) -> dict:
    out: dict = {}
    if "subdomain" in value:
        out["subdomain"] = value["subdomain"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateMonitorRequest:
    out: UpdateMonitorRequest = {}  # type: ignore[typeddict-item]
    if data.get("subdomain") is not None:
        out["subdomain"] = data["subdomain"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out
