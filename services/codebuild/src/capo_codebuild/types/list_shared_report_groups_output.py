"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSharedReportGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.report_group_arns
    import capo_codebuild.types.string


class ListSharedReportGroupsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    report_groups: NotRequired["capo_codebuild.types.report_group_arns.ReportGroupArns"]
    """<p> The list of ARNs for the report groups shared with the current Amazon Web Services account or user. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSharedReportGroupsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "report_groups" in value:
        import capo_codebuild.types.report_group_arns

        out["reportGroups"] = (
            capo_codebuild.types.report_group_arns.serialize_aws_json_1_1(
                value["report_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSharedReportGroupsOutput:
    out: ListSharedReportGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("reportGroups") is not None:
        import capo_codebuild.types.report_group_arns

        out["report_groups"] = (
            capo_codebuild.types.report_group_arns.deserialize_aws_json_1_1(
                data["reportGroups"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSharedReportGroupsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "report_groups" in value:
        import capo_codebuild.types.report_group_arns

        out["reportGroups"] = capo_codebuild.types.report_group_arns.serialize_cbor(
            value["report_groups"]
        )
    return out


def deserialize_cbor(data: dict) -> ListSharedReportGroupsOutput:
    out: ListSharedReportGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("reportGroups") is not None:
        import capo_codebuild.types.report_group_arns

        out["report_groups"] = capo_codebuild.types.report_group_arns.deserialize_cbor(
            data["reportGroups"]
        )
    return out
