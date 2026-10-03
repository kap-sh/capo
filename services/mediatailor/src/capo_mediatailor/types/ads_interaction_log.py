"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdsInteractionLog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__ads_interaction_exclude_event_types_list
    import capo_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list


class AdsInteractionLog(TypedDict, closed=True):
    publish_opt_in_event_types: NotRequired[
        "capo_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list.__adsInteractionPublishOptInEventTypesList"
    ]
    """<p>Indicates that MediaTailor will emit the selected events in the logs for playback sessions that are initialized with this configuration. These events are not emitted by default and must be explicitly opted in. For descriptions of each event type, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/ads-log-format.html">MediaTailor ADS logs description and event types</a> in Elemental MediaTailor User Guide.</p>"""
    exclude_event_types: NotRequired[
        "capo_mediatailor.types.__ads_interaction_exclude_event_types_list.__adsInteractionExcludeEventTypesList"
    ]
    """<p>Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdsInteractionLog) -> dict:
    out: dict = {}
    if "publish_opt_in_event_types" in value:
        import capo_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list

        out["PublishOptInEventTypes"] = (
            capo_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list.serialize_json(
                value["publish_opt_in_event_types"]
            )
        )
    if "exclude_event_types" in value:
        import capo_mediatailor.types.__ads_interaction_exclude_event_types_list

        out["ExcludeEventTypes"] = (
            capo_mediatailor.types.__ads_interaction_exclude_event_types_list.serialize_json(
                value["exclude_event_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdsInteractionLog:
    out: AdsInteractionLog = {}  # type: ignore[typeddict-item]
    if data.get("PublishOptInEventTypes") is not None:
        import capo_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list

        out["publish_opt_in_event_types"] = (
            capo_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list.deserialize_json(
                data["PublishOptInEventTypes"]
            )
        )
    if data.get("ExcludeEventTypes") is not None:
        import capo_mediatailor.types.__ads_interaction_exclude_event_types_list

        out["exclude_event_types"] = (
            capo_mediatailor.types.__ads_interaction_exclude_event_types_list.deserialize_json(
                data["ExcludeEventTypes"]
            )
        )
    return out
