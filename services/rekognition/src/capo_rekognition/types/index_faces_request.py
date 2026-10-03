"""Generated from Smithy shape ``com.amazonaws.rekognition#IndexFacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.attributes
    import capo_rekognition.types.collection_id
    import capo_rekognition.types.external_image_id
    import capo_rekognition.types.image
    import capo_rekognition.types.max_faces_to_index
    import capo_rekognition.types.quality_filter


class IndexFacesRequest(TypedDict, closed=True):
    collection_id: "capo_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection to which you want to add the faces that are detected in the input images.</p>"""
    image: "capo_rekognition.types.image.Image"
    """<p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes isn't supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>"""
    external_image_id: NotRequired[
        "capo_rekognition.types.external_image_id.ExternalImageId"
    ]
    """<p>The ID you want to assign to all the faces detected in the image.</p>"""
    detection_attributes: NotRequired["capo_rekognition.types.attributes.Attributes"]
    """<p>An array of facial attributes you want to be returned. A <code>DEFAULT</code> subset of facial attributes - <code>BoundingBox</code>, <code>Confidence</code>, <code>Pose</code>, <code>Quality</code>, and <code>Landmarks</code> - will always be returned. You can request for specific facial attributes (in addition to the default list) - by using <code>["DEFAULT", "FACE_OCCLUDED"]</code> or just <code>["FACE_OCCLUDED"]</code>. You can request for all facial attributes by using <code>["ALL"]</code>. Requesting more attributes may increase response time.</p> <p>If you provide both, <code>["ALL", "DEFAULT"]</code>, the service uses a logical AND operator to determine which attributes to return (in this case, all attributes). </p>"""
    max_faces: NotRequired["capo_rekognition.types.max_faces_to_index.MaxFacesToIndex"]
    """<p>The maximum number of faces to index. The value of <code>MaxFaces</code> must be greater than or equal to 1. <code>IndexFaces</code> returns no more than 100 detected faces in an image, even if you specify a larger value for <code>MaxFaces</code>.</p> <p>If <code>IndexFaces</code> detects more faces than the value of <code>MaxFaces</code>, the faces with the lowest quality are filtered out first. If there are still more faces than the value of <code>MaxFaces</code>, the faces with the smallest bounding boxes are filtered out (up to the number that's needed to satisfy the value of <code>MaxFaces</code>). Information about the unindexed faces is available in the <code>UnindexedFaces</code> array. </p> <p>The faces that are returned by <code>IndexFaces</code> are sorted by the largest face bounding box size to the smallest size, in descending order.</p> <p> <code>MaxFaces</code> can be used with a collection associated with any version of the face model.</p>"""
    quality_filter: NotRequired["capo_rekognition.types.quality_filter.QualityFilter"]
    """<p>A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren't indexed. If you specify <code>AUTO</code>, Amazon Rekognition chooses the quality bar. If you specify <code>LOW</code>, <code>MEDIUM</code>, or <code>HIGH</code>, filtering removes all faces that don’t meet the chosen quality bar. The default value is <code>AUTO</code>. The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object that's misidentified as a face, a face that's too blurry, or a face with a pose that's too extreme to use. If you specify <code>NONE</code>, no filtering is performed. </p> <p>To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexFacesRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    import capo_rekognition.types.image

    out["Image"] = capo_rekognition.types.image.serialize_aws_json_1_1(value["image"])
    if "external_image_id" in value:
        out["ExternalImageId"] = value["external_image_id"]
    if "detection_attributes" in value:
        import capo_rekognition.types.attributes

        out["DetectionAttributes"] = (
            capo_rekognition.types.attributes.serialize_aws_json_1_1(
                value["detection_attributes"]
            )
        )
    if "max_faces" in value:
        out["MaxFaces"] = value["max_faces"]
    if "quality_filter" in value:
        import capo_rekognition.types.quality_filter

        out["QualityFilter"] = (
            capo_rekognition.types.quality_filter.serialize_aws_json_1_1(
                value["quality_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IndexFacesRequest:
    out: IndexFacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("CollectionId") is not None:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("IndexFacesRequest.collection_id required")
    if data.get("Image") is not None:
        import capo_rekognition.types.image

        out["image"] = capo_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("IndexFacesRequest.image required")
    if data.get("ExternalImageId") is not None:
        out["external_image_id"] = data["ExternalImageId"]
    if data.get("DetectionAttributes") is not None:
        import capo_rekognition.types.attributes

        out["detection_attributes"] = (
            capo_rekognition.types.attributes.deserialize_aws_json_1_1(
                data["DetectionAttributes"]
            )
        )
    if data.get("MaxFaces") is not None:
        out["max_faces"] = data["MaxFaces"]
    if data.get("QualityFilter") is not None:
        import capo_rekognition.types.quality_filter

        out["quality_filter"] = (
            capo_rekognition.types.quality_filter.deserialize_aws_json_1_1(
                data["QualityFilter"]
            )
        )
    return out
