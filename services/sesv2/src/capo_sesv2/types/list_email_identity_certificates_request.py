"""Generated from Smithy shape ``com.amazonaws.sesv2#ListEmailIdentityCertificatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.identity
    import capo_sesv2.types.max_items
    import capo_sesv2.types.next_token


class ListEmailIdentityCertificatesRequest(TypedDict, closed=True):
    email_identity: "capo_sesv2.types.identity.Identity"
    """<p>The email identity whose certificate associations you want to list.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListEmailIdentityCertificates</code> to indicate the position in the list of certificates.</p>"""
    page_size: NotRequired["capo_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListEmailIdentityCertificates</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEmailIdentityCertificatesRequest) -> dict:
    out: dict = {}
    out["EmailIdentity"] = value["email_identity"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_json(data: dict) -> ListEmailIdentityCertificatesRequest:
    out: ListEmailIdentityCertificatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailIdentity") is not None:
        out["email_identity"] = data["EmailIdentity"]
    else:
        out["email_identity"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    return out
