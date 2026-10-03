"""Generated from Smithy shape ``com.amazonaws.apigateway#QuotaSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.integer
    import capo_api_gateway.types.quota_period_type


class QuotaSettings(TypedDict, closed=True):
    limit: "capo_api_gateway.types.integer.Integer"
    """<p>The target maximum number of requests that can be made in a given time period.</p>"""
    offset: "capo_api_gateway.types.integer.Integer"
    """<p>The number of requests subtracted from the given limit in the initial time period.</p>"""
    period: NotRequired["capo_api_gateway.types.quota_period_type.QuotaPeriodType"]
    """<p>The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuotaSettings) -> dict:
    out: dict = {}
    out["limit"] = value.get("limit", 0)
    out["offset"] = value.get("offset", 0)
    if "period" in value:
        import capo_api_gateway.types.quota_period_type

        out["period"] = capo_api_gateway.types.quota_period_type.serialize_json(
            value["period"]
        )
    return out


def deserialize_json(data: dict) -> QuotaSettings:
    out: QuotaSettings = {}  # type: ignore[typeddict-item]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    if data.get("offset") is not None:
        out["offset"] = data["offset"]
    else:
        out["offset"] = 0
    if data.get("period") is not None:
        import capo_api_gateway.types.quota_period_type

        out["period"] = capo_api_gateway.types.quota_period_type.deserialize_json(
            data["period"]
        )
    return out
