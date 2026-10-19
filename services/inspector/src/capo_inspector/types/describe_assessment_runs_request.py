"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.batch_describe_arn_list


class DescribeAssessmentRunsRequest(TypedDict, closed=True):
    assessment_run_arns: (
        "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    )
    """<p>The ARN that specifies the assessment run that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentRunsRequest) -> dict:
    out: dict = {}
    import capo_inspector.types.batch_describe_arn_list

    out["assessmentRunArns"] = (
        capo_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["assessment_run_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentRunsRequest:
    out: DescribeAssessmentRunsRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentRunArns") is not None:
        import capo_inspector.types.batch_describe_arn_list

        out["assessment_run_arns"] = (
            capo_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["assessmentRunArns"]
            )
        )
    else:
        out["assessment_run_arns"] = []
    return out
