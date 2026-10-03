"""Generated from Smithy shape ``com.amazonaws.s3#ListObjectsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_name
    import capo_s3.types.common_prefix_list
    import capo_s3.types.delimiter
    import capo_s3.types.encoding_type
    import capo_s3.types.is_truncated
    import capo_s3.types.marker
    import capo_s3.types.max_keys
    import capo_s3.types.next_marker
    import capo_s3.types.object_list
    import capo_s3.types.prefix
    import capo_s3.types.request_charged


class ListObjectsOutput(TypedDict, closed=True):
    is_truncated: NotRequired["capo_s3.types.is_truncated.IsTruncated"]
    """<p>A flag that indicates whether Amazon S3 returned all of the results that satisfied the search criteria.</p>"""
    marker: NotRequired["capo_s3.types.marker.Marker"]
    """<p>Indicates where in the bucket listing begins. Marker is included in the response if it was sent with the request.</p>"""
    next_marker: NotRequired["capo_s3.types.next_marker.NextMarker"]
    """<p>When the response is truncated (the <code>IsTruncated</code> element value in the response is <code>true</code>), you can use the key name in this field as the <code>marker</code> parameter in the subsequent request to get the next set of objects. Amazon S3 lists objects in alphabetical order. </p> <note> <p>This element is returned only if you have the <code>delimiter</code> request parameter specified. If the response does not include the <code>NextMarker</code> element and it is truncated, you can use the value of the last <code>Key</code> element in the response as the <code>marker</code> parameter in the subsequent request to get the next set of object keys.</p> </note>"""
    contents: NotRequired["capo_s3.types.object_list.ObjectList"]
    """<p>Metadata about each object returned.</p>"""
    name: NotRequired["capo_s3.types.bucket_name.BucketName"]
    """<p>The bucket name.</p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>Keys that begin with the indicated prefix.</p>"""
    delimiter: NotRequired["capo_s3.types.delimiter.Delimiter"]
    """<p>Causes keys that contain the same string between the prefix and the first occurrence of the delimiter to be rolled up into a single result element in the <code>CommonPrefixes</code> collection. These rolled-up keys are not returned elsewhere in the response. Each rolled-up result counts as only one return against the <code>MaxKeys</code> value.</p>"""
    max_keys: NotRequired["capo_s3.types.max_keys.MaxKeys"]
    """<p>The maximum number of keys returned in the response body.</p>"""
    common_prefixes: NotRequired["capo_s3.types.common_prefix_list.CommonPrefixList"]
    """<p>All of the keys (up to 1,000) rolled up in a common prefix count as a single return when calculating the number of returns. </p> <p>A response can contain <code>CommonPrefixes</code> only if you specify a delimiter.</p> <p> <code>CommonPrefixes</code> contains all (if there are any) keys between <code>Prefix</code> and the next occurrence of the string specified by the delimiter.</p> <p> <code>CommonPrefixes</code> lists keys that act like subdirectories in the directory specified by <code>Prefix</code>.</p> <p>For example, if the prefix is <code>notes/</code> and the delimiter is a slash (<code>/</code>), as in <code>notes/summer/july</code>, the common prefix is <code>notes/summer/</code>. All of the keys that roll up into a common prefix count as a single return when calculating the number of returns.</p>"""
    encoding_type: NotRequired["capo_s3.types.encoding_type.EncodingType"]
    """<p>Encoding type used by Amazon S3 to encode the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html">object keys</a> in the response. Responses are encoded only in UTF-8. An object key can contain any Unicode character. However, the XML 1.0 parser can't parse certain characters, such as characters with an ASCII value from 0 to 10. For characters that aren't supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the response. For more information about characters to avoid in object key names, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-guidelines">Object key naming guidelines</a>.</p> <note> <p>When using the URL encoding type, non-ASCII characters that are used in an object's key name will be percent-encoded according to UTF-8 code values. For example, the object <code>test_file(3).png</code> will appear as <code>test_file%283%29.png</code>.</p> </note>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: ListObjectsOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "is_truncated" in value:
        SubElement(el, "IsTruncated").text = (
            "true" if value["is_truncated"] else "false"
        )
    if "marker" in value:
        SubElement(el, "Marker").text = str(value["marker"])
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
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


def deserialize_xml(el: Element) -> ListObjectsOutput:
    out: ListObjectsOutput = {}  # type: ignore[typeddict-item]
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
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
    return out
