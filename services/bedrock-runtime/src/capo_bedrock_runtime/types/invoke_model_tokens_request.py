"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelTokensRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.body


class InvokeModelTokensRequest(TypedDict, closed=True):
    body: "capo_bedrock_runtime.types.body.Body"
    """<p>The request body to count tokens for, formatted according to the model's expected input format. To learn about the input format for different models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Model inference parameters and responses</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeModelTokensRequest) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.body

    out["body"] = capo_bedrock_runtime.types.body.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> InvokeModelTokensRequest:
    out: InvokeModelTokensRequest = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        import capo_bedrock_runtime.types.body

        out["body"] = capo_bedrock_runtime.types.body.deserialize_json(data["body"])
    else:
        raise DeserializationError("InvokeModelTokensRequest.body required")
    return out
