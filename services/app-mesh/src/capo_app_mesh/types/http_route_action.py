"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpRouteAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.weighted_targets


class HttpRouteAction(TypedDict, closed=True):
    weighted_targets: "capo_app_mesh.types.weighted_targets.WeightedTargets"
    """<p>An object that represents the targets that traffic is routed to when a request matches the route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpRouteAction) -> dict:
    out: dict = {}
    import capo_app_mesh.types.weighted_targets

    out["weightedTargets"] = capo_app_mesh.types.weighted_targets.serialize_json(
        value["weighted_targets"]
    )
    return out


def deserialize_json(data: dict) -> HttpRouteAction:
    out: HttpRouteAction = {}  # type: ignore[typeddict-item]
    if data.get("weightedTargets") is not None:
        import capo_app_mesh.types.weighted_targets

        out["weighted_targets"] = capo_app_mesh.types.weighted_targets.deserialize_json(
            data["weightedTargets"]
        )
    else:
        out["weighted_targets"] = []
    return out
