"""Generated from Smithy shape ``com.amazonaws.bedrockagent#OpenSearchServerlessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.open_search_serverless_collection_arn
    import capo_bedrock_agent.types.open_search_serverless_field_mapping
    import capo_bedrock_agent.types.open_search_serverless_index_name


class OpenSearchServerlessConfiguration(TypedDict, closed=True):
    collection_arn: "capo_bedrock_agent.types.open_search_serverless_collection_arn.OpenSearchServerlessCollectionArn"
    """<p>The Amazon Resource Name (ARN) of the OpenSearch Service vector store.</p>"""
    vector_index_name: "capo_bedrock_agent.types.open_search_serverless_index_name.OpenSearchServerlessIndexName"
    """<p>The name of the vector store.</p>"""
    field_mapping: "capo_bedrock_agent.types.open_search_serverless_field_mapping.OpenSearchServerlessFieldMapping"
    """<p>Contains the names of the fields to which to map information about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenSearchServerlessConfiguration) -> dict:
    out: dict = {}
    out["collectionArn"] = value["collection_arn"]
    out["vectorIndexName"] = value["vector_index_name"]
    import capo_bedrock_agent.types.open_search_serverless_field_mapping

    out["fieldMapping"] = (
        capo_bedrock_agent.types.open_search_serverless_field_mapping.serialize_json(
            value["field_mapping"]
        )
    )
    return out


def deserialize_json(data: dict) -> OpenSearchServerlessConfiguration:
    out: OpenSearchServerlessConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("collectionArn") is not None:
        out["collection_arn"] = data["collectionArn"]
    else:
        out["collection_arn"] = ""
    if data.get("vectorIndexName") is not None:
        out["vector_index_name"] = data["vectorIndexName"]
    else:
        out["vector_index_name"] = ""
    if data.get("fieldMapping") is not None:
        import capo_bedrock_agent.types.open_search_serverless_field_mapping

        out["field_mapping"] = (
            capo_bedrock_agent.types.open_search_serverless_field_mapping.deserialize_json(
                data["fieldMapping"]
            )
        )
    else:
        raise DeserializationError(
            "OpenSearchServerlessConfiguration.field_mapping required"
        )
    return out
