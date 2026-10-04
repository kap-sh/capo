"""Generated from Smithy shape ``com.amazonaws.sesv2#ListEmailIdentitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.identity_filter
    import capo_sesv2.types.max_items
    import capo_sesv2.types.next_token


class ListEmailIdentitiesRequest(TypedDict, closed=True):
    filter: NotRequired["capo_sesv2.types.identity_filter.IdentityFilter"]
    """<p>An object that contains filters to apply when listing email identities. You can filter by identity name, identity type, or verification status.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListEmailIdentities</code> to indicate the position in the list of identities.</p>"""
    page_size: NotRequired["capo_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListEmailIdentities</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 0, and can be no more than 1000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEmailIdentitiesRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_sesv2.types.identity_filter

        out["Filter"] = capo_sesv2.types.identity_filter.serialize_json(value["filter"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_json(data: dict) -> ListEmailIdentitiesRequest:
    out: ListEmailIdentitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_sesv2.types.identity_filter

        out["filter"] = capo_sesv2.types.identity_filter.deserialize_json(
            data["Filter"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    return out
