"""Generated from Smithy shape ``com.amazonaws.elementalinference#BedrockFunctionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.bedrock_api


class BedrockFunctionTarget(TypedDict, closed=True):
    api: "capo_elementalinference.types.bedrock_api.BedrockApi"
    """<p>The Amazon Bedrock API to call. The only valid value is INVOKE_MODEL.</p>"""
    model: "str"
    """<p>The model to invoke. Specify one of the following:</p> <ul> <li> <p>A model ID.</p> </li> <li> <p>An inference profile ID.</p> </li> <li> <p>The ARN of a custom model.</p> </li> <li> <p>The ARN of a provisioned model.</p> </li> </ul> <p>Elemental Inference invokes the model in the Region of the feed. To use a model in other Regions, specify a cross-Region inference profile ID. A custom or provisioned model must be in the Region of the feed. </p> <p>The request expression must produce a request body that this model accepts, and the model must accept the kind of media that the request expression references. For example, a text-only model can't accept a request that references media.frames. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockFunctionTarget) -> dict:
    out: dict = {}
    import capo_elementalinference.types.bedrock_api

    out["api"] = capo_elementalinference.types.bedrock_api.serialize_json(value["api"])
    out["model"] = value["model"]
    return out


def deserialize_json(data: dict) -> BedrockFunctionTarget:
    out: BedrockFunctionTarget = {}  # type: ignore[typeddict-item]
    if data.get("api") is not None:
        import capo_elementalinference.types.bedrock_api

        out["api"] = capo_elementalinference.types.bedrock_api.deserialize_json(
            data["api"]
        )
    else:
        import typing

        out["api"] = typing.cast(
            "capo_elementalinference.types.bedrock_api.BedrockApi", ""
        )
    if data.get("model") is not None:
        out["model"] = data["model"]
    else:
        out["model"] = ""
    return out
