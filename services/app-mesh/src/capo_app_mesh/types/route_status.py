"""Generated from Smithy shape ``com.amazonaws.appmesh#RouteStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.route_status_code


class RouteStatus(TypedDict, closed=True):
    status: "capo_app_mesh.types.route_status_code.RouteStatusCode"
    """<p>The current status for the route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> RouteStatus:
    out: RouteStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
