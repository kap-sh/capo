"""Generated from Smithy shape ``com.amazonaws.neptunegraph#VectorSearchConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.vector_search_dimension


class VectorSearchConfiguration(TypedDict, closed=True):
    dimension: "capo_neptune_graph.types.vector_search_dimension.VectorSearchDimension"
    """<p>The number of dimensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchConfiguration) -> dict:
    out: dict = {}
    out["dimension"] = value["dimension"]
    return out


def deserialize_json(data: dict) -> VectorSearchConfiguration:
    out: VectorSearchConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("dimension") is not None:
        out["dimension"] = data["dimension"]
    else:
        out["dimension"] = 0
    return out
