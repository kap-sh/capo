"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleNoticeDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_violated_constraints
    import capo_geo_routes.types.sensitive_string


class RouteVehicleNoticeDetail(TypedDict, closed=True):
    title: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The notice title.</p>"""
    violated_constraints: NotRequired[
        "capo_geo_routes.types.route_violated_constraints.RouteViolatedConstraints"
    ]
    """<p>Any violated constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleNoticeDetail) -> dict:
    out: dict = {}
    if "title" in value:
        out["Title"] = value["title"]
    if "violated_constraints" in value:
        import capo_geo_routes.types.route_violated_constraints

        out["ViolatedConstraints"] = (
            capo_geo_routes.types.route_violated_constraints.serialize_json(
                value["violated_constraints"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteVehicleNoticeDetail:
    out: RouteVehicleNoticeDetail = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("ViolatedConstraints") is not None:
        import capo_geo_routes.types.route_violated_constraints

        out["violated_constraints"] = (
            capo_geo_routes.types.route_violated_constraints.deserialize_json(
                data["ViolatedConstraints"]
            )
        )
    return out


def redact_sensitive(value: RouteVehicleNoticeDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "violated_constraints" in value:
        import capo_geo_routes.types.route_violated_constraints

        out["violated_constraints"] = (
            capo_geo_routes.types.route_violated_constraints.redact_sensitive(
                value["violated_constraints"]
            )
        )
    return out
