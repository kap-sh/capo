"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateIntermediateTableOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table


class UpdateIntermediateTableOutput(TypedDict, closed=True):
    intermediate_table: "capo_cleanrooms.types.intermediate_table.IntermediateTable"
    """<p>The updated intermediate table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntermediateTableOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.intermediate_table

    out["intermediateTable"] = capo_cleanrooms.types.intermediate_table.serialize_json(
        value["intermediate_table"]
    )
    return out


def deserialize_json(data: dict) -> UpdateIntermediateTableOutput:
    out: UpdateIntermediateTableOutput = {}  # type: ignore[typeddict-item]
    if data.get("intermediateTable") is not None:
        import capo_cleanrooms.types.intermediate_table

        out["intermediate_table"] = (
            capo_cleanrooms.types.intermediate_table.deserialize_json(
                data["intermediateTable"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIntermediateTableOutput.intermediate_table required"
        )
    return out


def redact_sensitive(value: UpdateIntermediateTableOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "intermediate_table" in value:
        import capo_cleanrooms.types.intermediate_table

        out["intermediate_table"] = (
            capo_cleanrooms.types.intermediate_table.redact_sensitive(
                value["intermediate_table"]
            )
        )
    return out
