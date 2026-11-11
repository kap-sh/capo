"""Generated from Smithy shape ``com.amazonaws.athena#CreateSystemTableConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.kms_key_arn
    import capo_athena.types.system_table_name
    import capo_athena.types.timestamp


class CreateSystemTableConfigurationOutput(TypedDict, closed=True):
    table_name: NotRequired["capo_athena.types.system_table_name.SystemTableName"]
    """<p>The system table configuration that was created. Always <code>ALL</code>.</p>"""
    kms_key_arn: NotRequired["capo_athena.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used for encrypting the system table data.</p>"""
    created_at: NotRequired["capo_athena.types.timestamp.Timestamp"]
    """<p>The date and time the system table configuration was created.</p>"""
    last_modified_at: NotRequired["capo_athena.types.timestamp.Timestamp"]
    """<p>The date and time the system table configuration was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSystemTableConfigurationOutput) -> dict:
    out: dict = {}
    if "table_name" in value:
        import capo_athena.types.system_table_name

        out["TableName"] = capo_athena.types.system_table_name.serialize_aws_json_1_1(
            value["table_name"]
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "created_at" in value:
        import capo_athena.types.timestamp

        out["CreatedAt"] = capo_athena.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "last_modified_at" in value:
        import capo_athena.types.timestamp

        out["LastModifiedAt"] = capo_athena.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSystemTableConfigurationOutput:
    out: CreateSystemTableConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        import capo_athena.types.system_table_name

        out["table_name"] = (
            capo_athena.types.system_table_name.deserialize_aws_json_1_1(
                data["TableName"]
            )
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("CreatedAt") is not None:
        import capo_athena.types.timestamp

        out["created_at"] = capo_athena.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("LastModifiedAt") is not None:
        import capo_athena.types.timestamp

        out["last_modified_at"] = capo_athena.types.timestamp.deserialize_aws_json_1_1(
            data["LastModifiedAt"]
        )
    return out
