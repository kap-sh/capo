"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#StartAsyncInvokeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.invocation_arn


class StartAsyncInvokeResponse(TypedDict, closed=True):
    invocation_arn: "capo_bedrock_runtime.types.invocation_arn.InvocationArn"
    """<p>The ARN of the invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAsyncInvokeResponse) -> dict:
    out: dict = {}
    out["invocationArn"] = value["invocation_arn"]
    return out


def deserialize_json(data: dict) -> StartAsyncInvokeResponse:
    out: StartAsyncInvokeResponse = {}  # type: ignore[typeddict-item]
    if data.get("invocationArn") is not None:
        out["invocation_arn"] = data["invocationArn"]
    else:
        out["invocation_arn"] = ""
    return out
