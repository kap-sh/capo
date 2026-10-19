"""Generated from Smithy shape ``com.amazonaws.omics#ListSharesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.filter
    import capo_omics.types.resource_owner


class ListSharesRequest(TypedDict, closed=True):
    resource_owner: "capo_omics.types.resource_owner.ResourceOwner"
    """<p>The account that owns the resource shares.</p>"""
    filter: NotRequired["capo_omics.types.filter.Filter"]
    """<p>Attributes that you use to filter for a specific subset of resource shares.</p>"""
    next_token: NotRequired["str"]
    """<p>Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of shares to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSharesRequest) -> dict:
    out: dict = {}
    out["resourceOwner"] = value["resource_owner"]
    if "filter" in value:
        import capo_omics.types.filter

        out["filter"] = capo_omics.types.filter.serialize_json(value["filter"])
    return out


def deserialize_json(data: dict) -> ListSharesRequest:
    out: ListSharesRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceOwner") is not None:
        out["resource_owner"] = data["resourceOwner"]
    else:
        out["resource_owner"] = ""
    if data.get("filter") is not None:
        import capo_omics.types.filter

        out["filter"] = capo_omics.types.filter.deserialize_json(data["filter"])
    return out
