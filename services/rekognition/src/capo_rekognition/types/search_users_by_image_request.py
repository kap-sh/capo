"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchUsersByImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.image
    import capo_rekognition.types.max_user_results
    import capo_rekognition.types.percent
    import capo_rekognition.types.quality_filter


class SearchUsersByImageRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection containing the UserID.</p>"""
    image: "capo_rekognition.types.image.Image"
    user_match_threshold: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Specifies the minimum confidence in the UserID match to return. Default value is 80.</p>"""
    max_users: NotRequired["capo_rekognition.types.max_user_results.MaxUserResults"]
    """<p>Maximum number of UserIDs to return.</p>"""
    quality_filter: NotRequired["capo_rekognition.types.quality_filter.QualityFilter"]
    """<p>A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren't searched for in the collection. The default value is NONE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchUsersByImageRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    import capo_rekognition.types.image

    out["Image"] = capo_rekognition.types.image.serialize_aws_json_1_1(value["image"])
    if "user_match_threshold" in value:
        out["UserMatchThreshold"] = (
            "NaN"
            if value["user_match_threshold"] != value["user_match_threshold"]
            else "Infinity"
            if value["user_match_threshold"] == float("inf")
            else "-Infinity"
            if value["user_match_threshold"] == float("-inf")
            else value["user_match_threshold"]
        )
    if "max_users" in value:
        out["MaxUsers"] = value["max_users"]
    if "quality_filter" in value:
        import capo_rekognition.types.quality_filter

        out["QualityFilter"] = (
            capo_rekognition.types.quality_filter.serialize_aws_json_1_1(
                value["quality_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchUsersByImageRequest:
    out: SearchUsersByImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("CollectionId") is not None:
        out["collection_id"] = data["CollectionId"]
    else:
        out["collection_id"] = ""
    if data.get("Image") is not None:
        import capo_rekognition.types.image

        out["image"] = capo_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("SearchUsersByImageRequest.image required")
    if data.get("UserMatchThreshold") is not None:
        out["user_match_threshold"] = float(data["UserMatchThreshold"])
    if data.get("MaxUsers") is not None:
        out["max_users"] = data["MaxUsers"]
    if data.get("QualityFilter") is not None:
        import capo_rekognition.types.quality_filter

        out["quality_filter"] = (
            capo_rekognition.types.quality_filter.deserialize_aws_json_1_1(
                data["QualityFilter"]
            )
        )
    return out
