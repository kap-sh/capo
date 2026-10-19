"""Generated from Smithy shape ``com.amazonaws.omics#CompleteMultipartReadSetUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.complete_read_set_upload_part_list
    import capo_omics.types.sequence_store_id
    import capo_omics.types.upload_id


class CompleteMultipartReadSetUploadRequest(TypedDict, closed=True):
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The sequence store ID for the store involved in the multipart upload.</p>"""
    upload_id: "capo_omics.types.upload_id.UploadId"
    """<p>The ID for the multipart upload.</p>"""
    parts: "capo_omics.types.complete_read_set_upload_part_list.CompleteReadSetUploadPartList"
    """<p>The individual uploads or parts of a multipart upload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteMultipartReadSetUploadRequest) -> dict:
    out: dict = {}
    import capo_omics.types.complete_read_set_upload_part_list

    out["parts"] = capo_omics.types.complete_read_set_upload_part_list.serialize_json(
        value["parts"]
    )
    return out


def deserialize_json(data: dict) -> CompleteMultipartReadSetUploadRequest:
    out: CompleteMultipartReadSetUploadRequest = {}  # type: ignore[typeddict-item]
    if data.get("parts") is not None:
        import capo_omics.types.complete_read_set_upload_part_list

        out["parts"] = (
            capo_omics.types.complete_read_set_upload_part_list.deserialize_json(
                data["parts"]
            )
        )
    else:
        out["parts"] = []
    return out
