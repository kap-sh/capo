"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningFinding``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding


class GuardrailAutomatedReasoningFindingValidMember(TypedDict, closed=True):
    valid: "capo_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding.GuardrailAutomatedReasoningValidFinding"


class GuardrailAutomatedReasoningFindingInvalidMember(TypedDict, closed=True):
    invalid: "capo_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding.GuardrailAutomatedReasoningInvalidFinding"


class GuardrailAutomatedReasoningFindingSatisfiableMember(TypedDict, closed=True):
    satisfiable: "capo_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding.GuardrailAutomatedReasoningSatisfiableFinding"


class GuardrailAutomatedReasoningFindingImpossibleMember(TypedDict, closed=True):
    impossible: "capo_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding.GuardrailAutomatedReasoningImpossibleFinding"


class GuardrailAutomatedReasoningFindingTranslationAmbiguousMember(
    TypedDict, closed=True
):
    translationAmbiguous: "capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding.GuardrailAutomatedReasoningTranslationAmbiguousFinding"


class GuardrailAutomatedReasoningFindingTooComplexMember(TypedDict, closed=True):
    tooComplex: "capo_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding.GuardrailAutomatedReasoningTooComplexFinding"


class GuardrailAutomatedReasoningFindingNoTranslationsMember(TypedDict, closed=True):
    noTranslations: "capo_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding.GuardrailAutomatedReasoningNoTranslationsFinding"


GuardrailAutomatedReasoningFinding: TypeAlias = (
    GuardrailAutomatedReasoningFindingValidMember
    | GuardrailAutomatedReasoningFindingInvalidMember
    | GuardrailAutomatedReasoningFindingSatisfiableMember
    | GuardrailAutomatedReasoningFindingImpossibleMember
    | GuardrailAutomatedReasoningFindingTranslationAmbiguousMember
    | GuardrailAutomatedReasoningFindingTooComplexMember
    | GuardrailAutomatedReasoningFindingNoTranslationsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningFinding) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GuardrailAutomatedReasoningFinding: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "valid" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding

        return {
            "valid": capo_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding.serialize_json(
                value["valid"]
            )
        }
    elif "invalid" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding

        return {
            "invalid": capo_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding.serialize_json(
                value["invalid"]
            )
        }
    elif "satisfiable" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding

        return {
            "satisfiable": capo_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding.serialize_json(
                value["satisfiable"]
            )
        }
    elif "impossible" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding

        return {
            "impossible": capo_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding.serialize_json(
                value["impossible"]
            )
        }
    elif "translationAmbiguous" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding

        return {
            "translationAmbiguous": capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding.serialize_json(
                value["translationAmbiguous"]
            )
        }
    elif "tooComplex" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding

        return {
            "tooComplex": capo_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding.serialize_json(
                value["tooComplex"]
            )
        }
    elif "noTranslations" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding

        return {
            "noTranslations": capo_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding.serialize_json(
                value["noTranslations"]
            )
        }
    else:
        raise SerializationError(
            "GuardrailAutomatedReasoningFinding: no variant present"
        )


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningFinding:
    if data.get("valid") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding

        return {
            "valid": capo_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding.deserialize_json(
                data["valid"]
            )
        }
    elif data.get("invalid") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding

        return {
            "invalid": capo_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding.deserialize_json(
                data["invalid"]
            )
        }
    elif data.get("satisfiable") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding

        return {
            "satisfiable": capo_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding.deserialize_json(
                data["satisfiable"]
            )
        }
    elif data.get("impossible") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding

        return {
            "impossible": capo_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding.deserialize_json(
                data["impossible"]
            )
        }
    elif data.get("translationAmbiguous") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding

        return {
            "translationAmbiguous": capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding.deserialize_json(
                data["translationAmbiguous"]
            )
        }
    elif data.get("tooComplex") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding

        return {
            "tooComplex": capo_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding.deserialize_json(
                data["tooComplex"]
            )
        }
    elif data.get("noTranslations") is not None:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding

        return {
            "noTranslations": capo_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding.deserialize_json(
                data["noTranslations"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "GuardrailAutomatedReasoningFinding: no recognized variant key"
        )


def redact_sensitive(value: GuardrailAutomatedReasoningFinding) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "valid" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding

        out["valid"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding.redact_sensitive(
                value["valid"]
            )
        )
    if "invalid" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding

        out["invalid"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding.redact_sensitive(
                value["invalid"]
            )
        )
    if "satisfiable" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding

        out["satisfiable"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding.redact_sensitive(
                value["satisfiable"]
            )
        )
    if "impossible" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding

        out["impossible"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding.redact_sensitive(
                value["impossible"]
            )
        )
    if "translationAmbiguous" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding

        out["translationAmbiguous"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding.redact_sensitive(
                value["translationAmbiguous"]
            )
        )
    return out
