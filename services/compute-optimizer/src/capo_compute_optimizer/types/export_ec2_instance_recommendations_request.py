"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportEC2InstanceRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_ids
    import capo_compute_optimizer.types.exportable_instance_fields
    import capo_compute_optimizer.types.file_format
    import capo_compute_optimizer.types.filters
    import capo_compute_optimizer.types.include_member_accounts
    import capo_compute_optimizer.types.recommendation_preferences
    import capo_compute_optimizer.types.s3_destination_config


class ExportEC2InstanceRecommendationsRequest(TypedDict, closed=True):
    account_ids: NotRequired["capo_compute_optimizer.types.account_ids.AccountIds"]
    """<p>The IDs of the Amazon Web Services accounts for which to export instance recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to export recommendations.</p> <p>This parameter cannot be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the include member accounts parameter, is omitted.</p> <p>You can specify multiple account IDs per request.</p>"""
    filters: NotRequired["capo_compute_optimizer.types.filters.Filters"]
    """<p>An array of objects to specify a filter that exports a more specific set of instance recommendations.</p>"""
    fields_to_export: NotRequired[
        "capo_compute_optimizer.types.exportable_instance_fields.ExportableInstanceFields"
    ]
    """<p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    s3_destination_config: (
        "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig"
    )
    """<p>An object to specify the destination Amazon Simple Storage Service (Amazon S3) bucket name and key prefix for the export job.</p> <p>You must create the destination Amazon S3 bucket for your recommendations export before you create the export job. Compute Optimizer does not create the S3 bucket for you. After you create the S3 bucket, ensure that it has the required permissions policy to allow Compute Optimizer to write the export file to it. If you plan to specify an object prefix when you create the export job, you must include the object prefix in the policy that you add to the S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/create-s3-bucket-policy-for-compute-optimizer.html">Amazon S3 Bucket Policy for Compute Optimizer</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    file_format: NotRequired["capo_compute_optimizer.types.file_format.FileFormat"]
    """<p>The format of the export file.</p> <p>The only export file format currently supported is <code>Csv</code>.</p>"""
    include_member_accounts: (
        "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
    )
    """<p>Indicates whether to include recommendations for resources in all member accounts of the organization if your account is the management account of an organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>Recommendations for member accounts of the organization are not included in the export file if this parameter is omitted.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the account IDs parameter, is omitted.</p>"""
    recommendation_preferences: NotRequired[
        "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
    ]
    """<p>An object to specify the preferences for the Amazon EC2 instance recommendations to export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportEC2InstanceRecommendationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_compute_optimizer.types.account_ids

        out["accountIds"] = (
            capo_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "filters" in value:
        import capo_compute_optimizer.types.filters

        out["filters"] = capo_compute_optimizer.types.filters.serialize_aws_json_1_0(
            value["filters"]
        )
    if "fields_to_export" in value:
        import capo_compute_optimizer.types.exportable_instance_fields

        out["fieldsToExport"] = (
            capo_compute_optimizer.types.exportable_instance_fields.serialize_aws_json_1_0(
                value["fields_to_export"]
            )
        )
    import capo_compute_optimizer.types.s3_destination_config

    out["s3DestinationConfig"] = (
        capo_compute_optimizer.types.s3_destination_config.serialize_aws_json_1_0(
            value["s3_destination_config"]
        )
    )
    if "file_format" in value:
        import capo_compute_optimizer.types.file_format

        out["fileFormat"] = (
            capo_compute_optimizer.types.file_format.serialize_aws_json_1_0(
                value["file_format"]
            )
        )
    out["includeMemberAccounts"] = value.get("include_member_accounts", False)
    if "recommendation_preferences" in value:
        import capo_compute_optimizer.types.recommendation_preferences

        out["recommendationPreferences"] = (
            capo_compute_optimizer.types.recommendation_preferences.serialize_aws_json_1_0(
                value["recommendation_preferences"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportEC2InstanceRecommendationsRequest:
    out: ExportEC2InstanceRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_compute_optimizer.types.account_ids

        out["account_ids"] = (
            capo_compute_optimizer.types.account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.filters

        out["filters"] = capo_compute_optimizer.types.filters.deserialize_aws_json_1_0(
            data["filters"]
        )
    if data.get("fieldsToExport") is not None:
        import capo_compute_optimizer.types.exportable_instance_fields

        out["fields_to_export"] = (
            capo_compute_optimizer.types.exportable_instance_fields.deserialize_aws_json_1_0(
                data["fieldsToExport"]
            )
        )
    if data.get("s3DestinationConfig") is not None:
        import capo_compute_optimizer.types.s3_destination_config

        out["s3_destination_config"] = (
            capo_compute_optimizer.types.s3_destination_config.deserialize_aws_json_1_0(
                data["s3DestinationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ExportEC2InstanceRecommendationsRequest.s3_destination_config required"
        )
    if data.get("fileFormat") is not None:
        import capo_compute_optimizer.types.file_format

        out["file_format"] = (
            capo_compute_optimizer.types.file_format.deserialize_aws_json_1_0(
                data["fileFormat"]
            )
        )
    if data.get("includeMemberAccounts") is not None:
        out["include_member_accounts"] = data["includeMemberAccounts"]
    else:
        out["include_member_accounts"] = False
    if data.get("recommendationPreferences") is not None:
        import capo_compute_optimizer.types.recommendation_preferences

        out["recommendation_preferences"] = (
            capo_compute_optimizer.types.recommendation_preferences.deserialize_aws_json_1_0(
                data["recommendationPreferences"]
            )
        )
    return out
