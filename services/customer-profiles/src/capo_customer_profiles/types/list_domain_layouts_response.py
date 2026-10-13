"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListDomainLayoutsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.layout_list
    import capo_customer_profiles.types.token


class ListDomainLayoutsResponse(TypedDict, closed=True):
    items: NotRequired["capo_customer_profiles.types.layout_list.LayoutList"]
    """<p>Contains summary information about an EventStream.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>Identifies the next page of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainLayoutsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_customer_profiles.types.layout_list

        out["Items"] = capo_customer_profiles.types.layout_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainLayoutsResponse:
    out: ListDomainLayoutsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_customer_profiles.types.layout_list

        out["items"] = capo_customer_profiles.types.layout_list.deserialize_json(
            data["Items"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListDomainLayoutsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_customer_profiles.types.layout_list

        out["items"] = capo_customer_profiles.types.layout_list.redact_sensitive(
            value["items"]
        )
    return out
