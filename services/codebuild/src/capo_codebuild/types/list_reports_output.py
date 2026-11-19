"""Generated from Smithy shape ``com.amazonaws.codebuild#ListReportsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.report_arns
    import capo_codebuild.types.string


class ListReportsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    reports: NotRequired["capo_codebuild.types.report_arns.ReportArns"]
    """<p> The list of returned ARNs for the reports in the current Amazon Web Services account. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReportsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "reports" in value:
        import capo_codebuild.types.report_arns

        out["reports"] = capo_codebuild.types.report_arns.serialize_aws_json_1_1(
            value["reports"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReportsOutput:
    out: ListReportsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("reports") is not None:
        import capo_codebuild.types.report_arns

        out["reports"] = capo_codebuild.types.report_arns.deserialize_aws_json_1_1(
            data["reports"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListReportsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "reports" in value:
        import capo_codebuild.types.report_arns

        out["reports"] = capo_codebuild.types.report_arns.serialize_cbor(
            value["reports"]
        )
    return out


def deserialize_cbor(data: dict) -> ListReportsOutput:
    out: ListReportsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("reports") is not None:
        import capo_codebuild.types.report_arns

        out["reports"] = capo_codebuild.types.report_arns.deserialize_cbor(
            data["reports"]
        )
    return out
