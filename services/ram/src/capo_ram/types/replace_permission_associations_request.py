"""Generated from Smithy shape ``com.amazonaws.ram#ReplacePermissionAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.integer
    import capo_ram.types.string


class ReplacePermissionAssociationsRequest(TypedDict, closed=True):
    from_permission_arn: "capo_ram.types.string.String"
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the managed permission that you want to replace.</p>"""
    from_permission_version: NotRequired["capo_ram.types.integer.Integer"]
    """<p>Specifies that you want to updated the permissions for only those resource shares that use the specified version of the managed permission.</p>"""
    to_permission_arn: "capo_ram.types.string.String"
    """<p>Specifies the ARN of the managed permission that you want to associate with resource shares in place of the one specified by <code>fromPerssionArn</code> and <code>fromPermissionVersion</code>.</p> <p>The operation always associates the version that is currently the default for the specified managed permission.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplacePermissionAssociationsRequest) -> dict:
    out: dict = {}
    out["fromPermissionArn"] = value["from_permission_arn"]
    if "from_permission_version" in value:
        out["fromPermissionVersion"] = value["from_permission_version"]
    out["toPermissionArn"] = value["to_permission_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ReplacePermissionAssociationsRequest:
    out: ReplacePermissionAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("fromPermissionArn") is not None:
        out["from_permission_arn"] = data["fromPermissionArn"]
    else:
        raise DeserializationError(
            "ReplacePermissionAssociationsRequest.from_permission_arn required"
        )
    if data.get("fromPermissionVersion") is not None:
        out["from_permission_version"] = data["fromPermissionVersion"]
    if data.get("toPermissionArn") is not None:
        out["to_permission_arn"] = data["toPermissionArn"]
    else:
        raise DeserializationError(
            "ReplacePermissionAssociationsRequest.to_permission_arn required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
