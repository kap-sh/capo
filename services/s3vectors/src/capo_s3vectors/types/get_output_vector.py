"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetOutputVector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.vector_data
    import capo_s3vectors.types.vector_key
    import capo_s3vectors.types.vector_metadata


class GetOutputVector(TypedDict, closed=True):
    key: "capo_s3vectors.types.vector_key.VectorKey"
    """<p>The name of the vector. </p>"""
    data: NotRequired["capo_s3vectors.types.vector_data.VectorData"]
    """<p>The vector data of the vector. </p>"""
    metadata: NotRequired["capo_s3vectors.types.vector_metadata.VectorMetadata"]
    """<p>Metadata about the vector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOutputVector) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "data" in value:
        import capo_s3vectors.types.vector_data

        out["data"] = capo_s3vectors.types.vector_data.serialize_json(value["data"])
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> GetOutputVector:
    out: GetOutputVector = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("data") is not None:
        import capo_s3vectors.types.vector_data

        out["data"] = capo_s3vectors.types.vector_data.deserialize_json(data["data"])
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    return out
