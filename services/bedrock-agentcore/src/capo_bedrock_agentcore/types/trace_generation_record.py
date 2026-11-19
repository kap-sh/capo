"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TraceGenerationRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.generation_sampling_config
    import capo_bedrock_agentcore.types.generation_selection_record
    import capo_bedrock_agentcore.types.ground_truth_config
    import capo_bedrock_agentcore.types.redaction_configuration
    import capo_bedrock_agentcore.types.trace_source_config


class TraceGenerationRecord(TypedDict, closed=True):
    source_config: NotRequired[
        "capo_bedrock_agentcore.types.trace_source_config.TraceSourceConfig"
    ]
    """<p>Where the generation reads sessions from, including the resolved time window.</p>"""
    selection: NotRequired[
        "capo_bedrock_agentcore.types.generation_selection_record.GenerationSelectionRecord"
    ]
    """<p>How the generation chooses sessions. Filters are returned as submitted, with the resolved maximum turn count. Session and trace IDs are returned as counts. If this is absent, the request had no selection.</p>"""
    sampling: NotRequired[
        "capo_bedrock_agentcore.types.generation_sampling_config.GenerationSamplingConfig"
    ]
    """<p>How many scenarios the generation produces.</p>"""
    ground_truth: NotRequired[
        "capo_bedrock_agentcore.types.ground_truth_config.GroundTruthConfig"
    ]
    """<p>The reference fields the generation copies into the examples. If the request didn't specify quality filters, the filters the generation applies are returned here.</p>"""
    redaction_configuration: NotRequired[
        "capo_bedrock_agentcore.types.redaction_configuration.RedactionConfiguration"
    ]
    """<p>The sensitive data the generation masks in the examples.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TraceGenerationRecord) -> dict:
    out: dict = {}
    if "source_config" in value:
        import capo_bedrock_agentcore.types.trace_source_config

        out["sourceConfig"] = (
            capo_bedrock_agentcore.types.trace_source_config.serialize_json(
                value["source_config"]
            )
        )
    if "selection" in value:
        import capo_bedrock_agentcore.types.generation_selection_record

        out["selection"] = (
            capo_bedrock_agentcore.types.generation_selection_record.serialize_json(
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


def deserialize_json(data: dict) -> TraceGenerationRecord:
    out: TraceGenerationRecord = {}  # type: ignore[typeddict-item]
    if data.get("sourceConfig") is not None:
        import capo_bedrock_agentcore.types.trace_source_config

        out["source_config"] = (
            capo_bedrock_agentcore.types.trace_source_config.deserialize_json(
                data["sourceConfig"]
            )
        )
    if data.get("selection") is not None:
        import capo_bedrock_agentcore.types.generation_selection_record

        out["selection"] = (
            capo_bedrock_agentcore.types.generation_selection_record.deserialize_json(
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
