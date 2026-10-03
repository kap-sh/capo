"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#CustomerAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.acknowledge_action_configuration
    import capo_iot_events_data.types.customer_action_name
    import capo_iot_events_data.types.disable_action_configuration
    import capo_iot_events_data.types.enable_action_configuration
    import capo_iot_events_data.types.reset_action_configuration
    import capo_iot_events_data.types.snooze_action_configuration


class CustomerAction(TypedDict, closed=True):
    action_name: NotRequired[
        "capo_iot_events_data.types.customer_action_name.CustomerActionName"
    ]
    """<p>The name of the action. The action name can be one of the following values:</p> <ul> <li> <p> <code>SNOOZE</code> - When you snooze the alarm, the alarm state changes to <code>SNOOZE_DISABLED</code>.</p> </li> <li> <p> <code>ENABLE</code> - When you enable the alarm, the alarm state changes to <code>NORMAL</code>.</p> </li> <li> <p> <code>DISABLE</code> - When you disable the alarm, the alarm state changes to <code>DISABLED</code>.</p> </li> <li> <p> <code>ACKNOWLEDGE</code> - When you acknowledge the alarm, the alarm state changes to <code>ACKNOWLEDGED</code>.</p> </li> <li> <p> <code>RESET</code> - When you reset the alarm, the alarm state changes to <code>NORMAL</code>.</p> </li> </ul> <p>For more information, see the <a href="https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_AlarmState.html">AlarmState</a> API.</p>"""
    snooze_action_configuration: NotRequired[
        "capo_iot_events_data.types.snooze_action_configuration.SnoozeActionConfiguration"
    ]
    """<p>Contains the configuration information of a snooze action.</p>"""
    enable_action_configuration: NotRequired[
        "capo_iot_events_data.types.enable_action_configuration.EnableActionConfiguration"
    ]
    """<p>Contains the configuration information of an enable action.</p>"""
    disable_action_configuration: NotRequired[
        "capo_iot_events_data.types.disable_action_configuration.DisableActionConfiguration"
    ]
    """<p>Contains the configuration information of a disable action.</p>"""
    acknowledge_action_configuration: NotRequired[
        "capo_iot_events_data.types.acknowledge_action_configuration.AcknowledgeActionConfiguration"
    ]
    """<p>Contains the configuration information of an acknowledge action.</p>"""
    reset_action_configuration: NotRequired[
        "capo_iot_events_data.types.reset_action_configuration.ResetActionConfiguration"
    ]
    """<p>Contains the configuration information of a reset action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerAction) -> dict:
    out: dict = {}
    if "action_name" in value:
        import capo_iot_events_data.types.customer_action_name

        out["actionName"] = (
            capo_iot_events_data.types.customer_action_name.serialize_json(
                value["action_name"]
            )
        )
    if "snooze_action_configuration" in value:
        import capo_iot_events_data.types.snooze_action_configuration

        out["snoozeActionConfiguration"] = (
            capo_iot_events_data.types.snooze_action_configuration.serialize_json(
                value["snooze_action_configuration"]
            )
        )
    if "enable_action_configuration" in value:
        import capo_iot_events_data.types.enable_action_configuration

        out["enableActionConfiguration"] = (
            capo_iot_events_data.types.enable_action_configuration.serialize_json(
                value["enable_action_configuration"]
            )
        )
    if "disable_action_configuration" in value:
        import capo_iot_events_data.types.disable_action_configuration

        out["disableActionConfiguration"] = (
            capo_iot_events_data.types.disable_action_configuration.serialize_json(
                value["disable_action_configuration"]
            )
        )
    if "acknowledge_action_configuration" in value:
        import capo_iot_events_data.types.acknowledge_action_configuration

        out["acknowledgeActionConfiguration"] = (
            capo_iot_events_data.types.acknowledge_action_configuration.serialize_json(
                value["acknowledge_action_configuration"]
            )
        )
    if "reset_action_configuration" in value:
        import capo_iot_events_data.types.reset_action_configuration

        out["resetActionConfiguration"] = (
            capo_iot_events_data.types.reset_action_configuration.serialize_json(
                value["reset_action_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomerAction:
    out: CustomerAction = {}  # type: ignore[typeddict-item]
    if data.get("actionName") is not None:
        import capo_iot_events_data.types.customer_action_name

        out["action_name"] = (
            capo_iot_events_data.types.customer_action_name.deserialize_json(
                data["actionName"]
            )
        )
    if data.get("snoozeActionConfiguration") is not None:
        import capo_iot_events_data.types.snooze_action_configuration

        out["snooze_action_configuration"] = (
            capo_iot_events_data.types.snooze_action_configuration.deserialize_json(
                data["snoozeActionConfiguration"]
            )
        )
    if data.get("enableActionConfiguration") is not None:
        import capo_iot_events_data.types.enable_action_configuration

        out["enable_action_configuration"] = (
            capo_iot_events_data.types.enable_action_configuration.deserialize_json(
                data["enableActionConfiguration"]
            )
        )
    if data.get("disableActionConfiguration") is not None:
        import capo_iot_events_data.types.disable_action_configuration

        out["disable_action_configuration"] = (
            capo_iot_events_data.types.disable_action_configuration.deserialize_json(
                data["disableActionConfiguration"]
            )
        )
    if data.get("acknowledgeActionConfiguration") is not None:
        import capo_iot_events_data.types.acknowledge_action_configuration

        out["acknowledge_action_configuration"] = (
            capo_iot_events_data.types.acknowledge_action_configuration.deserialize_json(
                data["acknowledgeActionConfiguration"]
            )
        )
    if data.get("resetActionConfiguration") is not None:
        import capo_iot_events_data.types.reset_action_configuration

        out["reset_action_configuration"] = (
            capo_iot_events_data.types.reset_action_configuration.deserialize_json(
                data["resetActionConfiguration"]
            )
        )
    return out
