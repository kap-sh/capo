"""Generated from Smithy shape ``com.amazonaws.qconnect#ManualSearchAIAgentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.association_configuration_list
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.uuid_with_qualifier


class ManualSearchAIAgentConfiguration(TypedDict, closed=True):
    answer_generation_ai_prompt_id: NotRequired[
        "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Prompt identifier for the Answer Generation prompt used by the MANUAL_SEARCH AI Agent.</p>"""
    answer_generation_ai_guardrail_id: NotRequired[
        "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Guardrail identifier for the Answer Generation guardrail used by the MANUAL_SEARCH AI Agent.</p>"""
    association_configurations: NotRequired[
        "capo_qconnect.types.association_configuration_list.AssociationConfigurationList"
    ]
    """<p>The association configurations for overriding behavior on this AI Agent.</p>"""
    locale: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The locale to which specifies the language and region settings that determine the response language for <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html">QueryAssistant</a>.</p> <note> <p>For more information on supported locales, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html#qic-notes-languages">Language support for Amazon Q in Connect</a>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManualSearchAIAgentConfiguration) -> dict:
    out: dict = {}
    if "answer_generation_ai_prompt_id" in value:
        out["answerGenerationAIPromptId"] = value["answer_generation_ai_prompt_id"]
    if "answer_generation_ai_guardrail_id" in value:
        out["answerGenerationAIGuardrailId"] = value[
            "answer_generation_ai_guardrail_id"
        ]
    if "association_configurations" in value:
        import capo_qconnect.types.association_configuration_list

        out["associationConfigurations"] = (
            capo_qconnect.types.association_configuration_list.serialize_json(
                value["association_configurations"]
            )
        )
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_json(data: dict) -> ManualSearchAIAgentConfiguration:
    out: ManualSearchAIAgentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("answerGenerationAIPromptId") is not None:
        out["answer_generation_ai_prompt_id"] = data["answerGenerationAIPromptId"]
    if data.get("answerGenerationAIGuardrailId") is not None:
        out["answer_generation_ai_guardrail_id"] = data["answerGenerationAIGuardrailId"]
    if data.get("associationConfigurations") is not None:
        import capo_qconnect.types.association_configuration_list

        out["association_configurations"] = (
            capo_qconnect.types.association_configuration_list.deserialize_json(
                data["associationConfigurations"]
            )
        )
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    return out
