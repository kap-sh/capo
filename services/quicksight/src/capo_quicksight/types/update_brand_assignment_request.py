"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateBrandAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id


class UpdateBrandAssignmentRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand assignment.</p>"""
    brand_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandAssignmentRequest) -> dict:
    out: dict = {}
    out["BrandArn"] = value["brand_arn"]
    return out


def deserialize_json(data: dict) -> UpdateBrandAssignmentRequest:
    out: UpdateBrandAssignmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("BrandArn") is not None:
        out["brand_arn"] = data["BrandArn"]
    else:
        out["brand_arn"] = ""
    return out
