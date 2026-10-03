"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#CreateDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_write.types.resource_create_api_name
    import capo_timestream_write.types.string_value2048
    import capo_timestream_write.types.tag_list


class CreateDatabaseRequest(TypedDict, closed=True):
    database_name: (
        "capo_timestream_write.types.resource_create_api_name.ResourceCreateAPIName"
    )
    """<p>The name of the Timestream database.</p>"""
    kms_key_id: NotRequired[
        "capo_timestream_write.types.string_value2048.StringValue2048"
    ]
    """<p>The KMS key for the database. If the KMS key is not specified, the database will be encrypted with a Timestream managed KMS key located in your account. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk">Amazon Web Services managed keys</a>.</p>"""
    tags: NotRequired["capo_timestream_write.types.tag_list.TagList"]
    """<p> A list of key-value pairs to label the table. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDatabaseRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_timestream_write.types.tag_list

        out["Tags"] = capo_timestream_write.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDatabaseRequest:
    out: CreateDatabaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("CreateDatabaseRequest.database_name required")
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("Tags") is not None:
        import capo_timestream_write.types.tag_list

        out["tags"] = capo_timestream_write.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
