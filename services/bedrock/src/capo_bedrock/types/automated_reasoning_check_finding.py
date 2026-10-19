"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckFinding``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_impossible_finding
    import capo_bedrock.types.automated_reasoning_check_invalid_finding
    import capo_bedrock.types.automated_reasoning_check_no_translations_finding
    import capo_bedrock.types.automated_reasoning_check_satisfiable_finding
    import capo_bedrock.types.automated_reasoning_check_too_complex_finding
    import capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding
    import capo_bedrock.types.automated_reasoning_check_valid_finding


class _AutomatedReasoningCheckFinding_valid(TypedDict, closed=True):
    valid: "capo_bedrock.types.automated_reasoning_check_valid_finding.AutomatedReasoningCheckValidFinding"


class _AutomatedReasoningCheckFinding_invalid(TypedDict, closed=True):
    invalid: "capo_bedrock.types.automated_reasoning_check_invalid_finding.AutomatedReasoningCheckInvalidFinding"


class _AutomatedReasoningCheckFinding_satisfiable(TypedDict, closed=True):
    satisfiable: "capo_bedrock.types.automated_reasoning_check_satisfiable_finding.AutomatedReasoningCheckSatisfiableFinding"


class _AutomatedReasoningCheckFinding_impossible(TypedDict, closed=True):
    impossible: "capo_bedrock.types.automated_reasoning_check_impossible_finding.AutomatedReasoningCheckImpossibleFinding"


class _AutomatedReasoningCheckFinding_translationAmbiguous(TypedDict, closed=True):
    translationAmbiguous: "capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding.AutomatedReasoningCheckTranslationAmbiguousFinding"


class _AutomatedReasoningCheckFinding_tooComplex(TypedDict, closed=True):
    tooComplex: "capo_bedrock.types.automated_reasoning_check_too_complex_finding.AutomatedReasoningCheckTooComplexFinding"


class _AutomatedReasoningCheckFinding_noTranslations(TypedDict, closed=True):
    noTranslations: "capo_bedrock.types.automated_reasoning_check_no_translations_finding.AutomatedReasoningCheckNoTranslationsFinding"


AutomatedReasoningCheckFinding: TypeAlias = (
    _AutomatedReasoningCheckFinding_valid
    | _AutomatedReasoningCheckFinding_invalid
    | _AutomatedReasoningCheckFinding_satisfiable
    | _AutomatedReasoningCheckFinding_impossible
    | _AutomatedReasoningCheckFinding_translationAmbiguous
    | _AutomatedReasoningCheckFinding_tooComplex
    | _AutomatedReasoningCheckFinding_noTranslations
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckFinding) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AutomatedReasoningCheckFinding: cannot serialize unknown variant {value.name!r}"
        )
    elif "valid" in value:
        import capo_bedrock.types.automated_reasoning_check_valid_finding

        return {
            "valid": capo_bedrock.types.automated_reasoning_check_valid_finding.serialize_json(
                value["valid"]
            )
        }
    elif "invalid" in value:
        import capo_bedrock.types.automated_reasoning_check_invalid_finding

        return {
            "invalid": capo_bedrock.types.automated_reasoning_check_invalid_finding.serialize_json(
                value["invalid"]
            )
        }
    elif "satisfiable" in value:
        import capo_bedrock.types.automated_reasoning_check_satisfiable_finding

        return {
            "satisfiable": capo_bedrock.types.automated_reasoning_check_satisfiable_finding.serialize_json(
                value["satisfiable"]
            )
        }
    elif "impossible" in value:
        import capo_bedrock.types.automated_reasoning_check_impossible_finding

        return {
            "impossible": capo_bedrock.types.automated_reasoning_check_impossible_finding.serialize_json(
                value["impossible"]
            )
        }
    elif "translationAmbiguous" in value:
        import capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding

        return {
            "translationAmbiguous": capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding.serialize_json(
                value["translationAmbiguous"]
            )
        }
    elif "tooComplex" in value:
        import capo_bedrock.types.automated_reasoning_check_too_complex_finding

        return {
            "tooComplex": capo_bedrock.types.automated_reasoning_check_too_complex_finding.serialize_json(
                value["tooComplex"]
            )
        }
    elif "noTranslations" in value:
        import capo_bedrock.types.automated_reasoning_check_no_translations_finding

        return {
            "noTranslations": capo_bedrock.types.automated_reasoning_check_no_translations_finding.serialize_json(
                value["noTranslations"]
            )
        }
    else:
        raise SerializationError("AutomatedReasoningCheckFinding: no variant present")


def deserialize_json(data: dict) -> AutomatedReasoningCheckFinding:
    if data.get("valid") is not None:
        import capo_bedrock.types.automated_reasoning_check_valid_finding

        return {
            "valid": capo_bedrock.types.automated_reasoning_check_valid_finding.deserialize_json(
                data["valid"]
            )
        }
    elif data.get("invalid") is not None:
        import capo_bedrock.types.automated_reasoning_check_invalid_finding

        return {
            "invalid": capo_bedrock.types.automated_reasoning_check_invalid_finding.deserialize_json(
                data["invalid"]
            )
        }
    elif data.get("satisfiable") is not None:
        import capo_bedrock.types.automated_reasoning_check_satisfiable_finding

        return {
            "satisfiable": capo_bedrock.types.automated_reasoning_check_satisfiable_finding.deserialize_json(
                data["satisfiable"]
            )
        }
    elif data.get("impossible") is not None:
        import capo_bedrock.types.automated_reasoning_check_impossible_finding

        return {
            "impossible": capo_bedrock.types.automated_reasoning_check_impossible_finding.deserialize_json(
                data["impossible"]
            )
        }
    elif data.get("translationAmbiguous") is not None:
        import capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding

        return {
            "translationAmbiguous": capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding.deserialize_json(
                data["translationAmbiguous"]
            )
        }
    elif data.get("tooComplex") is not None:
        import capo_bedrock.types.automated_reasoning_check_too_complex_finding

        return {
            "tooComplex": capo_bedrock.types.automated_reasoning_check_too_complex_finding.deserialize_json(
                data["tooComplex"]
            )
        }
    elif data.get("noTranslations") is not None:
        import capo_bedrock.types.automated_reasoning_check_no_translations_finding

        return {
            "noTranslations": capo_bedrock.types.automated_reasoning_check_no_translations_finding.deserialize_json(
                data["noTranslations"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "AutomatedReasoningCheckFinding: no recognized variant key"
        )


def redact_sensitive(
    value: AutomatedReasoningCheckFinding,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "valid" in value:
        import capo_bedrock.types.automated_reasoning_check_valid_finding

        out["valid"] = (
            capo_bedrock.types.automated_reasoning_check_valid_finding.redact_sensitive(
                value["valid"]
            )
        )
    if "invalid" in value:
        import capo_bedrock.types.automated_reasoning_check_invalid_finding

        out["invalid"] = (
            capo_bedrock.types.automated_reasoning_check_invalid_finding.redact_sensitive(
                value["invalid"]
            )
        )
    if "satisfiable" in value:
        import capo_bedrock.types.automated_reasoning_check_satisfiable_finding

        out["satisfiable"] = (
            capo_bedrock.types.automated_reasoning_check_satisfiable_finding.redact_sensitive(
                value["satisfiable"]
            )
        )
    if "impossible" in value:
        import capo_bedrock.types.automated_reasoning_check_impossible_finding

        out["impossible"] = (
            capo_bedrock.types.automated_reasoning_check_impossible_finding.redact_sensitive(
                value["impossible"]
            )
        )
    if "translationAmbiguous" in value:
        import capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding

        out["translationAmbiguous"] = (
            capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding.redact_sensitive(
                value["translationAmbiguous"]
            )
        )
    return out
