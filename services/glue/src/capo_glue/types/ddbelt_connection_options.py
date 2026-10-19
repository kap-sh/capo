"""Generated from Smithy shape ``com.amazonaws.glue#DDBELTConnectionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boolean_value
    import capo_glue.types.ddb_export_type
    import capo_glue.types.enclosed_in_string_property


class DDBELTConnectionOptions(TypedDict, closed=True):
    dynamodb_export: NotRequired["capo_glue.types.ddb_export_type.DdbExportType"]
    """<p>Specifies the export type for DynamoDB data extraction. This parameter determines how data is exported from the DynamoDB table during the ELT process.</p>"""
    dynamodb_unnest_ddb_json: "capo_glue.types.boolean_value.BooleanValue"
    """<p>A boolean value that specifies whether to unnest DynamoDB JSON format during data extraction. When set to <code>true</code>, the connector will flatten nested JSON structures from DynamoDB items. When set to <code>false</code>, the original DynamoDB JSON structure is preserved.</p>"""
    dynamodb_table_arn: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The Amazon Resource Name (ARN) of the DynamoDB table to extract data from. This parameter specifies the source table for the ELT operation. </p>"""
    dynamodb_s3_bucket: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The name of the Amazon S3 bucket used for intermediate storage during the DynamoDB ELT process. This bucket is used to temporarily store exported DynamoDB data before it is processed by the ELT job.</p>"""
    dynamodb_s3_prefix: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The S3 object key prefix for files stored in the intermediate S3 bucket during the DynamoDB ELT process. This prefix helps organize and identify the temporary files created during data extraction.</p>"""
    dynamodb_s3_bucket_owner: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The Amazon Web Services account ID of the owner of the S3 bucket specified in <code>DynamodbS3Bucket</code>. This parameter is required when the S3 bucket is owned by a different Amazon Web Services account than the one running the ELT job, enabling cross-account access to the intermediate storage bucket.</p>"""
    dynamodb_sts_role_arn: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Security Token Service (STS) role to assume for accessing DynamoDB and S3 resources during the ELT operation. This role must have the necessary permissions to read from the DynamoDB table and write to the intermediate S3 bucket. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DDBELTConnectionOptions) -> dict:
    out: dict = {}
    if "dynamodb_export" in value:
        import capo_glue.types.ddb_export_type

        out["DynamodbExport"] = capo_glue.types.ddb_export_type.serialize_aws_json_1_1(
            value["dynamodb_export"]
        )
    out["DynamodbUnnestDDBJson"] = value.get("dynamodb_unnest_ddb_json", False)
    out["DynamodbTableArn"] = value["dynamodb_table_arn"]
    if "dynamodb_s3_bucket" in value:
        out["DynamodbS3Bucket"] = value["dynamodb_s3_bucket"]
    if "dynamodb_s3_prefix" in value:
        out["DynamodbS3Prefix"] = value["dynamodb_s3_prefix"]
    if "dynamodb_s3_bucket_owner" in value:
        out["DynamodbS3BucketOwner"] = value["dynamodb_s3_bucket_owner"]
    if "dynamodb_sts_role_arn" in value:
        out["DynamodbStsRoleArn"] = value["dynamodb_sts_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DDBELTConnectionOptions:
    out: DDBELTConnectionOptions = {}  # type: ignore[typeddict-item]
    if data.get("DynamodbExport") is not None:
        import capo_glue.types.ddb_export_type

        out["dynamodb_export"] = (
            capo_glue.types.ddb_export_type.deserialize_aws_json_1_1(
                data["DynamodbExport"]
            )
        )
    if data.get("DynamodbUnnestDDBJson") is not None:
        out["dynamodb_unnest_ddb_json"] = data["DynamodbUnnestDDBJson"]
    else:
        out["dynamodb_unnest_ddb_json"] = False
    if data.get("DynamodbTableArn") is not None:
        out["dynamodb_table_arn"] = data["DynamodbTableArn"]
    else:
        out["dynamodb_table_arn"] = ""
    if data.get("DynamodbS3Bucket") is not None:
        out["dynamodb_s3_bucket"] = data["DynamodbS3Bucket"]
    if data.get("DynamodbS3Prefix") is not None:
        out["dynamodb_s3_prefix"] = data["DynamodbS3Prefix"]
    if data.get("DynamodbS3BucketOwner") is not None:
        out["dynamodb_s3_bucket_owner"] = data["DynamodbS3BucketOwner"]
    if data.get("DynamodbStsRoleArn") is not None:
        out["dynamodb_sts_role_arn"] = data["DynamodbStsRoleArn"]
    return out
