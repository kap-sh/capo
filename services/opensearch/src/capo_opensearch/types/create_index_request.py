"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.index_name
    import capo_opensearch.types.index_schema


class CreateIndexRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    index_name: "capo_opensearch.types.index_name.IndexName"
    """<p>The name of the index to create. Must be between 1 and 255 characters and follow OpenSearch naming conventions.</p>"""
    index_schema: "capo_opensearch.types.index_schema.IndexSchema"
    """<p>The JSON schema defining index mappings, settings, and semantic enrichment configuration. The schema specifies which text fields should be automatically enriched for semantic search capabilities and includes OpenSearch index configuration parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexRequest) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    out["IndexSchema"] = value["index_schema"]
    return out


def deserialize_json(data: dict) -> CreateIndexRequest:
    out: CreateIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        out["index_name"] = ""
    if data.get("IndexSchema") is not None:
        out["index_schema"] = data["IndexSchema"]
    else:
        out["index_schema"] = None
    return out
