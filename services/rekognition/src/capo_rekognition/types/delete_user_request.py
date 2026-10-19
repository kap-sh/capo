"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.client_request_token
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.user_id


class DeleteUserRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection from which the UserID needs to be deleted. </p>"""
    user_id: "capo_rekognition.types.user_id.UserId"
    """<p>ID for the UserID to be deleted. </p>"""
    client_request_token: NotRequired[
        "capo_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the request to <code>DeleteUser</code>. If you use the same token with multiple <code>DeleteUser </code>requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    out["UserId"] = value["user_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
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
    return out
