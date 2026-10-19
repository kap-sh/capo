"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTaskLogOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_event_log_option_list
    import capo_iot_wireless.types.fuota_task_type
    import capo_iot_wireless.types.log_level


class FuotaTaskLogOption(TypedDict, closed=True):
    type: "capo_iot_wireless.types.fuota_task_type.FuotaTaskType"
    """<p>The FUOTA task type.</p>"""
    log_level: "capo_iot_wireless.types.log_level.LogLevel"
    events: NotRequired[
        "capo_iot_wireless.types.fuota_task_event_log_option_list.FuotaTaskEventLogOptionList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FuotaTaskLogOption) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.fuota_task_type

    out["Type"] = capo_iot_wireless.types.fuota_task_type.serialize_json(value["type"])
    import capo_iot_wireless.types.log_level

    out["LogLevel"] = capo_iot_wireless.types.log_level.serialize_json(
        value["log_level"]
    )
    if "events" in value:
        import capo_iot_wireless.types.fuota_task_event_log_option_list

        out["Events"] = (
            capo_iot_wireless.types.fuota_task_event_log_option_list.serialize_json(
                value["events"]
            )
        )
    return out


def deserialize_json(data: dict) -> FuotaTaskLogOption:
    out: FuotaTaskLogOption = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_iot_wireless.types.fuota_task_type

        out["type"] = capo_iot_wireless.types.fuota_task_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_iot_wireless.types.fuota_task_type.FuotaTaskType", ""
        )
    if data.get("LogLevel") is not None:
        import capo_iot_wireless.types.log_level

        out["log_level"] = capo_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    else:
        import typing

        out["log_level"] = typing.cast("capo_iot_wireless.types.log_level.LogLevel", "")
    if data.get("Events") is not None:
        import capo_iot_wireless.types.fuota_task_event_log_option_list

        out["events"] = (
            capo_iot_wireless.types.fuota_task_event_log_option_list.deserialize_json(
                data["Events"]
            )
        )
    return out
