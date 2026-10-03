"""Generated from Smithy shape ``com.amazonaws.rum#PutRumEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rum.types.alias
    import capo_rum.types.app_monitor_details
    import capo_rum.types.app_monitor_id
    import capo_rum.types.rum_event_list
    import capo_rum.types.user_details


class PutRumEventsRequest(TypedDict, closed=True):
    id: "capo_rum.types.app_monitor_id.AppMonitorId"
    """<p>The ID of the app monitor that is sending this data.</p>"""
    batch_id: "str"
    """<p>A unique identifier for this batch of RUM event data.</p>"""
    app_monitor_details: "capo_rum.types.app_monitor_details.AppMonitorDetails"
    """<p>A structure that contains information about the app monitor that collected this telemetry information.</p>"""
    user_details: "capo_rum.types.user_details.UserDetails"
    """<p>A structure that contains information about the user session that this batch of events was collected from.</p>"""
    rum_events: "capo_rum.types.rum_event_list.RumEventList"
    """<p>An array of structures that contain the telemetry event data.</p>"""
    alias: NotRequired["capo_rum.types.alias.Alias"]
    """<p>If the app monitor uses a resource-based policy that requires <code>PutRumEvents</code> requests to specify a certain alias, specify that alias here. This alias will be compared to the <code>rum:alias</code> context key in the resource-based policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html">Using resource-based policies with CloudWatch RUM</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRumEventsRequest) -> dict:
    out: dict = {}
    out["BatchId"] = value["batch_id"]
    import capo_rum.types.app_monitor_details

    out["AppMonitorDetails"] = capo_rum.types.app_monitor_details.serialize_json(
        value["app_monitor_details"]
    )
    import capo_rum.types.user_details

    out["UserDetails"] = capo_rum.types.user_details.serialize_json(
        value["user_details"]
    )
    import capo_rum.types.rum_event_list

    out["RumEvents"] = capo_rum.types.rum_event_list.serialize_json(value["rum_events"])
    if "alias" in value:
        out["Alias"] = value["alias"]
    return out


def deserialize_json(data: dict) -> PutRumEventsRequest:
    out: PutRumEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("BatchId") is not None:
        out["batch_id"] = data["BatchId"]
    else:
        raise DeserializationError("PutRumEventsRequest.batch_id required")
    if data.get("AppMonitorDetails") is not None:
        import capo_rum.types.app_monitor_details

        out["app_monitor_details"] = (
            capo_rum.types.app_monitor_details.deserialize_json(
                data["AppMonitorDetails"]
            )
        )
    else:
        raise DeserializationError("PutRumEventsRequest.app_monitor_details required")
    if data.get("UserDetails") is not None:
        import capo_rum.types.user_details

        out["user_details"] = capo_rum.types.user_details.deserialize_json(
            data["UserDetails"]
        )
    else:
        raise DeserializationError("PutRumEventsRequest.user_details required")
    if data.get("RumEvents") is not None:
        import capo_rum.types.rum_event_list

        out["rum_events"] = capo_rum.types.rum_event_list.deserialize_json(
            data["RumEvents"]
        )
    else:
        raise DeserializationError("PutRumEventsRequest.rum_events required")
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    return out
