"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteScheduleActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.resource_name


class DeleteScheduleActionResponse(TypedDict, closed=True):
    action_name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the schedule action that Elemental Inference deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScheduleActionResponse) -> dict:
    out: dict = {}
    out["actionName"] = value["action_name"]
    return out


def deserialize_json(data: dict) -> DeleteScheduleActionResponse:
    out: DeleteScheduleActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    else:
        out["action_name"] = ""
    return out
