"""Generated from Smithy shape ``com.amazonaws.wisdom#CreateQuickResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.channels
    import capo_wisdom.types.grouping_configuration
    import capo_wisdom.types.language_code
    import capo_wisdom.types.non_empty_string
    import capo_wisdom.types.quick_response_data_provider
    import capo_wisdom.types.quick_response_description
    import capo_wisdom.types.quick_response_name
    import capo_wisdom.types.quick_response_type
    import capo_wisdom.types.short_cut_key
    import capo_wisdom.types.tags
    import capo_wisdom.types.uuid_or_arn


class CreateQuickResponseRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: "capo_wisdom.types.quick_response_name.QuickResponseName"
    """<p>The name of the quick response.</p>"""
    content: "capo_wisdom.types.quick_response_data_provider.QuickResponseDataProvider"
    """<p>The content of the quick response.</p>"""
    content_type: NotRequired["capo_wisdom.types.quick_response_type.QuickResponseType"]
    """<p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for a quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for a quick response written in richtext.</p> </li> </ul>"""
    grouping_configuration: NotRequired[
        "capo_wisdom.types.grouping_configuration.GroupingConfiguration"
    ]
    """<p>The configuration information of the user groups that the quick response is accessible to.</p>"""
    description: NotRequired[
        "capo_wisdom.types.quick_response_description.QuickResponseDescription"
    ]
    """<p>The description of the quick response.</p>"""
    shortcut_key: NotRequired["capo_wisdom.types.short_cut_key.ShortCutKey"]
    """<p>The shortcut key of the quick response. The value should be unique across the knowledge base. </p>"""
    is_active: NotRequired["bool"]
    """<p>Whether the quick response is active.</p>"""
    channels: NotRequired["capo_wisdom.types.channels.Channels"]
    """<p>The Amazon Connect channels this quick response applies to.</p>"""
    language: NotRequired["capo_wisdom.types.language_code.LanguageCode"]
    """<p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>"""
    client_token: NotRequired["capo_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuickResponseRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_wisdom.types.quick_response_data_provider

    out["content"] = capo_wisdom.types.quick_response_data_provider.serialize_json(
        value["content"]
    )
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "grouping_configuration" in value:
        import capo_wisdom.types.grouping_configuration

        out["groupingConfiguration"] = (
            capo_wisdom.types.grouping_configuration.serialize_json(
                value["grouping_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "shortcut_key" in value:
        out["shortcutKey"] = value["shortcut_key"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    if "channels" in value:
        import capo_wisdom.types.channels

        out["channels"] = capo_wisdom.types.channels.serialize_json(value["channels"])
    if "language" in value:
        out["language"] = value["language"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateQuickResponseRequest:
    out: CreateQuickResponseRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateQuickResponseRequest.name required")
    if data.get("content") is not None:
        import capo_wisdom.types.quick_response_data_provider

        out["content"] = (
            capo_wisdom.types.quick_response_data_provider.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("CreateQuickResponseRequest.content required")
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    if data.get("groupingConfiguration") is not None:
        import capo_wisdom.types.grouping_configuration

        out["grouping_configuration"] = (
            capo_wisdom.types.grouping_configuration.deserialize_json(
                data["groupingConfiguration"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("shortcutKey") is not None:
        out["shortcut_key"] = data["shortcutKey"]
    if data.get("isActive") is not None:
        out["is_active"] = data["isActive"]
    if data.get("channels") is not None:
        import capo_wisdom.types.channels

        out["channels"] = capo_wisdom.types.channels.deserialize_json(data["channels"])
    if data.get("language") is not None:
        out["language"] = data["language"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    return out
