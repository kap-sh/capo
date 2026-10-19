"""Generated from Smithy shape ``com.amazonaws.rekognition#AssociateFacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.client_request_token
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.percent
    import capo_rekognition.types.user_face_id_list
    import capo_rekognition.types.user_id


class AssociateFacesRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection containing the UserID.</p>"""
    user_id: "capo_rekognition.types.user_id.UserId"
    """<p>The ID for the existing UserID.</p>"""
    face_ids: "capo_rekognition.types.user_face_id_list.UserFaceIdList"
    """<p>An array of FaceIDs to associate with the UserID.</p>"""
    user_match_threshold: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>An optional value specifying the minimum confidence in the UserID match to return. The default value is 75.</p>"""
    client_request_token: NotRequired[
        "capo_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the request to <code>AssociateFaces</code>. If you use the same token with multiple <code>AssociateFaces</code> requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateFacesRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    out["UserId"] = value["user_id"]
    import capo_rekognition.types.user_face_id_list

    out["FaceIds"] = capo_rekognition.types.user_face_id_list.serialize_aws_json_1_1(
        value["face_ids"]
    )
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
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateFacesRequest:
    out: AssociateFacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("CollectionId") is not None:
        out["collection_id"] = data["CollectionId"]
    else:
        out["collection_id"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
    if data.get("FaceIds") is not None:
        import capo_rekognition.types.user_face_id_list

        out["face_ids"] = (
            capo_rekognition.types.user_face_id_list.deserialize_aws_json_1_1(
                data["FaceIds"]
            )
        )
    else:
        out["face_ids"] = []
    if data.get("UserMatchThreshold") is not None:
        out["user_match_threshold"] = float(data["UserMatchThreshold"])
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
