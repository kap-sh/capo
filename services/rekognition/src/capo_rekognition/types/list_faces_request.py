"""Generated from Smithy shape ``com.amazonaws.rekognition#ListFacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.face_id_list
    import capo_rekognition.types.page_size
    import capo_rekognition.types.pagination_token
    import capo_rekognition.types.user_id


class ListFacesRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>ID of the collection from which to list the faces.</p>"""
    next_token: NotRequired["capo_rekognition.types.pagination_token.PaginationToken"]
    """<p>If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of faces.</p>"""
    max_results: NotRequired["capo_rekognition.types.page_size.PageSize"]
    """<p>Maximum number of faces to return.</p>"""
    user_id: NotRequired["capo_rekognition.types.user_id.UserId"]
    """<p>An array of user IDs to filter results with when listing faces in a collection.</p>"""
    face_ids: NotRequired["capo_rekognition.types.face_id_list.FaceIdList"]
    """<p>An array of face IDs to filter results with when listing faces in a collection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFacesRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "face_ids" in value:
        import capo_rekognition.types.face_id_list

        out["FaceIds"] = capo_rekognition.types.face_id_list.serialize_aws_json_1_1(
            value["face_ids"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFacesRequest:
    out: ListFacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("CollectionId") is not None:
        out["collection_id"] = data["CollectionId"]
    else:
        out["collection_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("FaceIds") is not None:
        import capo_rekognition.types.face_id_list

        out["face_ids"] = capo_rekognition.types.face_id_list.deserialize_aws_json_1_1(
            data["FaceIds"]
        )
    return out
