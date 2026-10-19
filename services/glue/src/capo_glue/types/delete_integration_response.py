"""Generated from Smithy shape ``com.amazonaws.glue#DeleteIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_additional_encryption_context_map
    import capo_glue.types.integration_description
    import capo_glue.types.integration_error_list
    import capo_glue.types.integration_status
    import capo_glue.types.integration_tags_list
    import capo_glue.types.integration_timestamp
    import capo_glue.types.string128
    import capo_glue.types.string512
    import capo_glue.types.string2048


class DeleteIntegrationResponse(TypedDict, closed=True):
    source_arn: "capo_glue.types.string512.String512"
    """<p>The ARN of the source for the integration.</p>"""
    target_arn: "capo_glue.types.string512.String512"
    """<p>The ARN of the target for the integration.</p>"""
    integration_name: "capo_glue.types.string128.String128"
    """<p>A unique name for an integration in Glue.</p>"""
    description: NotRequired[
        "capo_glue.types.integration_description.IntegrationDescription"
    ]
    """<p>A description of the integration.</p>"""
    integration_arn: "capo_glue.types.string128.String128"
    """<p>The Amazon Resource Name (ARN) for the integration.</p>"""
    kms_key_id: NotRequired["capo_glue.types.string2048.String2048"]
    """<p>The ARN of a KMS key used for encrypting the channel.</p>"""
    additional_encryption_context: NotRequired[
        "capo_glue.types.integration_additional_encryption_context_map.IntegrationAdditionalEncryptionContextMap"
    ]
    """<p>An optional set of non-secret key–value pairs that contains additional contextual information for encryption.</p>"""
    tags: NotRequired["capo_glue.types.integration_tags_list.IntegrationTagsList"]
    """<p>Metadata assigned to the resource consisting of a list of key-value pairs.</p>"""
    status: "capo_glue.types.integration_status.IntegrationStatus"
    """<p>The status of the integration being deleted.</p> <p>The possible statuses are:</p> <ul> <li> <p>CREATING: The integration is being created.</p> </li> <li> <p>ACTIVE: The integration creation succeeds.</p> </li> <li> <p>MODIFYING: The integration is being modified.</p> </li> <li> <p>FAILED: The integration creation fails. </p> </li> <li> <p>DELETING: The integration is deleted.</p> </li> <li> <p>SYNCING: The integration is synchronizing.</p> </li> <li> <p>NEEDS_ATTENTION: The integration needs attention, such as synchronization.</p> </li> </ul>"""
    create_time: "capo_glue.types.integration_timestamp.IntegrationTimestamp"
    """<p>The time when the integration was created, in UTC.</p>"""
    errors: NotRequired["capo_glue.types.integration_error_list.IntegrationErrorList"]
    """<p>A list of errors associated with the integration.</p>"""
    data_filter: NotRequired["capo_glue.types.string2048.String2048"]
    """<p>Selects source tables for the integration using Maxwell filter syntax.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIntegrationResponse) -> dict:
    out: dict = {}
    out["SourceArn"] = value["source_arn"]
    out["TargetArn"] = value["target_arn"]
    out["IntegrationName"] = value["integration_name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["IntegrationArn"] = value["integration_arn"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "additional_encryption_context" in value:
        import capo_glue.types.integration_additional_encryption_context_map

        out["AdditionalEncryptionContext"] = (
            capo_glue.types.integration_additional_encryption_context_map.serialize_aws_json_1_1(
                value["additional_encryption_context"]
            )
        )
    if "tags" in value:
        import capo_glue.types.integration_tags_list

        out["Tags"] = capo_glue.types.integration_tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    import capo_glue.types.integration_status

    out["Status"] = capo_glue.types.integration_status.serialize_aws_json_1_1(
        value["status"]
    )
    import capo_glue.types.integration_timestamp

    out["CreateTime"] = capo_glue.types.integration_timestamp.serialize_aws_json_1_1(
        value["create_time"]
    )
    if "errors" in value:
        import capo_glue.types.integration_error_list

        out["Errors"] = capo_glue.types.integration_error_list.serialize_aws_json_1_1(
            value["errors"]
        )
    if "data_filter" in value:
        out["DataFilter"] = value["data_filter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIntegrationResponse:
    out: DeleteIntegrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    else:
        out["source_arn"] = ""
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    else:
        out["target_arn"] = ""
    if data.get("IntegrationName") is not None:
        out["integration_name"] = data["IntegrationName"]
    else:
        out["integration_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IntegrationArn") is not None:
        out["integration_arn"] = data["IntegrationArn"]
    else:
        out["integration_arn"] = ""
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("AdditionalEncryptionContext") is not None:
        import capo_glue.types.integration_additional_encryption_context_map

        out["additional_encryption_context"] = (
            capo_glue.types.integration_additional_encryption_context_map.deserialize_aws_json_1_1(
                data["AdditionalEncryptionContext"]
            )
        )
    if data.get("Tags") is not None:
        import capo_glue.types.integration_tags_list

        out["tags"] = capo_glue.types.integration_tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("Status") is not None:
        import capo_glue.types.integration_status

        out["status"] = capo_glue.types.integration_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_glue.types.integration_status.IntegrationStatus", ""
        )
    if data.get("CreateTime") is not None:
        import capo_glue.types.integration_timestamp

        out["create_time"] = (
            capo_glue.types.integration_timestamp.deserialize_aws_json_1_1(
                data["CreateTime"]
            )
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Errors") is not None:
        import capo_glue.types.integration_error_list

        out["errors"] = capo_glue.types.integration_error_list.deserialize_aws_json_1_1(
            data["Errors"]
        )
    if data.get("DataFilter") is not None:
        out["data_filter"] = data["DataFilter"]
    return out
