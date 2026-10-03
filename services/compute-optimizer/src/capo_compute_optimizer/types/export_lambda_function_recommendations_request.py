"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportLambdaFunctionRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_ids
    import capo_compute_optimizer.types.exportable_lambda_function_fields
    import capo_compute_optimizer.types.file_format
    import capo_compute_optimizer.types.include_member_accounts
    import capo_compute_optimizer.types.lambda_function_recommendation_filters
    import capo_compute_optimizer.types.s3_destination_config


class ExportLambdaFunctionRecommendationsRequest(TypedDict, closed=True):
    account_ids: NotRequired["capo_compute_optimizer.types.account_ids.AccountIds"]
    """<p>The IDs of the Amazon Web Services accounts for which to export Lambda function recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to export recommendations.</p> <p>This parameter cannot be specified together with the include member accounts parameter. The parameters are mutually exclusive.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the include member accounts parameter, is omitted.</p> <p>You can specify multiple account IDs per request.</p>"""
    filters: NotRequired[
        "capo_compute_optimizer.types.lambda_function_recommendation_filters.LambdaFunctionRecommendationFilters"
    ]
    """<p>An array of objects to specify a filter that exports a more specific set of Lambda function recommendations.</p>"""
    fields_to_export: NotRequired[
        "capo_compute_optimizer.types.exportable_lambda_function_fields.ExportableLambdaFunctionFields"
    ]
    """<p>The recommendations data to include in the export file. For more information about the fields that can be exported, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files">Exported files</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    s3_destination_config: (
        "capo_compute_optimizer.types.s3_destination_config.S3DestinationConfig"
    )
    file_format: NotRequired["capo_compute_optimizer.types.file_format.FileFormat"]
    """<p>The format of the export file.</p> <p>The only export file format currently supported is <code>Csv</code>.</p>"""
    include_member_accounts: (
        "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
    )
    """<p>Indicates whether to include recommendations for resources in all member accounts of the organization if your account is the management account of an organization.</p> <p>The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access">Compute Optimizer and Amazon Web Services Organizations trusted access</a> in the <i>Compute Optimizer User Guide</i>.</p> <p>Recommendations for member accounts of the organization are not included in the export file if this parameter is omitted.</p> <p>This parameter cannot be specified together with the account IDs parameter. The parameters are mutually exclusive.</p> <p>Recommendations for member accounts are not included in the export if this parameter, or the account IDs parameter, is omitted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportLambdaFunctionRecommendationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_compute_optimizer.types.account_ids

        out["accountIds"] = (
            capo_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "filters" in value:
        import capo_compute_optimizer.types.lambda_function_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.lambda_function_recommendation_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "fields_to_export" in value:
        import capo_compute_optimizer.types.exportable_lambda_function_fields

        out["fieldsToExport"] = (
            capo_compute_optimizer.types.exportable_lambda_function_fields.serialize_aws_json_1_0(
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
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportLambdaFunctionRecommendationsRequest:
    out: ExportLambdaFunctionRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_compute_optimizer.types.account_ids

        out["account_ids"] = (
            capo_compute_optimizer.types.account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if data.get("filters") is not None:
        import capo_compute_optimizer.types.lambda_function_recommendation_filters

        out["filters"] = (
            capo_compute_optimizer.types.lambda_function_recommendation_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if data.get("fieldsToExport") is not None:
        import capo_compute_optimizer.types.exportable_lambda_function_fields

        out["fields_to_export"] = (
            capo_compute_optimizer.types.exportable_lambda_function_fields.deserialize_aws_json_1_0(
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
            "ExportLambdaFunctionRecommendationsRequest.s3_destination_config required"
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
    return out
