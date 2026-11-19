"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_id
    import capo_compute_optimizer.types.last_refresh_timestamp
    import capo_compute_optimizer.types.license_configuration
    import capo_compute_optimizer.types.license_finding
    import capo_compute_optimizer.types.license_finding_reason_codes
    import capo_compute_optimizer.types.license_recommendation_options
    import capo_compute_optimizer.types.look_back_period_in_days
    import capo_compute_optimizer.types.resource_arn
    import capo_compute_optimizer.types.tags


class LicenseRecommendation(TypedDict, closed=True):
    resource_arn: NotRequired["capo_compute_optimizer.types.resource_arn.ResourceArn"]
    """<p> The ARN that identifies the Amazon EC2 instance. </p>"""
    account_id: NotRequired["capo_compute_optimizer.types.account_id.AccountId"]
    """<p> The Amazon Web Services account ID of the license. </p>"""
    current_license_configuration: NotRequired[
        "capo_compute_optimizer.types.license_configuration.LicenseConfiguration"
    ]
    """<p> An object that describes the current configuration of an instance that runs on a license. </p>"""
    lookback_period_in_days: (
        "capo_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p> The number of days for which utilization metrics were analyzed for an instance that runs on a license. </p>"""
    last_refresh_timestamp: NotRequired[
        "capo_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p> The timestamp of when the license recommendation was last generated. </p>"""
    finding: NotRequired["capo_compute_optimizer.types.license_finding.LicenseFinding"]
    """<p> The finding classification for an instance that runs on a license. </p> <p>Findings include:</p> <ul> <li> <p> <code>InsufficentMetrics</code> — When Compute Optimizer detects that your CloudWatch Application Insights isn't enabled or is enabled with insufficient permissions. </p> </li> <li> <p> <code>NotOptimized</code> — When Compute Optimizer detects that your EC2 infrastructure isn't using any of the SQL server license features you're paying for, a license is considered not optimized.</p> </li> <li> <p> <code>Optimized</code> — When Compute Optimizer detects that all specifications of your license meet the performance requirements of your workload. </p> </li> </ul>"""
    finding_reason_codes: NotRequired[
        "capo_compute_optimizer.types.license_finding_reason_codes.LicenseFindingReasonCodes"
    ]
    """<p> The reason for the finding classification for an instance that runs on a license. </p> <p>Finding reason codes include:</p> <ul> <li> <p> <code>Optimized</code> — All specifications of your license meet the performance requirements of your workload. </p> </li> <li> <p> <code>LicenseOverprovisioned</code> — A license is considered over-provisioned when your license can be downgraded while still meeting the performance requirements of your workload.</p> </li> <li> <p> <code>InvalidCloudwatchApplicationInsights</code> — CloudWatch Application Insights isn't configured properly.</p> </li> <li> <p> <code>CloudwatchApplicationInsightsError</code> — There is a CloudWatch Application Insights error. </p> </li> </ul>"""
    license_recommendation_options: NotRequired[
        "capo_compute_optimizer.types.license_recommendation_options.LicenseRecommendationOptions"
    ]
    """<p> An array of objects that describe the license recommendation options. </p>"""
    tags: NotRequired["capo_compute_optimizer.types.tags.Tags"]
    """<p> A list of tags assigned to an EC2 instance. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseRecommendation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "current_license_configuration" in value:
        import capo_compute_optimizer.types.license_configuration

        out["currentLicenseConfiguration"] = (
            capo_compute_optimizer.types.license_configuration.serialize_aws_json_1_0(
                value["current_license_configuration"]
            )
        )
    out["lookbackPeriodInDays"] = (
        "NaN"
        if value.get("lookback_period_in_days", 0)
        != value.get("lookback_period_in_days", 0)
        else "Infinity"
        if value.get("lookback_period_in_days", 0) == float("inf")
        else "-Infinity"
        if value.get("lookback_period_in_days", 0) == float("-inf")
        else value.get("lookback_period_in_days", 0)
    )
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "finding" in value:
        import capo_compute_optimizer.types.license_finding

        out["finding"] = (
            capo_compute_optimizer.types.license_finding.serialize_aws_json_1_0(
                value["finding"]
            )
        )
    if "finding_reason_codes" in value:
        import capo_compute_optimizer.types.license_finding_reason_codes

        out["findingReasonCodes"] = (
            capo_compute_optimizer.types.license_finding_reason_codes.serialize_aws_json_1_0(
                value["finding_reason_codes"]
            )
        )
    if "license_recommendation_options" in value:
        import capo_compute_optimizer.types.license_recommendation_options

        out["licenseRecommendationOptions"] = (
            capo_compute_optimizer.types.license_recommendation_options.serialize_aws_json_1_0(
                value["license_recommendation_options"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LicenseRecommendation:
    out: LicenseRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("currentLicenseConfiguration") is not None:
        import capo_compute_optimizer.types.license_configuration

        out["current_license_configuration"] = (
            capo_compute_optimizer.types.license_configuration.deserialize_aws_json_1_0(
                data["currentLicenseConfiguration"]
            )
        )
    if data.get("lookbackPeriodInDays") is not None:
        out["lookback_period_in_days"] = float(data["lookbackPeriodInDays"])
    else:
        out["lookback_period_in_days"] = 0
    if data.get("lastRefreshTimestamp") is not None:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("finding") is not None:
        import capo_compute_optimizer.types.license_finding

        out["finding"] = (
            capo_compute_optimizer.types.license_finding.deserialize_aws_json_1_0(
                data["finding"]
            )
        )
    if data.get("findingReasonCodes") is not None:
        import capo_compute_optimizer.types.license_finding_reason_codes

        out["finding_reason_codes"] = (
            capo_compute_optimizer.types.license_finding_reason_codes.deserialize_aws_json_1_0(
                data["findingReasonCodes"]
            )
        )
    if data.get("licenseRecommendationOptions") is not None:
        import capo_compute_optimizer.types.license_recommendation_options

        out["license_recommendation_options"] = (
            capo_compute_optimizer.types.license_recommendation_options.deserialize_aws_json_1_0(
                data["licenseRecommendationOptions"]
            )
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseRecommendation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "current_license_configuration" in value:
        import capo_compute_optimizer.types.license_configuration

        out["currentLicenseConfiguration"] = (
            capo_compute_optimizer.types.license_configuration.serialize_cbor(
                value["current_license_configuration"]
            )
        )
    out["lookbackPeriodInDays"] = value.get("lookback_period_in_days", 0)
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_cbor(
                value["last_refresh_timestamp"]
            )
        )
    if "finding" in value:
        import capo_compute_optimizer.types.license_finding

        out["finding"] = capo_compute_optimizer.types.license_finding.serialize_cbor(
            value["finding"]
        )
    if "finding_reason_codes" in value:
        import capo_compute_optimizer.types.license_finding_reason_codes

        out["findingReasonCodes"] = (
            capo_compute_optimizer.types.license_finding_reason_codes.serialize_cbor(
                value["finding_reason_codes"]
            )
        )
    if "license_recommendation_options" in value:
        import capo_compute_optimizer.types.license_recommendation_options

        out["licenseRecommendationOptions"] = (
            capo_compute_optimizer.types.license_recommendation_options.serialize_cbor(
                value["license_recommendation_options"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> LicenseRecommendation:
    out: LicenseRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("currentLicenseConfiguration") is not None:
        import capo_compute_optimizer.types.license_configuration

        out["current_license_configuration"] = (
            capo_compute_optimizer.types.license_configuration.deserialize_cbor(
                data["currentLicenseConfiguration"]
            )
        )
    if data.get("lookbackPeriodInDays") is not None:
        out["lookback_period_in_days"] = float(data["lookbackPeriodInDays"])
    else:
        out["lookback_period_in_days"] = 0
    if data.get("lastRefreshTimestamp") is not None:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_cbor(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("finding") is not None:
        import capo_compute_optimizer.types.license_finding

        out["finding"] = capo_compute_optimizer.types.license_finding.deserialize_cbor(
            data["finding"]
        )
    if data.get("findingReasonCodes") is not None:
        import capo_compute_optimizer.types.license_finding_reason_codes

        out["finding_reason_codes"] = (
            capo_compute_optimizer.types.license_finding_reason_codes.deserialize_cbor(
                data["findingReasonCodes"]
            )
        )
    if data.get("licenseRecommendationOptions") is not None:
        import capo_compute_optimizer.types.license_recommendation_options

        out["license_recommendation_options"] = (
            capo_compute_optimizer.types.license_recommendation_options.deserialize_cbor(
                data["licenseRecommendationOptions"]
            )
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.deserialize_cbor(data["tags"])
    return out
