"""Generated from Smithy shape ``com.amazonaws.rekognition#StopProjectVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.project_version_arn


class StopProjectVersionRequest(TypedDict, closed=True):
    project_version_arn: "capo_rekognition.types.project_version_arn.ProjectVersionArn"
    """<p>The Amazon Resource Name (ARN) of the model version that you want to stop.</p> <p>This operation requires permissions to perform the <code>rekognition:StopProjectVersion</code> action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopProjectVersionRequest) -> dict:
    out: dict = {}
    out["ProjectVersionArn"] = value["project_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopProjectVersionRequest:
    out: StopProjectVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProjectVersionArn") is not None:
        out["project_version_arn"] = data["ProjectVersionArn"]
    else:
        out["project_version_arn"] = ""
    return out
