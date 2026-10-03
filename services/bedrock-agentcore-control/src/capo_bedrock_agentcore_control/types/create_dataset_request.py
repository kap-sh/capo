"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.data_source_type
    import capo_bedrock_agentcore_control.types.dataset_name
    import capo_bedrock_agentcore_control.types.dataset_schema_type
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.tags_map


class CreateDatasetRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    dataset_name: "capo_bedrock_agentcore_control.types.dataset_name.DatasetName"
    """<p> Human-readable name for the dataset. Must be unique within the account. Immutable after creation. </p>"""
    description: NotRequired["str"]
    """<p> A description of the dataset. </p>"""
    source: "capo_bedrock_agentcore_control.types.data_source_type.DataSourceType"
    """<p> Source of initial examples. Provide either inline examples or an S3 URI pointing to a JSONL file. </p>"""
    schema_type: (
        "capo_bedrock_agentcore_control.types.dataset_schema_type.DatasetSchemaType"
    )
    """<p> Versioned schema type governing the structure of examples. Immutable after creation. </p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p> Optional KMS key ARN for server-side encryption on service Amazon S3 writes. </p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p> A map of tag keys and values to assign to the dataset. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["datasetName"] = value["dataset_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.data_source_type

    out["source"] = (
        capo_bedrock_agentcore_control.types.data_source_type.serialize_json(
            value["source"]
        )
    )
    import capo_bedrock_agentcore_control.types.dataset_schema_type

    out["schemaType"] = (
        capo_bedrock_agentcore_control.types.dataset_schema_type.serialize_json(
            value["schema_type"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("datasetName") is not None:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("source") is not None:
        import capo_bedrock_agentcore_control.types.data_source_type

        out["source"] = (
            capo_bedrock_agentcore_control.types.data_source_type.deserialize_json(
                data["source"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetRequest.source required")
    if data.get("schemaType") is not None:
        import capo_bedrock_agentcore_control.types.dataset_schema_type

        out["schema_type"] = (
            capo_bedrock_agentcore_control.types.dataset_schema_type.deserialize_json(
                data["schemaType"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetRequest.schema_type required")
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
