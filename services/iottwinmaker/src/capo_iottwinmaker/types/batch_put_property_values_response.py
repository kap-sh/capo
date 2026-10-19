"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#BatchPutPropertyValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.error_entries


class BatchPutPropertyValuesResponse(TypedDict, closed=True):
    error_entries: "capo_iottwinmaker.types.error_entries.ErrorEntries"
    """<p>Entries that caused errors in the batch put operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutPropertyValuesResponse) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.error_entries

    out["errorEntries"] = capo_iottwinmaker.types.error_entries.serialize_json(
        value["error_entries"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutPropertyValuesResponse:
    out: BatchPutPropertyValuesResponse = {}  # type: ignore[typeddict-item]
    if data.get("errorEntries") is not None:
        import capo_iottwinmaker.types.error_entries

        out["error_entries"] = capo_iottwinmaker.types.error_entries.deserialize_json(
            data["errorEntries"]
        )
    else:
        out["error_entries"] = []
    return out
