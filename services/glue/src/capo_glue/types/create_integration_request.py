"""Generated from Smithy shape ``com.amazonaws.glue#CreateIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_additional_encryption_context_map
    import capo_glue.types.integration_config
    import capo_glue.types.integration_description
    import capo_glue.types.integration_tags_list
    import capo_glue.types.string128
    import capo_glue.types.string512
    import capo_glue.types.string2048


class CreateIntegrationRequest(TypedDict, closed=True):
    integration_name: "capo_glue.types.string128.String128"
    """<p>A unique name for an integration in Glue.</p>"""
    source_arn: "capo_glue.types.string512.String512"
    """<p>The ARN of the source resource for the integration.</p>"""
    target_arn: "capo_glue.types.string512.String512"
    """<p>The ARN of the target resource for the integration.</p>"""
    description: NotRequired[
        "capo_glue.types.integration_description.IntegrationDescription"
    ]
    """<p>A description of the integration.</p>"""
    data_filter: NotRequired["capo_glue.types.string2048.String2048"]
    """<p>Selects source tables for the integration using Maxwell filter syntax.</p>"""
    kms_key_id: NotRequired["capo_glue.types.string2048.String2048"]
    """<p>The ARN of a KMS key used for encrypting the channel.</p>"""
    additional_encryption_context: NotRequired[
        "capo_glue.types.integration_additional_encryption_context_map.IntegrationAdditionalEncryptionContextMap"
    ]
    """<p>An optional set of non-secret key–value pairs that contains additional contextual information for encryption. This can only be provided if <code>KMSKeyId</code> is provided.</p>"""
    tags: NotRequired["capo_glue.types.integration_tags_list.IntegrationTagsList"]
    """<p>Metadata assigned to the resource consisting of a list of key-value pairs.</p>"""
    integration_config: NotRequired[
        "capo_glue.types.integration_config.IntegrationConfig"
    ]
    """<p>The configuration settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIntegrationRequest) -> dict:
    out: dict = {}
    out["IntegrationName"] = value["integration_name"]
    out["SourceArn"] = value["source_arn"]
    out["TargetArn"] = value["target_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "data_filter" in value:
        out["DataFilter"] = value["data_filter"]
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
    if "integration_config" in value:
        import capo_glue.types.integration_config

        out["IntegrationConfig"] = (
            capo_glue.types.integration_config.serialize_aws_json_1_1(
                value["integration_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIntegrationRequest:
    out: CreateIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("IntegrationName") is not None:
        out["integration_name"] = data["IntegrationName"]
    else:
        out["integration_name"] = ""
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    else:
        out["source_arn"] = ""
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    else:
        out["target_arn"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DataFilter") is not None:
        out["data_filter"] = data["DataFilter"]
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
    if data.get("IntegrationConfig") is not None:
        import capo_glue.types.integration_config

        out["integration_config"] = (
            capo_glue.types.integration_config.deserialize_aws_json_1_1(
                data["IntegrationConfig"]
            )
        )
    return out
