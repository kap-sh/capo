"""Generated from Smithy shape ``com.amazonaws.bedrockagent#BedrockEmbeddingModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.audio_configurations
    import capo_bedrock_agent.types.dimensions
    import capo_bedrock_agent.types.embedding_data_type
    import capo_bedrock_agent.types.video_configurations


class BedrockEmbeddingModelConfiguration(TypedDict, closed=True):
    dimensions: NotRequired["capo_bedrock_agent.types.dimensions.Dimensions"]
    """<p>The dimensions details for the vector configuration used on the Bedrock embeddings model.</p>"""
    embedding_data_type: NotRequired[
        "capo_bedrock_agent.types.embedding_data_type.EmbeddingDataType"
    ]
    """<p>The data type for the vectors when using a model to convert text into vector embeddings. The model must support the specified data type for vector embeddings. Floating-point (float32) is the default data type, and is supported by most models for vector embeddings. See <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html">Supported embeddings models</a> for information on the available models and their vector data types.</p>"""
    audio: NotRequired[
        "capo_bedrock_agent.types.audio_configurations.AudioConfigurations"
    ]
    """<p>Configuration settings for processing audio content in multimodal knowledge bases.</p> <important> <p>This field is deprecated. Use <code>modelConfiguration</code> instead.</p> </important>"""
    video: NotRequired[
        "capo_bedrock_agent.types.video_configurations.VideoConfigurations"
    ]
    """<p>Configuration settings for processing video content in multimodal knowledge bases.</p> <important> <p>This field is deprecated. Use <code>modelConfiguration</code> instead.</p> </important>"""
    model_configuration: NotRequired["object"]
    """<p>Model-specific configuration for the embedding model, provided as a JSON object. Use this field to specify settings that apply to the embedding model that you selected, such as how audio and video files are divided into segments.</p> <p>The fields that this object accepts depend on the embedding model. For the settings that each model accepts, see the documentation for that model.</p> <p>For an example of a <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateKnowledgeBase.html">CreateKnowledgeBase</a> request that uses this field to configure a multimodal embedding model, see the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateKnowledgeBase.html#API_agent_CreateKnowledgeBase_Examples">Examples</a> section of <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateKnowledgeBase.html">CreateKnowledgeBase</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockEmbeddingModelConfiguration) -> dict:
    out: dict = {}
    if "dimensions" in value:
        out["dimensions"] = value["dimensions"]
    if "embedding_data_type" in value:
        import capo_bedrock_agent.types.embedding_data_type

        out["embeddingDataType"] = (
            capo_bedrock_agent.types.embedding_data_type.serialize_json(
                value["embedding_data_type"]
            )
        )
    if "audio" in value:
        import capo_bedrock_agent.types.audio_configurations

        out["audio"] = capo_bedrock_agent.types.audio_configurations.serialize_json(
            value["audio"]
        )
    if "video" in value:
        import capo_bedrock_agent.types.video_configurations

        out["video"] = capo_bedrock_agent.types.video_configurations.serialize_json(
            value["video"]
        )
    if "model_configuration" in value:
        out["modelConfiguration"] = value["model_configuration"]
    return out


def deserialize_json(data: dict) -> BedrockEmbeddingModelConfiguration:
    out: BedrockEmbeddingModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("dimensions") is not None:
        out["dimensions"] = data["dimensions"]
    if data.get("embeddingDataType") is not None:
        import capo_bedrock_agent.types.embedding_data_type

        out["embedding_data_type"] = (
            capo_bedrock_agent.types.embedding_data_type.deserialize_json(
                data["embeddingDataType"]
            )
        )
    if data.get("audio") is not None:
        import capo_bedrock_agent.types.audio_configurations

        out["audio"] = capo_bedrock_agent.types.audio_configurations.deserialize_json(
            data["audio"]
        )
    if data.get("video") is not None:
        import capo_bedrock_agent.types.video_configurations

        out["video"] = capo_bedrock_agent.types.video_configurations.deserialize_json(
            data["video"]
        )
    if data.get("modelConfiguration") is not None:
        out["model_configuration"] = data["modelConfiguration"]
    return out
