"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#StartQueryWorkloadInsightsTopContributorsDataOutput``."""

from typing_extensions import TypedDict


class StartQueryWorkloadInsightsTopContributorsDataOutput(TypedDict, closed=True):
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryWorkloadInsightsTopContributorsDataOutput) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    return out


def deserialize_json(data: dict) -> StartQueryWorkloadInsightsTopContributorsDataOutput:
    out: StartQueryWorkloadInsightsTopContributorsDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    else:
        out["query_id"] = ""
    return out
