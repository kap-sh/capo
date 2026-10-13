"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetIntermediateTableOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table


class GetIntermediateTableOutput(TypedDict, closed=True):
    intermediate_table: "capo_cleanrooms.types.intermediate_table.IntermediateTable"
    """<p>The intermediate table retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntermediateTableOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.intermediate_table

    out["intermediateTable"] = capo_cleanrooms.types.intermediate_table.serialize_json(
        value["intermediate_table"]
    )
    return out


def deserialize_json(data: dict) -> GetIntermediateTableOutput:
    out: GetIntermediateTableOutput = {}  # type: ignore[typeddict-item]
    if data.get("intermediateTable") is not None:
        import capo_cleanrooms.types.intermediate_table

        out["intermediate_table"] = (
            capo_cleanrooms.types.intermediate_table.deserialize_json(
                data["intermediateTable"]
            )
        )
    else:
        raise DeserializationError(
            "GetIntermediateTableOutput.intermediate_table required"
        )
    return out


def redact_sensitive(value: GetIntermediateTableOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "intermediate_table" in value:
        import capo_cleanrooms.types.intermediate_table

        out["intermediate_table"] = (
            capo_cleanrooms.types.intermediate_table.redact_sensitive(
                value["intermediate_table"]
            )
        )
    return out
