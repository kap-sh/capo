"""Generated from Smithy shape ``com.amazonaws.amp#WorkspaceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.workspace_status_code


class WorkspaceStatus(TypedDict, closed=True):
    status_code: "capo_amp.types.workspace_status_code.WorkspaceStatusCode"
    """<p>The current status of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    return out


def deserialize_json(data: dict) -> WorkspaceStatus:
    out: WorkspaceStatus = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    else:
        out["status_code"] = ""
    return out
