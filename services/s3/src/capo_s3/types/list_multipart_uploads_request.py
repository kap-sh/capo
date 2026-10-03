"""Generated from Smithy shape ``com.amazonaws.s3#ListMultipartUploadsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.delimiter
    import capo_s3.types.encoding_type
    import capo_s3.types.key_marker
    import capo_s3.types.max_uploads
    import capo_s3.types.prefix
    import capo_s3.types.request_payer
    import capo_s3.types.upload_id_marker


class ListMultipartUploadsRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket to which the multipart upload was initiated. </p> <p> <b>Directory buckets</b> - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format <code> <i>Bucket-name</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>amzn-s3-demo-bucket</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Object Lambda access points are not supported by directory buckets.</p> </note> <p> <b>S3 on Outposts</b> - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.<i>outpostID</i>.s3-outposts.<i>Region</i>.amazonaws.com</code>. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">What is S3 on Outposts?</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    delimiter: NotRequired["capo_s3.types.delimiter.Delimiter"]
    """<p>Character you use to group keys.</p> <p>All keys that contain the same string between the prefix, if specified, and the first occurrence of the delimiter after the prefix are grouped under a single result element, <code>CommonPrefixes</code>. If you don't specify the prefix parameter, then the substring starts at the beginning of the key. The keys that are grouped under <code>CommonPrefixes</code> result element are not returned elsewhere in the response.</p> <p> <code>CommonPrefixes</code> is filtered out from results if it is not lexicographically greater than the key-marker.</p> <note> <p> <b>Directory buckets</b> - For directory buckets, <code>/</code> is the only supported delimiter.</p> </note>"""
    encoding_type: NotRequired["capo_s3.types.encoding_type.EncodingType"]
    key_marker: NotRequired["capo_s3.types.key_marker.KeyMarker"]
    """<p>Specifies the multipart upload after which listing should begin.</p> <note> <ul> <li> <p> <b>General purpose buckets</b> - For general purpose buckets, <code>key-marker</code> is an object key. Together with <code>upload-id-marker</code>, this parameter specifies the multipart upload after which listing should begin.</p> <p>If <code>upload-id-marker</code> is not specified, only the keys lexicographically greater than the specified <code>key-marker</code> will be included in the list.</p> <p>If <code>upload-id-marker</code> is specified, any multipart uploads for a key equal to the <code>key-marker</code> might also be included, provided those multipart uploads have upload IDs lexicographically greater than the specified <code>upload-id-marker</code>.</p> </li> <li> <p> <b>Directory buckets</b> - For directory buckets, <code>key-marker</code> is obfuscated and isn't a real object key. The <code>upload-id-marker</code> parameter isn't supported by directory buckets. To list the additional multipart uploads, you only need to set the value of <code>key-marker</code> to the <code>NextKeyMarker</code> value from the previous response. </p> <p>In the <code>ListMultipartUploads</code> response, the multipart uploads aren't sorted lexicographically based on the object keys. </p> </li> </ul> </note>"""
    max_uploads: NotRequired["capo_s3.types.max_uploads.MaxUploads"]
    """<p>Sets the maximum number of multipart uploads, from 1 to 1,000, to return in the response body. 1,000 is the maximum number of uploads that can be returned in a response.</p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>Lists in-progress uploads only for those keys that begin with the specified prefix. You can use prefixes to separate a bucket into different grouping of keys. (You can think of using <code>prefix</code> to make groups in the same way that you'd use a folder in a file system.)</p> <note> <p> <b>Directory buckets</b> - For directory buckets, only prefixes that end in a delimiter (<code>/</code>) are supported.</p> </note>"""
    upload_id_marker: NotRequired["capo_s3.types.upload_id_marker.UploadIdMarker"]
    """<p>Together with key-marker, specifies the multipart upload after which listing should begin. If key-marker is not specified, the upload-id-marker parameter is ignored. Otherwise, any multipart uploads for a key equal to the key-marker might be included in the list only if they have an upload ID lexicographically greater than the specified <code>upload-id-marker</code>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]


# --- restXml ser/de ---
def serialize_xml(
    value: ListMultipartUploadsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListMultipartUploadsRequest:
    out: ListMultipartUploadsRequest = {}  # type: ignore[typeddict-item]
    return out
