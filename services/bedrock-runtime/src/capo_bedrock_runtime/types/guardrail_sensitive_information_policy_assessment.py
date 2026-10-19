"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailSensitiveInformationPolicyAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_pii_entity_filter_list
    import capo_bedrock_runtime.types.guardrail_regex_filter_list


class GuardrailSensitiveInformationPolicyAssessment(TypedDict, closed=True):
    pii_entities: "capo_bedrock_runtime.types.guardrail_pii_entity_filter_list.GuardrailPiiEntityFilterList"
    """<p>The PII entities in the assessment.</p>"""
    regexes: "capo_bedrock_runtime.types.guardrail_regex_filter_list.GuardrailRegexFilterList"
    """<p>The regex queries in the assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSensitiveInformationPolicyAssessment) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_pii_entity_filter_list

    out["piiEntities"] = (
        capo_bedrock_runtime.types.guardrail_pii_entity_filter_list.serialize_json(
            value["pii_entities"]
        )
    )
    import capo_bedrock_runtime.types.guardrail_regex_filter_list

    out["regexes"] = (
        capo_bedrock_runtime.types.guardrail_regex_filter_list.serialize_json(
            value["regexes"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailSensitiveInformationPolicyAssessment:
    out: GuardrailSensitiveInformationPolicyAssessment = {}  # type: ignore[typeddict-item]
    if data.get("piiEntities") is not None:
        import capo_bedrock_runtime.types.guardrail_pii_entity_filter_list

        out["pii_entities"] = (
            capo_bedrock_runtime.types.guardrail_pii_entity_filter_list.deserialize_json(
                data["piiEntities"]
            )
        )
    else:
        out["pii_entities"] = []
    if data.get("regexes") is not None:
        import capo_bedrock_runtime.types.guardrail_regex_filter_list

        out["regexes"] = (
            capo_bedrock_runtime.types.guardrail_regex_filter_list.deserialize_json(
                data["regexes"]
            )
        )
    else:
        out["regexes"] = []
    return out
