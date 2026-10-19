"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetStageSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.stage_arn
    import capo_ivs_realtime.types.stage_session_id


class GetStageSessionRequest(TypedDict, closed=True):
    stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage for which the information is to be retrieved.</p>"""
    session_id: "capo_ivs_realtime.types.stage_session_id.StageSessionId"
    """<p>ID of a session within the stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStageSessionRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> GetStageSessionRequest:
    out: GetStageSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("stageArn") is not None:
        out["stage_arn"] = data["stageArn"]
    else:
        out["stage_arn"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    return out
