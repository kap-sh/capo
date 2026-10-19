"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckTranslation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_input_text_reference_list
    import capo_bedrock.types.automated_reasoning_check_translation_confidence
    import capo_bedrock.types.automated_reasoning_logic_statement_list


class AutomatedReasoningCheckTranslation(TypedDict, closed=True):
    premises: NotRequired[
        "capo_bedrock.types.automated_reasoning_logic_statement_list.AutomatedReasoningLogicStatementList"
    ]
    """<p>The logical statements that serve as the foundation or assumptions for the claims.</p>"""
    claims: "capo_bedrock.types.automated_reasoning_logic_statement_list.AutomatedReasoningLogicStatementList"
    """<p>The logical statements that are being validated against the premises and policy rules.</p>"""
    untranslated_premises: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_input_text_reference_list.AutomatedReasoningCheckInputTextReferenceList"
    ]
    """<p>References to portions of the original input text that correspond to the premises but could not be fully translated.</p>"""
    untranslated_claims: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_input_text_reference_list.AutomatedReasoningCheckInputTextReferenceList"
    ]
    """<p>References to portions of the original input text that correspond to the claims but could not be fully translated.</p>"""
    confidence: "capo_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
    """<p>A confidence score between 0 and 1 indicating how certain the system is about the logical translation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckTranslation) -> dict:
    out: dict = {}
    if "premises" in value:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["premises"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.serialize_json(
                value["premises"]
            )
        )
    import capo_bedrock.types.automated_reasoning_logic_statement_list

    out["claims"] = (
        capo_bedrock.types.automated_reasoning_logic_statement_list.serialize_json(
            value["claims"]
        )
    )
    if "untranslated_premises" in value:
        import capo_bedrock.types.automated_reasoning_check_input_text_reference_list

        out["untranslatedPremises"] = (
            capo_bedrock.types.automated_reasoning_check_input_text_reference_list.serialize_json(
                value["untranslated_premises"]
            )
        )
    if "untranslated_claims" in value:
        import capo_bedrock.types.automated_reasoning_check_input_text_reference_list

        out["untranslatedClaims"] = (
            capo_bedrock.types.automated_reasoning_check_input_text_reference_list.serialize_json(
                value["untranslated_claims"]
            )
        )
    out["confidence"] = (
        "NaN"
        if value["confidence"] != value["confidence"]
        else "Infinity"
        if value["confidence"] == float("inf")
        else "-Infinity"
        if value["confidence"] == float("-inf")
        else value["confidence"]
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckTranslation:
    out: AutomatedReasoningCheckTranslation = {}  # type: ignore[typeddict-item]
    if data.get("premises") is not None:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["premises"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.deserialize_json(
                data["premises"]
            )
        )
    if data.get("claims") is not None:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["claims"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.deserialize_json(
                data["claims"]
            )
        )
    else:
        out["claims"] = []
    if data.get("untranslatedPremises") is not None:
        import capo_bedrock.types.automated_reasoning_check_input_text_reference_list

        out["untranslated_premises"] = (
            capo_bedrock.types.automated_reasoning_check_input_text_reference_list.deserialize_json(
                data["untranslatedPremises"]
            )
        )
    if data.get("untranslatedClaims") is not None:
        import capo_bedrock.types.automated_reasoning_check_input_text_reference_list

        out["untranslated_claims"] = (
            capo_bedrock.types.automated_reasoning_check_input_text_reference_list.deserialize_json(
                data["untranslatedClaims"]
            )
        )
    if data.get("confidence") is not None:
        out["confidence"] = float(data["confidence"])
    else:
        out["confidence"] = 0.0
    return out


def redact_sensitive(value: AutomatedReasoningCheckTranslation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "premises" in value:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["premises"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.redact_sensitive(
                value["premises"]
            )
        )
    if "claims" in value:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["claims"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.redact_sensitive(
                value["claims"]
            )
        )
    if "untranslated_premises" in value:
        import capo_bedrock.types.automated_reasoning_check_input_text_reference_list

        out["untranslated_premises"] = (
            capo_bedrock.types.automated_reasoning_check_input_text_reference_list.redact_sensitive(
                value["untranslated_premises"]
            )
        )
    if "untranslated_claims" in value:
        import capo_bedrock.types.automated_reasoning_check_input_text_reference_list

        out["untranslated_claims"] = (
            capo_bedrock.types.automated_reasoning_check_input_text_reference_list.redact_sensitive(
                value["untranslated_claims"]
            )
        )
    return out
