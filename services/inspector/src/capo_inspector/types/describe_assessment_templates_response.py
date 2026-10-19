"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.assessment_template_list
    import capo_inspector.types.failed_items


class DescribeAssessmentTemplatesResponse(TypedDict, closed=True):
    assessment_templates: (
        "capo_inspector.types.assessment_template_list.AssessmentTemplateList"
    )
    """<p>Information about the assessment templates.</p>"""
    failed_items: "capo_inspector.types.failed_items.FailedItems"
    """<p>Assessment template details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentTemplatesResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.assessment_template_list

    out["assessmentTemplates"] = (
        capo_inspector.types.assessment_template_list.serialize_aws_json_1_1(
            value["assessment_templates"]
        )
    )
    import capo_inspector.types.failed_items

    out["failedItems"] = capo_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentTemplatesResponse:
    out: DescribeAssessmentTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessmentTemplates") is not None:
        import capo_inspector.types.assessment_template_list

        out["assessment_templates"] = (
            capo_inspector.types.assessment_template_list.deserialize_aws_json_1_1(
                data["assessmentTemplates"]
            )
        )
    else:
        out["assessment_templates"] = []
    if data.get("failedItems") is not None:
        import capo_inspector.types.failed_items

        out["failed_items"] = (
            capo_inspector.types.failed_items.deserialize_aws_json_1_1(
                data["failedItems"]
            )
        )
    else:
        out["failed_items"] = {}
    return out
