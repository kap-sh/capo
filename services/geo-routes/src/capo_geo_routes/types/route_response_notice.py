"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteResponseNotice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_notice_impact
    import capo_geo_routes.types.route_response_notice_code


class RouteResponseNotice(TypedDict, closed=True):
    code: "capo_geo_routes.types.route_response_notice_code.RouteResponseNoticeCode"
    """<p>Code corresponding to the issue.</p>"""
    impact: NotRequired["capo_geo_routes.types.route_notice_impact.RouteNoticeImpact"]
    """<p>Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteResponseNotice) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_response_notice_code

    out["Code"] = capo_geo_routes.types.route_response_notice_code.serialize_json(
        value["code"]
    )
    if "impact" in value:
        import capo_geo_routes.types.route_notice_impact

        out["Impact"] = capo_geo_routes.types.route_notice_impact.serialize_json(
            value["impact"]
        )
    return out


def deserialize_json(data: dict) -> RouteResponseNotice:
    out: RouteResponseNotice = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_geo_routes.types.route_response_notice_code

        out["code"] = capo_geo_routes.types.route_response_notice_code.deserialize_json(
            data["Code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_geo_routes.types.route_response_notice_code.RouteResponseNoticeCode",
            "",
        )
    if data.get("Impact") is not None:
        import capo_geo_routes.types.route_notice_impact

        out["impact"] = capo_geo_routes.types.route_notice_impact.deserialize_json(
            data["Impact"]
        )
    return out
