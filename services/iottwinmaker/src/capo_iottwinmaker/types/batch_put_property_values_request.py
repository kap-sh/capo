"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#BatchPutPropertyValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.entries
    import capo_iottwinmaker.types.id


class BatchPutPropertyValuesRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the properties to set.</p>"""
    entries: "capo_iottwinmaker.types.entries.Entries"
    """<p>An object that maps strings to the property value entries to set. Each string in the mapping must be unique to this object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutPropertyValuesRequest) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.entries

    out["entries"] = capo_iottwinmaker.types.entries.serialize_json(value["entries"])
    return out


def deserialize_json(data: dict) -> BatchPutPropertyValuesRequest:
    out: BatchPutPropertyValuesRequest = {}  # type: ignore[typeddict-item]
    if data.get("entries") is not None:
        import capo_iottwinmaker.types.entries

        out["entries"] = capo_iottwinmaker.types.entries.deserialize_json(
            data["entries"]
        )
    else:
        out["entries"] = []
    return out
