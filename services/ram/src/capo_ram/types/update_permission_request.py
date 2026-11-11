"""Generated from Smithy shape ``com.amazonaws.ram#UpdatePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.string
    import capo_ram.types.update_permission_status


class UpdatePermissionRequest(TypedDict, closed=True):
    permission_arn: "capo_ram.types.string.String"
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the customer managed permission that you want to update.</p>"""
    status: "capo_ram.types.update_permission_status.UpdatePermissionStatus"
    """<p>Specifies the new status for the permission. This can be one of the following values:</p> <ul> <li> <p> <code>ATTACHABLE</code> – Restores a previously deprecated permission so it can be associated with resource shares again.</p> </li> <li> <p> <code>DEPRECATED</code> – Deprecates the permission so it can no longer be associated with new resource shares.</p> </li> </ul>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePermissionRequest) -> dict:
    out: dict = {}
    out["permissionArn"] = value["permission_arn"]
    import capo_ram.types.update_permission_status

    out["status"] = capo_ram.types.update_permission_status.serialize_json(
        value["status"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdatePermissionRequest:
    out: UpdatePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("permissionArn") is not None:
        out["permission_arn"] = data["permissionArn"]
    else:
        out["permission_arn"] = ""
    if data.get("status") is not None:
        import capo_ram.types.update_permission_status

        out["status"] = capo_ram.types.update_permission_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_ram.types.update_permission_status.UpdatePermissionStatus", ""
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
