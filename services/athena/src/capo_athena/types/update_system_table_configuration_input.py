"""Generated from Smithy shape ``com.amazonaws.athena#UpdateSystemTableConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.kms_key_arn
    import capo_athena.types.system_table_name


class UpdateSystemTableConfigurationInput(TypedDict, closed=True):
    table_name: "capo_athena.types.system_table_name.SystemTableName"
    """<p>The system table configuration to update. The only accepted value is <code>ALL</code>.</p>"""
    kms_key_arn: NotRequired["capo_athena.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key to use for encrypting the system table data. The encryption key is immutable while the system table exists, so a change takes effect only after the table has been deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSystemTableConfigurationInput) -> dict:
    out: dict = {}
    import capo_athena.types.system_table_name

    out["TableName"] = capo_athena.types.system_table_name.serialize_aws_json_1_1(
        value["table_name"]
    )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSystemTableConfigurationInput:
    out: UpdateSystemTableConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        import capo_athena.types.system_table_name

        out["table_name"] = (
            capo_athena.types.system_table_name.deserialize_aws_json_1_1(
                data["TableName"]
            )
        )
    else:
        import typing

        out["table_name"] = typing.cast(
            "capo_athena.types.system_table_name.SystemTableName", ""
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
