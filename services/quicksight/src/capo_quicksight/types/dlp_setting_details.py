"""Generated from Smithy shape ``com.amazonaws.quicksight#DlpSettingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.dlp_action
    import capo_quicksight.types.dlp_provider_type
    import capo_quicksight.types.dlp_setting_id
    import capo_quicksight.types.dlp_setting_name
    import capo_quicksight.types.dlp_setting_status
    import capo_quicksight.types.provider_config
    import capo_quicksight.types.timestamp


class DlpSettingDetails(TypedDict, closed=True):
    dlp_setting_id: "capo_quicksight.types.dlp_setting_id.DlpSettingId"
    """<p>The ID of the DLP setting.</p>"""
    name: "capo_quicksight.types.dlp_setting_name.DlpSettingName"
    """<p>The display name of the DLP setting.</p>"""
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the DLP setting.</p>"""
    status: "capo_quicksight.types.dlp_setting_status.DlpSettingStatus"
    """<p>The status of the DLP setting. Valid values are <code>ACTIVE</code> and <code>INACTIVE</code>.</p>"""
    provider_type: "capo_quicksight.types.dlp_provider_type.DlpProviderType"
    """<p>The type of external DLP provider used for sensitivity label classification.</p>"""
    provider_config: "capo_quicksight.types.provider_config.ProviderConfig"
    """<p>The provider-specific configuration for the DLP integration.</p>"""
    provider_outage_action: "capo_quicksight.types.dlp_action.DlpAction"
    """<p>The behavior applied when the DLP provider is unreachable. Valid values are <code>ALLOW</code>, <code>WARN</code>, and <code>BLOCK</code>.</p>"""
    created_at: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The date and time that the DLP setting was created, in ISO 8601 format.</p>"""
    updated_at: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The date and time that the DLP setting was most recently updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DlpSettingDetails) -> dict:
    out: dict = {}
    out["DlpSettingId"] = value["dlp_setting_id"]
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    import capo_quicksight.types.dlp_setting_status

    out["Status"] = capo_quicksight.types.dlp_setting_status.serialize_json(
        value["status"]
    )
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
    import capo_quicksight.types.timestamp

    out["CreatedAt"] = capo_quicksight.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_quicksight.types.timestamp

    out["UpdatedAt"] = capo_quicksight.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> DlpSettingDetails:
    out: DlpSettingDetails = {}  # type: ignore[typeddict-item]
    if data.get("DlpSettingId") is not None:
        out["dlp_setting_id"] = data["DlpSettingId"]
    else:
        out["dlp_setting_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Status") is not None:
        import capo_quicksight.types.dlp_setting_status

        out["status"] = capo_quicksight.types.dlp_setting_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_quicksight.types.dlp_setting_status.DlpSettingStatus", ""
        )
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
        import capo_quicksight.types._unknown

        out["provider_config"] = capo_quicksight.types._unknown.UnknownUnionMember("")
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
    if data.get("CreatedAt") is not None:
        import capo_quicksight.types.timestamp

        out["created_at"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("UpdatedAt") is not None:
        import capo_quicksight.types.timestamp

        out["updated_at"] = capo_quicksight.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
