"""Generated from Smithy shape ``com.amazonaws.ram#AssociateResourceSharePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.boolean
    import capo_ram.types.integer
    import capo_ram.types.string


class AssociateResourceSharePermissionRequest(TypedDict, closed=True):
    resource_share_arn: "capo_ram.types.string.String"
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share to which you want to add or replace permissions.</p>"""
    permission_arn: "capo_ram.types.string.String"
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the RAM permission to associate with the resource share. To find the ARN for a permission, use either the <a>ListPermissions</a> operation or go to the <a href="https://console.aws.amazon.com/ram/home#Permissions:">Permissions library</a> page in the RAM console and then choose the name of the permission. The ARN is displayed on the detail page.</p>"""
    replace: NotRequired["capo_ram.types.boolean.Boolean"]
    """<p>Specifies whether the specified permission should replace the existing permission associated with the resource share. Use <code>true</code> to replace the current permissions. Use <code>false</code> to add the permission to a resource share that currently doesn't have a permission. The default value is <code>false</code>.</p> <note> <p>A resource share can have only one permission per resource type. If a resource share already has a permission for the specified resource type and you don't set <code>replace</code> to <code>true</code> then the operation returns an error. This helps prevent accidental overwriting of a permission.</p> </note>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    permission_version: NotRequired["capo_ram.types.integer.Integer"]
    """<p>Specifies the version of the RAM permission to associate with the resource share. You can specify <i>only</i> the version that is currently set as the default version for the permission. If you also set the <code>replace</code> pararameter to <code>true</code>, then this operation updates an outdated version of the permission to the current default version.</p> <note> <p>You don't need to specify this parameter because the default behavior is to use the version that is currently set as the default version for the permission. This parameter is supported for backwards compatibility.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateResourceSharePermissionRequest) -> dict:
    out: dict = {}
    out["resourceShareArn"] = value["resource_share_arn"]
    out["permissionArn"] = value["permission_arn"]
    if "replace" in value:
        out["replace"] = value["replace"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "permission_version" in value:
        out["permissionVersion"] = value["permission_version"]
    return out


def deserialize_json(data: dict) -> AssociateResourceSharePermissionRequest:
    out: AssociateResourceSharePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    else:
        raise DeserializationError(
            "AssociateResourceSharePermissionRequest.resource_share_arn required"
        )
    if data.get("permissionArn") is not None:
        out["permission_arn"] = data["permissionArn"]
    else:
        raise DeserializationError(
            "AssociateResourceSharePermissionRequest.permission_arn required"
        )
    if data.get("replace") is not None:
        out["replace"] = data["replace"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("permissionVersion") is not None:
        out["permission_version"] = data["permissionVersion"]
    return out
