"""Generated from Smithy shape ``com.amazonaws.connect#OutboundStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.outbound_strategy_config
    import capo_connect.types.outbound_strategy_type


class OutboundStrategy(TypedDict, closed=True):
    type: "capo_connect.types.outbound_strategy_type.OutboundStrategyType"
    """<p>Type of the outbound strategy.</p>"""
    config: NotRequired[
        "capo_connect.types.outbound_strategy_config.OutboundStrategyConfig"
    ]
    """<p>Config of the outbound strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundStrategy) -> dict:
    out: dict = {}
    import capo_connect.types.outbound_strategy_type

    out["Type"] = capo_connect.types.outbound_strategy_type.serialize_json(
        value["type"]
    )
    if "config" in value:
        import capo_connect.types.outbound_strategy_config

        out["Config"] = capo_connect.types.outbound_strategy_config.serialize_json(
            value["config"]
        )
    return out


def deserialize_json(data: dict) -> OutboundStrategy:
    out: OutboundStrategy = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_connect.types.outbound_strategy_type

        out["type"] = capo_connect.types.outbound_strategy_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_connect.types.outbound_strategy_type.OutboundStrategyType", ""
        )
    if data.get("Config") is not None:
        import capo_connect.types.outbound_strategy_config

        out["config"] = capo_connect.types.outbound_strategy_config.deserialize_json(
            data["Config"]
        )
    return out
