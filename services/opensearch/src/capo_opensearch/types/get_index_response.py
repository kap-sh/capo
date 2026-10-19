"""Generated from Smithy shape ``com.amazonaws.opensearch#GetIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.index_schema


class GetIndexResponse(TypedDict, closed=True):
    index_schema: "capo_opensearch.types.index_schema.IndexSchema"
    """<p>The JSON schema of the index including mappings, settings, and semantic enrichment configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexResponse) -> dict:
    out: dict = {}
    out["IndexSchema"] = value["index_schema"]
    return out


def deserialize_json(data: dict) -> GetIndexResponse:
    out: GetIndexResponse = {}  # type: ignore[typeddict-item]
    if data.get("IndexSchema") is not None:
        out["index_schema"] = data["IndexSchema"]
    else:
        out["index_schema"] = None
    return out
