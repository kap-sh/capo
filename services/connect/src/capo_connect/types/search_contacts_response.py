"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contacts
    import capo_connect.types.large_next_token
    import capo_connect.types.total_count


class SearchContactsResponse(TypedDict, closed=True):
    contacts: "capo_connect.types.contacts.Contacts"
    """<p>Information about the contacts.</p>"""
    next_token: NotRequired["capo_connect.types.large_next_token.LargeNextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    total_count: NotRequired["capo_connect.types.total_count.TotalCount"]
    """<p>The total number of contacts which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsResponse) -> dict:
    out: dict = {}
    import capo_connect.types.contacts

    out["Contacts"] = capo_connect.types.contacts.serialize_json(value["contacts"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    return out


def deserialize_json(data: dict) -> SearchContactsResponse:
    out: SearchContactsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Contacts") is not None:
        import capo_connect.types.contacts

        out["contacts"] = capo_connect.types.contacts.deserialize_json(data["Contacts"])
    else:
        out["contacts"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("TotalCount") is not None:
        out["total_count"] = data["TotalCount"]
    return out


def redact_sensitive(value: SearchContactsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contacts" in value:
        import capo_connect.types.contacts

        out["contacts"] = capo_connect.types.contacts.redact_sensitive(
            value["contacts"]
        )
    return out
