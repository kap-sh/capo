"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.client_request_token
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.user_id


class CreateUserRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection to which the new UserID needs to be created.</p>"""
    user_id: "capo_rekognition.types.user_id.UserId"
    """<p>ID for the UserID to be created. This ID needs to be unique within the collection.</p>"""
    client_request_token: NotRequired[
        "capo_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the request to <code>CreateUser</code>. If you use the same token with multiple <code>CreateUser</code> requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    out["UserId"] = value["user_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
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
