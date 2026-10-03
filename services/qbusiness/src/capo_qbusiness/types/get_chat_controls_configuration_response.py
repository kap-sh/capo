"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetChatControlsConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.applied_creator_mode_configuration
    import capo_qbusiness.types.applied_orchestration_configuration
    import capo_qbusiness.types.blocked_phrases_configuration
    import capo_qbusiness.types.hallucination_reduction_configuration
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.response_scope
    import capo_qbusiness.types.topic_configurations


class GetChatControlsConfigurationResponse(TypedDict, closed=True):
    response_scope: NotRequired["capo_qbusiness.types.response_scope.ResponseScope"]
    """<p>The response scope configured for a Amazon Q Business application. This determines whether your application uses its retrieval augmented generation (RAG) system to generate answers only from your enterprise data, or also uses the large language models (LLM) knowledge to respons to end user questions in chat.</p>"""
    orchestration_configuration: NotRequired[
        "capo_qbusiness.types.applied_orchestration_configuration.AppliedOrchestrationConfiguration"
    ]
    """<p> The chat response orchestration settings for your application.</p> <note> <p>Chat orchestration is optimized to work for English language content. For more details on language support in Amazon Q Business, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-languages.html">Supported languages</a>.</p> </note>"""
    blocked_phrases: NotRequired[
        "capo_qbusiness.types.blocked_phrases_configuration.BlockedPhrasesConfiguration"
    ]
    """<p>The phrases blocked from chat by your chat control configuration.</p>"""
    topic_configurations: NotRequired[
        "capo_qbusiness.types.topic_configurations.TopicConfigurations"
    ]
    """<p>The topic specific controls configured for a Amazon Q Business application.</p>"""
    creator_mode_configuration: NotRequired[
        "capo_qbusiness.types.applied_creator_mode_configuration.AppliedCreatorModeConfiguration"
    ]
    """<p>The configuration details for <code>CREATOR_MODE</code>.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business chat controls configured.</p>"""
    hallucination_reduction_configuration: NotRequired[
        "capo_qbusiness.types.hallucination_reduction_configuration.HallucinationReductionConfiguration"
    ]
    """<p> The hallucination reduction settings for your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChatControlsConfigurationResponse) -> dict:
    out: dict = {}
    if "response_scope" in value:
        import capo_qbusiness.types.response_scope

        out["responseScope"] = capo_qbusiness.types.response_scope.serialize_json(
            value["response_scope"]
        )
    if "orchestration_configuration" in value:
        import capo_qbusiness.types.applied_orchestration_configuration

        out["orchestrationConfiguration"] = (
            capo_qbusiness.types.applied_orchestration_configuration.serialize_json(
                value["orchestration_configuration"]
            )
        )
    if "blocked_phrases" in value:
        import capo_qbusiness.types.blocked_phrases_configuration

        out["blockedPhrases"] = (
            capo_qbusiness.types.blocked_phrases_configuration.serialize_json(
                value["blocked_phrases"]
            )
        )
    if "topic_configurations" in value:
        import capo_qbusiness.types.topic_configurations

        out["topicConfigurations"] = (
            capo_qbusiness.types.topic_configurations.serialize_json(
                value["topic_configurations"]
            )
        )
    if "creator_mode_configuration" in value:
        import capo_qbusiness.types.applied_creator_mode_configuration

        out["creatorModeConfiguration"] = (
            capo_qbusiness.types.applied_creator_mode_configuration.serialize_json(
                value["creator_mode_configuration"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "hallucination_reduction_configuration" in value:
        import capo_qbusiness.types.hallucination_reduction_configuration

        out["hallucinationReductionConfiguration"] = (
            capo_qbusiness.types.hallucination_reduction_configuration.serialize_json(
                value["hallucination_reduction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetChatControlsConfigurationResponse:
    out: GetChatControlsConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("responseScope") is not None:
        import capo_qbusiness.types.response_scope

        out["response_scope"] = capo_qbusiness.types.response_scope.deserialize_json(
            data["responseScope"]
        )
    if data.get("orchestrationConfiguration") is not None:
        import capo_qbusiness.types.applied_orchestration_configuration

        out["orchestration_configuration"] = (
            capo_qbusiness.types.applied_orchestration_configuration.deserialize_json(
                data["orchestrationConfiguration"]
            )
        )
    if data.get("blockedPhrases") is not None:
        import capo_qbusiness.types.blocked_phrases_configuration

        out["blocked_phrases"] = (
            capo_qbusiness.types.blocked_phrases_configuration.deserialize_json(
                data["blockedPhrases"]
            )
        )
    if data.get("topicConfigurations") is not None:
        import capo_qbusiness.types.topic_configurations

        out["topic_configurations"] = (
            capo_qbusiness.types.topic_configurations.deserialize_json(
                data["topicConfigurations"]
            )
        )
    if data.get("creatorModeConfiguration") is not None:
        import capo_qbusiness.types.applied_creator_mode_configuration

        out["creator_mode_configuration"] = (
            capo_qbusiness.types.applied_creator_mode_configuration.deserialize_json(
                data["creatorModeConfiguration"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("hallucinationReductionConfiguration") is not None:
        import capo_qbusiness.types.hallucination_reduction_configuration

        out["hallucination_reduction_configuration"] = (
            capo_qbusiness.types.hallucination_reduction_configuration.deserialize_json(
                data["hallucinationReductionConfiguration"]
            )
        )
    return out
