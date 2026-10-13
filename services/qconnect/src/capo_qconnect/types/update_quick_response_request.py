"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateQuickResponseRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.channels
    import capo_qconnect.types.grouping_configuration
    import capo_qconnect.types.language_code
    import capo_qconnect.types.quick_response_data_provider
    import capo_qconnect.types.quick_response_description
    import capo_qconnect.types.quick_response_name
    import capo_qconnect.types.quick_response_type
    import capo_qconnect.types.short_cut_key
    import capo_qconnect.types.uuid_or_arn


class UpdateQuickResponseRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    quick_response_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the quick response.</p>"""
    name: NotRequired["capo_qconnect.types.quick_response_name.QuickResponseName"]
    """<p>The name of the quick response.</p>"""
    content: NotRequired[
        "capo_qconnect.types.quick_response_data_provider.QuickResponseDataProvider"
    ]
    """<p>The updated content of the quick response.</p>"""
    content_type: NotRequired[
        "capo_qconnect.types.quick_response_type.QuickResponseType"
    ]
    """<p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for quick response written in richtext.</p> </li> </ul>"""
    grouping_configuration: NotRequired[
        "capo_qconnect.types.grouping_configuration.GroupingConfiguration"
    ]
    """<p>The updated grouping configuration of the quick response.</p>"""
    remove_grouping_configuration: NotRequired["bool"]
    """<p>Whether to remove the grouping configuration of the quick response.</p>"""
    description: NotRequired[
        "capo_qconnect.types.quick_response_description.QuickResponseDescription"
    ]
    """<p>The updated description of the quick response.</p>"""
    remove_description: NotRequired["bool"]
    """<p>Whether to remove the description from the quick response.</p>"""
    shortcut_key: NotRequired["capo_qconnect.types.short_cut_key.ShortCutKey"]
    """<p>The shortcut key of the quick response. The value should be unique across the knowledge base.</p>"""
    remove_shortcut_key: NotRequired["bool"]
    """<p>Whether to remove the shortcut key of the quick response.</p>"""
    is_active: NotRequired["bool"]
    """<p>Whether the quick response is active. </p>"""
    channels: NotRequired["capo_qconnect.types.channels.Channels"]
    """<p>The Connect Customer contact channels this quick response applies to. The supported contact channel types include <code>Chat</code>.</p>"""
    language: NotRequired["capo_qconnect.types.language_code.LanguageCode"]
    """<p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuickResponseRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "content" in value:
        import capo_qconnect.types.quick_response_data_provider

        out["content"] = (
            capo_qconnect.types.quick_response_data_provider.serialize_json(
                value["content"]
            )
        )
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "grouping_configuration" in value:
        import capo_qconnect.types.grouping_configuration

        out["groupingConfiguration"] = (
            capo_qconnect.types.grouping_configuration.serialize_json(
                value["grouping_configuration"]
            )
        )
    if "remove_grouping_configuration" in value:
        out["removeGroupingConfiguration"] = value["remove_grouping_configuration"]
    if "description" in value:
        out["description"] = value["description"]
    if "remove_description" in value:
        out["removeDescription"] = value["remove_description"]
    if "shortcut_key" in value:
        out["shortcutKey"] = value["shortcut_key"]
    if "remove_shortcut_key" in value:
        out["removeShortcutKey"] = value["remove_shortcut_key"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    if "channels" in value:
        import capo_qconnect.types.channels

        out["channels"] = capo_qconnect.types.channels.serialize_json(value["channels"])
    if "language" in value:
        out["language"] = value["language"]
    return out


def deserialize_json(data: dict) -> UpdateQuickResponseRequest:
    out: UpdateQuickResponseRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("content") is not None:
        import capo_qconnect.types.quick_response_data_provider

        out["content"] = (
            capo_qconnect.types.quick_response_data_provider.deserialize_json(
                data["content"]
            )
        )
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    if data.get("groupingConfiguration") is not None:
        import capo_qconnect.types.grouping_configuration

        out["grouping_configuration"] = (
            capo_qconnect.types.grouping_configuration.deserialize_json(
                data["groupingConfiguration"]
            )
        )
    if data.get("removeGroupingConfiguration") is not None:
        out["remove_grouping_configuration"] = data["removeGroupingConfiguration"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("removeDescription") is not None:
        out["remove_description"] = data["removeDescription"]
    if data.get("shortcutKey") is not None:
        out["shortcut_key"] = data["shortcutKey"]
    if data.get("removeShortcutKey") is not None:
        out["remove_shortcut_key"] = data["removeShortcutKey"]
    if data.get("isActive") is not None:
        out["is_active"] = data["isActive"]
    if data.get("channels") is not None:
        import capo_qconnect.types.channels

        out["channels"] = capo_qconnect.types.channels.deserialize_json(
            data["channels"]
        )
    if data.get("language") is not None:
        out["language"] = data["language"]
    return out


def redact_sensitive(value: UpdateQuickResponseRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_qconnect.types.quick_response_data_provider

        out["content"] = (
            capo_qconnect.types.quick_response_data_provider.redact_sensitive(
                value["content"]
            )
        )
    if "grouping_configuration" in value:
        import capo_qconnect.types.grouping_configuration

        out["grouping_configuration"] = (
            capo_qconnect.types.grouping_configuration.redact_sensitive(
                value["grouping_configuration"]
            )
        )
    if "channels" in value:
        import capo_qconnect.types.channels

        out["channels"] = capo_qconnect.types.channels.redact_sensitive(
            value["channels"]
        )
    return out
