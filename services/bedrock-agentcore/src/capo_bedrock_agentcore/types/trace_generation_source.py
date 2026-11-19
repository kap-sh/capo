"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TraceGenerationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.generation_sampling_config
    import capo_bedrock_agentcore.types.generation_selection
    import capo_bedrock_agentcore.types.ground_truth_config
    import capo_bedrock_agentcore.types.redaction_configuration
    import capo_bedrock_agentcore.types.trace_source_config


class TraceGenerationSource(TypedDict, closed=True):
    source_config: "capo_bedrock_agentcore.types.trace_source_config.TraceSourceConfig"
    """<p>Where to read the sessions from.</p>"""
    selection: NotRequired[
        "capo_bedrock_agentcore.types.generation_selection.GenerationSelection"
    ]
    """<p>How to choose sessions from the source. If you don't specify a selection, the generation uses every session in the source and time window that has at most 100 turns.</p>"""
    sampling: NotRequired[
        "capo_bedrock_agentcore.types.generation_sampling_config.GenerationSamplingConfig"
    ]
    """<p>How many scenarios to generate from the selected sessions.</p>"""
    ground_truth: NotRequired[
        "capo_bedrock_agentcore.types.ground_truth_config.GroundTruthConfig"
    ]
    """<p>Reference fields to copy from the sessions into the examples. If you don't specify this, the examples have no reference fields.</p>"""
    redaction_configuration: NotRequired[
        "capo_bedrock_agentcore.types.redaction_configuration.RedactionConfiguration"
    ]
    """<p>Sensitive data to mask in the examples. If you don't specify this, nothing is redacted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TraceGenerationSource) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.trace_source_config

    out["sourceConfig"] = (
        capo_bedrock_agentcore.types.trace_source_config.serialize_json(
            value["source_config"]
        )
    )
    if "selection" in value:
        import capo_bedrock_agentcore.types.generation_selection

        out["selection"] = (
            capo_bedrock_agentcore.types.generation_selection.serialize_json(
                value["selection"]
            )
        )
    if "sampling" in value:
        import capo_bedrock_agentcore.types.generation_sampling_config

        out["sampling"] = (
            capo_bedrock_agentcore.types.generation_sampling_config.serialize_json(
                value["sampling"]
            )
        )
    if "ground_truth" in value:
        import capo_bedrock_agentcore.types.ground_truth_config

        out["groundTruth"] = (
            capo_bedrock_agentcore.types.ground_truth_config.serialize_json(
                value["ground_truth"]
            )
        )
    if "redaction_configuration" in value:
        import capo_bedrock_agentcore.types.redaction_configuration

        out["redactionConfiguration"] = (
            capo_bedrock_agentcore.types.redaction_configuration.serialize_json(
                value["redaction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TraceGenerationSource:
    out: TraceGenerationSource = {}  # type: ignore[typeddict-item]
    if data.get("sourceConfig") is not None:
        import capo_bedrock_agentcore.types.trace_source_config

        out["source_config"] = (
            capo_bedrock_agentcore.types.trace_source_config.deserialize_json(
                data["sourceConfig"]
            )
        )
    else:
        out["source_config"] = {"$unknown": {"name": ""}}
    if data.get("selection") is not None:
        import capo_bedrock_agentcore.types.generation_selection

        out["selection"] = (
            capo_bedrock_agentcore.types.generation_selection.deserialize_json(
                data["selection"]
            )
        )
    if data.get("sampling") is not None:
        import capo_bedrock_agentcore.types.generation_sampling_config

        out["sampling"] = (
            capo_bedrock_agentcore.types.generation_sampling_config.deserialize_json(
                data["sampling"]
            )
        )
    if data.get("groundTruth") is not None:
        import capo_bedrock_agentcore.types.ground_truth_config

        out["ground_truth"] = (
            capo_bedrock_agentcore.types.ground_truth_config.deserialize_json(
                data["groundTruth"]
            )
        )
    if data.get("redactionConfiguration") is not None:
        import capo_bedrock_agentcore.types.redaction_configuration

        out["redaction_configuration"] = (
            capo_bedrock_agentcore.types.redaction_configuration.deserialize_json(
                data["redactionConfiguration"]
            )
        )
    return out
