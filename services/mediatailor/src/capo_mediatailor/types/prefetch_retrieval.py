"""Generated from Smithy shape ``com.amazonaws.mediatailor#PrefetchRetrieval``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.traffic_shaping_retrieval_window
    import capo_mediatailor.types.traffic_shaping_tps_configuration
    import capo_mediatailor.types.traffic_shaping_type


class PrefetchRetrieval(TypedDict, closed=True):
    dynamic_variables: NotRequired[
        "capo_mediatailor.types.__map_of__string.__mapOf__string"
    ]
    """<p>The dynamic variables to use for substitution during prefetch requests to the ad decision server (ADS).</p> <p>You initially configure <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/variables.html">dynamic variables</a> for the ADS URL when you set up your playback configuration. When you specify <code>DynamicVariables</code> for prefetch retrieval, MediaTailor includes the dynamic variables in the request to the ADS.</p>"""
    end_time: "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    """<p>The time when prefetch retrieval ends for the ad break. Prefetching will be attempted for manifest requests that occur at or before this time.</p>"""
    start_time: NotRequired["capo_mediatailor.types.__timestamp_unix.__timestampUnix"]
    """<p>The time when prefetch retrievals can start for this break. Ad prefetching will be attempted for manifest requests that occur at or after this time. Defaults to the current time. If not specified, the prefetch retrieval starts as soon as possible.</p>"""
    traffic_shaping_type: NotRequired[
        "capo_mediatailor.types.traffic_shaping_type.TrafficShapingType"
    ]
    """<p>Indicates the type of traffic shaping used to limit the number of requests to the ADS at one time.</p>"""
    traffic_shaping_retrieval_window: NotRequired[
        "capo_mediatailor.types.traffic_shaping_retrieval_window.TrafficShapingRetrievalWindow"
    ]
    """<p>The configuration that tells Elemental MediaTailor how many seconds to spread out requests to the ad decision server (ADS). Instead of sending ADS requests for all sessions at the same time, MediaTailor spreads the requests across the amount of time specified in the retrieval window.</p>"""
    traffic_shaping_tps_configuration: NotRequired[
        "capo_mediatailor.types.traffic_shaping_tps_configuration.TrafficShapingTpsConfiguration"
    ]
    """<p>The configuration for TPS-based traffic shaping. This approach limits requests to the ad decision server (ADS) based on transactions per second and concurrent users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrefetchRetrieval) -> dict:
    out: dict = {}
    if "dynamic_variables" in value:
        import capo_mediatailor.types.__map_of__string

        out["DynamicVariables"] = (
            capo_mediatailor.types.__map_of__string.serialize_json(
                value["dynamic_variables"]
            )
        )
    import capo_mediatailor.types.__timestamp_unix

    out["EndTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
        value["end_time"]
    )
    if "start_time" in value:
        import capo_mediatailor.types.__timestamp_unix

        out["StartTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
            value["start_time"]
        )
    if "traffic_shaping_type" in value:
        import capo_mediatailor.types.traffic_shaping_type

        out["TrafficShapingType"] = (
            capo_mediatailor.types.traffic_shaping_type.serialize_json(
                value["traffic_shaping_type"]
            )
        )
    if "traffic_shaping_retrieval_window" in value:
        import capo_mediatailor.types.traffic_shaping_retrieval_window

        out["TrafficShapingRetrievalWindow"] = (
            capo_mediatailor.types.traffic_shaping_retrieval_window.serialize_json(
                value["traffic_shaping_retrieval_window"]
            )
        )
    if "traffic_shaping_tps_configuration" in value:
        import capo_mediatailor.types.traffic_shaping_tps_configuration

        out["TrafficShapingTpsConfiguration"] = (
            capo_mediatailor.types.traffic_shaping_tps_configuration.serialize_json(
                value["traffic_shaping_tps_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrefetchRetrieval:
    out: PrefetchRetrieval = {}  # type: ignore[typeddict-item]
    if data.get("DynamicVariables") is not None:
        import capo_mediatailor.types.__map_of__string

        out["dynamic_variables"] = (
            capo_mediatailor.types.__map_of__string.deserialize_json(
                data["DynamicVariables"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["end_time"] = capo_mediatailor.types.__timestamp_unix.deserialize_json(
            data["EndTime"]
        )
    else:
        raise DeserializationError("PrefetchRetrieval.end_time required")
    if data.get("StartTime") is not None:
        import capo_mediatailor.types.__timestamp_unix

        out["start_time"] = capo_mediatailor.types.__timestamp_unix.deserialize_json(
            data["StartTime"]
        )
    if data.get("TrafficShapingType") is not None:
        import capo_mediatailor.types.traffic_shaping_type

        out["traffic_shaping_type"] = (
            capo_mediatailor.types.traffic_shaping_type.deserialize_json(
                data["TrafficShapingType"]
            )
        )
    if data.get("TrafficShapingRetrievalWindow") is not None:
        import capo_mediatailor.types.traffic_shaping_retrieval_window

        out["traffic_shaping_retrieval_window"] = (
            capo_mediatailor.types.traffic_shaping_retrieval_window.deserialize_json(
                data["TrafficShapingRetrievalWindow"]
            )
        )
    if data.get("TrafficShapingTpsConfiguration") is not None:
        import capo_mediatailor.types.traffic_shaping_tps_configuration

        out["traffic_shaping_tps_configuration"] = (
            capo_mediatailor.types.traffic_shaping_tps_configuration.deserialize_json(
                data["TrafficShapingTpsConfiguration"]
            )
        )
    return out
