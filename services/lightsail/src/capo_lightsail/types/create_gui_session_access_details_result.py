"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateGUISessionAccessDetailsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.integer
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.sessions
    import capo_lightsail.types.status
    import capo_lightsail.types.string


class CreateGUISessionAccessDetailsResult(TypedDict, closed=True):
    resource_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The resource name.</p>"""
    status: NotRequired["capo_lightsail.types.status.Status"]
    """<p>The status of the operation.</p>"""
    percentage_complete: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The percentage of completion for the operation.</p>"""
    failure_reason: NotRequired["capo_lightsail.types.string.string"]
    """<p>The reason the operation failed.</p>"""
    sessions: NotRequired["capo_lightsail.types.sessions.Sessions"]
    """<p>Returns information about the specified Amazon DCV GUI session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGUISessionAccessDetailsResult) -> dict:
    out: dict = {}
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "status" in value:
        import capo_lightsail.types.status

        out["status"] = capo_lightsail.types.status.serialize_aws_json_1_1(
            value["status"]
        )
    if "percentage_complete" in value:
        out["percentageComplete"] = value["percentage_complete"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "sessions" in value:
        import capo_lightsail.types.sessions

        out["sessions"] = capo_lightsail.types.sessions.serialize_aws_json_1_1(
            value["sessions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGUISessionAccessDetailsResult:
    out: CreateGUISessionAccessDetailsResult = {}  # type: ignore[typeddict-item]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    if data.get("status") is not None:
        import capo_lightsail.types.status

        out["status"] = capo_lightsail.types.status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("percentageComplete") is not None:
        out["percentage_complete"] = data["percentageComplete"]
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("sessions") is not None:
        import capo_lightsail.types.sessions

        out["sessions"] = capo_lightsail.types.sessions.deserialize_aws_json_1_1(
            data["sessions"]
        )
    return out


def redact_sensitive(value: CreateGUISessionAccessDetailsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sessions" in value:
        import capo_lightsail.types.sessions

        out["sessions"] = capo_lightsail.types.sessions.redact_sensitive(
            value["sessions"]
        )
    return out
