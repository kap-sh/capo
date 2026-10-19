"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetCollaborationAnalysisTemplateOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.batch_get_collaboration_analysis_template_error_list
    import capo_cleanrooms.types.collaboration_analysis_template_list


class BatchGetCollaborationAnalysisTemplateOutput(TypedDict, closed=True):
    collaboration_analysis_templates: "capo_cleanrooms.types.collaboration_analysis_template_list.CollaborationAnalysisTemplateList"
    """<p>The retrieved list of analysis templates within a collaboration.</p>"""
    errors: "capo_cleanrooms.types.batch_get_collaboration_analysis_template_error_list.BatchGetCollaborationAnalysisTemplateErrorList"
    """<p>Error reasons for collaboration analysis templates that could not be retrieved. One error is returned for every collaboration analysis template that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCollaborationAnalysisTemplateOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.collaboration_analysis_template_list

    out["collaborationAnalysisTemplates"] = (
        capo_cleanrooms.types.collaboration_analysis_template_list.serialize_json(
            value["collaboration_analysis_templates"]
        )
    )
    import capo_cleanrooms.types.batch_get_collaboration_analysis_template_error_list

    out["errors"] = (
        capo_cleanrooms.types.batch_get_collaboration_analysis_template_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetCollaborationAnalysisTemplateOutput:
    out: BatchGetCollaborationAnalysisTemplateOutput = {}  # type: ignore[typeddict-item]
    if data.get("collaborationAnalysisTemplates") is not None:
        import capo_cleanrooms.types.collaboration_analysis_template_list

        out["collaboration_analysis_templates"] = (
            capo_cleanrooms.types.collaboration_analysis_template_list.deserialize_json(
                data["collaborationAnalysisTemplates"]
            )
        )
    else:
        out["collaboration_analysis_templates"] = []
    if data.get("errors") is not None:
        import capo_cleanrooms.types.batch_get_collaboration_analysis_template_error_list

        out["errors"] = (
            capo_cleanrooms.types.batch_get_collaboration_analysis_template_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out


def redact_sensitive(
    value: BatchGetCollaborationAnalysisTemplateOutput,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "collaboration_analysis_templates" in value:
        import capo_cleanrooms.types.collaboration_analysis_template_list

        out["collaboration_analysis_templates"] = (
            capo_cleanrooms.types.collaboration_analysis_template_list.redact_sensitive(
                value["collaboration_analysis_templates"]
            )
        )
    return out
