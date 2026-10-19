"""Generated from Smithy shape ``com.amazonaws.quicksight#JoinOperandProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.output_column_name_override_list


class JoinOperandProperties(TypedDict, closed=True):
    output_column_name_overrides: "capo_quicksight.types.output_column_name_override_list.OutputColumnNameOverrideList"
    """<p>A list of column name overrides to apply to the join operand's output columns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinOperandProperties) -> dict:
    out: dict = {}
    import capo_quicksight.types.output_column_name_override_list

    out["OutputColumnNameOverrides"] = (
        capo_quicksight.types.output_column_name_override_list.serialize_json(
            value["output_column_name_overrides"]
        )
    )
    return out


def deserialize_json(data: dict) -> JoinOperandProperties:
    out: JoinOperandProperties = {}  # type: ignore[typeddict-item]
    if data.get("OutputColumnNameOverrides") is not None:
        import capo_quicksight.types.output_column_name_override_list

        out["output_column_name_overrides"] = (
            capo_quicksight.types.output_column_name_override_list.deserialize_json(
                data["OutputColumnNameOverrides"]
            )
        )
    else:
        out["output_column_name_overrides"] = []
    return out
