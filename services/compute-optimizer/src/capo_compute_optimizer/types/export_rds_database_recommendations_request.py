"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportRDSDatabaseRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_ids
    import capo_compute_optimizer.types.exportable_rdsdb_fields
    import capo_compute_optimizer.types.file_format
    import capo_compute_optimizer.types.include_member_accounts
    import capo_compute_optimizer.types.rdsdb_recommendation_filters
    import capo_compute_optimizer.types.recommendation_preferences
    import capo_compute_optimizer.types.s3_destination_config


class ExportRDSDatabaseRecommendationsRequest(TypedDict, closed=True):
    account_ids: NotRequired["capo_compute_optimizer.types.account_ids.AccountIds"]
    """<p> The Amazon Web Services account IDs for the export Amazon Aurora and RDS database recommendations. </p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to specify the member account you want to export recommendations to.</p> <p>This parameter can't be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>If this parameter or the include member accounts parameter is omitted, the recommendations for member accounts aren't included in the export.</p> <p>You can specify multiple account IDs per request.</p>"""
    filters: NotRequired[
        "capo_compute_optimizer.types.rdsdb_recommendation_filters.RDSDBRecommendationFilters"
    ]
    """<p> An array of objects to specify a filter that exports a more specific set of Amazon Aurora and RDS recommendations. </p>"""
    fields_to_export: NotRequired[
        "capo_compute_optimizer.types.exportable_rdsdb_fields.ExportableRDSDBFields"
    ]
    """<p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    s3_destination_config: (
        "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig"
    )
    file_format: NotRequired["capo_compute_optimizer.types.file_format.FileFormat"]
    """<p> The format of the export file. </p> <p>The CSV file is the only export file format currently supported.</p>"""
    include_member_accounts: (
        "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
    )
    """<p>If your account is the management account or the delegated administrator of an organization, this parameter indicates whether to include recommendations for resources in all member accounts of the organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>If this parameter is omitted, recommendations for member accounts of the organization aren't included in the export file.</p> <p>If this parameter or the account ID parameter is omitted, recommendations for member accounts aren't included in the export.</p>"""
    recommendation_preferences: NotRequired[
        "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportRDSDatabaseRecommendationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_compute_optimizer.types.account_ids

        out["accountIds"] = (
            capo_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "filters" in value:
        import capo_compute_optimizer.types.rdsdb_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.rdsdb_recommendation_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "fields_to_export" in value:
        import capo_compute_optimizer.types.exportable_rdsdb_fields

        out["fieldsToExport"] = (
            capo_compute_optimizer.types.exportable_rdsdb_fields.serialize_aws_json_1_0(
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


def deserialize_aws_json_1_0(data: dict) -> ExportRDSDatabaseRecommendationsRequest:
    out: ExportRDSDatabaseRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_compute_optimizer.types.account_ids

        out["account_ids"] = (
            capo_compute_optimizer.types.account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.rdsdb_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.rdsdb_recommendation_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if data.get("fieldsToExport") is not None:
        import capo_compute_optimizer.types.exportable_rdsdb_fields

        out["fields_to_export"] = (
            capo_compute_optimizer.types.exportable_rdsdb_fields.deserialize_aws_json_1_0(
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
            "ExportRDSDatabaseRecommendationsRequest.s3_destination_config required"
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
