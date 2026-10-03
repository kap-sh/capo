"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.boolean
    import capo_s3_control.types.non_empty_max_length1024_string
    import capo_s3_control.types.s3_content_length
    import capo_s3_control.types.s3_sse_algorithm
    import capo_s3_control.types.s3_user_metadata
    import capo_s3_control.types.time_stamp


class S3ObjectMetadata(TypedDict, closed=True):
    cache_control: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p></p>"""
    content_disposition: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p></p>"""
    content_encoding: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p></p>"""
    content_language: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p></p>"""
    user_metadata: NotRequired["capo_s3_control.types.s3_user_metadata.S3UserMetadata"]
    """<p></p>"""
    content_length: NotRequired[
        "capo_s3_control.types.s3_content_length.S3ContentLength"
    ]
    """<p> <i>This member has been deprecated.</i> </p> <p></p>"""
    content_md5: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p> <i>This member has been deprecated.</i> </p> <p></p>"""
    content_type: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p></p>"""
    http_expires_date: NotRequired["capo_s3_control.types.time_stamp.TimeStamp"]
    """<p></p>"""
    requester_charged: "capo_s3_control.types.boolean.Boolean"
    """<p> <i>This member has been deprecated.</i> </p> <p></p>"""
    sse_algorithm: NotRequired["capo_s3_control.types.s3_sse_algorithm.S3SSEAlgorithm"]
    """<p>The server-side encryption algorithm used when storing objects in Amazon S3.</p> <p> <b>Directory buckets </b> - For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (<code>AES256</code>) and server-side encryption with KMS keys (SSE-KMS) (<code>KMS</code>). For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html">Protecting data with server-side encryption</a> in the <i>Amazon S3 User Guide</i>. For <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops">the Copy operation in Batch Operations</a>, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3CopyObjectOperation.html">S3CopyObjectOperation</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3ObjectMetadata, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "cache_control" in value:
        SubElement(el, "CacheControl").text = str(value["cache_control"])
    if "content_disposition" in value:
        SubElement(el, "ContentDisposition").text = str(value["content_disposition"])
    if "content_encoding" in value:
        SubElement(el, "ContentEncoding").text = str(value["content_encoding"])
    if "content_language" in value:
        SubElement(el, "ContentLanguage").text = str(value["content_language"])
    if "user_metadata" in value:
        import capo_s3_control.types.s3_user_metadata

        capo_s3_control.types.s3_user_metadata.serialize_xml(
            value["user_metadata"], el, "UserMetadata"
        )
    if "content_length" in value:
        SubElement(el, "ContentLength").text = str(value["content_length"])
    if "content_md5" in value:
        SubElement(el, "ContentMD5").text = str(value["content_md5"])
    if "content_type" in value:
        SubElement(el, "ContentType").text = str(value["content_type"])
    if "http_expires_date" in value:
        import capo_s3_control.types.time_stamp

        capo_s3_control.types.time_stamp.serialize_xml(
            value["http_expires_date"], el, "HttpExpiresDate"
        )
    SubElement(el, "RequesterCharged").text = (
        "true" if value.get("requester_charged", False) else "false"
    )
    if "sse_algorithm" in value:
        import capo_s3_control.types.s3_sse_algorithm

        capo_s3_control.types.s3_sse_algorithm.serialize_xml(
            value["sse_algorithm"], el, "SSEAlgorithm"
        )


def deserialize_xml(el: Element) -> S3ObjectMetadata:
    out: S3ObjectMetadata = {}  # type: ignore[typeddict-item]
    child_cache_control = el.find("CacheControl")
    if child_cache_control is not None:
        out["cache_control"] = str(child_cache_control.text or "")
    child_content_disposition = el.find("ContentDisposition")
    if child_content_disposition is not None:
        out["content_disposition"] = str(child_content_disposition.text or "")
    child_content_encoding = el.find("ContentEncoding")
    if child_content_encoding is not None:
        out["content_encoding"] = str(child_content_encoding.text or "")
    child_content_language = el.find("ContentLanguage")
    if child_content_language is not None:
        out["content_language"] = str(child_content_language.text or "")
    child_user_metadata = el.find("UserMetadata")
    if child_user_metadata is not None:
        import capo_s3_control.types.s3_user_metadata

        out["user_metadata"] = capo_s3_control.types.s3_user_metadata.deserialize_xml(
            child_user_metadata
        )
    child_content_length = el.find("ContentLength")
    if child_content_length is not None:
        out["content_length"] = int(child_content_length.text or "")
    child_content_md5 = el.find("ContentMD5")
    if child_content_md5 is not None:
        out["content_md5"] = str(child_content_md5.text or "")
    child_content_type = el.find("ContentType")
    if child_content_type is not None:
        out["content_type"] = str(child_content_type.text or "")
    child_http_expires_date = el.find("HttpExpiresDate")
    if child_http_expires_date is not None:
        import capo_s3_control.types.time_stamp

        out["http_expires_date"] = capo_s3_control.types.time_stamp.deserialize_xml(
            child_http_expires_date
        )
    child_requester_charged = el.find("RequesterCharged")
    if child_requester_charged is not None:
        out["requester_charged"] = (
            child_requester_charged.text or ""
        ).lower() == "true"
    else:
        out["requester_charged"] = False
    child_sse_algorithm = el.find("SSEAlgorithm")
    if child_sse_algorithm is not None:
        import capo_s3_control.types.s3_sse_algorithm

        out["sse_algorithm"] = capo_s3_control.types.s3_sse_algorithm.deserialize_xml(
            child_sse_algorithm
        )
    return out
