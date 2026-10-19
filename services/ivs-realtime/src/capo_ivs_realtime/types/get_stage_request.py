"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.stage_arn


class GetStageRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage for which the information is to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStageRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetStageRequest:
    out: GetStageRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
