"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#BatchPutPropertyErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.errors


class BatchPutPropertyErrorEntry(TypedDict, closed=True):
    errors: "capo_iottwinmaker.types.errors.Errors"
    """<p>A list of objects that contain information about errors returned by the <code>BatchPutProperty</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutPropertyErrorEntry) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.errors

    out["errors"] = capo_iottwinmaker.types.errors.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> BatchPutPropertyErrorEntry:
    out: BatchPutPropertyErrorEntry = {}  # type: ignore[typeddict-item]
    if data.get("errors") is not None:
        import capo_iottwinmaker.types.errors

        out["errors"] = capo_iottwinmaker.types.errors.deserialize_json(data["errors"])
    else:
        out["errors"] = []
    return out
