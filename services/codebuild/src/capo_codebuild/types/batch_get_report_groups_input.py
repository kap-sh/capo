"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetReportGroupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.report_group_arns


class BatchGetReportGroupsInput(TypedDict, closed=True):
    report_group_arns: "capo_codebuild.types.report_group_arns.ReportGroupArns"
    """<p> An array of report group ARNs that identify the report groups to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetReportGroupsInput) -> dict:
    out: dict = {}
    import capo_codebuild.types.report_group_arns

    out["reportGroupArns"] = (
        capo_codebuild.types.report_group_arns.serialize_aws_json_1_1(
            value["report_group_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetReportGroupsInput:
    out: BatchGetReportGroupsInput = {}  # type: ignore[typeddict-item]
    if data.get("reportGroupArns") is not None:
        import capo_codebuild.types.report_group_arns

        out["report_group_arns"] = (
            capo_codebuild.types.report_group_arns.deserialize_aws_json_1_1(
                data["reportGroupArns"]
            )
        )
    else:
        out["report_group_arns"] = []
    return out
