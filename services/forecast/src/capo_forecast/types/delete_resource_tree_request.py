"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteResourceTreeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DeleteResourceTreeRequest(TypedDict, closed=True):
    resource_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the parent resource to delete. All child resources of the parent resource will also be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourceTreeRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourceTreeRequest:
    out: DeleteResourceTreeRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
