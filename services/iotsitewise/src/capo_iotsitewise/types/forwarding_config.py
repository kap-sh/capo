"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ForwardingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.forwarding_config_state


class ForwardingConfig(TypedDict, closed=True):
    state: "capo_iotsitewise.types.forwarding_config_state.ForwardingConfigState"
    """<p>The forwarding state for the given property. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForwardingConfig) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.forwarding_config_state

    out["state"] = capo_iotsitewise.types.forwarding_config_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> ForwardingConfig:
    out: ForwardingConfig = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_iotsitewise.types.forwarding_config_state

        out["state"] = capo_iotsitewise.types.forwarding_config_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_iotsitewise.types.forwarding_config_state.ForwardingConfigState", ""
        )
    return out
