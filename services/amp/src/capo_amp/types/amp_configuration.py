"""Generated from Smithy shape ``com.amazonaws.amp#AmpConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.workspace_arn


class AmpConfiguration(TypedDict, closed=True):
    workspace_arn: "capo_amp.types.workspace_arn.WorkspaceArn"
    """<p>ARN of the Amazon Managed Service for Prometheus workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmpConfiguration) -> dict:
    out: dict = {}
    out["workspaceArn"] = value["workspace_arn"]
    return out


def deserialize_json(data: dict) -> AmpConfiguration:
    out: AmpConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("workspaceArn") is not None:
        out["workspace_arn"] = data["workspaceArn"]
    else:
        out["workspace_arn"] = ""
    return out
