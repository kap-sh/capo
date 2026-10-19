"""Generated from Smithy shape ``com.amazonaws.omics#ListSequenceStoresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.next_token
    import capo_omics.types.sequence_store_detail_list


class ListSequenceStoresResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_omics.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""
    sequence_stores: (
        "capo_omics.types.sequence_store_detail_list.SequenceStoreDetailList"
    )
    """<p>A list of sequence stores.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSequenceStoresResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_omics.types.sequence_store_detail_list

    out["sequenceStores"] = capo_omics.types.sequence_store_detail_list.serialize_json(
        value["sequence_stores"]
    )
    return out


def deserialize_json(data: dict) -> ListSequenceStoresResponse:
    out: ListSequenceStoresResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("sequenceStores") is not None:
        import capo_omics.types.sequence_store_detail_list

        out["sequence_stores"] = (
            capo_omics.types.sequence_store_detail_list.deserialize_json(
                data["sequenceStores"]
            )
        )
    else:
        out["sequence_stores"] = []
    return out
