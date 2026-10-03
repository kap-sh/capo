"""Generated from Smithy shape ``com.amazonaws.s3#ListObjectsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.delimiter
    import capo_s3.types.encoding_type
    import capo_s3.types.fetch_owner
    import capo_s3.types.max_keys
    import capo_s3.types.optional_object_attributes_list
    import capo_s3.types.prefix
    import capo_s3.types.request_payer
    import capo_s3.types.start_after
    import capo_s3.types.token


class ListObjectsV2Request(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p> <b>Directory buckets</b> - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format <code> <i>Bucket-name</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>amzn-s3-demo-bucket</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Object Lambda access points are not supported by directory buckets.</p> </note> <p> <b>S3 on Outposts</b> - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.<i>outpostID</i>.s3-outposts.<i>Region</i>.amazonaws.com</code>. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">What is S3 on Outposts?</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    delimiter: NotRequired["capo_s3.types.delimiter.Delimiter"]
    """<p>A delimiter is a character that you use to group keys.</p> <p> <code>CommonPrefixes</code> is filtered out from results if it is not lexicographically greater than the <code>StartAfter</code> value.</p> <note> <ul> <li> <p> <b>Directory buckets</b> - For directory buckets, <code>/</code> is the only supported delimiter.</p> </li> <li> <p> <b>Directory buckets </b> - When you query <code>ListObjectsV2</code> with a delimiter during in-progress multipart uploads, the <code>CommonPrefixes</code> response parameter contains the prefixes that are associated with the in-progress multipart uploads. For more information about multipart uploads, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html">Multipart Upload Overview</a> in the <i>Amazon S3 User Guide</i>.</p> </li> </ul> </note>"""
    encoding_type: NotRequired["capo_s3.types.encoding_type.EncodingType"]
    """<p>Encoding type used by Amazon S3 to encode the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html">object keys</a> in the response. Responses are encoded only in UTF-8. An object key can contain any Unicode character. However, the XML 1.0 parser can't parse certain characters, such as characters with an ASCII value from 0 to 10. For characters that aren't supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response. For more information about characters to avoid in object key names, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-guidelines">Object key naming guidelines</a>.</p> <note> <p>When using the URL encoding type, non-ASCII characters that are used in an object's key name will be percent-encoded according to UTF-8 code values. For example, the object <code>test_file(3).png</code> will appear as <code>test_file%283%29.png</code>.</p> </note>"""
    max_keys: NotRequired["capo_s3.types.max_keys.MaxKeys"]
    """<p>Sets the maximum number of keys returned in the response. By default, the action returns up to 1,000 key names. The response might contain fewer keys but will never contain more.</p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>Limits the response to keys that begin with the specified prefix.</p> <note> <p> <b>Directory buckets</b> - For directory buckets, only prefixes that end in a delimiter (<code>/</code>) are supported.</p> </note>"""
    continuation_token: NotRequired["capo_s3.types.token.Token"]
    """<p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results. </p>"""
    fetch_owner: NotRequired["capo_s3.types.fetch_owner.FetchOwner"]
    """<p>The owner field is not present in <code>ListObjectsV2</code> by default. If you want to return the owner field with each key in the result, then set the <code>FetchOwner</code> field to <code>true</code>.</p> <note> <p> <b>Directory buckets</b> - For directory buckets, the bucket owner is returned as the object owner for all objects.</p> </note>"""
    start_after: NotRequired["capo_s3.types.start_after.StartAfter"]
    """<p>StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    """<p>Confirms that the requester knows that she or he will be charged for the list objects request in V2 style. Bucket owners need not specify this parameter in their requests.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    optional_object_attributes: NotRequired[
        "capo_s3.types.optional_object_attributes_list.OptionalObjectAttributesList"
    ]
    """<p>Specifies the optional fields that you want returned in the response. Fields that you do not specify are not returned.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: ListObjectsV2Request, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListObjectsV2Request:
    out: ListObjectsV2Request = {}  # type: ignore[typeddict-item]
    return out
