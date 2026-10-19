"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldLevelEncryptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.content_type_profile_config
    import capo_cloudfront.types.query_arg_profile_config
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class FieldLevelEncryptionSummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The unique ID of a field-level encryption item.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The last time that the summary of field-level encryption items was modified.</p>"""
    comment: NotRequired["capo_cloudfront.types.string.string"]
    """<p>An optional comment about the field-level encryption item. The comment cannot be longer than 128 characters.</p>"""
    query_arg_profile_config: NotRequired[
        "capo_cloudfront.types.query_arg_profile_config.QueryArgProfileConfig"
    ]
    """<p>A summary of a query argument-profile mapping.</p>"""
    content_type_profile_config: NotRequired[
        "capo_cloudfront.types.content_type_profile_config.ContentTypeProfileConfig"
    ]
    """<p>A summary of a content type-profile mapping.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: FieldLevelEncryptionSummary, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    if "query_arg_profile_config" in value:
        import capo_cloudfront.types.query_arg_profile_config

        capo_cloudfront.types.query_arg_profile_config.serialize_xml(
            value["query_arg_profile_config"], el, "QueryArgProfileConfig"
        )
    if "content_type_profile_config" in value:
        import capo_cloudfront.types.content_type_profile_config

        capo_cloudfront.types.content_type_profile_config.serialize_xml(
            value["content_type_profile_config"], el, "ContentTypeProfileConfig"
        )


def deserialize_xml(el: Element) -> FieldLevelEncryptionSummary:
    out: FieldLevelEncryptionSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_query_arg_profile_config = el.find("QueryArgProfileConfig")
    if child_query_arg_profile_config is not None:
        import capo_cloudfront.types.query_arg_profile_config

        out["query_arg_profile_config"] = (
            capo_cloudfront.types.query_arg_profile_config.deserialize_xml(
                child_query_arg_profile_config
            )
        )
    child_content_type_profile_config = el.find("ContentTypeProfileConfig")
    if child_content_type_profile_config is not None:
        import capo_cloudfront.types.content_type_profile_config

        out["content_type_profile_config"] = (
            capo_cloudfront.types.content_type_profile_config.deserialize_xml(
                child_content_type_profile_config
            )
        )
    return out
