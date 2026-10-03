"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.collection_retention_days
    import capo_cloudwatch_logs.types.dashboard_viewer_principals


class OpenSearchResourceConfig(TypedDict, closed=True):
    kms_key_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>To have the vended dashboard data encrypted with KMS instead of the CloudWatch Logs default encryption method, specify the ARN of the KMS key that you want to use.</p>"""
    data_source_role_arn: "capo_cloudwatch_logs.types.arn.Arn"
    """<p>Specify the ARN of an IAM role that CloudWatch Logs will use to create the integration. This role must have the permissions necessary to access the OpenSearch Service collection to be able to create the dashboards. For more information about the permissions needed, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-CreateRole.html">Permissions that the integration needs</a> in the CloudWatch Logs User Guide.</p>"""
    dashboard_viewer_principals: "capo_cloudwatch_logs.types.dashboard_viewer_principals.DashboardViewerPrincipals"
    """<p>Specify the ARNs of IAM roles and IAM users who you want to grant permission to for viewing the dashboards.</p> <important> <p>In addition to specifying these users here, you must also grant them the <b>CloudWatchOpenSearchDashboardAccess</b> IAM policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-UserRoles.html">IAM policies for users</a>.</p> </important>"""
    application_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>If you want to use an existing OpenSearch Service application for your integration with OpenSearch Service, specify it here. If you omit this, a new application will be created.</p>"""
    retention_days: (
        "capo_cloudwatch_logs.types.collection_retention_days.CollectionRetentionDays"
    )
    """<p>Specify how many days that you want the data derived by OpenSearch Service to be retained in the index that the dashboard refers to. This also sets the maximum time period that you can choose when viewing data in the dashboard. Choosing a longer time frame will incur additional costs. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenSearchResourceConfig) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    out["dataSourceRoleArn"] = value["data_source_role_arn"]
    import capo_cloudwatch_logs.types.dashboard_viewer_principals

    out["dashboardViewerPrincipals"] = (
        capo_cloudwatch_logs.types.dashboard_viewer_principals.serialize_aws_json_1_1(
            value["dashboard_viewer_principals"]
        )
    )
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    out["retentionDays"] = value["retention_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchResourceConfig:
    out: OpenSearchResourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("dataSourceRoleArn") is not None:
        out["data_source_role_arn"] = data["dataSourceRoleArn"]
    else:
        raise DeserializationError(
            "OpenSearchResourceConfig.data_source_role_arn required"
        )
    if data.get("dashboardViewerPrincipals") is not None:
        import capo_cloudwatch_logs.types.dashboard_viewer_principals

        out["dashboard_viewer_principals"] = (
            capo_cloudwatch_logs.types.dashboard_viewer_principals.deserialize_aws_json_1_1(
                data["dashboardViewerPrincipals"]
            )
        )
    else:
        raise DeserializationError(
            "OpenSearchResourceConfig.dashboard_viewer_principals required"
        )
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    if data.get("retentionDays") is not None:
        out["retention_days"] = data["retentionDays"]
    else:
        raise DeserializationError("OpenSearchResourceConfig.retention_days required")
    return out
