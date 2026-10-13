"""Generated from Smithy shape ``com.amazonaws.quicksight#TableUnaggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.table_unaggregated_field_list


class TableUnaggregatedFieldWells(TypedDict, closed=True):
    values: NotRequired[
        "capo_quicksight.types.table_unaggregated_field_list.TableUnaggregatedFieldList"
    ]
    """<p>The values field well for a pivot table. Values are unaggregated for an unaggregated table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableUnaggregatedFieldWells) -> dict:
    out: dict = {}
    if "values" in value:
        import capo_quicksight.types.table_unaggregated_field_list

        out["Values"] = (
            capo_quicksight.types.table_unaggregated_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableUnaggregatedFieldWells:
    out: TableUnaggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("Values") is not None:
        import capo_quicksight.types.table_unaggregated_field_list

        out["values"] = (
            capo_quicksight.types.table_unaggregated_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out


def redact_sensitive(value: TableUnaggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_quicksight.types.table_unaggregated_field_list

        out["values"] = (
            capo_quicksight.types.table_unaggregated_field_list.redact_sensitive(
                value["values"]
            )
        )
    return out
