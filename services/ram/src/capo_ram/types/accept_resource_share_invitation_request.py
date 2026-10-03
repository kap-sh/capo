"""Generated from Smithy shape ``com.amazonaws.ram#AcceptResourceShareInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.string


class AcceptResourceShareInvitationRequest(TypedDict, closed=True):
    resource_share_invitation_arn: "capo_ram.types.string.String"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the invitation that you want to accept.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptResourceShareInvitationRequest) -> dict:
    out: dict = {}
    out["resourceShareInvitationArn"] = value["resource_share_invitation_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AcceptResourceShareInvitationRequest:
    out: AcceptResourceShareInvitationRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceShareInvitationArn") is not None:
        out["resource_share_invitation_arn"] = data["resourceShareInvitationArn"]
    else:
        raise DeserializationError(
            "AcceptResourceShareInvitationRequest.resource_share_invitation_arn required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
