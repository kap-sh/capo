"""Generated from Smithy shape ``com.amazonaws.scheduler#TargetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.target_arn


class TargetSummary(TypedDict, closed=True):
    arn: "capo_scheduler.types.target_arn.TargetArn"
    """<p>The Amazon Resource Name (ARN) of the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> TargetSummary:
    out: TargetSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
