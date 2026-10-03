"""Generated from Smithy shape ``com.amazonaws.connect#MonitorContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.agent_resource_id
    import capo_connect.types.allowed_monitor_capabilities
    import capo_connect.types.client_token
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id


class MonitorContactRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact.</p>"""
    user_id: "capo_connect.types.agent_resource_id.AgentResourceId"
    """<p>The identifier of the user account.</p>"""
    allowed_monitor_capabilities: NotRequired[
        "capo_connect.types.allowed_monitor_capabilities.AllowedMonitorCapabilities"
    ]
    """<p>Specify which monitoring actions the user is allowed to take. For example, whether the user is allowed to escalate from silent monitoring to barge. AllowedMonitorCapabilities is required if barge is enabled.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    out["UserId"] = value["user_id"]
    if "allowed_monitor_capabilities" in value:
        import capo_connect.types.allowed_monitor_capabilities

        out["AllowedMonitorCapabilities"] = (
            capo_connect.types.allowed_monitor_capabilities.serialize_json(
                value["allowed_monitor_capabilities"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> MonitorContactRequest:
    out: MonitorContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("MonitorContactRequest.instance_id required")
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("MonitorContactRequest.contact_id required")
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("MonitorContactRequest.user_id required")
    if data.get("AllowedMonitorCapabilities") is not None:
        import capo_connect.types.allowed_monitor_capabilities

        out["allowed_monitor_capabilities"] = (
            capo_connect.types.allowed_monitor_capabilities.deserialize_json(
                data["AllowedMonitorCapabilities"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
