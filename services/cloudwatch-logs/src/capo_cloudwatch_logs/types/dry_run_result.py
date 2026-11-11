"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DryRunResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.dry_run_count
    import capo_cloudwatch_logs.types.log_group_impacts


class DryRunResult(TypedDict, closed=True):
    total_matched_log_groups: "capo_cloudwatch_logs.types.dry_run_count.DryRunCount"
    """<p>The number of log groups in the scope of the policy that were analyzed. This value is the sum of <code>increasedRetentionLogGroupCount</code>, <code>decreasedRetentionLogGroupCount</code>, and <code>unchangedRetentionLogGroupCount</code>, and does not include log groups that could not be analyzed.</p>"""
    increased_retention_log_group_count: (
        "capo_cloudwatch_logs.types.dry_run_count.DryRunCount"
    )
    """<p>The number of log groups whose effective retention period would become longer.</p>"""
    decreased_retention_log_group_count: (
        "capo_cloudwatch_logs.types.dry_run_count.DryRunCount"
    )
    """<p>The number of log groups whose effective retention period would become shorter.</p>"""
    unchanged_retention_log_group_count: (
        "capo_cloudwatch_logs.types.dry_run_count.DryRunCount"
    )
    """<p>The number of log groups whose effective retention period would not change.</p>"""
    failed_analysis_count: "capo_cloudwatch_logs.types.dry_run_count.DryRunCount"
    """<p>The number of log groups in the scope of the policy that could not be analyzed. These log groups are not included in <code>totalMatchedLogGroups</code>.</p>"""
    top_log_groups_impacted: NotRequired[
        "capo_cloudwatch_logs.types.log_group_impacts.LogGroupImpacts"
    ]
    """<p>Up to 20 log groups in the scope of the policy, sorted by stored bytes in descending order. This list can include log groups whose effective retention period would not change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DryRunResult) -> dict:
    out: dict = {}
    out["totalMatchedLogGroups"] = value.get("total_matched_log_groups", 0)
    out["increasedRetentionLogGroupCount"] = value.get(
        "increased_retention_log_group_count", 0
    )
    out["decreasedRetentionLogGroupCount"] = value.get(
        "decreased_retention_log_group_count", 0
    )
    out["unchangedRetentionLogGroupCount"] = value.get(
        "unchanged_retention_log_group_count", 0
    )
    out["failedAnalysisCount"] = value.get("failed_analysis_count", 0)
    if "top_log_groups_impacted" in value:
        import capo_cloudwatch_logs.types.log_group_impacts

        out["topLogGroupsImpacted"] = (
            capo_cloudwatch_logs.types.log_group_impacts.serialize_aws_json_1_1(
                value["top_log_groups_impacted"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DryRunResult:
    out: DryRunResult = {}  # type: ignore[typeddict-item]
    if data.get("totalMatchedLogGroups") is not None:
        out["total_matched_log_groups"] = data["totalMatchedLogGroups"]
    else:
        out["total_matched_log_groups"] = 0
    if data.get("increasedRetentionLogGroupCount") is not None:
        out["increased_retention_log_group_count"] = data[
            "increasedRetentionLogGroupCount"
        ]
    else:
        out["increased_retention_log_group_count"] = 0
    if data.get("decreasedRetentionLogGroupCount") is not None:
        out["decreased_retention_log_group_count"] = data[
            "decreasedRetentionLogGroupCount"
        ]
    else:
        out["decreased_retention_log_group_count"] = 0
    if data.get("unchangedRetentionLogGroupCount") is not None:
        out["unchanged_retention_log_group_count"] = data[
            "unchangedRetentionLogGroupCount"
        ]
    else:
        out["unchanged_retention_log_group_count"] = 0
    if data.get("failedAnalysisCount") is not None:
        out["failed_analysis_count"] = data["failedAnalysisCount"]
    else:
        out["failed_analysis_count"] = 0
    if data.get("topLogGroupsImpacted") is not None:
        import capo_cloudwatch_logs.types.log_group_impacts

        out["top_log_groups_impacted"] = (
            capo_cloudwatch_logs.types.log_group_impacts.deserialize_aws_json_1_1(
                data["topLogGroupsImpacted"]
            )
        )
    return out
