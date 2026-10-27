"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateIngestionStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.ingestion_index_name
    import capo_opensearchserverless.types.ingestion_stream_name
    import capo_opensearchserverless.types.ingestion_stream_source
    import capo_opensearchserverless.types.role_arn
    import capo_opensearchserverless.types.tags


class CreateIngestionStreamRequest(TypedDict, closed=True):
    collection_id: "capo_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection to ingest data into.</p>"""
    ingestion_stream_name: (
        "capo_opensearchserverless.types.ingestion_stream_name.IngestionStreamName"
    )
    """<p>The name of the ingestion stream. The name must be unique within the collection.</p>"""
    index_name: (
        "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
    )
    """<p>The name of the index to ingest documents into.</p>"""
    failure_index_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
    ]
    """<p>The name of the index where documents that fail to be ingested are recorded.</p>"""
    source: (
        "capo_opensearchserverless.types.ingestion_stream_source.IngestionStreamSource"
    )
    """<p>The Amazon S3 source to ingest data from, including the Amazon SQS queue that receives S3 event notifications.</p>"""
    role_arn: "capo_opensearchserverless.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that OpenSearch Serverless assumes to read data from the source. The role must be in the same account as the collection.</p>"""
    tags: NotRequired["capo_opensearchserverless.types.tags.Tags"]
    """<p>An arbitrary set of tags (key–value pairs) to associate with the ingestion stream.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIngestionStreamRequest) -> dict:
    out: dict = {}
    out["collectionId"] = value["collection_id"]
    out["ingestionStreamName"] = value["ingestion_stream_name"]
    out["indexName"] = value["index_name"]
    if "failure_index_name" in value:
        out["failureIndexName"] = value["failure_index_name"]
    import capo_opensearchserverless.types.ingestion_stream_source

    out["source"] = (
        capo_opensearchserverless.types.ingestion_stream_source.serialize_aws_json_1_0(
            value["source"]
        )
    )
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIngestionStreamRequest:
    out: CreateIngestionStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("collectionId") is not None:
        out["collection_id"] = data["collectionId"]
    else:
        out["collection_id"] = ""
    if data.get("ingestionStreamName") is not None:
        out["ingestion_stream_name"] = data["ingestionStreamName"]
    else:
        out["ingestion_stream_name"] = ""
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    else:
        out["index_name"] = ""
    if data.get("failureIndexName") is not None:
        out["failure_index_name"] = data["failureIndexName"]
    if data.get("source") is not None:
        import capo_opensearchserverless.types.ingestion_stream_source

        out["source"] = (
            capo_opensearchserverless.types.ingestion_stream_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    else:
        raise DeserializationError("CreateIngestionStreamRequest.source required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("tags") is not None:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
