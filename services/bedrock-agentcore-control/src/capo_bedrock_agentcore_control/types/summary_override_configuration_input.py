"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SummaryOverrideConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input


class SummaryOverrideConfigurationInput(TypedDict, closed=True):
    consolidation: NotRequired[
        "capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.SummaryOverrideConsolidationConfigurationInput"
    ]
    """<p>The consolidation configuration for a summary override.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummaryOverrideConfigurationInput) -> dict:
    out: dict = {}
    if "consolidation" in value:
        import capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.serialize_json(
                value["consolidation"]
            )
        )
    return out


def deserialize_json(data: dict) -> SummaryOverrideConfigurationInput:
    out: SummaryOverrideConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("consolidation") is not None:
        import capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.deserialize_json(
                data["consolidation"]
            )
        )
    return out


def redact_sensitive(value: SummaryOverrideConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "consolidation" in value:
        import capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input

        out["consolidation"] = (
            capo_bedrock_agentcore_control.types.summary_override_consolidation_configuration_input.redact_sensitive(
                value["consolidation"]
            )
        )
    return out
