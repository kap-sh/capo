"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.batch_describe_arn_list


class DescribeAssessmentTargetsRequest(TypedDict, closed=True):
    assessment_target_arns: (
        "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    )
    """<p>The ARNs that specifies the assessment targets that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentTargetsRequest) -> dict:
    out: dict = {}
    import capo_inspector.types.batch_describe_arn_list

    out["assessmentTargetArns"] = (
        capo_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["assessment_target_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentTargetsRequest:
    out: DescribeAssessmentTargetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentTargetArns") is not None:
        import capo_inspector.types.batch_describe_arn_list

        out["assessment_target_arns"] = (
            capo_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["assessmentTargetArns"]
            )
        )
    else:
        out["assessment_target_arns"] = []
    return out
