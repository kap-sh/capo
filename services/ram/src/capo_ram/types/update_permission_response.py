"""Generated from Smithy shape ``com.amazonaws.ram#UpdatePermissionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.string
    import capo_ram.types.update_permission_status


class UpdatePermissionResponse(TypedDict, closed=True):
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""
    permission_status: NotRequired[
        "capo_ram.types.update_permission_status.UpdatePermissionStatus"
    ]
    """<p>The updated status of the permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePermissionResponse) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "permission_status" in value:
        import capo_ram.types.update_permission_status

        out["permissionStatus"] = (
            capo_ram.types.update_permission_status.serialize_json(
                value["permission_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePermissionResponse:
    out: UpdatePermissionResponse = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("permissionStatus") is not None:
        import capo_ram.types.update_permission_status

        out["permission_status"] = (
            capo_ram.types.update_permission_status.deserialize_json(
                data["permissionStatus"]
            )
        )
    return out
