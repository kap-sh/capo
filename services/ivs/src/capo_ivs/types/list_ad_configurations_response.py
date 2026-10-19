"""Generated from Smithy shape ``com.amazonaws.ivs#ListAdConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.ad_configuration_list
    import capo_ivs.types.pagination_token


class ListAdConfigurationsResponse(TypedDict, closed=True):
    ad_configurations: "capo_ivs.types.ad_configuration_list.AdConfigurationList"
    """<p>List of the matching ad configurations.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more ad configurations than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAdConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_ivs.types.ad_configuration_list

    out["adConfigurations"] = capo_ivs.types.ad_configuration_list.serialize_json(
        value["ad_configurations"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAdConfigurationsResponse:
    out: ListAdConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("adConfigurations") is not None:
        import capo_ivs.types.ad_configuration_list

        out["ad_configurations"] = (
            capo_ivs.types.ad_configuration_list.deserialize_json(
                data["adConfigurations"]
            )
        )
    else:
        out["ad_configurations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
