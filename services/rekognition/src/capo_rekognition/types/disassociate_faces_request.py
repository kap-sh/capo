"""Generated from Smithy shape ``com.amazonaws.rekognition#DisassociateFacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.client_request_token
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.user_face_id_list
    import capo_rekognition.types.user_id


class DisassociateFacesRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection containing the UserID.</p>"""
    user_id: "capo_rekognition.types.user_id.UserId"
    """<p>ID for the existing UserID.</p>"""
    client_request_token: NotRequired[
        "capo_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the request to <code>DisassociateFaces</code>. If you use the same token with multiple <code>DisassociateFaces</code> requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>"""
    face_ids: "capo_rekognition.types.user_face_id_list.UserFaceIdList"
    """<p>An array of face IDs to disassociate from the UserID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFacesRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    out["UserId"] = value["user_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    import capo_rekognition.types.user_face_id_list

    out["FaceIds"] = capo_rekognition.types.user_face_id_list.serialize_aws_json_1_1(
        value["face_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFacesRequest:
    out: DisassociateFacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("CollectionId") is not None:
        out["collection_id"] = data["CollectionId"]
    else:
        out["collection_id"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("FaceIds") is not None:
        import capo_rekognition.types.user_face_id_list

        out["face_ids"] = (
            capo_rekognition.types.user_face_id_list.deserialize_aws_json_1_1(
                data["FaceIds"]
            )
        )
    else:
        out["face_ids"] = []
    return out
