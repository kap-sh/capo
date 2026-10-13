"""Generated from Smithy shape ``com.amazonaws.quicksight#TransformStep``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aggregate_operation
    import capo_quicksight.types.append_operation
    import capo_quicksight.types.cast_column_types_operation
    import capo_quicksight.types.create_columns_operation
    import capo_quicksight.types.filters_operation
    import capo_quicksight.types.import_table_operation
    import capo_quicksight.types.join_operation
    import capo_quicksight.types.pivot_operation
    import capo_quicksight.types.project_operation
    import capo_quicksight.types.rename_columns_operation
    import capo_quicksight.types.unpivot_operation


class TransformStep(TypedDict, closed=True):
    import_table_step: NotRequired[
        "capo_quicksight.types.import_table_operation.ImportTableOperation"
    ]
    """<p>A transform step that brings data from a source table.</p>"""
    project_step: NotRequired[
        "capo_quicksight.types.project_operation.ProjectOperation"
    ]
    filters_step: NotRequired[
        "capo_quicksight.types.filters_operation.FiltersOperation"
    ]
    """<p>A transform step that applies filter conditions.</p>"""
    create_columns_step: NotRequired[
        "capo_quicksight.types.create_columns_operation.CreateColumnsOperation"
    ]
    rename_columns_step: NotRequired[
        "capo_quicksight.types.rename_columns_operation.RenameColumnsOperation"
    ]
    """<p>A transform step that changes the names of one or more columns.</p>"""
    cast_column_types_step: NotRequired[
        "capo_quicksight.types.cast_column_types_operation.CastColumnTypesOperation"
    ]
    """<p>A transform step that changes the data types of one or more columns.</p>"""
    join_step: NotRequired["capo_quicksight.types.join_operation.JoinOperation"]
    """<p>A transform step that combines data from two sources based on specified join conditions.</p>"""
    aggregate_step: NotRequired[
        "capo_quicksight.types.aggregate_operation.AggregateOperation"
    ]
    """<p>A transform step that groups data and applies aggregation functions to calculate summary values.</p>"""
    pivot_step: NotRequired["capo_quicksight.types.pivot_operation.PivotOperation"]
    """<p>A transform step that converts row values into columns to reshape the data structure.</p>"""
    unpivot_step: NotRequired[
        "capo_quicksight.types.unpivot_operation.UnpivotOperation"
    ]
    """<p>A transform step that converts columns into rows to normalize the data structure.</p>"""
    append_step: NotRequired["capo_quicksight.types.append_operation.AppendOperation"]
    """<p>A transform step that combines rows from multiple sources by stacking them vertically.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransformStep) -> dict:
    out: dict = {}
    if "import_table_step" in value:
        import capo_quicksight.types.import_table_operation

        out["ImportTableStep"] = (
            capo_quicksight.types.import_table_operation.serialize_json(
                value["import_table_step"]
            )
        )
    if "project_step" in value:
        import capo_quicksight.types.project_operation

        out["ProjectStep"] = capo_quicksight.types.project_operation.serialize_json(
            value["project_step"]
        )
    if "filters_step" in value:
        import capo_quicksight.types.filters_operation

        out["FiltersStep"] = capo_quicksight.types.filters_operation.serialize_json(
            value["filters_step"]
        )
    if "create_columns_step" in value:
        import capo_quicksight.types.create_columns_operation

        out["CreateColumnsStep"] = (
            capo_quicksight.types.create_columns_operation.serialize_json(
                value["create_columns_step"]
            )
        )
    if "rename_columns_step" in value:
        import capo_quicksight.types.rename_columns_operation

        out["RenameColumnsStep"] = (
            capo_quicksight.types.rename_columns_operation.serialize_json(
                value["rename_columns_step"]
            )
        )
    if "cast_column_types_step" in value:
        import capo_quicksight.types.cast_column_types_operation

        out["CastColumnTypesStep"] = (
            capo_quicksight.types.cast_column_types_operation.serialize_json(
                value["cast_column_types_step"]
            )
        )
    if "join_step" in value:
        import capo_quicksight.types.join_operation

        out["JoinStep"] = capo_quicksight.types.join_operation.serialize_json(
            value["join_step"]
        )
    if "aggregate_step" in value:
        import capo_quicksight.types.aggregate_operation

        out["AggregateStep"] = capo_quicksight.types.aggregate_operation.serialize_json(
            value["aggregate_step"]
        )
    if "pivot_step" in value:
        import capo_quicksight.types.pivot_operation

        out["PivotStep"] = capo_quicksight.types.pivot_operation.serialize_json(
            value["pivot_step"]
        )
    if "unpivot_step" in value:
        import capo_quicksight.types.unpivot_operation

        out["UnpivotStep"] = capo_quicksight.types.unpivot_operation.serialize_json(
            value["unpivot_step"]
        )
    if "append_step" in value:
        import capo_quicksight.types.append_operation

        out["AppendStep"] = capo_quicksight.types.append_operation.serialize_json(
            value["append_step"]
        )
    return out


def deserialize_json(data: dict) -> TransformStep:
    out: TransformStep = {}  # type: ignore[typeddict-item]
    if data.get("ImportTableStep") is not None:
        import capo_quicksight.types.import_table_operation

        out["import_table_step"] = (
            capo_quicksight.types.import_table_operation.deserialize_json(
                data["ImportTableStep"]
            )
        )
    if data.get("ProjectStep") is not None:
        import capo_quicksight.types.project_operation

        out["project_step"] = capo_quicksight.types.project_operation.deserialize_json(
            data["ProjectStep"]
        )
    if data.get("FiltersStep") is not None:
        import capo_quicksight.types.filters_operation

        out["filters_step"] = capo_quicksight.types.filters_operation.deserialize_json(
            data["FiltersStep"]
        )
    if data.get("CreateColumnsStep") is not None:
        import capo_quicksight.types.create_columns_operation

        out["create_columns_step"] = (
            capo_quicksight.types.create_columns_operation.deserialize_json(
                data["CreateColumnsStep"]
            )
        )
    if data.get("RenameColumnsStep") is not None:
        import capo_quicksight.types.rename_columns_operation

        out["rename_columns_step"] = (
            capo_quicksight.types.rename_columns_operation.deserialize_json(
                data["RenameColumnsStep"]
            )
        )
    if data.get("CastColumnTypesStep") is not None:
        import capo_quicksight.types.cast_column_types_operation

        out["cast_column_types_step"] = (
            capo_quicksight.types.cast_column_types_operation.deserialize_json(
                data["CastColumnTypesStep"]
            )
        )
    if data.get("JoinStep") is not None:
        import capo_quicksight.types.join_operation

        out["join_step"] = capo_quicksight.types.join_operation.deserialize_json(
            data["JoinStep"]
        )
    if data.get("AggregateStep") is not None:
        import capo_quicksight.types.aggregate_operation

        out["aggregate_step"] = (
            capo_quicksight.types.aggregate_operation.deserialize_json(
                data["AggregateStep"]
            )
        )
    if data.get("PivotStep") is not None:
        import capo_quicksight.types.pivot_operation

        out["pivot_step"] = capo_quicksight.types.pivot_operation.deserialize_json(
            data["PivotStep"]
        )
    if data.get("UnpivotStep") is not None:
        import capo_quicksight.types.unpivot_operation

        out["unpivot_step"] = capo_quicksight.types.unpivot_operation.deserialize_json(
            data["UnpivotStep"]
        )
    if data.get("AppendStep") is not None:
        import capo_quicksight.types.append_operation

        out["append_step"] = capo_quicksight.types.append_operation.deserialize_json(
            data["AppendStep"]
        )
    return out


def redact_sensitive(value: TransformStep) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters_step" in value:
        import capo_quicksight.types.filters_operation

        out["filters_step"] = capo_quicksight.types.filters_operation.redact_sensitive(
            value["filters_step"]
        )
    if "create_columns_step" in value:
        import capo_quicksight.types.create_columns_operation

        out["create_columns_step"] = (
            capo_quicksight.types.create_columns_operation.redact_sensitive(
                value["create_columns_step"]
            )
        )
    if "join_step" in value:
        import capo_quicksight.types.join_operation

        out["join_step"] = capo_quicksight.types.join_operation.redact_sensitive(
            value["join_step"]
        )
    return out
