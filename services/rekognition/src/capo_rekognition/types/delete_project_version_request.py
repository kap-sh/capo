"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteProjectVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.project_version_arn


class DeleteProjectVersionRequest(TypedDict, closed=True):
    project_version_arn: "capo_rekognition.types.project_version_arn.ProjectVersionArn"
    """<p>The Amazon Resource Name (ARN) of the project version that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProjectVersionRequest) -> dict:
    out: dict = {}
    out["ProjectVersionArn"] = value["project_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProjectVersionRequest:
    out: DeleteProjectVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProjectVersionArn") is not None:
        out["project_version_arn"] = data["ProjectVersionArn"]
    else:
        out["project_version_arn"] = ""
    return out
