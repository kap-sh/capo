"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.collection_id


class DescribeCollectionRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>The ID of the collection to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCollectionRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCollectionRequest:
    out: DescribeCollectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CollectionId") is not None:
        out["collection_id"] = data["CollectionId"]
    else:
        out["collection_id"] = ""
    return out
