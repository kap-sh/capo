"""Generated from Smithy shape ``com.amazonaws.ram#SetDefaultPermissionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ram.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ram.types.integer
    import capo_ram.types.string


class SetDefaultPermissionVersionRequest(TypedDict, closed=True):
    permission_arn: "capo_ram.types.string.String"
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the customer managed permission whose default version you want to change.</p>"""
    permission_version: "capo_ram.types.integer.Integer"
    """<p>Specifies the version number that you want to designate as the default for customer managed permission. To see a list of all available version numbers, use <a>ListPermissionVersions</a>.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetDefaultPermissionVersionRequest) -> dict:
    out: dict = {}
    out["permissionArn"] = value["permission_arn"]
    out["permissionVersion"] = value["permission_version"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> SetDefaultPermissionVersionRequest:
    out: SetDefaultPermissionVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("permissionArn") is not None:
        out["permission_arn"] = data["permissionArn"]
    else:
        raise DeserializationError(
            "SetDefaultPermissionVersionRequest.permission_arn required"
        )
    if data.get("permissionVersion") is not None:
        out["permission_version"] = data["permissionVersion"]
    else:
        raise DeserializationError(
            "SetDefaultPermissionVersionRequest.permission_version required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
