"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateKeyValueStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.import_source
    import capo_cloudfront.types.key_value_store_comment
    import capo_cloudfront.types.key_value_store_name
    import capo_cloudfront.types.tags


class CreateKeyValueStoreRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.key_value_store_name.KeyValueStoreName"
    """<p>The name of the key value store. The minimum length is 1 character and the maximum length is 64 characters.</p>"""
    comment: NotRequired[
        "capo_cloudfront.types.key_value_store_comment.KeyValueStoreComment"
    ]
    """<p>The comment of the key value store.</p>"""
    import_source: NotRequired["capo_cloudfront.types.import_source.ImportSource"]
    """<p>The S3 bucket that provides the source for the import. The source must be in a valid JSON format.</p>"""
    tags: NotRequired["capo_cloudfront.types.tags.Tags"]


# --- restXml ser/de ---
def serialize_xml(value: CreateKeyValueStoreRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    if "import_source" in value:
        import capo_cloudfront.types.import_source

        capo_cloudfront.types.import_source.serialize_xml(
            value["import_source"], el, "ImportSource"
        )
    if "tags" in value:
        import capo_cloudfront.types.tags

        capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateKeyValueStoreRequest:
    out: CreateKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_import_source = el.find("ImportSource")
    if child_import_source is not None:
        import capo_cloudfront.types.import_source

        out["import_source"] = capo_cloudfront.types.import_source.deserialize_xml(
            child_import_source
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    return out
