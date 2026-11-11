"""Generated from Smithy shape ``com.amazonaws.athena#CreateSystemTableConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.idempotency_token
    import capo_athena.types.kms_key_arn
    import capo_athena.types.system_table_name
    import capo_athena.types.tag_list


class CreateSystemTableConfigurationInput(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_athena.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique case-sensitive string used to ensure the request to create the system table configuration is idempotent (executes only once). If another <code>CreateSystemTableConfiguration</code> request is received with the same client token but different parameters, the request fails with an <code>InvalidRequestException</code>.</p>"""
    table_name: "capo_athena.types.system_table_name.SystemTableName"
    """<p>The system table configuration to create. The only accepted value is <code>ALL</code>, the reserved keyword that enables all system tables for the account.</p>"""
    kms_key_arn: NotRequired["capo_athena.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key to use for encrypting the system table data.</p>"""
    tags: NotRequired["capo_athena.types.tag_list.TagList"]
    """<p>The tags to add to the system table configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSystemTableConfigurationInput) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    import capo_athena.types.system_table_name

    out["TableName"] = capo_athena.types.system_table_name.serialize_aws_json_1_1(
        value["table_name"]
    )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import capo_athena.types.tag_list

        out["Tags"] = capo_athena.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSystemTableConfigurationInput:
    out: CreateSystemTableConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
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
    if data.get("Tags") is not None:
        import capo_athena.types.tag_list

        out["tags"] = capo_athena.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
