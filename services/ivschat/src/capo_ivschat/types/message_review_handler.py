"""Generated from Smithy shape ``com.amazonaws.ivschat#MessageReviewHandler``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.fallback_result
    import capo_ivschat.types.lambda_arn


class MessageReviewHandler(TypedDict, closed=True):
    uri: NotRequired["capo_ivschat.types.lambda_arn.LambdaArn"]
    """<p>Identifier of the message review handler. Currently this must be an ARN of a lambda function.</p>"""
    fallback_result: NotRequired["capo_ivschat.types.fallback_result.FallbackResult"]
    """<p>Specifies the fallback behavior (whether the message is allowed or denied) if the handler does not return a valid response, encounters an error, or times out. (For the timeout period, see <a href="https://docs.aws.amazon.com/ivs/latest/userguide/service-quotas.html"> Service Quotas</a>.) If allowed, the message is delivered with returned content to all users connected to the room. If denied, the message is not delivered to any user. Default: <code>ALLOW</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageReviewHandler) -> dict:
    out: dict = {}
    if "uri" in value:
        out["uri"] = value["uri"]
    if "fallback_result" in value:
        out["fallbackResult"] = value["fallback_result"]
    return out


def deserialize_json(data: dict) -> MessageReviewHandler:
    out: MessageReviewHandler = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    if data.get("fallbackResult") is not None:
        out["fallback_result"] = data["fallbackResult"]
    return out
