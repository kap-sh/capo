"""Generated from Smithy shape ``com.amazonaws.omics#ListReadSetUploadPartsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.next_token
    import capo_omics.types.read_set_part_source
    import capo_omics.types.read_set_upload_part_list_filter
    import capo_omics.types.sequence_store_id
    import capo_omics.types.upload_id


class ListReadSetUploadPartsRequest(TypedDict, closed=True):
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The Sequence Store ID used for the multipart uploads.</p>"""
    upload_id: "capo_omics.types.upload_id.UploadId"
    """<p>The ID for the initiated multipart upload.</p>"""
    part_source: "capo_omics.types.read_set_part_source.ReadSetPartSource"
    """<p>The source file for the upload part.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of read set upload parts returned in a page.</p>"""
    next_token: NotRequired["capo_omics.types.next_token.NextToken"]
    """<p>Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.</p>"""
    filter: NotRequired[
        "capo_omics.types.read_set_upload_part_list_filter.ReadSetUploadPartListFilter"
    ]
    """<p>Attributes used to filter for a specific subset of read set part uploads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReadSetUploadPartsRequest) -> dict:
    out: dict = {}
    out["partSource"] = value["part_source"]
    if "filter" in value:
        import capo_omics.types.read_set_upload_part_list_filter

        out["filter"] = (
            capo_omics.types.read_set_upload_part_list_filter.serialize_json(
                value["filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListReadSetUploadPartsRequest:
    out: ListReadSetUploadPartsRequest = {}  # type: ignore[typeddict-item]
    if data.get("partSource") is not None:
        out["part_source"] = data["partSource"]
    else:
        out["part_source"] = ""
    if data.get("filter") is not None:
        import capo_omics.types.read_set_upload_part_list_filter

        out["filter"] = (
            capo_omics.types.read_set_upload_part_list_filter.deserialize_json(
                data["filter"]
            )
        )
    return out
