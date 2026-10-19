"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ChunkingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.chunking_strategy
    import capo_bedrock_agent.types.fixed_size_chunking_configuration
    import capo_bedrock_agent.types.hierarchical_chunking_configuration
    import capo_bedrock_agent.types.semantic_chunking_configuration


class ChunkingConfiguration(TypedDict, closed=True):
    chunking_strategy: "capo_bedrock_agent.types.chunking_strategy.ChunkingStrategy"
    """<p>Knowledge base can split your source data into chunks. A <i>chunk</i> refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried. You have the following options for chunking your data. If you opt for <code>NONE</code>, then you may want to pre-process your files by splitting them up such that each file corresponds to a chunk.</p> <ul> <li> <p> <code>FIXED_SIZE</code> – Amazon Bedrock splits your source data into chunks of the approximate size that you set in the <code>fixedSizeChunkingConfiguration</code>.</p> </li> <li> <p> <code>HIERARCHICAL</code> – Split documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.</p> </li> <li> <p> <code>SEMANTIC</code> – Split documents into chunks based on groups of similar content derived with natural language processing.</p> </li> <li> <p> <code>NONE</code> – Amazon Bedrock treats each file as one chunk. If you choose this option, you may want to pre-process your documents by splitting them into separate files.</p> </li> </ul>"""
    fixed_size_chunking_configuration: NotRequired[
        "capo_bedrock_agent.types.fixed_size_chunking_configuration.FixedSizeChunkingConfiguration"
    ]
    """<p>Configurations for when you choose fixed-size chunking. If you set the <code>chunkingStrategy</code> as <code>NONE</code>, exclude this field.</p>"""
    hierarchical_chunking_configuration: NotRequired[
        "capo_bedrock_agent.types.hierarchical_chunking_configuration.HierarchicalChunkingConfiguration"
    ]
    """<p>Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.</p>"""
    semantic_chunking_configuration: NotRequired[
        "capo_bedrock_agent.types.semantic_chunking_configuration.SemanticChunkingConfiguration"
    ]
    """<p>Settings for semantic document chunking for a data source. Semantic chunking splits a document into into smaller documents based on groups of similar content derived from the text with natural language processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChunkingConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.chunking_strategy

    out["chunkingStrategy"] = capo_bedrock_agent.types.chunking_strategy.serialize_json(
        value["chunking_strategy"]
    )
    if "fixed_size_chunking_configuration" in value:
        import capo_bedrock_agent.types.fixed_size_chunking_configuration

        out["fixedSizeChunkingConfiguration"] = (
            capo_bedrock_agent.types.fixed_size_chunking_configuration.serialize_json(
                value["fixed_size_chunking_configuration"]
            )
        )
    if "hierarchical_chunking_configuration" in value:
        import capo_bedrock_agent.types.hierarchical_chunking_configuration

        out["hierarchicalChunkingConfiguration"] = (
            capo_bedrock_agent.types.hierarchical_chunking_configuration.serialize_json(
                value["hierarchical_chunking_configuration"]
            )
        )
    if "semantic_chunking_configuration" in value:
        import capo_bedrock_agent.types.semantic_chunking_configuration

        out["semanticChunkingConfiguration"] = (
            capo_bedrock_agent.types.semantic_chunking_configuration.serialize_json(
                value["semantic_chunking_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChunkingConfiguration:
    out: ChunkingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("chunkingStrategy") is not None:
        import capo_bedrock_agent.types.chunking_strategy

        out["chunking_strategy"] = (
            capo_bedrock_agent.types.chunking_strategy.deserialize_json(
                data["chunkingStrategy"]
            )
        )
    else:
        import typing

        out["chunking_strategy"] = typing.cast(
            "capo_bedrock_agent.types.chunking_strategy.ChunkingStrategy", ""
        )
    if data.get("fixedSizeChunkingConfiguration") is not None:
        import capo_bedrock_agent.types.fixed_size_chunking_configuration

        out["fixed_size_chunking_configuration"] = (
            capo_bedrock_agent.types.fixed_size_chunking_configuration.deserialize_json(
                data["fixedSizeChunkingConfiguration"]
            )
        )
    if data.get("hierarchicalChunkingConfiguration") is not None:
        import capo_bedrock_agent.types.hierarchical_chunking_configuration

        out["hierarchical_chunking_configuration"] = (
            capo_bedrock_agent.types.hierarchical_chunking_configuration.deserialize_json(
                data["hierarchicalChunkingConfiguration"]
            )
        )
    if data.get("semanticChunkingConfiguration") is not None:
        import capo_bedrock_agent.types.semantic_chunking_configuration

        out["semantic_chunking_configuration"] = (
            capo_bedrock_agent.types.semantic_chunking_configuration.deserialize_json(
                data["semanticChunkingConfiguration"]
            )
        )
    return out
