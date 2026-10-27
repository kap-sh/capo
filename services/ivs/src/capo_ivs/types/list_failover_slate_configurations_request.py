"""Generated from Smithy shape ``com.amazonaws.ivs#ListFailoverSlateConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.max_failover_slate_configuration_results
    import capo_ivs.types.pagination_token


class ListFailoverSlateConfigurationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>The first failover slate configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "capo_ivs.types.max_failover_slate_configuration_results.MaxFailoverSlateConfigurationResults"
    ]
    """<p>Maximum number of failover slate configurations to return. Default: your service quota or 100, whichever is smaller.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFailoverSlateConfigurationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListFailoverSlateConfigurationsRequest:
    out: ListFailoverSlateConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
