"""Generated from Smithy shape ``com.amazonaws.omics#BatchDeleteReadSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.read_set_id_list
    import capo_omics.types.sequence_store_id


class BatchDeleteReadSetRequest(TypedDict, closed=True):
    ids: "capo_omics.types.read_set_id_list.ReadSetIdList"
    """<p>The read sets' IDs.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read sets' sequence store ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteReadSetRequest) -> dict:
    out: dict = {}
    import capo_omics.types.read_set_id_list

    out["ids"] = capo_omics.types.read_set_id_list.serialize_json(value["ids"])
    return out


def deserialize_json(data: dict) -> BatchDeleteReadSetRequest:
    out: BatchDeleteReadSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_omics.types.read_set_id_list

        out["ids"] = capo_omics.types.read_set_id_list.deserialize_json(data["ids"])
    else:
        out["ids"] = []
    return out
