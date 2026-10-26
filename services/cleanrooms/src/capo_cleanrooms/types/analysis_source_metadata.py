"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisSourceMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_artifact_metadata


class _AnalysisSourceMetadata_artifacts(TypedDict, closed=True):
    artifacts: "capo_cleanrooms.types.analysis_template_artifact_metadata.AnalysisTemplateArtifactMetadata"


AnalysisSourceMetadata: TypeAlias = (
    _AnalysisSourceMetadata_artifacts | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSourceMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AnalysisSourceMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "artifacts" in value:
        import capo_cleanrooms.types.analysis_template_artifact_metadata

        return {
            "artifacts": capo_cleanrooms.types.analysis_template_artifact_metadata.serialize_json(
                value["artifacts"]
            )
        }
    else:
        raise SerializationError("AnalysisSourceMetadata: no variant present")


def deserialize_json(data: dict) -> AnalysisSourceMetadata:
    if data.get("artifacts") is not None:
        import capo_cleanrooms.types.analysis_template_artifact_metadata

        return {
            "artifacts": capo_cleanrooms.types.analysis_template_artifact_metadata.deserialize_json(
                data["artifacts"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AnalysisSourceMetadata: no recognized variant key")
