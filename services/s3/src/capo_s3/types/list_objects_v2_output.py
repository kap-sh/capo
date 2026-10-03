"""Generated from Smithy shape ``com.amazonaws.s3#ListObjectsV2Output``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_name
    import capo_s3.types.common_prefix_list
    import capo_s3.types.delimiter
    import capo_s3.types.encoding_type
    import capo_s3.types.is_truncated
    import capo_s3.types.key_count
    import capo_s3.types.max_keys
    import capo_s3.types.next_token
    import capo_s3.types.object_list
    import capo_s3.types.prefix
    import capo_s3.types.request_charged
    import capo_s3.types.start_after
    import capo_s3.types.token


class ListObjectsV2Output(TypedDict, closed=True):
    is_truncated: NotRequired["capo_s3.types.is_truncated.IsTruncated"]
    """<p>Set to <code>false</code> if all of the results were returned. Set to <code>true</code> if more keys are available to return. If the number of results exceeds that specified by <code>MaxKeys</code>, all of the results might not be returned.</p>"""
    contents: NotRequired["capo_s3.types.object_list.ObjectList"]
    """<p>Metadata about each object returned.</p>"""
    name: NotRequired["capo_s3.types.bucket_name.BucketName"]
    """<p>The bucket name.</p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>Keys that begin with the indicated prefix.</p> <note> <p> <b>Directory buckets</b> - For directory buckets, only prefixes that end in a delimiter (<code>/</code>) are supported.</p> </note>"""
    delimiter: NotRequired["capo_s3.types.delimiter.Delimiter"]
    """<p>Causes keys that contain the same string between the <code>prefix</code> and the first occurrence of the delimiter to be rolled up into a single result element in the <code>CommonPrefixes</code> collection. These rolled-up keys are not returned elsewhere in the response. Each rolled-up result counts as only one return against the <code>MaxKeys</code> value.</p> <note> <p> <b>Directory buckets</b> - For directory buckets, <code>/</code> is the only supported delimiter.</p> </note>"""
    max_keys: NotRequired["capo_s3.types.max_keys.MaxKeys"]
    """<p>Sets the maximum number of keys returned in the response. By default, the action returns up to 1,000 key names. The response might contain fewer keys but will never contain more.</p>"""
    common_prefixes: NotRequired["capo_s3.types.common_prefix_list.CommonPrefixList"]
    """<p>All of the keys (up to 1,000) that share the same prefix are grouped together. When counting the total numbers of returns by this API operation, this group of keys is considered as one item.</p> <p>A response can contain <code>CommonPrefixes</code> only if you specify a delimiter.</p> <p> <code>CommonPrefixes</code> contains all (if there are any) keys between <code>Prefix</code> and the next occurrence of the string specified by a delimiter.</p> <p> <code>CommonPrefixes</code> lists keys that act like subdirectories in the directory specified by <code>Prefix</code>.</p> <p>For example, if the prefix is <code>notes/</code> and the delimiter is a slash (<code>/</code>) as in <code>notes/summer/july</code>, the common prefix is <code>notes/summer/</code>. All of the keys that roll up into a common prefix count as a single return when calculating the number of returns. </p> <note> <ul> <li> <p> <b>Directory buckets</b> - For directory buckets, only prefixes that end in a delimiter (<code>/</code>) are supported.</p> </li> <li> <p> <b>Directory buckets </b> - When you query <code>ListObjectsV2</code> with a delimiter during in-progress multipart uploads, the <code>CommonPrefixes</code> response parameter contains the prefixes that are associated with the in-progress multipart uploads. For more information about multipart uploads, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html">Multipart Upload Overview</a> in the <i>Amazon S3 User Guide</i>.</p> </li> </ul> </note>"""
    encoding_type: NotRequired["capo_s3.types.encoding_type.EncodingType"]
    """<p>Encoding type used by Amazon S3 to encode object key names in the XML response.</p> <p>If you specify the <code>encoding-type</code> request parameter, Amazon S3 includes this element in the response, and returns encoded key name values in the following response elements:</p> <p> <code>Delimiter, Prefix, Key,</code> and <code>StartAfter</code>.</p>"""
    key_count: NotRequired["capo_s3.types.key_count.KeyCount"]
    """<p> <code>KeyCount</code> is the number of keys returned with this request. <code>KeyCount</code> will always be less than or equal to the <code>MaxKeys</code> field. For example, if you ask for 50 keys, your result will include 50 keys or fewer.</p>"""
    continuation_token: NotRequired["capo_s3.types.token.Token"]
    """<p> If <code>ContinuationToken</code> was sent with the request, it is included in the response. You can use the returned <code>ContinuationToken</code> for pagination of the list response.</p>"""
    next_continuation_token: NotRequired["capo_s3.types.next_token.NextToken"]
    """<p> <code>NextContinuationToken</code> is sent when <code>isTruncated</code> is true, which means there are more keys in the bucket that can be listed. The next list requests to Amazon S3 can be continued with this <code>NextContinuationToken</code>. <code>NextContinuationToken</code> is obfuscated and is not a real key</p>"""
    start_after: NotRequired["capo_s3.types.start_after.StartAfter"]
    """<p>If StartAfter was sent with the request, it is included in the response.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: ListObjectsV2Output, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "is_truncated" in value:
        SubElement(el, "IsTruncated").text = (
            "true" if value["is_truncated"] else "false"
        )
    if "contents" in value:
        import capo_s3.types.object_list

        capo_s3.types.object_list.serialize_xml_flat(value["contents"], el, "Contents")
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "delimiter" in value:
        SubElement(el, "Delimiter").text = str(value["delimiter"])
    if "max_keys" in value:
        SubElement(el, "MaxKeys").text = str(value["max_keys"])
    if "common_prefixes" in value:
        import capo_s3.types.common_prefix_list

        capo_s3.types.common_prefix_list.serialize_xml_flat(
            value["common_prefixes"], el, "CommonPrefixes"
        )
    if "encoding_type" in value:
        import capo_s3.types.encoding_type

        capo_s3.types.encoding_type.serialize_xml(
            value["encoding_type"], el, "EncodingType"
        )
    if "key_count" in value:
        SubElement(el, "KeyCount").text = str(value["key_count"])
    if "continuation_token" in value:
        SubElement(el, "ContinuationToken").text = str(value["continuation_token"])
    if "next_continuation_token" in value:
        SubElement(el, "NextContinuationToken").text = str(
            value["next_continuation_token"]
        )
    if "start_after" in value:
        SubElement(el, "StartAfter").text = str(value["start_after"])


def deserialize_xml(el: Element) -> ListObjectsV2Output:
    out: ListObjectsV2Output = {}  # type: ignore[typeddict-item]
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    if el.find("Contents") is not None:
        import capo_s3.types.object_list

        out["contents"] = capo_s3.types.object_list.deserialize_xml_flat(el, "Contents")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_delimiter = el.find("Delimiter")
    if child_delimiter is not None:
        out["delimiter"] = str(child_delimiter.text or "")
    child_max_keys = el.find("MaxKeys")
    if child_max_keys is not None:
        out["max_keys"] = int(child_max_keys.text or "")
    if el.find("CommonPrefixes") is not None:
        import capo_s3.types.common_prefix_list

        out["common_prefixes"] = capo_s3.types.common_prefix_list.deserialize_xml_flat(
            el, "CommonPrefixes"
        )
    child_encoding_type = el.find("EncodingType")
    if child_encoding_type is not None:
        import capo_s3.types.encoding_type

        out["encoding_type"] = capo_s3.types.encoding_type.deserialize_xml(
            child_encoding_type
        )
    child_key_count = el.find("KeyCount")
    if child_key_count is not None:
        out["key_count"] = int(child_key_count.text or "")
    child_continuation_token = el.find("ContinuationToken")
    if child_continuation_token is not None:
        out["continuation_token"] = str(child_continuation_token.text or "")
    child_next_continuation_token = el.find("NextContinuationToken")
    if child_next_continuation_token is not None:
        out["next_continuation_token"] = str(child_next_continuation_token.text or "")
    child_start_after = el.find("StartAfter")
    if child_start_after is not None:
        out["start_after"] = str(child_start_after.text or "")
    return out
