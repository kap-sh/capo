"""Generated from Smithy shape ``com.amazonaws.support#GetAttachmentUploadLinksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.integer
    import capo_support.types.part_size_bytes
    import capo_support.types.upload_id
    import capo_support.types.upload_url_list


class GetAttachmentUploadLinksResponse(TypedDict, closed=True):
    upload_id: "capo_support.types.upload_id.UploadId"
    """<p>The unique identifier for the multipart upload. Use this value in subsequent calls to <code>GetAttachmentUploadLinks</code>, <a>DescribeAttachmentUploadStatus</a>, and <a>CompleteAttachmentUpload</a>, and to attach the upload to a case through the <code>uploadIds</code> parameter on <a>CreateCase</a> or <a>AddCommunicationToCase</a>.</p>"""
    part_size_bytes: "capo_support.types.part_size_bytes.PartSizeBytes"
    """<p>The size, in bytes, of each part. Split the file into parts of this size before you upload them to the presigned URLs. For an upload with <code>n</code> total parts, parts 1 through <code>n</code> - 1 are exactly this size; the last part may be smaller. Maximum: 104,857,600 bytes (approximately 100 MB).</p>"""
    total_parts: "capo_support.types.integer.Integer"
    """<p>The total number of parts that the file is split into. Upload one part to each presigned URL.</p>"""
    next_index: "capo_support.types.integer.Integer"
    """<p>The next part index to request presigned URLs for. If all upload URLs for the file have been returned, this field is <code>null</code>. Use this value as the <code>startIndex</code> in <code>uploadRange</code> on a subsequent call to <code>GetAttachmentUploadLinks</code> to retrieve the next batch of upload URLs.</p>"""
    upload_urls: "capo_support.types.upload_url_list.UploadUrlList"
    """<p>The list of presigned upload URLs for the requested range of parts. The list contains at most 10 URLs per call. Upload each part to its corresponding URL by using HTTP <code>PUT</code> before the URL expires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAttachmentUploadLinksResponse) -> dict:
    out: dict = {}
    out["uploadId"] = value["upload_id"]
    out["partSizeBytes"] = value["part_size_bytes"]
    out["totalParts"] = value.get("total_parts", 0)
    out["nextIndex"] = value.get("next_index", 0)
    import capo_support.types.upload_url_list

    out["uploadUrls"] = capo_support.types.upload_url_list.serialize_aws_json_1_1(
        value["upload_urls"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAttachmentUploadLinksResponse:
    out: GetAttachmentUploadLinksResponse = {}  # type: ignore[typeddict-item]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        out["upload_id"] = ""
    if data.get("partSizeBytes") is not None:
        out["part_size_bytes"] = data["partSizeBytes"]
    else:
        out["part_size_bytes"] = 0
    if data.get("totalParts") is not None:
        out["total_parts"] = data["totalParts"]
    else:
        out["total_parts"] = 0
    if data.get("nextIndex") is not None:
        out["next_index"] = data["nextIndex"]
    else:
        out["next_index"] = 0
    if data.get("uploadUrls") is not None:
        import capo_support.types.upload_url_list

        out["upload_urls"] = (
            capo_support.types.upload_url_list.deserialize_aws_json_1_1(
                data["uploadUrls"]
            )
        )
    else:
        out["upload_urls"] = []
    return out
