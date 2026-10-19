"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.batch_describe_arn_list


class DescribeAssessmentTemplatesRequest(TypedDict, closed=True):
    assessment_template_arns: (
        "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    )


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentTemplatesRequest) -> dict:
    out: dict = {}
    import capo_inspector.types.batch_describe_arn_list

    out["assessmentTemplateArns"] = (
        capo_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["assessment_template_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentTemplatesRequest:
    out: DescribeAssessmentTemplatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentTemplateArns") is not None:
        import capo_inspector.types.batch_describe_arn_list

        out["assessment_template_arns"] = (
            capo_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["assessmentTemplateArns"]
            )
        )
    else:
        out["assessment_template_arns"] = []
    return out
