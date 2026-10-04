"""Generated from Smithy shape ``com.amazonaws.mediatailor#ClientSideBeaconingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.beacon_event_type_list
    import capo_mediatailor.types.client_side_beaconing_mode


class ClientSideBeaconingConfiguration(TypedDict, closed=True):
    reporting_mode: (
        "capo_mediatailor.types.client_side_beaconing_mode.ClientSideBeaconingMode"
    )
    """<p>Specifies whether MediaTailor includes its beacons in the ad tracking response. Valid values, which are case-sensitive:</p> <ul> <li> <p> <code>INSIGHTS</code> – MediaTailor includes its beacons in the ad tracking response.</p> </li> <li> <p> <code>DISABLED</code> – MediaTailor doesn't include its beacons in the ad tracking response.</p> </li> </ul> <p>If you send a <code>ClientSide</code> object, this setting is required. If you omit <code>BeaconingConfiguration</code> or <code>ClientSide</code> entirely, MediaTailor uses <code>INSIGHTS</code>.</p> <p> <code>PutPlaybackConfiguration</code> replaces the whole playback configuration. To keep beaconing off, include <code>DISABLED</code> in every subsequent write.</p>"""
    additional_event_types: NotRequired[
        "capo_mediatailor.types.beacon_event_type_list.BeaconEventTypeList"
    ]
    """<p>The player operation events to report on, in addition to the ad progress events that MediaTailor always reports on. The default is an empty list. This parameter is valid only when <code>ReportingMode</code> is <code>INSIGHTS</code>. MediaTailor rejects the request if you specify a value while <code>ReportingMode</code> is <code>DISABLED</code>, or if you specify duplicate values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientSideBeaconingConfiguration) -> dict:
    out: dict = {}
    import capo_mediatailor.types.client_side_beaconing_mode

    out["ReportingMode"] = (
        capo_mediatailor.types.client_side_beaconing_mode.serialize_json(
            value["reporting_mode"]
        )
    )
    if "additional_event_types" in value:
        import capo_mediatailor.types.beacon_event_type_list

        out["AdditionalEventTypes"] = (
            capo_mediatailor.types.beacon_event_type_list.serialize_json(
                value["additional_event_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClientSideBeaconingConfiguration:
    out: ClientSideBeaconingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ReportingMode") is not None:
        import capo_mediatailor.types.client_side_beaconing_mode

        out["reporting_mode"] = (
            capo_mediatailor.types.client_side_beaconing_mode.deserialize_json(
                data["ReportingMode"]
            )
        )
    else:
        raise DeserializationError(
            "ClientSideBeaconingConfiguration.reporting_mode required"
        )
    if data.get("AdditionalEventTypes") is not None:
        import capo_mediatailor.types.beacon_event_type_list

        out["additional_event_types"] = (
            capo_mediatailor.types.beacon_event_type_list.deserialize_json(
                data["AdditionalEventTypes"]
            )
        )
    return out
