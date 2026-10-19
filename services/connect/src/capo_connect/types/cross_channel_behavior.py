"""Generated from Smithy shape ``com.amazonaws.connect#CrossChannelBehavior``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.behavior_type


class CrossChannelBehavior(TypedDict, closed=True):
    behavior_type: "capo_connect.types.behavior_type.BehaviorType"
    """<p>Specifies the other channels that can be routed to an agent handling their current channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossChannelBehavior) -> dict:
    out: dict = {}
    import capo_connect.types.behavior_type

    out["BehaviorType"] = capo_connect.types.behavior_type.serialize_json(
        value["behavior_type"]
    )
    return out


def deserialize_json(data: dict) -> CrossChannelBehavior:
    out: CrossChannelBehavior = {}  # type: ignore[typeddict-item]
    if data.get("BehaviorType") is not None:
        import capo_connect.types.behavior_type

        out["behavior_type"] = capo_connect.types.behavior_type.deserialize_json(
            data["BehaviorType"]
        )
    else:
        import typing

        out["behavior_type"] = typing.cast(
            "capo_connect.types.behavior_type.BehaviorType", ""
        )
    return out
