"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DeleteEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.state


class DeleteEntityResponse(TypedDict, closed=True):
    state: "capo_iottwinmaker.types.state.State"
    """<p>The current state of the deleted entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEntityResponse) -> dict:
    out: dict = {}
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> DeleteEntityResponse:
    out: DeleteEntityResponse = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    return out
