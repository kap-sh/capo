"""Generated from Smithy shape ``com.amazonaws.quicksight#ValidationStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.validation_strategy_mode


class ValidationStrategy(TypedDict, closed=True):
    mode: "capo_quicksight.types.validation_strategy_mode.ValidationStrategyMode"
    """<p>The mode of validation for the asset to be created or updated. When you set this value to <code>STRICT</code>, strict validation for every error is enforced. When you set this value to <code>LENIENT</code>, validation is skipped for specific UI errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationStrategy) -> dict:
    out: dict = {}
    import capo_quicksight.types.validation_strategy_mode

    out["Mode"] = capo_quicksight.types.validation_strategy_mode.serialize_json(
        value["mode"]
    )
    return out


def deserialize_json(data: dict) -> ValidationStrategy:
    out: ValidationStrategy = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_quicksight.types.validation_strategy_mode

        out["mode"] = capo_quicksight.types.validation_strategy_mode.deserialize_json(
            data["Mode"]
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_quicksight.types.validation_strategy_mode.ValidationStrategyMode", ""
        )
    return out
