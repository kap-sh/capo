"""Generated from Smithy shape ``com.amazonaws.grafana#User``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.sso_id
    import capo_grafana.types.user_type


class User(TypedDict, closed=True):
    id: "capo_grafana.types.sso_id.SsoId"
    """<p>The ID of the user or group.</p> <p>Pattern: <code>^([0-9a-fA-F]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$</code> </p>"""
    type: "capo_grafana.types.user_type.UserType"
    """<p>Specifies whether this is a single user or a group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
