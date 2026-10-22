"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotResolutionSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_resolution_strategy


class SlotResolutionSetting(TypedDict, closed=True):
    slot_resolution_strategy: (
        "capo_lex_models_v2.types.slot_resolution_strategy.SlotResolutionStrategy"
    )
    """<p>Specifies whether assisted slot resolution is turned on for the slot or not. If the value is <code>EnhancedFallback</code>, assisted slot resolution is activated when Amazon Lex V2 defaults to the <code>AMAZON.FallbackIntent</code>. If the value is <code>Default</code>, assisted slot resolution is turned off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotResolutionSetting) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.slot_resolution_strategy

    out["slotResolutionStrategy"] = (
        capo_lex_models_v2.types.slot_resolution_strategy.serialize_json(
            value["slot_resolution_strategy"]
        )
    )
    return out


def deserialize_json(data: dict) -> SlotResolutionSetting:
    out: SlotResolutionSetting = {}  # type: ignore[typeddict-item]
    if data.get("slotResolutionStrategy") is not None:
        import capo_lex_models_v2.types.slot_resolution_strategy

        out["slot_resolution_strategy"] = (
            capo_lex_models_v2.types.slot_resolution_strategy.deserialize_json(
                data["slotResolutionStrategy"]
            )
        )
    else:
        import typing

        out["slot_resolution_strategy"] = typing.cast(
            "capo_lex_models_v2.types.slot_resolution_strategy.SlotResolutionStrategy",
            "",
        )
    return out
