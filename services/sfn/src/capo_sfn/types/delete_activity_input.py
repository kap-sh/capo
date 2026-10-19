"""Generated from Smithy shape ``com.amazonaws.sfn#DeleteActivityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn


class DeleteActivityInput(TypedDict, closed=True):
    activity_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the activity to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteActivityInput) -> dict:
    out: dict = {}
    out["activityArn"] = value["activity_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteActivityInput:
    out: DeleteActivityInput = {}  # type: ignore[typeddict-item]
    if data.get("activityArn") is not None:
        out["activity_arn"] = data["activityArn"]
    else:
        out["activity_arn"] = ""
    return out
