"""Generated from Smithy shape ``com.amazonaws.s3#ListObjectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.delimiter
    import capo_s3.types.encoding_type
    import capo_s3.types.marker
    import capo_s3.types.max_keys
    import capo_s3.types.optional_object_attributes_list
    import capo_s3.types.prefix
    import capo_s3.types.request_payer


class ListObjectsRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket containing the objects.</p> <p> <b>Directory buckets</b> - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format <code> <i>Bucket-name</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>amzn-s3-demo-bucket</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Object Lambda access points are not supported by directory buckets.</p> </note> <p> <b>S3 on Outposts</b> - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.<i>outpostID</i>.s3-outposts.<i>Region</i>.amazonaws.com</code>. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">What is S3 on Outposts?</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    delimiter: NotRequired["capo_s3.types.delimiter.Delimiter"]
    """<p>A delimiter is a character that you use to group keys.</p> <p> <code>CommonPrefixes</code> is filtered out from results if it is not lexicographically greater than the key-marker.</p>"""
    encoding_type: NotRequired["capo_s3.types.encoding_type.EncodingType"]
    marker: NotRequired["capo_s3.types.marker.Marker"]
    """<p>Marker is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. Marker can be any key in the bucket.</p>"""
    max_keys: NotRequired["capo_s3.types.max_keys.MaxKeys"]
    """<p>Sets the maximum number of keys returned in the response. By default, the action returns up to 1,000 key names. The response might contain fewer keys but will never contain more. </p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>Limits the response to keys that begin with the specified prefix.</p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    """<p>Confirms that the requester knows that she or he will be charged for the list objects request. Bucket owners need not specify this parameter in their requests.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    optional_object_attributes: NotRequired[
        "capo_s3.types.optional_object_attributes_list.OptionalObjectAttributesList"
    ]
    """<p>Specifies the optional fields that you want returned in the response. Fields that you do not specify are not returned.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListObjectsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListObjectsRequest:
    out: ListObjectsRequest = {}  # type: ignore[typeddict-item]
    return out
