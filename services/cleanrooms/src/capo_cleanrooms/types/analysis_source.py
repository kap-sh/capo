"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_artifacts
    import capo_cleanrooms.types.analysis_template_text


class _AnalysisSource_text(TypedDict, closed=True):
    text: "capo_cleanrooms.types.analysis_template_text.AnalysisTemplateText"


class _AnalysisSource_artifacts(TypedDict, closed=True):
    artifacts: (
        "capo_cleanrooms.types.analysis_template_artifacts.AnalysisTemplateArtifacts"
    )


AnalysisSource: TypeAlias = _AnalysisSource_text | _AnalysisSource_artifacts


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSource) -> dict:
    if "text" in value:
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
        raise DeserializationError("AnalysisSource: no recognized variant key")


def redact_sensitive(value: AnalysisSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
