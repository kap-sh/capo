"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateProxySessionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.capability_list
    import capo_chime_sdk_voice.types.geo_match_level
    import capo_chime_sdk_voice.types.geo_match_params
    import capo_chime_sdk_voice.types.number_selection_behavior
    import capo_chime_sdk_voice.types.participant_phone_number_list
    import capo_chime_sdk_voice.types.positive_integer
    import capo_chime_sdk_voice.types.proxy_session_name_string
    import capo_chime_sdk_voice.types.voice_connector_id


class CreateProxySessionRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    participant_phone_numbers: "capo_chime_sdk_voice.types.participant_phone_number_list.ParticipantPhoneNumberList"
    """<p>The participant phone numbers.</p>"""
    name: NotRequired[
        "capo_chime_sdk_voice.types.proxy_session_name_string.ProxySessionNameString"
    ]
    """<p>The name of the proxy session.</p>"""
    expiry_minutes: NotRequired[
        "capo_chime_sdk_voice.types.positive_integer.PositiveInteger"
    ]
    """<p>The number of minutes allowed for the proxy session.</p>"""
    capabilities: "capo_chime_sdk_voice.types.capability_list.CapabilityList"
    """<p>The proxy session's capabilities.</p>"""
    number_selection_behavior: NotRequired[
        "capo_chime_sdk_voice.types.number_selection_behavior.NumberSelectionBehavior"
    ]
    """<p>The preference for proxy phone number reuse, or stickiness, between the same participants across sessions.</p>"""
    geo_match_level: NotRequired[
        "capo_chime_sdk_voice.types.geo_match_level.GeoMatchLevel"
    ]
    """<p>The preference for matching the country or area code of the proxy phone number with that of the first participant.</p>"""
    geo_match_params: NotRequired[
        "capo_chime_sdk_voice.types.geo_match_params.GeoMatchParams"
    ]
    """<p>The country and area code for the proxy phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProxySessionRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.participant_phone_number_list

    out["ParticipantPhoneNumbers"] = (
        capo_chime_sdk_voice.types.participant_phone_number_list.serialize_json(
            value["participant_phone_numbers"]
        )
    )
    if "name" in value:
        out["Name"] = value["name"]
    if "expiry_minutes" in value:
        out["ExpiryMinutes"] = value["expiry_minutes"]
    import capo_chime_sdk_voice.types.capability_list

    out["Capabilities"] = capo_chime_sdk_voice.types.capability_list.serialize_json(
        value["capabilities"]
    )
    if "number_selection_behavior" in value:
        import capo_chime_sdk_voice.types.number_selection_behavior

        out["NumberSelectionBehavior"] = (
            capo_chime_sdk_voice.types.number_selection_behavior.serialize_json(
                value["number_selection_behavior"]
            )
        )
    if "geo_match_level" in value:
        import capo_chime_sdk_voice.types.geo_match_level

        out["GeoMatchLevel"] = (
            capo_chime_sdk_voice.types.geo_match_level.serialize_json(
                value["geo_match_level"]
            )
        )
    if "geo_match_params" in value:
        import capo_chime_sdk_voice.types.geo_match_params

        out["GeoMatchParams"] = (
            capo_chime_sdk_voice.types.geo_match_params.serialize_json(
                value["geo_match_params"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateProxySessionRequest:
    out: CreateProxySessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParticipantPhoneNumbers") is not None:
        import capo_chime_sdk_voice.types.participant_phone_number_list

        out["participant_phone_numbers"] = (
            capo_chime_sdk_voice.types.participant_phone_number_list.deserialize_json(
                data["ParticipantPhoneNumbers"]
            )
        )
    else:
        out["participant_phone_numbers"] = []
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ExpiryMinutes") is not None:
        out["expiry_minutes"] = data["ExpiryMinutes"]
    if data.get("Capabilities") is not None:
        import capo_chime_sdk_voice.types.capability_list

        out["capabilities"] = (
            capo_chime_sdk_voice.types.capability_list.deserialize_json(
                data["Capabilities"]
            )
        )
    else:
        out["capabilities"] = []
    if data.get("NumberSelectionBehavior") is not None:
        import capo_chime_sdk_voice.types.number_selection_behavior

        out["number_selection_behavior"] = (
            capo_chime_sdk_voice.types.number_selection_behavior.deserialize_json(
                data["NumberSelectionBehavior"]
            )
        )
    if data.get("GeoMatchLevel") is not None:
        import capo_chime_sdk_voice.types.geo_match_level

        out["geo_match_level"] = (
            capo_chime_sdk_voice.types.geo_match_level.deserialize_json(
                data["GeoMatchLevel"]
            )
        )
    if data.get("GeoMatchParams") is not None:
        import capo_chime_sdk_voice.types.geo_match_params

        out["geo_match_params"] = (
            capo_chime_sdk_voice.types.geo_match_params.deserialize_json(
                data["GeoMatchParams"]
            )
        )
    return out


def redact_sensitive(value: CreateProxySessionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "participant_phone_numbers" in value:
        import capo_chime_sdk_voice.types.participant_phone_number_list

        out["participant_phone_numbers"] = (
            capo_chime_sdk_voice.types.participant_phone_number_list.redact_sensitive(
                value["participant_phone_numbers"]
            )
        )
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
