"""Generated from Smithy shape ``com.amazonaws.timestreamquery#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.long
    import capo_timestream_query.types.string


class Endpoint(TypedDict, closed=True):
    address: "capo_timestream_query.types.string.String"
    """<p>An endpoint address.</p>"""
    cache_period_in_minutes: "capo_timestream_query.types.long.Long"
    """<p>The TTL for the endpoint, in minutes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Endpoint) -> dict:
    out: dict = {}
    out["Address"] = value["address"]
    out["CachePeriodInMinutes"] = value.get("cache_period_in_minutes", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if data.get("Address") is not None:
        out["address"] = data["Address"]
    else:
        out["address"] = ""
    if data.get("CachePeriodInMinutes") is not None:
        out["cache_period_in_minutes"] = data["CachePeriodInMinutes"]
    else:
        out["cache_period_in_minutes"] = 0
    return out
