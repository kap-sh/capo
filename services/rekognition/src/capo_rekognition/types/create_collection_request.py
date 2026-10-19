"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.tag_map


class CreateCollectionRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>ID for the collection that you are creating.</p>"""
    tags: NotRequired["capo_rekognition.types.tag_map.TagMap"]
    """<p> A set of tags (key-value pairs) that you want to attach to the collection. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCollectionRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    if "tags" in value:
        import capo_rekognition.types.tag_map

        out["Tags"] = capo_rekognition.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCollectionRequest:
    out: CreateCollectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CollectionId") is not None:
        out["collection_id"] = data["CollectionId"]
    else:
        out["collection_id"] = ""
    if data.get("Tags") is not None:
        import capo_rekognition.types.tag_map

        out["tags"] = capo_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
