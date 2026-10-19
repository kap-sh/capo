"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetActivationJobSourceItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.read_set_id


class StartReadSetActivationJobSourceItem(TypedDict, closed=True):
    read_set_id: "capo_omics.types.read_set_id.ReadSetId"
    """<p>The source's read set ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetActivationJobSourceItem) -> dict:
    out: dict = {}
    out["readSetId"] = value["read_set_id"]
    return out


def deserialize_json(data: dict) -> StartReadSetActivationJobSourceItem:
    out: StartReadSetActivationJobSourceItem = {}  # type: ignore[typeddict-item]
    if data.get("readSetId") is not None:
        out["read_set_id"] = data["readSetId"]
    else:
        out["read_set_id"] = ""
    return out
