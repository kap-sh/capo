"""Generated from Smithy shape ``com.amazonaws.iot#LogTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.log_target_name
    import capo_iot.types.log_target_type


class LogTarget(TypedDict, closed=True):
    target_type: "capo_iot.types.log_target_type.LogTargetType"
    """<p>The target type.</p>"""
    target_name: NotRequired["capo_iot.types.log_target_name.LogTargetName"]
    """<p>The target name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogTarget) -> dict:
    out: dict = {}
    import capo_iot.types.log_target_type

    out["targetType"] = capo_iot.types.log_target_type.serialize_json(
        value["target_type"]
    )
    if "target_name" in value:
        out["targetName"] = value["target_name"]
    return out


def deserialize_json(data: dict) -> LogTarget:
    out: LogTarget = {}  # type: ignore[typeddict-item]
    if data.get("targetType") is not None:
        import capo_iot.types.log_target_type

        out["target_type"] = capo_iot.types.log_target_type.deserialize_json(
            data["targetType"]
        )
    else:
        import typing

        out["target_type"] = typing.cast(
            "capo_iot.types.log_target_type.LogTargetType", ""
        )
    if data.get("targetName") is not None:
        out["target_name"] = data["targetName"]
    return out
