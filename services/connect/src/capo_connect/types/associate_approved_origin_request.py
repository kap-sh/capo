"""Generated from Smithy shape ``com.amazonaws.connect#AssociateApprovedOriginRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.origin


class AssociateApprovedOriginRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    origin: "capo_connect.types.origin.Origin"
    """<p>The domain to add to your allow list.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateApprovedOriginRequest) -> dict:
    out: dict = {}
    out["Origin"] = value["origin"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AssociateApprovedOriginRequest:
    out: AssociateApprovedOriginRequest = {}  # type: ignore[typeddict-item]
    if data.get("Origin") is not None:
        out["origin"] = data["Origin"]
    else:
        raise DeserializationError("AssociateApprovedOriginRequest.origin required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
