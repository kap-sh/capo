"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateEventLogConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.log_configuration_id
    import capo_iot_managed_integrations.types.log_level


class UpdateEventLogConfigurationRequest(TypedDict, closed=True):
    id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId"
    """<p>The log configuration id.</p>"""
    event_log_level: "capo_iot_managed_integrations.types.log_level.LogLevel"
    """<p>The log level for the event in terms of severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventLogConfigurationRequest) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.log_level

    out["EventLogLevel"] = capo_iot_managed_integrations.types.log_level.serialize_json(
        value["event_log_level"]
    )
    return out


def deserialize_json(data: dict) -> UpdateEventLogConfigurationRequest:
    out: UpdateEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventLogLevel") is not None:
        import capo_iot_managed_integrations.types.log_level

        out["event_log_level"] = (
            capo_iot_managed_integrations.types.log_level.deserialize_json(
                data["EventLogLevel"]
            )
        )
    else:
        import typing

        out["event_log_level"] = typing.cast(
            "capo_iot_managed_integrations.types.log_level.LogLevel", ""
        )
    return out
