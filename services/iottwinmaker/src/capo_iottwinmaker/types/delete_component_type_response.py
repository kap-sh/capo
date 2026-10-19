"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DeleteComponentTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.state


class DeleteComponentTypeResponse(TypedDict, closed=True):
    state: "capo_iottwinmaker.types.state.State"
    """<p>The current state of the component type to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteComponentTypeResponse) -> dict:
    out: dict = {}
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> DeleteComponentTypeResponse:
    out: DeleteComponentTypeResponse = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    return out
