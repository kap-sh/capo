"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LookupTableConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.kms_key_id
    import capo_cloudwatch_logs.types.lookup_table_description
    import capo_cloudwatch_logs.types.lookup_table_name
    import capo_cloudwatch_logs.types.role_arn
    import capo_cloudwatch_logs.types.tags


class LookupTableConfiguration(TypedDict, closed=True):
    table_name: "capo_cloudwatch_logs.types.lookup_table_name.LookupTableName"
    """<p>The name of the lookup table to create or update with query results. The name can contain only alphanumeric characters and underscores.</p>"""
    role_arn: "capo_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that grants permissions to create or update the lookup table with query results.</p>"""
    description: NotRequired[
        "capo_cloudwatch_logs.types.lookup_table_description.LookupTableDescription"
    ]
    """<p>A description of the lookup table.</p>"""
    kms_key_id: NotRequired["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key to use to encrypt the lookup table data. If you don't specify a key, the data is encrypted with an Amazon Web Services-owned key.</p>"""
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>Key-value pairs to associate with the lookup table for resource management and cost allocation. The service applies tags only during initial table creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LookupTableConfiguration) -> dict:
    out: dict = {}
    out["tableName"] = value["table_name"]
    out["roleArn"] = value["role_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LookupTableConfiguration:
    out: LookupTableConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
