"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.face_id
    import capo_rekognition.types.max_user_results
    import capo_rekognition.types.percent
    import capo_rekognition.types.user_id


class SearchUsersRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection containing the UserID, used with a UserId or FaceId. If a FaceId is provided, UserId isn’t required to be present in the Collection.</p>"""
    user_id: NotRequired["capo_rekognition.types.user_id.UserId"]
    """<p>ID for the existing User.</p>"""
    face_id: NotRequired["capo_rekognition.types.face_id.FaceId"]
    """<p>ID for the existing face.</p>"""
    user_match_threshold: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Optional value that specifies the minimum confidence in the matched UserID to return. Default value of 80.</p>"""
    max_users: NotRequired["capo_rekognition.types.max_user_results.MaxUserResults"]
    """<p>Maximum number of identities to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchUsersRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "face_id" in value:
        out["FaceId"] = value["face_id"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchUsersRequest:
    out: SearchUsersRequest = {}  # type: ignore[typeddict-item]
    if data.get("CollectionId") is not None:
        out["collection_id"] = data["CollectionId"]
    else:
        out["collection_id"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("FaceId") is not None:
        out["face_id"] = data["FaceId"]
    if data.get("UserMatchThreshold") is not None:
        out["user_match_threshold"] = float(data["UserMatchThreshold"])
    if data.get("MaxUsers") is not None:
        out["max_users"] = data["MaxUsers"]
    return out
