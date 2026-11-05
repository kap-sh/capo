"""Generated from Smithy shape ``com.amazonaws.ecs#LogDriverVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.log_driver


class LogDriverVolumeConfiguration(TypedDict, closed=True):
    driver: "capo_ecs.types.log_driver.LogDriver"
    """<p>The log driver whose log files the volume contains. The only supported value is <code>json-file</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogDriverVolumeConfiguration) -> dict:
    out: dict = {}
    import capo_ecs.types.log_driver

    out["driver"] = capo_ecs.types.log_driver.serialize_aws_json_1_1(value["driver"])
    return out


def deserialize_aws_json_1_1(data: dict) -> LogDriverVolumeConfiguration:
    out: LogDriverVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("driver") is not None:
        import capo_ecs.types.log_driver

        out["driver"] = capo_ecs.types.log_driver.deserialize_aws_json_1_1(
            data["driver"]
        )
    else:
        import typing

        out["driver"] = typing.cast("capo_ecs.types.log_driver.LogDriver", "")
    return out
