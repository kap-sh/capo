"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteLimitsProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.resource_arn


class DeleteLimitsProfileResponse(TypedDict, closed=True):
    arn: "capo_quicksight.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the deleted limits profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLimitsProfileResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteLimitsProfileResponse:
    out: DeleteLimitsProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
