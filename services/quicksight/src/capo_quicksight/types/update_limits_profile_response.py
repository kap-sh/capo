"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateLimitsProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.resource_arn


class UpdateLimitsProfileResponse(TypedDict, closed=True):
    arn: "capo_quicksight.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the updated limits profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLimitsProfileResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> UpdateLimitsProfileResponse:
    out: UpdateLimitsProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
