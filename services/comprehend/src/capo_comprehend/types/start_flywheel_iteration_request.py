"""Generated from Smithy shape ``com.amazonaws.comprehend#StartFlywheelIterationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.client_request_token_string
    import capo_comprehend.types.comprehend_flywheel_arn


class StartFlywheelIterationRequest(TypedDict, closed=True):
    flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    """<p>The ARN of the flywheel.</p>"""
    client_request_token: NotRequired[
        "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartFlywheelIterationRequest) -> dict:
    out: dict = {}
    out["FlywheelArn"] = value["flywheel_arn"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartFlywheelIterationRequest:
    out: StartFlywheelIterationRequest = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    else:
        out["flywheel_arn"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
