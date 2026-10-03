"""Generated from Smithy shape ``com.amazonaws.apigateway#Usage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.map_of_key_usages
    import capo_api_gateway.types.string


class Usage(TypedDict, closed=True):
    usage_plan_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The plan Id associated with this usage data.</p>"""
    start_date: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The starting date of the usage data.</p>"""
    end_date: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The ending date of the usage data.</p>"""
    items: NotRequired["capo_api_gateway.types.map_of_key_usages.MapOfKeyUsages"]
    """<p>The usage data, as daily logs of used and remaining quotas, over the specified time interval indexed over the API keys in a usage plan. For example, <code>{..., "values" : { "{api_key}" : [ [0, 100], [10, 90], [100, 10]]}</code>, where <code>{api_key}</code> stands for an API key value and the daily log entry is of the format <code>[used quota, remaining quota]</code>.</p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Usage) -> dict:
    out: dict = {}
    if "usage_plan_id" in value:
        out["usagePlanId"] = value["usage_plan_id"]
    if "start_date" in value:
        out["startDate"] = value["start_date"]
    if "end_date" in value:
        out["endDate"] = value["end_date"]
    if "items" in value:
        import capo_api_gateway.types.map_of_key_usages

        out["values"] = capo_api_gateway.types.map_of_key_usages.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> Usage:
    out: Usage = {}  # type: ignore[typeddict-item]
    if data.get("usagePlanId") is not None:
        out["usage_plan_id"] = data["usagePlanId"]
    if data.get("startDate") is not None:
        out["start_date"] = data["startDate"]
    if data.get("endDate") is not None:
        out["end_date"] = data["endDate"]
    if data.get("values") is not None:
        import capo_api_gateway.types.map_of_key_usages

        out["items"] = capo_api_gateway.types.map_of_key_usages.deserialize_json(
            data["values"]
        )
    return out
