"""Generated from Smithy shape ``com.amazonaws.sesv2#ListConfigurationSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_filter
    import capo_sesv2.types.max_items
    import capo_sesv2.types.next_token


class ListConfigurationSetsRequest(TypedDict, closed=True):
    filter: NotRequired[
        "capo_sesv2.types.configuration_set_filter.ConfigurationSetFilter"
    ]
    """<p>An object that contains filters to apply when listing configuration sets. You can filter by configuration set name.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListConfigurationSets</code> to indicate the position in the list of configuration sets.</p>"""
    page_size: NotRequired["capo_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListConfigurationSets</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationSetsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_sesv2.types.configuration_set_filter

        out["Filter"] = capo_sesv2.types.configuration_set_filter.serialize_json(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_json(data: dict) -> ListConfigurationSetsRequest:
    out: ListConfigurationSetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_sesv2.types.configuration_set_filter

        out["filter"] = capo_sesv2.types.configuration_set_filter.deserialize_json(
            data["Filter"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    return out
