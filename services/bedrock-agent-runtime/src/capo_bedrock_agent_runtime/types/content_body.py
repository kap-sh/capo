"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ContentBody``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.image_inputs


class ContentBody(TypedDict, closed=True):
    body: NotRequired["str"]
    """<p>The body of the API response.</p>"""
    images: NotRequired["capo_bedrock_agent_runtime.types.image_inputs.ImageInputs"]
    """<p>Lists details, including format and source, for the image in the response from the function call. You can specify only one image and the function in the <code>returnControlInvocationResults</code> must be a computer use action. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agent-computer-use.html">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentBody) -> dict:
    out: dict = {}
    if "body" in value:
        out["body"] = value["body"]
    if "images" in value:
        import capo_bedrock_agent_runtime.types.image_inputs

        out["images"] = capo_bedrock_agent_runtime.types.image_inputs.serialize_json(
            value["images"]
        )
    return out


def deserialize_json(data: dict) -> ContentBody:
    out: ContentBody = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        out["body"] = data["body"]
    if data.get("images") is not None:
        import capo_bedrock_agent_runtime.types.image_inputs

        out["images"] = capo_bedrock_agent_runtime.types.image_inputs.deserialize_json(
            data["images"]
        )
    return out
