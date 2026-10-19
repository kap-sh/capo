"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_artifacts
    import capo_cleanrooms.types.analysis_template_text


class _AnalysisSource_text(TypedDict, closed=True):
    text: "capo_cleanrooms.types.analysis_template_text.AnalysisTemplateText"


class _AnalysisSource_artifacts(TypedDict, closed=True):
    artifacts: (
        "capo_cleanrooms.types.analysis_template_artifacts.AnalysisTemplateArtifacts"
    )


AnalysisSource: TypeAlias = (
    _AnalysisSource_text | _AnalysisSource_artifacts | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AnalysisSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "artifacts" in value:
        import capo_cleanrooms.types.analysis_template_artifacts

        return {
            "artifacts": capo_cleanrooms.types.analysis_template_artifacts.serialize_json(
                value["artifacts"]
            )
        }
    else:
        raise SerializationError("AnalysisSource: no variant present")


def deserialize_json(data: dict) -> AnalysisSource:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("artifacts") is not None:
        import capo_cleanrooms.types.analysis_template_artifacts

        return {
            "artifacts": capo_cleanrooms.types.analysis_template_artifacts.deserialize_json(
                data["artifacts"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AnalysisSource: no recognized variant key")


def redact_sensitive(value: AnalysisSource) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
