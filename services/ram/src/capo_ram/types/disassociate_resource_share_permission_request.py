"""Generated from Smithy shape ``com.amazonaws.ram#DisassociateResourceSharePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.string


class DisassociateResourceSharePermissionRequest(TypedDict, closed=True):
    resource_share_arn: "capo_ram.types.string.String"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share that you want to remove the managed permission from.</p>"""
    permission_arn: "capo_ram.types.string.String"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the managed permission to disassociate from the resource share. Changes to permissions take effect immediately.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourceSharePermissionRequest) -> dict:
    out: dict = {}
    out["resourceShareArn"] = value["resource_share_arn"]
    out["permissionArn"] = value["permission_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DisassociateResourceSharePermissionRequest:
    out: DisassociateResourceSharePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    else:
        raise DeserializationError(
            "DisassociateResourceSharePermissionRequest.resource_share_arn required"
        )
    if data.get("permissionArn") is not None:
        out["permission_arn"] = data["permissionArn"]
    else:
        raise DeserializationError(
            "DisassociateResourceSharePermissionRequest.permission_arn required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
