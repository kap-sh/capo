"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetReportsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.report_arns


class BatchGetReportsInput(TypedDict, closed=True):
    report_arns: "capo_codebuild.types.report_arns.ReportArns"
    """<p> An array of ARNs that identify the <code>Report</code> objects to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetReportsInput) -> dict:
    out: dict = {}
    import capo_codebuild.types.report_arns

    out["reportArns"] = capo_codebuild.types.report_arns.serialize_aws_json_1_1(
        value["report_arns"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetReportsInput:
    out: BatchGetReportsInput = {}  # type: ignore[typeddict-item]
    if data.get("reportArns") is not None:
        import capo_codebuild.types.report_arns

        out["report_arns"] = capo_codebuild.types.report_arns.deserialize_aws_json_1_1(
            data["reportArns"]
        )
    else:
        out["report_arns"] = []
    return out
