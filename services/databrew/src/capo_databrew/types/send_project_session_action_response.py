"""Generated from Smithy shape ``com.amazonaws.databrew#SendProjectSessionActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.action_id
    import capo_databrew.types.project_name
    import capo_databrew.types.result


class SendProjectSessionActionResponse(TypedDict, closed=True):
    result: NotRequired["capo_databrew.types.result.Result"]
    """<p>A message indicating the result of performing the action.</p>"""
    name: "capo_databrew.types.project_name.ProjectName"
    """<p>The name of the project that was affected by the action.</p>"""
    action_id: NotRequired["capo_databrew.types.action_id.ActionId"]
    """<p>A unique identifier for the action that was performed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendProjectSessionActionResponse) -> dict:
    out: dict = {}
    if "result" in value:
        out["Result"] = value["result"]
    out["Name"] = value["name"]
    if "action_id" in value:
        out["ActionId"] = value["action_id"]
    return out


def deserialize_json(data: dict) -> SendProjectSessionActionResponse:
    out: SendProjectSessionActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Result") is not None:
        out["result"] = data["Result"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ActionId") is not None:
        out["action_id"] = data["ActionId"]
    return out
