"""Generated from Smithy shape ``com.amazonaws.resiliencehub#BatchUpdateRecommendationStatusFailedEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.error_message
    import capo_resiliencehub.types.string255


class BatchUpdateRecommendationStatusFailedEntry(TypedDict, closed=True):
    entry_id: "capo_resiliencehub.types.string255.String255"
    """<p>An identifier of an entry in this batch that is used to communicate the result.</p> <note> <p>The <code>entryId</code>s of a batch request need to be unique within a request.</p> </note>"""
    error_message: "capo_resiliencehub.types.error_message.ErrorMessage"
    """<p>Indicates the error that occurred while excluding an operational recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRecommendationStatusFailedEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateRecommendationStatusFailedEntry:
    out: BatchUpdateRecommendationStatusFailedEntry = {}  # type: ignore[typeddict-item]
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    else:
        out["entry_id"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
