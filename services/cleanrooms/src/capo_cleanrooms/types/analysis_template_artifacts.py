"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateArtifacts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_artifact
    import capo_cleanrooms.types.analysis_template_artifact_list
    import capo_cleanrooms.types.role_arn


class AnalysisTemplateArtifacts(TypedDict, closed=True):
    entry_point: (
        "capo_cleanrooms.types.analysis_template_artifact.AnalysisTemplateArtifact"
    )
    """<p> The entry point for the analysis template artifacts.</p>"""
    additional_artifacts: NotRequired[
        "capo_cleanrooms.types.analysis_template_artifact_list.AnalysisTemplateArtifactList"
    ]
    """<p> Additional artifacts for the analysis template.</p>"""
    role_arn: "capo_cleanrooms.types.role_arn.RoleArn"
    """<p> The role ARN for the analysis template artifacts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateArtifacts) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_template_artifact

    out["entryPoint"] = capo_cleanrooms.types.analysis_template_artifact.serialize_json(
        value["entry_point"]
    )
    if "additional_artifacts" in value:
        import capo_cleanrooms.types.analysis_template_artifact_list

        out["additionalArtifacts"] = (
            capo_cleanrooms.types.analysis_template_artifact_list.serialize_json(
                value["additional_artifacts"]
            )
        )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AnalysisTemplateArtifacts:
    out: AnalysisTemplateArtifacts = {}  # type: ignore[typeddict-item]
    if data.get("entryPoint") is not None:
        import capo_cleanrooms.types.analysis_template_artifact

        out["entry_point"] = (
            capo_cleanrooms.types.analysis_template_artifact.deserialize_json(
                data["entryPoint"]
            )
        )
    else:
        raise DeserializationError("AnalysisTemplateArtifacts.entry_point required")
    if data.get("additionalArtifacts") is not None:
        import capo_cleanrooms.types.analysis_template_artifact_list

        out["additional_artifacts"] = (
            capo_cleanrooms.types.analysis_template_artifact_list.deserialize_json(
                data["additionalArtifacts"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
