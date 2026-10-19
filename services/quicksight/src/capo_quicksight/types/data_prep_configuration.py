"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPrepConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.destination_table_map
    import capo_quicksight.types.source_table_map
    import capo_quicksight.types.transform_step_map


class DataPrepConfiguration(TypedDict, closed=True):
    source_table_map: "capo_quicksight.types.source_table_map.SourceTableMap"
    """<p>A map of source tables that provide information about underlying sources.</p>"""
    transform_step_map: "capo_quicksight.types.transform_step_map.TransformStepMap"
    """<p>A map of transformation steps that process the data.</p>"""
    destination_table_map: (
        "capo_quicksight.types.destination_table_map.DestinationTableMap"
    )
    """<p>A map of destination tables that receive the final prepared data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPrepConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.source_table_map

    out["SourceTableMap"] = capo_quicksight.types.source_table_map.serialize_json(
        value["source_table_map"]
    )
    import capo_quicksight.types.transform_step_map

    out["TransformStepMap"] = capo_quicksight.types.transform_step_map.serialize_json(
        value["transform_step_map"]
    )
    import capo_quicksight.types.destination_table_map

    out["DestinationTableMap"] = (
        capo_quicksight.types.destination_table_map.serialize_json(
            value["destination_table_map"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataPrepConfiguration:
    out: DataPrepConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SourceTableMap") is not None:
        import capo_quicksight.types.source_table_map

        out["source_table_map"] = (
            capo_quicksight.types.source_table_map.deserialize_json(
                data["SourceTableMap"]
            )
        )
    else:
        out["source_table_map"] = {}
    if data.get("TransformStepMap") is not None:
        import capo_quicksight.types.transform_step_map

        out["transform_step_map"] = (
            capo_quicksight.types.transform_step_map.deserialize_json(
                data["TransformStepMap"]
            )
        )
    else:
        out["transform_step_map"] = {}
    if data.get("DestinationTableMap") is not None:
        import capo_quicksight.types.destination_table_map

        out["destination_table_map"] = (
            capo_quicksight.types.destination_table_map.deserialize_json(
                data["DestinationTableMap"]
            )
        )
    else:
        out["destination_table_map"] = {}
    return out


def redact_sensitive(value: DataPrepConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "transform_step_map" in value:
        import capo_quicksight.types.transform_step_map

        out["transform_step_map"] = (
            capo_quicksight.types.transform_step_map.redact_sensitive(
                value["transform_step_map"]
            )
        )
    return out
