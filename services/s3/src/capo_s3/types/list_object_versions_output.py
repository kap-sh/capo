"""Generated from Smithy shape ``com.amazonaws.s3#ListObjectVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_name
    import capo_s3.types.common_prefix_list
    import capo_s3.types.delete_markers
    import capo_s3.types.delimiter
    import capo_s3.types.encoding_type
    import capo_s3.types.is_truncated
    import capo_s3.types.key_marker
    import capo_s3.types.max_keys
    import capo_s3.types.next_key_marker
    import capo_s3.types.next_version_id_marker
    import capo_s3.types.object_version_list
    import capo_s3.types.prefix
    import capo_s3.types.request_charged
    import capo_s3.types.version_id_marker


class ListObjectVersionsOutput(TypedDict, closed=True):
    is_truncated: NotRequired["capo_s3.types.is_truncated.IsTruncated"]
    """<p>A flag that indicates whether Amazon S3 returned all of the results that satisfied the search criteria. If your results were truncated, you can make a follow-up paginated request by using the <code>NextKeyMarker</code> and <code>NextVersionIdMarker</code> response parameters as a starting place in another request to return the rest of the results.</p>"""
    key_marker: NotRequired["capo_s3.types.key_marker.KeyMarker"]
    """<p>Marks the last key returned in a truncated response.</p>"""
    version_id_marker: NotRequired["capo_s3.types.version_id_marker.VersionIdMarker"]
    """<p>Marks the last version of the key returned in a truncated response.</p>"""
    next_key_marker: NotRequired["capo_s3.types.next_key_marker.NextKeyMarker"]
    """<p>When the number of responses exceeds the value of <code>MaxKeys</code>, <code>NextKeyMarker</code> specifies the first key not returned that satisfies the search criteria. Use this value for the key-marker request parameter in a subsequent request.</p>"""
    next_version_id_marker: NotRequired[
        "capo_s3.types.next_version_id_marker.NextVersionIdMarker"
    ]
    """<p>When the number of responses exceeds the value of <code>MaxKeys</code>, <code>NextVersionIdMarker</code> specifies the first object version not returned that satisfies the search criteria. Use this value for the <code>version-id-marker</code> request parameter in a subsequent request.</p>"""
    versions: NotRequired["capo_s3.types.object_version_list.ObjectVersionList"]
    """<p>Container for version information.</p>"""
    delete_markers: NotRequired["capo_s3.types.delete_markers.DeleteMarkers"]
    """<p>Container for an object that is a delete marker. To learn more about delete markers, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html">Working with delete markers</a>.</p>"""
    name: NotRequired["capo_s3.types.bucket_name.BucketName"]
    """<p>The bucket name.</p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>Selects objects that start with the value supplied by this parameter.</p>"""
    delimiter: NotRequired["capo_s3.types.delimiter.Delimiter"]
    """<p>The delimiter grouping the included keys. A delimiter is a character that you specify to group keys. All keys that contain the same string between the prefix and the first occurrence of the delimiter are grouped under a single result element in <code>CommonPrefixes</code>. These groups are counted as one result against the <code>max-keys</code> limitation. These keys are not returned elsewhere in the response.</p>"""
    max_keys: NotRequired["capo_s3.types.max_keys.MaxKeys"]
    """<p>Specifies the maximum number of objects to return.</p>"""
    common_prefixes: NotRequired["capo_s3.types.common_prefix_list.CommonPrefixList"]
    """<p>All of the keys rolled up into a common prefix count as a single return when calculating the number of returns.</p>"""
    encoding_type: NotRequired["capo_s3.types.encoding_type.EncodingType"]
    """<p> Encoding type used by Amazon S3 to encode object key names in the XML response.</p> <p>If you specify the <code>encoding-type</code> request parameter, Amazon S3 includes this element in the response, and returns encoded key name values in the following response elements:</p> <p> <code>KeyMarker, NextKeyMarker, Prefix, Key</code>, and <code>Delimiter</code>.</p>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: ListObjectVersionsOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "is_truncated" in value:
        SubElement(el, "IsTruncated").text = (
            "true" if value["is_truncated"] else "false"
        )
    if "key_marker" in value:
        SubElement(el, "KeyMarker").text = str(value["key_marker"])
    if "version_id_marker" in value:
        SubElement(el, "VersionIdMarker").text = str(value["version_id_marker"])
    if "next_key_marker" in value:
        SubElement(el, "NextKeyMarker").text = str(value["next_key_marker"])
    if "next_version_id_marker" in value:
        SubElement(el, "NextVersionIdMarker").text = str(
            value["next_version_id_marker"]
        )
    if "versions" in value:
        import capo_s3.types.object_version_list

        capo_s3.types.object_version_list.serialize_xml_flat(
            value["versions"], el, "Version"
        )
    if "delete_markers" in value:
        import capo_s3.types.delete_markers

        capo_s3.types.delete_markers.serialize_xml_flat(
            value["delete_markers"], el, "DeleteMarker"
        )
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


def deserialize_xml(el: Element) -> ListObjectVersionsOutput:
    out: ListObjectVersionsOutput = {}  # type: ignore[typeddict-item]
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    child_key_marker = el.find("KeyMarker")
    if child_key_marker is not None:
        out["key_marker"] = str(child_key_marker.text or "")
    child_version_id_marker = el.find("VersionIdMarker")
    if child_version_id_marker is not None:
        out["version_id_marker"] = str(child_version_id_marker.text or "")
    child_next_key_marker = el.find("NextKeyMarker")
    if child_next_key_marker is not None:
        out["next_key_marker"] = str(child_next_key_marker.text or "")
    child_next_version_id_marker = el.find("NextVersionIdMarker")
    if child_next_version_id_marker is not None:
        out["next_version_id_marker"] = str(child_next_version_id_marker.text or "")
    if el.find("Version") is not None:
        import capo_s3.types.object_version_list

        out["versions"] = capo_s3.types.object_version_list.deserialize_xml_flat(
            el, "Version"
        )
    if el.find("DeleteMarker") is not None:
        import capo_s3.types.delete_markers

        out["delete_markers"] = capo_s3.types.delete_markers.deserialize_xml_flat(
            el, "DeleteMarker"
        )
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
