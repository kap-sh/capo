"""Generated from Smithy shape ``com.amazonaws.apprunner#DeleteConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn


class DeleteConnectionRequest(TypedDict, closed=True):
    connection_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner connection that you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteConnectionRequest) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteConnectionRequest:
    out: DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        out["connection_arn"] = ""
    return out
