"""Generated from Smithy shape ``com.amazonaws.apprunner#ResumeServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn


class ResumeServiceRequest(TypedDict, closed=True):
    service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service that you want to resume.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResumeServiceRequest) -> dict:
    out: dict = {}
    out["ServiceArn"] = value["service_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResumeServiceRequest:
    out: ResumeServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceArn") is not None:
        out["service_arn"] = data["ServiceArn"]
    else:
        out["service_arn"] = ""
    return out
