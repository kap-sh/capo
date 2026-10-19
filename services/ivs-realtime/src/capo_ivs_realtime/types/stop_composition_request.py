"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StopCompositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.composition_arn


class StopCompositionRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.composition_arn.CompositionArn"
    """<p>ARN of the Composition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCompositionRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> StopCompositionRequest:
    out: StopCompositionRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
