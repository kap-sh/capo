"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateIngestionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.ingestion_index_name
    import capo_opensearchserverless.types.ingestion_job_name
    import capo_opensearchserverless.types.ingestion_job_source
    import capo_opensearchserverless.types.tags


class CreateIngestionJobRequest(TypedDict, closed=True):
    collection_id: "capo_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection to ingest data into.</p>"""
    ingestion_job_name: (
        "capo_opensearchserverless.types.ingestion_job_name.IngestionJobName"
    )
    """<p>The name of the ingestion job. The name must be unique within the collection.</p>"""
    index_name: (
        "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
    )
    """<p>The name of the index to ingest documents into.</p>"""
    failure_index_name: NotRequired[
        "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
    ]
    """<p>The name of the index where documents that fail to be ingested are recorded.</p>"""
    source: "capo_opensearchserverless.types.ingestion_job_source.IngestionJobSource"
    """<p>The Amazon S3 source to ingest data from.</p>"""
    tags: NotRequired["capo_opensearchserverless.types.tags.Tags"]
    """<p>An arbitrary set of tags (key–value pairs) to associate with the ingestion job.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIngestionJobRequest) -> dict:
    out: dict = {}
    out["collectionId"] = value["collection_id"]
    out["ingestionJobName"] = value["ingestion_job_name"]
    out["indexName"] = value["index_name"]
    if "failure_index_name" in value:
        out["failureIndexName"] = value["failure_index_name"]
    import capo_opensearchserverless.types.ingestion_job_source

    out["source"] = (
        capo_opensearchserverless.types.ingestion_job_source.serialize_aws_json_1_0(
            value["source"]
        )
    )
    if "tags" in value:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIngestionJobRequest:
    out: CreateIngestionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("collectionId") is not None:
        out["collection_id"] = data["collectionId"]
    else:
        out["collection_id"] = ""
    if data.get("ingestionJobName") is not None:
        out["ingestion_job_name"] = data["ingestionJobName"]
    else:
        out["ingestion_job_name"] = ""
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    else:
        out["index_name"] = ""
    if data.get("failureIndexName") is not None:
        out["failure_index_name"] = data["failureIndexName"]
    if data.get("source") is not None:
        import capo_opensearchserverless.types.ingestion_job_source

        out["source"] = (
            capo_opensearchserverless.types.ingestion_job_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    else:
        raise DeserializationError("CreateIngestionJobRequest.source required")
    if data.get("tags") is not None:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
