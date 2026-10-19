"""Generated from Smithy shape ``com.amazonaws.sfn#RedriveExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.client_token


class RedriveExecutionInput(TypedDict, closed=True):
    execution_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the execution to be redriven.</p>"""
    client_token: NotRequired["capo_sfn.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The API will return idempotent responses for the last 10 client tokens used to successfully redrive the execution. These client tokens are valid for up to 15 minutes after they are first used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RedriveExecutionInput) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RedriveExecutionInput:
    out: RedriveExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("executionArn") is not None:
        out["execution_arn"] = data["executionArn"]
    else:
        out["execution_arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
