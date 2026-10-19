"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailPiiEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_pii_entity_type
    import capo_bedrock.types.guardrail_sensitive_information_action


class GuardrailPiiEntity(TypedDict, closed=True):
    type: "capo_bedrock.types.guardrail_pii_entity_type.GuardrailPiiEntityType"
    """<p>The type of PII entity. For example, Social Security Number.</p>"""
    action: "capo_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    """<p>The configured guardrail action when PII entity is detected.</p>"""
    input_action: NotRequired[
        "capo_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    ]
    """<p>The action to take when harmful content is detected in the input. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>ANONYMIZE</code> – Mask the content and replace it with identifier tags.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    output_action: NotRequired[
        "capo_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    ]
    """<p>The action to take when harmful content is detected in the output. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>ANONYMIZE</code> – Mask the content and replace it with identifier tags.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    input_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""
    output_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntity) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_pii_entity_type

    out["type"] = capo_bedrock.types.guardrail_pii_entity_type.serialize_json(
        value["type"]
    )
    import capo_bedrock.types.guardrail_sensitive_information_action

    out["action"] = (
        capo_bedrock.types.guardrail_sensitive_information_action.serialize_json(
            value["action"]
        )
    )
    if "input_action" in value:
        import capo_bedrock.types.guardrail_sensitive_information_action

        out["inputAction"] = (
            capo_bedrock.types.guardrail_sensitive_information_action.serialize_json(
                value["input_action"]
            )
        )
    if "output_action" in value:
        import capo_bedrock.types.guardrail_sensitive_information_action

        out["outputAction"] = (
            capo_bedrock.types.guardrail_sensitive_information_action.serialize_json(
                value["output_action"]
            )
        )
    if "input_enabled" in value:
        out["inputEnabled"] = value["input_enabled"]
    if "output_enabled" in value:
        out["outputEnabled"] = value["output_enabled"]
    return out


def deserialize_json(data: dict) -> GuardrailPiiEntity:
    out: GuardrailPiiEntity = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock.types.guardrail_pii_entity_type

        out["type"] = capo_bedrock.types.guardrail_pii_entity_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock.types.guardrail_pii_entity_type.GuardrailPiiEntityType", ""
        )
    if data.get("action") is not None:
        import capo_bedrock.types.guardrail_sensitive_information_action

        out["action"] = (
            capo_bedrock.types.guardrail_sensitive_information_action.deserialize_json(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_bedrock.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction",
            "",
        )
    if data.get("inputAction") is not None:
        import capo_bedrock.types.guardrail_sensitive_information_action

        out["input_action"] = (
            capo_bedrock.types.guardrail_sensitive_information_action.deserialize_json(
                data["inputAction"]
            )
        )
    if data.get("outputAction") is not None:
        import capo_bedrock.types.guardrail_sensitive_information_action

        out["output_action"] = (
            capo_bedrock.types.guardrail_sensitive_information_action.deserialize_json(
                data["outputAction"]
            )
        )
    if data.get("inputEnabled") is not None:
        out["input_enabled"] = data["inputEnabled"]
    if data.get("outputEnabled") is not None:
        out["output_enabled"] = data["outputEnabled"]
    return out
