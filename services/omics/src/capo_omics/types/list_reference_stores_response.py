"""Generated from Smithy shape ``com.amazonaws.omics#ListReferenceStoresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.next_token
    import capo_omics.types.reference_store_detail_list


class ListReferenceStoresResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_omics.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""
    reference_stores: (
        "capo_omics.types.reference_store_detail_list.ReferenceStoreDetailList"
    )
    """<p>A list of reference stores.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReferenceStoresResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_omics.types.reference_store_detail_list

    out["referenceStores"] = (
        capo_omics.types.reference_store_detail_list.serialize_json(
            value["reference_stores"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListReferenceStoresResponse:
    out: ListReferenceStoresResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("referenceStores") is not None:
        import capo_omics.types.reference_store_detail_list

        out["reference_stores"] = (
            capo_omics.types.reference_store_detail_list.deserialize_json(
                data["referenceStores"]
            )
        )
    else:
        out["reference_stores"] = []
    return out
