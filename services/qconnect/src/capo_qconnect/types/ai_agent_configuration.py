"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.answer_recommendation_ai_agent_configuration
    import capo_qconnect.types.case_summarization_ai_agent_configuration
    import capo_qconnect.types.email_generative_answer_ai_agent_configuration
    import capo_qconnect.types.email_overview_ai_agent_configuration
    import capo_qconnect.types.email_response_ai_agent_configuration
    import capo_qconnect.types.manual_search_ai_agent_configuration
    import capo_qconnect.types.note_taking_ai_agent_configuration
    import capo_qconnect.types.orchestration_ai_agent_configuration
    import capo_qconnect.types.self_service_ai_agent_configuration


class AIAgentConfigurationManualSearchAIAgentConfigurationMember(
    TypedDict, closed=True
):
    manualSearchAIAgentConfiguration: "capo_qconnect.types.manual_search_ai_agent_configuration.ManualSearchAIAgentConfiguration"


class AIAgentConfigurationAnswerRecommendationAIAgentConfigurationMember(
    TypedDict, closed=True
):
    answerRecommendationAIAgentConfiguration: "capo_qconnect.types.answer_recommendation_ai_agent_configuration.AnswerRecommendationAIAgentConfiguration"


class AIAgentConfigurationSelfServiceAIAgentConfigurationMember(TypedDict, closed=True):
    selfServiceAIAgentConfiguration: "capo_qconnect.types.self_service_ai_agent_configuration.SelfServiceAIAgentConfiguration"


class AIAgentConfigurationEmailResponseAIAgentConfigurationMember(
    TypedDict, closed=True
):
    emailResponseAIAgentConfiguration: "capo_qconnect.types.email_response_ai_agent_configuration.EmailResponseAIAgentConfiguration"


class AIAgentConfigurationEmailOverviewAIAgentConfigurationMember(
    TypedDict, closed=True
):
    emailOverviewAIAgentConfiguration: "capo_qconnect.types.email_overview_ai_agent_configuration.EmailOverviewAIAgentConfiguration"


class AIAgentConfigurationEmailGenerativeAnswerAIAgentConfigurationMember(
    TypedDict, closed=True
):
    emailGenerativeAnswerAIAgentConfiguration: "capo_qconnect.types.email_generative_answer_ai_agent_configuration.EmailGenerativeAnswerAIAgentConfiguration"


class AIAgentConfigurationOrchestrationAIAgentConfigurationMember(
    TypedDict, closed=True
):
    orchestrationAIAgentConfiguration: "capo_qconnect.types.orchestration_ai_agent_configuration.OrchestrationAIAgentConfiguration"


class AIAgentConfigurationNoteTakingAIAgentConfigurationMember(TypedDict, closed=True):
    noteTakingAIAgentConfiguration: "capo_qconnect.types.note_taking_ai_agent_configuration.NoteTakingAIAgentConfiguration"


class AIAgentConfigurationCaseSummarizationAIAgentConfigurationMember(
    TypedDict, closed=True
):
    caseSummarizationAIAgentConfiguration: "capo_qconnect.types.case_summarization_ai_agent_configuration.CaseSummarizationAIAgentConfiguration"


AIAgentConfiguration: TypeAlias = (
    AIAgentConfigurationManualSearchAIAgentConfigurationMember
    | AIAgentConfigurationAnswerRecommendationAIAgentConfigurationMember
    | AIAgentConfigurationSelfServiceAIAgentConfigurationMember
    | AIAgentConfigurationEmailResponseAIAgentConfigurationMember
    | AIAgentConfigurationEmailOverviewAIAgentConfigurationMember
    | AIAgentConfigurationEmailGenerativeAnswerAIAgentConfigurationMember
    | AIAgentConfigurationOrchestrationAIAgentConfigurationMember
    | AIAgentConfigurationNoteTakingAIAgentConfigurationMember
    | AIAgentConfigurationCaseSummarizationAIAgentConfigurationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AIAgentConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "manualSearchAIAgentConfiguration" in value:
        import capo_qconnect.types.manual_search_ai_agent_configuration

        return {
            "manualSearchAIAgentConfiguration": capo_qconnect.types.manual_search_ai_agent_configuration.serialize_json(
                value["manualSearchAIAgentConfiguration"]
            )
        }
    elif "answerRecommendationAIAgentConfiguration" in value:
        import capo_qconnect.types.answer_recommendation_ai_agent_configuration

        return {
            "answerRecommendationAIAgentConfiguration": capo_qconnect.types.answer_recommendation_ai_agent_configuration.serialize_json(
                value["answerRecommendationAIAgentConfiguration"]
            )
        }
    elif "selfServiceAIAgentConfiguration" in value:
        import capo_qconnect.types.self_service_ai_agent_configuration

        return {
            "selfServiceAIAgentConfiguration": capo_qconnect.types.self_service_ai_agent_configuration.serialize_json(
                value["selfServiceAIAgentConfiguration"]
            )
        }
    elif "emailResponseAIAgentConfiguration" in value:
        import capo_qconnect.types.email_response_ai_agent_configuration

        return {
            "emailResponseAIAgentConfiguration": capo_qconnect.types.email_response_ai_agent_configuration.serialize_json(
                value["emailResponseAIAgentConfiguration"]
            )
        }
    elif "emailOverviewAIAgentConfiguration" in value:
        import capo_qconnect.types.email_overview_ai_agent_configuration

        return {
            "emailOverviewAIAgentConfiguration": capo_qconnect.types.email_overview_ai_agent_configuration.serialize_json(
                value["emailOverviewAIAgentConfiguration"]
            )
        }
    elif "emailGenerativeAnswerAIAgentConfiguration" in value:
        import capo_qconnect.types.email_generative_answer_ai_agent_configuration

        return {
            "emailGenerativeAnswerAIAgentConfiguration": capo_qconnect.types.email_generative_answer_ai_agent_configuration.serialize_json(
                value["emailGenerativeAnswerAIAgentConfiguration"]
            )
        }
    elif "orchestrationAIAgentConfiguration" in value:
        import capo_qconnect.types.orchestration_ai_agent_configuration

        return {
            "orchestrationAIAgentConfiguration": capo_qconnect.types.orchestration_ai_agent_configuration.serialize_json(
                value["orchestrationAIAgentConfiguration"]
            )
        }
    elif "noteTakingAIAgentConfiguration" in value:
        import capo_qconnect.types.note_taking_ai_agent_configuration

        return {
            "noteTakingAIAgentConfiguration": capo_qconnect.types.note_taking_ai_agent_configuration.serialize_json(
                value["noteTakingAIAgentConfiguration"]
            )
        }
    elif "caseSummarizationAIAgentConfiguration" in value:
        import capo_qconnect.types.case_summarization_ai_agent_configuration

        return {
            "caseSummarizationAIAgentConfiguration": capo_qconnect.types.case_summarization_ai_agent_configuration.serialize_json(
                value["caseSummarizationAIAgentConfiguration"]
            )
        }
    else:
        raise SerializationError("AIAgentConfiguration: no variant present")


def deserialize_json(data: dict) -> AIAgentConfiguration:
    if data.get("manualSearchAIAgentConfiguration") is not None:
        import capo_qconnect.types.manual_search_ai_agent_configuration

        return {
            "manualSearchAIAgentConfiguration": capo_qconnect.types.manual_search_ai_agent_configuration.deserialize_json(
                data["manualSearchAIAgentConfiguration"]
            )
        }
    elif data.get("answerRecommendationAIAgentConfiguration") is not None:
        import capo_qconnect.types.answer_recommendation_ai_agent_configuration

        return {
            "answerRecommendationAIAgentConfiguration": capo_qconnect.types.answer_recommendation_ai_agent_configuration.deserialize_json(
                data["answerRecommendationAIAgentConfiguration"]
            )
        }
    elif data.get("selfServiceAIAgentConfiguration") is not None:
        import capo_qconnect.types.self_service_ai_agent_configuration

        return {
            "selfServiceAIAgentConfiguration": capo_qconnect.types.self_service_ai_agent_configuration.deserialize_json(
                data["selfServiceAIAgentConfiguration"]
            )
        }
    elif data.get("emailResponseAIAgentConfiguration") is not None:
        import capo_qconnect.types.email_response_ai_agent_configuration

        return {
            "emailResponseAIAgentConfiguration": capo_qconnect.types.email_response_ai_agent_configuration.deserialize_json(
                data["emailResponseAIAgentConfiguration"]
            )
        }
    elif data.get("emailOverviewAIAgentConfiguration") is not None:
        import capo_qconnect.types.email_overview_ai_agent_configuration

        return {
            "emailOverviewAIAgentConfiguration": capo_qconnect.types.email_overview_ai_agent_configuration.deserialize_json(
                data["emailOverviewAIAgentConfiguration"]
            )
        }
    elif data.get("emailGenerativeAnswerAIAgentConfiguration") is not None:
        import capo_qconnect.types.email_generative_answer_ai_agent_configuration

        return {
            "emailGenerativeAnswerAIAgentConfiguration": capo_qconnect.types.email_generative_answer_ai_agent_configuration.deserialize_json(
                data["emailGenerativeAnswerAIAgentConfiguration"]
            )
        }
    elif data.get("orchestrationAIAgentConfiguration") is not None:
        import capo_qconnect.types.orchestration_ai_agent_configuration

        return {
            "orchestrationAIAgentConfiguration": capo_qconnect.types.orchestration_ai_agent_configuration.deserialize_json(
                data["orchestrationAIAgentConfiguration"]
            )
        }
    elif data.get("noteTakingAIAgentConfiguration") is not None:
        import capo_qconnect.types.note_taking_ai_agent_configuration

        return {
            "noteTakingAIAgentConfiguration": capo_qconnect.types.note_taking_ai_agent_configuration.deserialize_json(
                data["noteTakingAIAgentConfiguration"]
            )
        }
    elif data.get("caseSummarizationAIAgentConfiguration") is not None:
        import capo_qconnect.types.case_summarization_ai_agent_configuration

        return {
            "caseSummarizationAIAgentConfiguration": capo_qconnect.types.case_summarization_ai_agent_configuration.deserialize_json(
                data["caseSummarizationAIAgentConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AIAgentConfiguration: no recognized variant key")


def redact_sensitive(value: AIAgentConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "answerRecommendationAIAgentConfiguration" in value:
        import capo_qconnect.types.answer_recommendation_ai_agent_configuration

        out["answerRecommendationAIAgentConfiguration"] = (
            capo_qconnect.types.answer_recommendation_ai_agent_configuration.redact_sensitive(
                value["answerRecommendationAIAgentConfiguration"]
            )
        )
    if "orchestrationAIAgentConfiguration" in value:
        import capo_qconnect.types.orchestration_ai_agent_configuration

        out["orchestrationAIAgentConfiguration"] = (
            capo_qconnect.types.orchestration_ai_agent_configuration.redact_sensitive(
                value["orchestrationAIAgentConfiguration"]
            )
        )
    return out
