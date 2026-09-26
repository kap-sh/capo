"""Generated from Smithy shape ``com.amazonaws.supportauthz#GetActionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supportauthz.types.action


class GetActionInput(TypedDict, closed=True):
    action: "capo_supportauthz.types.action.Action"
    """<p>The name of the support action to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetActionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetActionInput:
    out: GetActionInput = {}  # type: ignore[typeddict-item]
    return out
