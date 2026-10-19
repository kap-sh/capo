"""Generated from Smithy shape ``com.amazonaws.grafana#PermissionEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.role
    import capo_grafana.types.user


class PermissionEntry(TypedDict, closed=True):
    user: "capo_grafana.types.user.User"
    """<p>A structure with the ID of the user or group with this role.</p>"""
    role: "capo_grafana.types.role.Role"
    """<p>Specifies whether the user or group has the <code>Admin</code>, <code>Editor</code>, or <code>Viewer</code> role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionEntry) -> dict:
    out: dict = {}
    import capo_grafana.types.user

    out["user"] = capo_grafana.types.user.serialize_json(value["user"])
    out["role"] = value["role"]
    return out


def deserialize_json(data: dict) -> PermissionEntry:
    out: PermissionEntry = {}  # type: ignore[typeddict-item]
    if data.get("user") is not None:
        import capo_grafana.types.user

        out["user"] = capo_grafana.types.user.deserialize_json(data["user"])
    else:
        raise DeserializationError("PermissionEntry.user required")
    if data.get("role") is not None:
        out["role"] = data["role"]
    else:
        out["role"] = ""
    return out
