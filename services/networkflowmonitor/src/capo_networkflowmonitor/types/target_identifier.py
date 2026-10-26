"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TargetIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.target_id
    import capo_networkflowmonitor.types.target_type


class TargetIdentifier(TypedDict, closed=True):
    target_id: "capo_networkflowmonitor.types.target_id.TargetId"
    """<p>The identifier for a target, which is currently always an account ID .</p>"""
    target_type: "capo_networkflowmonitor.types.target_type.TargetType"
    """<p>The type of a target. A target type is currently always <code>ACCOUNT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetIdentifier) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.target_id

    out["targetId"] = capo_networkflowmonitor.types.target_id.serialize_json(
        value["target_id"]
    )
    import capo_networkflowmonitor.types.target_type

    out["targetType"] = capo_networkflowmonitor.types.target_type.serialize_json(
        value["target_type"]
    )
    return out


def deserialize_json(data: dict) -> TargetIdentifier:
    out: TargetIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("targetId") is not None:
        import capo_networkflowmonitor.types.target_id

        out["target_id"] = capo_networkflowmonitor.types.target_id.deserialize_json(
            data["targetId"]
        )
    else:
        out["target_id"] = {"$unknown": {"name": ""}}
    if data.get("targetType") is not None:
        import capo_networkflowmonitor.types.target_type

        out["target_type"] = capo_networkflowmonitor.types.target_type.deserialize_json(
            data["targetType"]
        )
    else:
        import typing

        out["target_type"] = typing.cast(
            "capo_networkflowmonitor.types.target_type.TargetType", ""
        )
    return out
