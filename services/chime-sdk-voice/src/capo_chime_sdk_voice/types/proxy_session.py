"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ProxySession``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.capability_list
    import capo_chime_sdk_voice.types.geo_match_level
    import capo_chime_sdk_voice.types.geo_match_params
    import capo_chime_sdk_voice.types.iso8601_timestamp
    import capo_chime_sdk_voice.types.non_empty_string128
    import capo_chime_sdk_voice.types.number_selection_behavior
    import capo_chime_sdk_voice.types.participants
    import capo_chime_sdk_voice.types.positive_integer
    import capo_chime_sdk_voice.types.proxy_session_status
    import capo_chime_sdk_voice.types.string128
    import capo_chime_sdk_voice.types.voice_connector_id


class ProxySession(TypedDict, closed=True):
    voice_connector_id: NotRequired[
        "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    ]
    """<p>The Voice Connector ID.</p>"""
    proxy_session_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    ]
    """<p>The proxy session ID.</p>"""
    name: NotRequired["capo_chime_sdk_voice.types.string128.String128"]
    """<p>The proxy session name.</p>"""
    status: NotRequired[
        "capo_chime_sdk_voice.types.proxy_session_status.ProxySessionStatus"
    ]
    """<p>The proxy session status.</p>"""
    expiry_minutes: NotRequired[
        "capo_chime_sdk_voice.types.positive_integer.PositiveInteger"
    ]
    """<p>The number of minutes allowed for the proxy session.</p>"""
    capabilities: NotRequired[
        "capo_chime_sdk_voice.types.capability_list.CapabilityList"
    ]
    """<p>The proxy session capabilities.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The created time stamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The updated time stamp, in ISO 8601 format.</p>"""
    ended_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The ended time stamp, in ISO 8601 format.</p>"""
    participants: NotRequired["capo_chime_sdk_voice.types.participants.Participants"]
    """<p>The proxy session participants.</p>"""
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
def serialize_json(value: ProxySession) -> dict:
    out: dict = {}
    if "voice_connector_id" in value:
        out["VoiceConnectorId"] = value["voice_connector_id"]
    if "proxy_session_id" in value:
        out["ProxySessionId"] = value["proxy_session_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_chime_sdk_voice.types.proxy_session_status

        out["Status"] = capo_chime_sdk_voice.types.proxy_session_status.serialize_json(
            value["status"]
        )
    if "expiry_minutes" in value:
        out["ExpiryMinutes"] = value["expiry_minutes"]
    if "capabilities" in value:
        import capo_chime_sdk_voice.types.capability_list

        out["Capabilities"] = capo_chime_sdk_voice.types.capability_list.serialize_json(
            value["capabilities"]
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "ended_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["EndedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["ended_timestamp"]
            )
        )
    if "participants" in value:
        import capo_chime_sdk_voice.types.participants

        out["Participants"] = capo_chime_sdk_voice.types.participants.serialize_json(
            value["participants"]
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


def deserialize_json(data: dict) -> ProxySession:
    out: ProxySession = {}  # type: ignore[typeddict-item]
    if data.get("VoiceConnectorId") is not None:
        out["voice_connector_id"] = data["VoiceConnectorId"]
    if data.get("ProxySessionId") is not None:
        out["proxy_session_id"] = data["ProxySessionId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_chime_sdk_voice.types.proxy_session_status

        out["status"] = (
            capo_chime_sdk_voice.types.proxy_session_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("ExpiryMinutes") is not None:
        out["expiry_minutes"] = data["ExpiryMinutes"]
    if data.get("Capabilities") is not None:
        import capo_chime_sdk_voice.types.capability_list

        out["capabilities"] = (
            capo_chime_sdk_voice.types.capability_list.deserialize_json(
                data["Capabilities"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if data.get("EndedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["ended_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["EndedTimestamp"]
            )
        )
    if data.get("Participants") is not None:
        import capo_chime_sdk_voice.types.participants

        out["participants"] = capo_chime_sdk_voice.types.participants.deserialize_json(
            data["Participants"]
        )
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


def redact_sensitive(value: ProxySession) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "participants" in value:
        import capo_chime_sdk_voice.types.participants

        out["participants"] = capo_chime_sdk_voice.types.participants.redact_sensitive(
            value["participants"]
        )
    return out
