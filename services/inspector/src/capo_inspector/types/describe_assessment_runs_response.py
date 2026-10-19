"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.assessment_run_list
    import capo_inspector.types.failed_items


class DescribeAssessmentRunsResponse(TypedDict, closed=True):
    assessment_runs: "capo_inspector.types.assessment_run_list.AssessmentRunList"
    """<p>Information about the assessment run.</p>"""
    failed_items: "capo_inspector.types.failed_items.FailedItems"
    """<p>Assessment run details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentRunsResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.assessment_run_list

    out["assessmentRuns"] = (
        capo_inspector.types.assessment_run_list.serialize_aws_json_1_1(
            value["assessment_runs"]
        )
    )
    import capo_inspector.types.failed_items

    out["failedItems"] = capo_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentRunsResponse:
    out: DescribeAssessmentRunsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessmentRuns") is not None:
        import capo_inspector.types.assessment_run_list

        out["assessment_runs"] = (
            capo_inspector.types.assessment_run_list.deserialize_aws_json_1_1(
                data["assessmentRuns"]
            )
        )
    else:
        out["assessment_runs"] = []
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
