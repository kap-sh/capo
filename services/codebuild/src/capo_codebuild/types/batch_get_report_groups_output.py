"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetReportGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.report_group_arns
    import capo_codebuild.types.report_groups


class BatchGetReportGroupsOutput(TypedDict, closed=True):
    report_groups: NotRequired["capo_codebuild.types.report_groups.ReportGroups"]
    """<p> The array of report groups returned by <code>BatchGetReportGroups</code>. </p>"""
    report_groups_not_found: NotRequired[
        "capo_codebuild.types.report_group_arns.ReportGroupArns"
    ]
    """<p> An array of ARNs passed to <code>BatchGetReportGroups</code> that are not associated with a <code>ReportGroup</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetReportGroupsOutput) -> dict:
    out: dict = {}
    if "report_groups" in value:
        import capo_codebuild.types.report_groups

        out["reportGroups"] = capo_codebuild.types.report_groups.serialize_aws_json_1_1(
            value["report_groups"]
        )
    if "report_groups_not_found" in value:
        import capo_codebuild.types.report_group_arns

        out["reportGroupsNotFound"] = (
            capo_codebuild.types.report_group_arns.serialize_aws_json_1_1(
                value["report_groups_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetReportGroupsOutput:
    out: BatchGetReportGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("reportGroups") is not None:
        import capo_codebuild.types.report_groups

        out["report_groups"] = (
            capo_codebuild.types.report_groups.deserialize_aws_json_1_1(
                data["reportGroups"]
            )
        )
    if data.get("reportGroupsNotFound") is not None:
        import capo_codebuild.types.report_group_arns

        out["report_groups_not_found"] = (
            capo_codebuild.types.report_group_arns.deserialize_aws_json_1_1(
                data["reportGroupsNotFound"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetReportGroupsOutput) -> dict:
    out: dict = {}
    if "report_groups" in value:
        import capo_codebuild.types.report_groups

        out["reportGroups"] = capo_codebuild.types.report_groups.serialize_cbor(
            value["report_groups"]
        )
    if "report_groups_not_found" in value:
        import capo_codebuild.types.report_group_arns

        out["reportGroupsNotFound"] = (
            capo_codebuild.types.report_group_arns.serialize_cbor(
                value["report_groups_not_found"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetReportGroupsOutput:
    out: BatchGetReportGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("reportGroups") is not None:
        import capo_codebuild.types.report_groups

        out["report_groups"] = capo_codebuild.types.report_groups.deserialize_cbor(
            data["reportGroups"]
        )
    if data.get("reportGroupsNotFound") is not None:
        import capo_codebuild.types.report_group_arns

        out["report_groups_not_found"] = (
            capo_codebuild.types.report_group_arns.deserialize_cbor(
                data["reportGroupsNotFound"]
            )
        )
    return out
