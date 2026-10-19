"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.index_name
    import capo_opensearch.types.index_schema


class UpdateIndexRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    index_name: "capo_opensearch.types.index_name.IndexName"
    """<p>The name of the index to update.</p>"""
    index_schema: "capo_opensearch.types.index_schema.IndexSchema"
    """<p>The updated JSON schema for the index including any changes to mappings, settings, and semantic enrichment configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexRequest) -> dict:
    out: dict = {}
    out["IndexSchema"] = value["index_schema"]
    return out


def deserialize_json(data: dict) -> UpdateIndexRequest:
    out: UpdateIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexSchema") is not None:
        out["index_schema"] = data["IndexSchema"]
    else:
        out["index_schema"] = None
    return out
