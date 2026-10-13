"""Generated from Smithy shape ``com.amazonaws.bedrock#GetGuardrailResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_arn
    import capo_bedrock.types.guardrail_automated_reasoning_policy
    import capo_bedrock.types.guardrail_blocked_messaging
    import capo_bedrock.types.guardrail_content_policy
    import capo_bedrock.types.guardrail_contextual_grounding_policy
    import capo_bedrock.types.guardrail_cross_region_details
    import capo_bedrock.types.guardrail_description
    import capo_bedrock.types.guardrail_failure_recommendations
    import capo_bedrock.types.guardrail_id
    import capo_bedrock.types.guardrail_name
    import capo_bedrock.types.guardrail_sensitive_information_policy
    import capo_bedrock.types.guardrail_status
    import capo_bedrock.types.guardrail_status_reasons
    import capo_bedrock.types.guardrail_topic_policy
    import capo_bedrock.types.guardrail_version
    import capo_bedrock.types.guardrail_word_policy
    import capo_bedrock.types.kms_key_arn
    import capo_bedrock.types.timestamp


class GetGuardrailResponse(TypedDict, closed=True):
    name: "capo_bedrock.types.guardrail_name.GuardrailName"
    """<p>The name of the guardrail.</p>"""
    description: NotRequired[
        "capo_bedrock.types.guardrail_description.GuardrailDescription"
    ]
    """<p>The description of the guardrail.</p>"""
    guardrail_id: "capo_bedrock.types.guardrail_id.GuardrailId"
    """<p>The unique identifier of the guardrail.</p>"""
    guardrail_arn: "capo_bedrock.types.guardrail_arn.GuardrailArn"
    """<p>The ARN of the guardrail.</p>"""
    version: "capo_bedrock.types.guardrail_version.GuardrailVersion"
    """<p>The version of the guardrail.</p>"""
    status: "capo_bedrock.types.guardrail_status.GuardrailStatus"
    """<p>The status of the guardrail.</p>"""
    topic_policy: NotRequired[
        "capo_bedrock.types.guardrail_topic_policy.GuardrailTopicPolicy"
    ]
    """<p>The topic policy that was configured for the guardrail.</p>"""
    content_policy: NotRequired[
        "capo_bedrock.types.guardrail_content_policy.GuardrailContentPolicy"
    ]
    """<p>The content policy that was configured for the guardrail.</p>"""
    word_policy: NotRequired[
        "capo_bedrock.types.guardrail_word_policy.GuardrailWordPolicy"
    ]
    """<p>The word policy that was configured for the guardrail.</p>"""
    sensitive_information_policy: NotRequired[
        "capo_bedrock.types.guardrail_sensitive_information_policy.GuardrailSensitiveInformationPolicy"
    ]
    """<p>The sensitive information policy that was configured for the guardrail.</p>"""
    contextual_grounding_policy: NotRequired[
        "capo_bedrock.types.guardrail_contextual_grounding_policy.GuardrailContextualGroundingPolicy"
    ]
    """<p>The contextual grounding policy used in the guardrail.</p>"""
    automated_reasoning_policy: NotRequired[
        "capo_bedrock.types.guardrail_automated_reasoning_policy.GuardrailAutomatedReasoningPolicy"
    ]
    """<p>The current Automated Reasoning policy configuration for the guardrail, if any is configured.</p>"""
    cross_region_details: NotRequired[
        "capo_bedrock.types.guardrail_cross_region_details.GuardrailCrossRegionDetails"
    ]
    """<p>Details about the system-defined guardrail profile that you're using with your guardrail, including the guardrail profile ID and Amazon Resource Name (ARN).</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The date and time at which the guardrail was created.</p>"""
    updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The date and time at which the guardrail was updated.</p>"""
    status_reasons: NotRequired[
        "capo_bedrock.types.guardrail_status_reasons.GuardrailStatusReasons"
    ]
    """<p>Appears if the <code>status</code> is <code>FAILED</code>. A list of reasons for why the guardrail failed to be created, updated, versioned, or deleted.</p>"""
    failure_recommendations: NotRequired[
        "capo_bedrock.types.guardrail_failure_recommendations.GuardrailFailureRecommendations"
    ]
    """<p>Appears if the <code>status</code> of the guardrail is <code>FAILED</code>. A list of recommendations to carry out before retrying the request.</p>"""
    blocked_input_messaging: (
        "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging"
    )
    """<p>The message that the guardrail returns when it blocks a prompt.</p>"""
    blocked_outputs_messaging: (
        "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging"
    )
    """<p>The message that the guardrail returns when it blocks a model response.</p>"""
    kms_key_arn: NotRequired["capo_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key that encrypts the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGuardrailResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["guardrailId"] = value["guardrail_id"]
    out["guardrailArn"] = value["guardrail_arn"]
    out["version"] = value["version"]
    import capo_bedrock.types.guardrail_status

    out["status"] = capo_bedrock.types.guardrail_status.serialize_json(value["status"])
    if "topic_policy" in value:
        import capo_bedrock.types.guardrail_topic_policy

        out["topicPolicy"] = capo_bedrock.types.guardrail_topic_policy.serialize_json(
            value["topic_policy"]
        )
    if "content_policy" in value:
        import capo_bedrock.types.guardrail_content_policy

        out["contentPolicy"] = (
            capo_bedrock.types.guardrail_content_policy.serialize_json(
                value["content_policy"]
            )
        )
    if "word_policy" in value:
        import capo_bedrock.types.guardrail_word_policy

        out["wordPolicy"] = capo_bedrock.types.guardrail_word_policy.serialize_json(
            value["word_policy"]
        )
    if "sensitive_information_policy" in value:
        import capo_bedrock.types.guardrail_sensitive_information_policy

        out["sensitiveInformationPolicy"] = (
            capo_bedrock.types.guardrail_sensitive_information_policy.serialize_json(
                value["sensitive_information_policy"]
            )
        )
    if "contextual_grounding_policy" in value:
        import capo_bedrock.types.guardrail_contextual_grounding_policy

        out["contextualGroundingPolicy"] = (
            capo_bedrock.types.guardrail_contextual_grounding_policy.serialize_json(
                value["contextual_grounding_policy"]
            )
        )
    if "automated_reasoning_policy" in value:
        import capo_bedrock.types.guardrail_automated_reasoning_policy

        out["automatedReasoningPolicy"] = (
            capo_bedrock.types.guardrail_automated_reasoning_policy.serialize_json(
                value["automated_reasoning_policy"]
            )
        )
    if "cross_region_details" in value:
        import capo_bedrock.types.guardrail_cross_region_details

        out["crossRegionDetails"] = (
            capo_bedrock.types.guardrail_cross_region_details.serialize_json(
                value["cross_region_details"]
            )
        )
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    import capo_bedrock.types.timestamp

    out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(value["updated_at"])
    if "status_reasons" in value:
        import capo_bedrock.types.guardrail_status_reasons

        out["statusReasons"] = (
            capo_bedrock.types.guardrail_status_reasons.serialize_json(
                value["status_reasons"]
            )
        )
    if "failure_recommendations" in value:
        import capo_bedrock.types.guardrail_failure_recommendations

        out["failureRecommendations"] = (
            capo_bedrock.types.guardrail_failure_recommendations.serialize_json(
                value["failure_recommendations"]
            )
        )
    out["blockedInputMessaging"] = value["blocked_input_messaging"]
    out["blockedOutputsMessaging"] = value["blocked_outputs_messaging"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetGuardrailResponse:
    out: GetGuardrailResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetGuardrailResponse.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("guardrailId") is not None:
        out["guardrail_id"] = data["guardrailId"]
    else:
        raise DeserializationError("GetGuardrailResponse.guardrail_id required")
    if data.get("guardrailArn") is not None:
        out["guardrail_arn"] = data["guardrailArn"]
    else:
        raise DeserializationError("GetGuardrailResponse.guardrail_arn required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("GetGuardrailResponse.version required")
    if data.get("status") is not None:
        import capo_bedrock.types.guardrail_status

        out["status"] = capo_bedrock.types.guardrail_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetGuardrailResponse.status required")
    if data.get("topicPolicy") is not None:
        import capo_bedrock.types.guardrail_topic_policy

        out["topic_policy"] = (
            capo_bedrock.types.guardrail_topic_policy.deserialize_json(
                data["topicPolicy"]
            )
        )
    if data.get("contentPolicy") is not None:
        import capo_bedrock.types.guardrail_content_policy

        out["content_policy"] = (
            capo_bedrock.types.guardrail_content_policy.deserialize_json(
                data["contentPolicy"]
            )
        )
    if data.get("wordPolicy") is not None:
        import capo_bedrock.types.guardrail_word_policy

        out["word_policy"] = capo_bedrock.types.guardrail_word_policy.deserialize_json(
            data["wordPolicy"]
        )
    if data.get("sensitiveInformationPolicy") is not None:
        import capo_bedrock.types.guardrail_sensitive_information_policy

        out["sensitive_information_policy"] = (
            capo_bedrock.types.guardrail_sensitive_information_policy.deserialize_json(
                data["sensitiveInformationPolicy"]
            )
        )
    if data.get("contextualGroundingPolicy") is not None:
        import capo_bedrock.types.guardrail_contextual_grounding_policy

        out["contextual_grounding_policy"] = (
            capo_bedrock.types.guardrail_contextual_grounding_policy.deserialize_json(
                data["contextualGroundingPolicy"]
            )
        )
    if data.get("automatedReasoningPolicy") is not None:
        import capo_bedrock.types.guardrail_automated_reasoning_policy

        out["automated_reasoning_policy"] = (
            capo_bedrock.types.guardrail_automated_reasoning_policy.deserialize_json(
                data["automatedReasoningPolicy"]
            )
        )
    if data.get("crossRegionDetails") is not None:
        import capo_bedrock.types.guardrail_cross_region_details

        out["cross_region_details"] = (
            capo_bedrock.types.guardrail_cross_region_details.deserialize_json(
                data["crossRegionDetails"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetGuardrailResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetGuardrailResponse.updated_at required")
    if data.get("statusReasons") is not None:
        import capo_bedrock.types.guardrail_status_reasons

        out["status_reasons"] = (
            capo_bedrock.types.guardrail_status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    if data.get("failureRecommendations") is not None:
        import capo_bedrock.types.guardrail_failure_recommendations

        out["failure_recommendations"] = (
            capo_bedrock.types.guardrail_failure_recommendations.deserialize_json(
                data["failureRecommendations"]
            )
        )
    if data.get("blockedInputMessaging") is not None:
        out["blocked_input_messaging"] = data["blockedInputMessaging"]
    else:
        raise DeserializationError(
            "GetGuardrailResponse.blocked_input_messaging required"
        )
    if data.get("blockedOutputsMessaging") is not None:
        out["blocked_outputs_messaging"] = data["blockedOutputsMessaging"]
    else:
        raise DeserializationError(
            "GetGuardrailResponse.blocked_outputs_messaging required"
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out


def redact_sensitive(value: GetGuardrailResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "topic_policy" in value:
        import capo_bedrock.types.guardrail_topic_policy

        out["topic_policy"] = (
            capo_bedrock.types.guardrail_topic_policy.redact_sensitive(
                value["topic_policy"]
            )
        )
    if "content_policy" in value:
        import capo_bedrock.types.guardrail_content_policy

        out["content_policy"] = (
            capo_bedrock.types.guardrail_content_policy.redact_sensitive(
                value["content_policy"]
            )
        )
    if "word_policy" in value:
        import capo_bedrock.types.guardrail_word_policy

        out["word_policy"] = capo_bedrock.types.guardrail_word_policy.redact_sensitive(
            value["word_policy"]
        )
    if "contextual_grounding_policy" in value:
        import capo_bedrock.types.guardrail_contextual_grounding_policy

        out["contextual_grounding_policy"] = (
            capo_bedrock.types.guardrail_contextual_grounding_policy.redact_sensitive(
                value["contextual_grounding_policy"]
            )
        )
    if "status_reasons" in value:
        import capo_bedrock.types.guardrail_status_reasons

        out["status_reasons"] = (
            capo_bedrock.types.guardrail_status_reasons.redact_sensitive(
                value["status_reasons"]
            )
        )
    if "failure_recommendations" in value:
        import capo_bedrock.types.guardrail_failure_recommendations

        out["failure_recommendations"] = (
            capo_bedrock.types.guardrail_failure_recommendations.redact_sensitive(
                value["failure_recommendations"]
            )
        )
    if "blocked_input_messaging" in value:
        out["blocked_input_messaging"] = "*** Sensitive Data Redacted ***"
    if "blocked_outputs_messaging" in value:
        out["blocked_outputs_messaging"] = "*** Sensitive Data Redacted ***"
    return out
