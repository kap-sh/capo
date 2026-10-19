"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetTestGridProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_farm_arn


class GetTestGridProjectRequest(TypedDict, closed=True):
    project_arn: "capo_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>The ARN of the Selenium testing project, from either <a>CreateTestGridProject</a> or <a>ListTestGridProjects</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTestGridProjectRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTestGridProjectRequest:
    out: GetTestGridProjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    else:
        out["project_arn"] = ""
    return out
