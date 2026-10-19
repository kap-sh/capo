"""Generated from Smithy shape ``com.amazonaws.appintegrations#ExecutionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.execution_mode
    import capo_appintegrations.types.on_demand_configuration
    import capo_appintegrations.types.schedule_configuration


class ExecutionConfiguration(TypedDict, closed=True):
    execution_mode: "capo_appintegrations.types.execution_mode.ExecutionMode"
    """<p>The mode for data import/export execution.</p>"""
    on_demand_configuration: NotRequired[
        "capo_appintegrations.types.on_demand_configuration.OnDemandConfiguration"
    ]
    schedule_configuration: NotRequired[
        "capo_appintegrations.types.schedule_configuration.ScheduleConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionConfiguration) -> dict:
    out: dict = {}
    import capo_appintegrations.types.execution_mode

    out["ExecutionMode"] = capo_appintegrations.types.execution_mode.serialize_json(
        value["execution_mode"]
    )
    if "on_demand_configuration" in value:
        import capo_appintegrations.types.on_demand_configuration

        out["OnDemandConfiguration"] = (
            capo_appintegrations.types.on_demand_configuration.serialize_json(
                value["on_demand_configuration"]
            )
        )
    if "schedule_configuration" in value:
        import capo_appintegrations.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            capo_appintegrations.types.schedule_configuration.serialize_json(
                value["schedule_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExecutionConfiguration:
    out: ExecutionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ExecutionMode") is not None:
        import capo_appintegrations.types.execution_mode

        out["execution_mode"] = (
            capo_appintegrations.types.execution_mode.deserialize_json(
                data["ExecutionMode"]
            )
        )
    else:
        import typing

        out["execution_mode"] = typing.cast(
            "capo_appintegrations.types.execution_mode.ExecutionMode", ""
        )
    if data.get("OnDemandConfiguration") is not None:
        import capo_appintegrations.types.on_demand_configuration

        out["on_demand_configuration"] = (
            capo_appintegrations.types.on_demand_configuration.deserialize_json(
                data["OnDemandConfiguration"]
            )
        )
    if data.get("ScheduleConfiguration") is not None:
        import capo_appintegrations.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_appintegrations.types.schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    return out
