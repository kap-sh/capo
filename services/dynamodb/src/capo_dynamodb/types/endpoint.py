"""Generated from Smithy shape ``com.amazonaws.dynamodb#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.long
    import capo_dynamodb.types.string


class Endpoint(TypedDict, closed=True):
    address: "capo_dynamodb.types.string.String"
    """<p>IP address of the endpoint.</p>"""
    cache_period_in_minutes: "capo_dynamodb.types.long.Long"
    """<p>Endpoint cache time to live (TTL) value.</p>"""


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
