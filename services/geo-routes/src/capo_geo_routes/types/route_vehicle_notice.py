"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleNotice``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_notice_impact
    import capo_geo_routes.types.route_vehicle_notice_code
    import capo_geo_routes.types.route_vehicle_notice_detail_list


class RouteVehicleNotice(TypedDict, closed=True):
    code: "capo_geo_routes.types.route_vehicle_notice_code.RouteVehicleNoticeCode"
    """<p>Code corresponding to the issue.</p>"""
    details: "capo_geo_routes.types.route_vehicle_notice_detail_list.RouteVehicleNoticeDetailList"
    """<p>Additional details of the notice.</p>"""
    impact: NotRequired["capo_geo_routes.types.route_notice_impact.RouteNoticeImpact"]
    """<p>Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleNotice) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_vehicle_notice_code

    out["Code"] = capo_geo_routes.types.route_vehicle_notice_code.serialize_json(
        value["code"]
    )
    import capo_geo_routes.types.route_vehicle_notice_detail_list

    out["Details"] = (
        capo_geo_routes.types.route_vehicle_notice_detail_list.serialize_json(
            value["details"]
        )
    )
    if "impact" in value:
        import capo_geo_routes.types.route_notice_impact

        out["Impact"] = capo_geo_routes.types.route_notice_impact.serialize_json(
            value["impact"]
        )
    return out


def deserialize_json(data: dict) -> RouteVehicleNotice:
    out: RouteVehicleNotice = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_geo_routes.types.route_vehicle_notice_code

        out["code"] = capo_geo_routes.types.route_vehicle_notice_code.deserialize_json(
            data["Code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_geo_routes.types.route_vehicle_notice_code.RouteVehicleNoticeCode", ""
        )
    if data.get("Details") is not None:
        import capo_geo_routes.types.route_vehicle_notice_detail_list

        out["details"] = (
            capo_geo_routes.types.route_vehicle_notice_detail_list.deserialize_json(
                data["Details"]
            )
        )
    else:
        out["details"] = []
    if data.get("Impact") is not None:
        import capo_geo_routes.types.route_notice_impact

        out["impact"] = capo_geo_routes.types.route_notice_impact.deserialize_json(
            data["Impact"]
        )
    return out


def redact_sensitive(value: RouteVehicleNotice) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "details" in value:
        import capo_geo_routes.types.route_vehicle_notice_detail_list

        out["details"] = (
            capo_geo_routes.types.route_vehicle_notice_detail_list.redact_sensitive(
                value["details"]
            )
        )
    return out
