"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.assessment_target_list
    import capo_inspector.types.failed_items


class DescribeAssessmentTargetsResponse(TypedDict, closed=True):
    assessment_targets: (
        "capo_inspector.types.assessment_target_list.AssessmentTargetList"
    )
    """<p>Information about the assessment targets.</p>"""
    failed_items: "capo_inspector.types.failed_items.FailedItems"
    """<p>Assessment target details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentTargetsResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.assessment_target_list

    out["assessmentTargets"] = (
        capo_inspector.types.assessment_target_list.serialize_aws_json_1_1(
            value["assessment_targets"]
        )
    )
    import capo_inspector.types.failed_items

    out["failedItems"] = capo_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentTargetsResponse:
    out: DescribeAssessmentTargetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessmentTargets") is not None:
        import capo_inspector.types.assessment_target_list

        out["assessment_targets"] = (
            capo_inspector.types.assessment_target_list.deserialize_aws_json_1_1(
                data["assessmentTargets"]
            )
        )
    else:
        out["assessment_targets"] = []
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
