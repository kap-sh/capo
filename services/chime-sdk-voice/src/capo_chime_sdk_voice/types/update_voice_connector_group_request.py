"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateVoiceConnectorGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.call_distribution_type
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.voice_connector_group_name
    import capo_chime_sdk_voice.types.voice_connector_item_list


class UpdateVoiceConnectorGroupRequest(TypedDict, closed=True):
    voice_connector_group_id: (
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The Voice Connector ID.</p>"""
    name: (
        "capo_chime_sdk_voice.types.voice_connector_group_name.VoiceConnectorGroupName"
    )
    """<p>The name of the Voice Connector group.</p>"""
    voice_connector_items: (
        "capo_chime_sdk_voice.types.voice_connector_item_list.VoiceConnectorItemList"
    )
    """<p>The <code>VoiceConnectorItems</code> to associate with the Voice Connector group.</p>"""
    call_distribution_type: NotRequired[
        "capo_chime_sdk_voice.types.call_distribution_type.CallDistributionType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceConnectorGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_chime_sdk_voice.types.voice_connector_item_list

    out["VoiceConnectorItems"] = (
        capo_chime_sdk_voice.types.voice_connector_item_list.serialize_json(
            value["voice_connector_items"]
        )
    )
    if "call_distribution_type" in value:
        import capo_chime_sdk_voice.types.call_distribution_type

        out["CallDistributionType"] = (
            capo_chime_sdk_voice.types.call_distribution_type.serialize_json(
                value["call_distribution_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateVoiceConnectorGroupRequest:
    out: UpdateVoiceConnectorGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("VoiceConnectorItems") is not None:
        import capo_chime_sdk_voice.types.voice_connector_item_list

        out["voice_connector_items"] = (
            capo_chime_sdk_voice.types.voice_connector_item_list.deserialize_json(
                data["VoiceConnectorItems"]
            )
        )
    else:
        out["voice_connector_items"] = []
    if data.get("CallDistributionType") is not None:
        import capo_chime_sdk_voice.types.call_distribution_type

        out["call_distribution_type"] = (
            capo_chime_sdk_voice.types.call_distribution_type.deserialize_json(
                data["CallDistributionType"]
            )
        )
    return out
