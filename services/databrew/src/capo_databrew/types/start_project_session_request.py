"""Generated from Smithy shape ``com.amazonaws.databrew#StartProjectSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.assume_control
    import capo_databrew.types.project_name


class StartProjectSessionRequest(TypedDict, closed=True):
    name: "capo_databrew.types.project_name.ProjectName"
    """<p>The name of the project to act upon.</p>"""
    assume_control: NotRequired["capo_databrew.types.assume_control.AssumeControl"]
    """<p>A value that, if true, enables you to take control of a session, even if a different client is currently accessing the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProjectSessionRequest) -> dict:
    out: dict = {}
    if "assume_control" in value:
        out["AssumeControl"] = value["assume_control"]
    return out


def deserialize_json(data: dict) -> StartProjectSessionRequest:
    out: StartProjectSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssumeControl") is not None:
        out["assume_control"] = data["AssumeControl"]
    return out
