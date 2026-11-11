"""Generated from Smithy shape ``com.amazonaws.ram#CreatePermissionVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.resource_share_permission_detail
    import capo_ram.types.string


class CreatePermissionVersionResponse(TypedDict, closed=True):
    permission: NotRequired[
        "capo_ram.types.resource_share_permission_detail.ResourceSharePermissionDetail"
    ]
    """<p>The details of the new permission version, including its <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a>, version number, status, and policy document.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePermissionVersionResponse) -> dict:
    out: dict = {}
    if "permission" in value:
        import capo_ram.types.resource_share_permission_detail

        out["permission"] = (
            capo_ram.types.resource_share_permission_detail.serialize_json(
                value["permission"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePermissionVersionResponse:
    out: CreatePermissionVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("permission") is not None:
        import capo_ram.types.resource_share_permission_detail

        out["permission"] = (
            capo_ram.types.resource_share_permission_detail.deserialize_json(
                data["permission"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
