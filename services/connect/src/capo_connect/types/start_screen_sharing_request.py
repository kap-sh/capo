"""Generated from Smithy shape ``com.amazonaws.connect#StartScreenSharingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id


class StartScreenSharingRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartScreenSharingRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    return out


def deserialize_json(data: dict) -> StartScreenSharingRequest:
    out: StartScreenSharingRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StartScreenSharingRequest.instance_id required")
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("StartScreenSharingRequest.contact_id required")
    return out
