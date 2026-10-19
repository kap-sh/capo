"""Generated from Smithy shape ``com.amazonaws.apprunner#StartDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.uuid


class StartDeploymentResponse(TypedDict, closed=True):
    operation_id: "capo_apprunner.types.uuid.UUID"
    """<p>The unique ID of the asynchronous operation that this request started. You can use it combined with the <a>ListOperations</a> call to track the operation's progress.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartDeploymentResponse) -> dict:
    out: dict = {}
    out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartDeploymentResponse:
    out: StartDeploymentResponse = {}  # type: ignore[typeddict-item]
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    else:
        out["operation_id"] = ""
    return out
