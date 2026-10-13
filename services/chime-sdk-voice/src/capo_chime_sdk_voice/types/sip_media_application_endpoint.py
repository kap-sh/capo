"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipMediaApplicationEndpoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.function_arn


class SipMediaApplicationEndpoint(TypedDict, closed=True):
    lambda_arn: NotRequired["capo_chime_sdk_voice.types.function_arn.FunctionArn"]
    """<p>Valid Amazon Resource Name (ARN) of the Lambda function, version, or alias. The function must be created in the same AWS Region as the SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SipMediaApplicationEndpoint) -> dict:
    out: dict = {}
    if "lambda_arn" in value:
        out["LambdaArn"] = value["lambda_arn"]
    return out


def deserialize_json(data: dict) -> SipMediaApplicationEndpoint:
    out: SipMediaApplicationEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("LambdaArn") is not None:
        out["lambda_arn"] = data["LambdaArn"]
    return out


def redact_sensitive(value: SipMediaApplicationEndpoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "lambda_arn" in value:
        out["lambda_arn"] = "*** Sensitive Data Redacted ***"
    return out
