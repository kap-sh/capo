"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetCollaborationAnalysisTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_arn_list
    import capo_cleanrooms.types.collaboration_identifier


class BatchGetCollaborationAnalysisTemplateInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>"""
    analysis_template_arns: (
        "capo_cleanrooms.types.analysis_template_arn_list.AnalysisTemplateArnList"
    )
    """<p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCollaborationAnalysisTemplateInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_template_arn_list

    out["analysisTemplateArns"] = (
        capo_cleanrooms.types.analysis_template_arn_list.serialize_json(
            value["analysis_template_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetCollaborationAnalysisTemplateInput:
    out: BatchGetCollaborationAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("analysisTemplateArns") is not None:
        import capo_cleanrooms.types.analysis_template_arn_list

        out["analysis_template_arns"] = (
            capo_cleanrooms.types.analysis_template_arn_list.deserialize_json(
                data["analysisTemplateArns"]
            )
        )
    else:
        out["analysis_template_arns"] = []
    return out
