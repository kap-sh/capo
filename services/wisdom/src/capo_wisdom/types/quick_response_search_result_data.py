"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseSearchResultData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_wisdom.types.arn
    import capo_wisdom.types.channels
    import capo_wisdom.types.contact_attribute_keys
    import capo_wisdom.types.generic_arn
    import capo_wisdom.types.grouping_configuration
    import capo_wisdom.types.language_code
    import capo_wisdom.types.quick_response_contents
    import capo_wisdom.types.quick_response_description
    import capo_wisdom.types.quick_response_name
    import capo_wisdom.types.quick_response_status
    import capo_wisdom.types.quick_response_type
    import capo_wisdom.types.short_cut_key
    import capo_wisdom.types.tags
    import capo_wisdom.types.uuid


class QuickResponseSearchResultData(TypedDict, closed=True):
    quick_response_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the quick response.</p>"""
    quick_response_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the quick response.</p>"""
    knowledge_base_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: "capo_wisdom.types.quick_response_name.QuickResponseName"
    """<p>The name of the quick response.</p>"""
    content_type: "capo_wisdom.types.quick_response_type.QuickResponseType"
    """<p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for quick response written in richtext.</p> </li> </ul>"""
    status: "capo_wisdom.types.quick_response_status.QuickResponseStatus"
    """<p>The resource status of the quick response.</p>"""
    contents: "capo_wisdom.types.quick_response_contents.QuickResponseContents"
    """<p>The contents of the quick response.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the quick response was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the quick response search result data was last modified.</p>"""
    is_active: "bool"
    """<p>Whether the quick response is active.</p>"""
    description: NotRequired[
        "capo_wisdom.types.quick_response_description.QuickResponseDescription"
    ]
    """<p>The description of the quick response.</p>"""
    grouping_configuration: NotRequired[
        "capo_wisdom.types.grouping_configuration.GroupingConfiguration"
    ]
    """<p>The configuration information of the user groups that the quick response is accessible to.</p>"""
    shortcut_key: NotRequired["capo_wisdom.types.short_cut_key.ShortCutKey"]
    """<p>The shortcut key of the quick response. The value should be unique across the knowledge base.</p>"""
    last_modified_by: NotRequired["capo_wisdom.types.generic_arn.GenericArn"]
    """<p>The Amazon Resource Name (ARN) of the user who last updated the quick response search result data.</p>"""
    channels: NotRequired["capo_wisdom.types.channels.Channels"]
    """<p>The Amazon Connect contact channels this quick response applies to. The supported contact channel types include <code>Chat</code>.</p>"""
    language: NotRequired["capo_wisdom.types.language_code.LanguageCode"]
    """<p>The language code value for the language in which the quick response is written.</p>"""
    attributes_not_interpolated: NotRequired[
        "capo_wisdom.types.contact_attribute_keys.ContactAttributeKeys"
    ]
    """<p>The user defined contact attributes that are not resolved when the search result is returned.</p>"""
    attributes_interpolated: NotRequired[
        "capo_wisdom.types.contact_attribute_keys.ContactAttributeKeys"
    ]
    """<p>The user defined contact attributes that are resolved when the search result is returned.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseSearchResultData) -> dict:
    out: dict = {}
    out["quickResponseArn"] = value["quick_response_arn"]
    out["quickResponseId"] = value["quick_response_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    out["contentType"] = value["content_type"]
    out["status"] = value["status"]
    import capo_wisdom.types.quick_response_contents

    out["contents"] = capo_wisdom.types.quick_response_contents.serialize_json(
        value["contents"]
    )
    out["createdTime"] = value["created_time"].timestamp()
    out["lastModifiedTime"] = value["last_modified_time"].timestamp()
    out["isActive"] = value["is_active"]
    if "description" in value:
        out["description"] = value["description"]
    if "grouping_configuration" in value:
        import capo_wisdom.types.grouping_configuration

        out["groupingConfiguration"] = (
            capo_wisdom.types.grouping_configuration.serialize_json(
                value["grouping_configuration"]
            )
        )
    if "shortcut_key" in value:
        out["shortcutKey"] = value["shortcut_key"]
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "channels" in value:
        import capo_wisdom.types.channels

        out["channels"] = capo_wisdom.types.channels.serialize_json(value["channels"])
    if "language" in value:
        out["language"] = value["language"]
    if "attributes_not_interpolated" in value:
        import capo_wisdom.types.contact_attribute_keys

        out["attributesNotInterpolated"] = (
            capo_wisdom.types.contact_attribute_keys.serialize_json(
                value["attributes_not_interpolated"]
            )
        )
    if "attributes_interpolated" in value:
        import capo_wisdom.types.contact_attribute_keys

        out["attributesInterpolated"] = (
            capo_wisdom.types.contact_attribute_keys.serialize_json(
                value["attributes_interpolated"]
            )
        )
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> QuickResponseSearchResultData:
    out: QuickResponseSearchResultData = {}  # type: ignore[typeddict-item]
    if data.get("quickResponseArn") is not None:
        out["quick_response_arn"] = data["quickResponseArn"]
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.quick_response_arn required"
        )
    if data.get("quickResponseId") is not None:
        out["quick_response_id"] = data["quickResponseId"]
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.quick_response_id required"
        )
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.knowledge_base_arn required"
        )
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.knowledge_base_id required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("QuickResponseSearchResultData.name required")
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.content_type required"
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("QuickResponseSearchResultData.status required")
    if data.get("contents") is not None:
        import capo_wisdom.types.quick_response_contents

        out["contents"] = capo_wisdom.types.quick_response_contents.deserialize_json(
            data["contents"]
        )
    else:
        raise DeserializationError("QuickResponseSearchResultData.contents required")
    if data.get("createdTime") is not None:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            float(data["createdTime"]), tz=datetime.timezone.utc
        )
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.created_time required"
        )
    if data.get("lastModifiedTime") is not None:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            float(data["lastModifiedTime"]), tz=datetime.timezone.utc
        )
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.last_modified_time required"
        )
    if data.get("isActive") is not None:
        out["is_active"] = data["isActive"]
    else:
        raise DeserializationError("QuickResponseSearchResultData.is_active required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("groupingConfiguration") is not None:
        import capo_wisdom.types.grouping_configuration

        out["grouping_configuration"] = (
            capo_wisdom.types.grouping_configuration.deserialize_json(
                data["groupingConfiguration"]
            )
        )
    if data.get("shortcutKey") is not None:
        out["shortcut_key"] = data["shortcutKey"]
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    if data.get("channels") is not None:
        import capo_wisdom.types.channels

        out["channels"] = capo_wisdom.types.channels.deserialize_json(data["channels"])
    if data.get("language") is not None:
        out["language"] = data["language"]
    if data.get("attributesNotInterpolated") is not None:
        import capo_wisdom.types.contact_attribute_keys

        out["attributes_not_interpolated"] = (
            capo_wisdom.types.contact_attribute_keys.deserialize_json(
                data["attributesNotInterpolated"]
            )
        )
    if data.get("attributesInterpolated") is not None:
        import capo_wisdom.types.contact_attribute_keys

        out["attributes_interpolated"] = (
            capo_wisdom.types.contact_attribute_keys.deserialize_json(
                data["attributesInterpolated"]
            )
        )
    if data.get("tags") is not None:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: QuickResponseSearchResultData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contents" in value:
        import capo_wisdom.types.quick_response_contents

        out["contents"] = capo_wisdom.types.quick_response_contents.redact_sensitive(
            value["contents"]
        )
    if "grouping_configuration" in value:
        import capo_wisdom.types.grouping_configuration

        out["grouping_configuration"] = (
            capo_wisdom.types.grouping_configuration.redact_sensitive(
                value["grouping_configuration"]
            )
        )
    if "channels" in value:
        import capo_wisdom.types.channels

        out["channels"] = capo_wisdom.types.channels.redact_sensitive(value["channels"])
    if "attributes_not_interpolated" in value:
        out["attributes_not_interpolated"] = "*** Sensitive Data Redacted ***"
    if "attributes_interpolated" in value:
        out["attributes_interpolated"] = "*** Sensitive Data Redacted ***"
    return out
