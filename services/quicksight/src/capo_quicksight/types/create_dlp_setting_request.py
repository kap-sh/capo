"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateDlpSettingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean
    import capo_quicksight.types.dlp_action
    import capo_quicksight.types.dlp_provider_type
    import capo_quicksight.types.dlp_setting_id
    import capo_quicksight.types.dlp_setting_name
    import capo_quicksight.types.provider_config
    import capo_quicksight.types.tag_list


class CreateDlpSettingRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account in which to create the DLP setting.</p>"""
    dlp_setting_id: "capo_quicksight.types.dlp_setting_id.DlpSettingId"
    """<p>A unique identifier for the DLP setting.</p>"""
    name: "capo_quicksight.types.dlp_setting_name.DlpSettingName"
    """<p>A human-readable display name for the DLP setting.</p>"""
    provider_type: "capo_quicksight.types.dlp_provider_type.DlpProviderType"
    """<p>The type of external DLP provider to use for sensitivity label classification. Currently, the only supported value is <code>MICROSOFT_PURVIEW</code>.</p>"""
    provider_config: "capo_quicksight.types.provider_config.ProviderConfig"
    """<p>The provider-specific configuration for the DLP integration. This is a union type structure. For this structure to be valid, only one of the attributes can be defined.</p>"""
    provider_outage_action: "capo_quicksight.types.dlp_action.DlpAction"
    """<p>The behavior to apply when the DLP provider is unreachable. Valid values are <code>ALLOW</code>, <code>WARN</code>, and <code>BLOCK</code>.</p>"""
    enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>Specifies whether DLP enforcement is active for this setting. Set to <code>true</code> to enable enforcement, or <code>false</code> to disable it at time of setting creation.</p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>A list of resource tags to apply to the DLP setting. You can use tags to manage access to your Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDlpSettingRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_quicksight.types.dlp_provider_type

    out["ProviderType"] = capo_quicksight.types.dlp_provider_type.serialize_json(
        value["provider_type"]
    )
    import capo_quicksight.types.provider_config

    out["ProviderConfig"] = capo_quicksight.types.provider_config.serialize_json(
        value["provider_config"]
    )
    import capo_quicksight.types.dlp_action

    out["ProviderOutageAction"] = capo_quicksight.types.dlp_action.serialize_json(
        value["provider_outage_action"]
    )
    out["Enabled"] = value["enabled"]
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDlpSettingRequest:
    out: CreateDlpSettingRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ProviderType") is not None:
        import capo_quicksight.types.dlp_provider_type

        out["provider_type"] = capo_quicksight.types.dlp_provider_type.deserialize_json(
            data["ProviderType"]
        )
    else:
        import typing

        out["provider_type"] = typing.cast(
            "capo_quicksight.types.dlp_provider_type.DlpProviderType", ""
        )
    if data.get("ProviderConfig") is not None:
        import capo_quicksight.types.provider_config

        out["provider_config"] = capo_quicksight.types.provider_config.deserialize_json(
            data["ProviderConfig"]
        )
    else:
        out["provider_config"] = {"$unknown": {"name": ""}}
    if data.get("ProviderOutageAction") is not None:
        import capo_quicksight.types.dlp_action

        out["provider_outage_action"] = (
            capo_quicksight.types.dlp_action.deserialize_json(
                data["ProviderOutageAction"]
            )
        )
    else:
        import typing

        out["provider_outage_action"] = typing.cast(
            "capo_quicksight.types.dlp_action.DlpAction", ""
        )
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out
