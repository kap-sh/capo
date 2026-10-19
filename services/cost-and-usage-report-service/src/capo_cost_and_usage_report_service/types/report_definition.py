"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ReportDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.additional_artifact_list
    import capo_cost_and_usage_report_service.types.aws_region
    import capo_cost_and_usage_report_service.types.billing_view_arn
    import capo_cost_and_usage_report_service.types.compression_format
    import capo_cost_and_usage_report_service.types.refresh_closed_reports
    import capo_cost_and_usage_report_service.types.report_format
    import capo_cost_and_usage_report_service.types.report_name
    import capo_cost_and_usage_report_service.types.report_status
    import capo_cost_and_usage_report_service.types.report_versioning
    import capo_cost_and_usage_report_service.types.s3_bucket
    import capo_cost_and_usage_report_service.types.s3_prefix
    import capo_cost_and_usage_report_service.types.schema_element_list
    import capo_cost_and_usage_report_service.types.time_unit


class ReportDefinition(TypedDict, closed=True):
    report_name: "capo_cost_and_usage_report_service.types.report_name.ReportName"
    time_unit: "capo_cost_and_usage_report_service.types.time_unit.TimeUnit"
    format: "capo_cost_and_usage_report_service.types.report_format.ReportFormat"
    compression: (
        "capo_cost_and_usage_report_service.types.compression_format.CompressionFormat"
    )
    additional_schema_elements: (
        "capo_cost_and_usage_report_service.types.schema_element_list.SchemaElementList"
    )
    """<p>A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs. </p>"""
    s3_bucket: "capo_cost_and_usage_report_service.types.s3_bucket.S3Bucket"
    s3_prefix: "capo_cost_and_usage_report_service.types.s3_prefix.S3Prefix"
    s3_region: "capo_cost_and_usage_report_service.types.aws_region.AWSRegion"
    additional_artifacts: NotRequired[
        "capo_cost_and_usage_report_service.types.additional_artifact_list.AdditionalArtifactList"
    ]
    """<p>A list of manifests that you want Amazon Web Services to create for this report.</p>"""
    refresh_closed_reports: NotRequired[
        "capo_cost_and_usage_report_service.types.refresh_closed_reports.RefreshClosedReports"
    ]
    """<p>Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.</p>"""
    report_versioning: NotRequired[
        "capo_cost_and_usage_report_service.types.report_versioning.ReportVersioning"
    ]
    """<p>Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.</p>"""
    billing_view_arn: NotRequired[
        "capo_cost_and_usage_report_service.types.billing_view_arn.BillingViewArn"
    ]
    """<p> The Amazon resource name of the billing view. The <code>BillingViewArn</code> is needed to create Amazon Web Services Cost and Usage Report for each billing group maintained in the Amazon Web Services Billing Conductor service. The <code>BillingViewArn</code> for a billing group can be constructed as: <code>arn:aws:billing::payer-account-id:billingview/billing-group-primary-account-id</code> </p>"""
    report_status: NotRequired[
        "capo_cost_and_usage_report_service.types.report_status.ReportStatus"
    ]
    """<p>The status of the report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportDefinition) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    import capo_cost_and_usage_report_service.types.time_unit

    out["TimeUnit"] = (
        capo_cost_and_usage_report_service.types.time_unit.serialize_aws_json_1_1(
            value["time_unit"]
        )
    )
    import capo_cost_and_usage_report_service.types.report_format

    out["Format"] = (
        capo_cost_and_usage_report_service.types.report_format.serialize_aws_json_1_1(
            value["format"]
        )
    )
    import capo_cost_and_usage_report_service.types.compression_format

    out["Compression"] = (
        capo_cost_and_usage_report_service.types.compression_format.serialize_aws_json_1_1(
            value["compression"]
        )
    )
    import capo_cost_and_usage_report_service.types.schema_element_list

    out["AdditionalSchemaElements"] = (
        capo_cost_and_usage_report_service.types.schema_element_list.serialize_aws_json_1_1(
            value["additional_schema_elements"]
        )
    )
    out["S3Bucket"] = value["s3_bucket"]
    out["S3Prefix"] = value["s3_prefix"]
    import capo_cost_and_usage_report_service.types.aws_region

    out["S3Region"] = (
        capo_cost_and_usage_report_service.types.aws_region.serialize_aws_json_1_1(
            value["s3_region"]
        )
    )
    if "additional_artifacts" in value:
        import capo_cost_and_usage_report_service.types.additional_artifact_list

        out["AdditionalArtifacts"] = (
            capo_cost_and_usage_report_service.types.additional_artifact_list.serialize_aws_json_1_1(
                value["additional_artifacts"]
            )
        )
    if "refresh_closed_reports" in value:
        out["RefreshClosedReports"] = value["refresh_closed_reports"]
    if "report_versioning" in value:
        import capo_cost_and_usage_report_service.types.report_versioning

        out["ReportVersioning"] = (
            capo_cost_and_usage_report_service.types.report_versioning.serialize_aws_json_1_1(
                value["report_versioning"]
            )
        )
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    if "report_status" in value:
        import capo_cost_and_usage_report_service.types.report_status

        out["ReportStatus"] = (
            capo_cost_and_usage_report_service.types.report_status.serialize_aws_json_1_1(
                value["report_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportDefinition:
    out: ReportDefinition = {}  # type: ignore[typeddict-item]
    if data.get("ReportName") is not None:
        out["report_name"] = data["ReportName"]
    else:
        out["report_name"] = ""
    if data.get("TimeUnit") is not None:
        import capo_cost_and_usage_report_service.types.time_unit

        out["time_unit"] = (
            capo_cost_and_usage_report_service.types.time_unit.deserialize_aws_json_1_1(
                data["TimeUnit"]
            )
        )
    else:
        import typing

        out["time_unit"] = typing.cast(
            "capo_cost_and_usage_report_service.types.time_unit.TimeUnit", ""
        )
    if data.get("Format") is not None:
        import capo_cost_and_usage_report_service.types.report_format

        out["format"] = (
            capo_cost_and_usage_report_service.types.report_format.deserialize_aws_json_1_1(
                data["Format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_cost_and_usage_report_service.types.report_format.ReportFormat", ""
        )
    if data.get("Compression") is not None:
        import capo_cost_and_usage_report_service.types.compression_format

        out["compression"] = (
            capo_cost_and_usage_report_service.types.compression_format.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    else:
        import typing

        out["compression"] = typing.cast(
            "capo_cost_and_usage_report_service.types.compression_format.CompressionFormat",
            "",
        )
    if data.get("AdditionalSchemaElements") is not None:
        import capo_cost_and_usage_report_service.types.schema_element_list

        out["additional_schema_elements"] = (
            capo_cost_and_usage_report_service.types.schema_element_list.deserialize_aws_json_1_1(
                data["AdditionalSchemaElements"]
            )
        )
    else:
        out["additional_schema_elements"] = []
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("S3Prefix") is not None:
        out["s3_prefix"] = data["S3Prefix"]
    else:
        out["s3_prefix"] = ""
    if data.get("S3Region") is not None:
        import capo_cost_and_usage_report_service.types.aws_region

        out["s3_region"] = (
            capo_cost_and_usage_report_service.types.aws_region.deserialize_aws_json_1_1(
                data["S3Region"]
            )
        )
    else:
        import typing

        out["s3_region"] = typing.cast(
            "capo_cost_and_usage_report_service.types.aws_region.AWSRegion", ""
        )
    if data.get("AdditionalArtifacts") is not None:
        import capo_cost_and_usage_report_service.types.additional_artifact_list

        out["additional_artifacts"] = (
            capo_cost_and_usage_report_service.types.additional_artifact_list.deserialize_aws_json_1_1(
                data["AdditionalArtifacts"]
            )
        )
    if data.get("RefreshClosedReports") is not None:
        out["refresh_closed_reports"] = data["RefreshClosedReports"]
    if data.get("ReportVersioning") is not None:
        import capo_cost_and_usage_report_service.types.report_versioning

        out["report_versioning"] = (
            capo_cost_and_usage_report_service.types.report_versioning.deserialize_aws_json_1_1(
                data["ReportVersioning"]
            )
        )
    if data.get("BillingViewArn") is not None:
        out["billing_view_arn"] = data["BillingViewArn"]
    if data.get("ReportStatus") is not None:
        import capo_cost_and_usage_report_service.types.report_status

        out["report_status"] = (
            capo_cost_and_usage_report_service.types.report_status.deserialize_aws_json_1_1(
                data["ReportStatus"]
            )
        )
    return out
