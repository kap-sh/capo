"""Generated from Smithy shape ``com.amazonaws.connect#DisassociateApprovedOriginRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.origin


class DisassociateApprovedOriginRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    origin: "capo_connect.types.origin.Origin"
    """<p>The domain URL of the integrated application.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateApprovedOriginRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateApprovedOriginRequest:
    out: DisassociateApprovedOriginRequest = {}  # type: ignore[typeddict-item]
    return out
