"""Generated from Smithy shape ``com.amazonaws.ivs#ListFailoverSlateConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.failover_slate_configuration_list
    import capo_ivs.types.pagination_token


class ListFailoverSlateConfigurationsResponse(TypedDict, closed=True):
    failover_slate_configurations: "capo_ivs.types.failover_slate_configuration_list.FailoverSlateConfigurationList"
    """<p>List of the matching failover slate configurations.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more failover slate configurations than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFailoverSlateConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_ivs.types.failover_slate_configuration_list

    out["failoverSlateConfigurations"] = (
        capo_ivs.types.failover_slate_configuration_list.serialize_json(
            value["failover_slate_configurations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFailoverSlateConfigurationsResponse:
    out: ListFailoverSlateConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("failoverSlateConfigurations") is not None:
        import capo_ivs.types.failover_slate_configuration_list

        out["failover_slate_configurations"] = (
            capo_ivs.types.failover_slate_configuration_list.deserialize_json(
                data["failoverSlateConfigurations"]
            )
        )
    else:
        out["failover_slate_configurations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
