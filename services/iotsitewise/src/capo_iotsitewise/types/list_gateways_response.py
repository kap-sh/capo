"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListGatewaysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.gateway_summaries
    import capo_iotsitewise.types.next_token


class ListGatewaysResponse(TypedDict, closed=True):
    gateway_summaries: "capo_iotsitewise.types.gateway_summaries.GatewaySummaries"
    """<p>A list that summarizes each gateway.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewaysResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.gateway_summaries

    out["gatewaySummaries"] = capo_iotsitewise.types.gateway_summaries.serialize_json(
        value["gateway_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGatewaysResponse:
    out: ListGatewaysResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewaySummaries") is not None:
        import capo_iotsitewise.types.gateway_summaries

        out["gateway_summaries"] = (
            capo_iotsitewise.types.gateway_summaries.deserialize_json(
                data["gatewaySummaries"]
            )
        )
    else:
        out["gateway_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
