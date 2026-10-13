"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldCollapseStateOption``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_field_collapse_state
    import capo_quicksight.types.pivot_table_field_collapse_state_target


class PivotTableFieldCollapseStateOption(TypedDict, closed=True):
    target: "capo_quicksight.types.pivot_table_field_collapse_state_target.PivotTableFieldCollapseStateTarget"
    """<p>A tagged-union object that sets the collapse state.</p>"""
    state: NotRequired[
        "capo_quicksight.types.pivot_table_field_collapse_state.PivotTableFieldCollapseState"
    ]
    """<p>The state of the field target of a pivot table. Choose one of the following options:</p> <ul> <li> <p> <code>COLLAPSED</code> </p> </li> <li> <p> <code>EXPANDED</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldCollapseStateOption) -> dict:
    out: dict = {}
    import capo_quicksight.types.pivot_table_field_collapse_state_target

    out["Target"] = (
        capo_quicksight.types.pivot_table_field_collapse_state_target.serialize_json(
            value["target"]
        )
    )
    if "state" in value:
        import capo_quicksight.types.pivot_table_field_collapse_state

        out["State"] = (
            capo_quicksight.types.pivot_table_field_collapse_state.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableFieldCollapseStateOption:
    out: PivotTableFieldCollapseStateOption = {}  # type: ignore[typeddict-item]
    if data.get("Target") is not None:
        import capo_quicksight.types.pivot_table_field_collapse_state_target

        out["target"] = (
            capo_quicksight.types.pivot_table_field_collapse_state_target.deserialize_json(
                data["Target"]
            )
        )
    else:
        raise DeserializationError("PivotTableFieldCollapseStateOption.target required")
    if data.get("State") is not None:
        import capo_quicksight.types.pivot_table_field_collapse_state

        out["state"] = (
            capo_quicksight.types.pivot_table_field_collapse_state.deserialize_json(
                data["State"]
            )
        )
    return out


def redact_sensitive(value: PivotTableFieldCollapseStateOption) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target" in value:
        import capo_quicksight.types.pivot_table_field_collapse_state_target

        out["target"] = (
            capo_quicksight.types.pivot_table_field_collapse_state_target.redact_sensitive(
                value["target"]
            )
        )
    return out
