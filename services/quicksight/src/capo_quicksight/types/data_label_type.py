"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_path_label_type
    import capo_quicksight.types.field_label_type
    import capo_quicksight.types.maximum_label_type
    import capo_quicksight.types.minimum_label_type
    import capo_quicksight.types.range_ends_label_type


class DataLabelType(TypedDict, closed=True):
    field_label_type: NotRequired[
        "capo_quicksight.types.field_label_type.FieldLabelType"
    ]
    """<p>Determines the label configuration for the entire field.</p>"""
    data_path_label_type: NotRequired[
        "capo_quicksight.types.data_path_label_type.DataPathLabelType"
    ]
    """<p>The option that specifies individual data values for labels.</p>"""
    range_ends_label_type: NotRequired[
        "capo_quicksight.types.range_ends_label_type.RangeEndsLabelType"
    ]
    """<p>Determines the label configuration for range end value in a visual.</p>"""
    minimum_label_type: NotRequired[
        "capo_quicksight.types.minimum_label_type.MinimumLabelType"
    ]
    """<p>Determines the label configuration for the minimum value in a visual.</p>"""
    maximum_label_type: NotRequired[
        "capo_quicksight.types.maximum_label_type.MaximumLabelType"
    ]
    """<p>Determines the label configuration for the maximum value in a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLabelType) -> dict:
    out: dict = {}
    if "field_label_type" in value:
        import capo_quicksight.types.field_label_type

        out["FieldLabelType"] = capo_quicksight.types.field_label_type.serialize_json(
            value["field_label_type"]
        )
    if "data_path_label_type" in value:
        import capo_quicksight.types.data_path_label_type

        out["DataPathLabelType"] = (
            capo_quicksight.types.data_path_label_type.serialize_json(
                value["data_path_label_type"]
            )
        )
    if "range_ends_label_type" in value:
        import capo_quicksight.types.range_ends_label_type

        out["RangeEndsLabelType"] = (
            capo_quicksight.types.range_ends_label_type.serialize_json(
                value["range_ends_label_type"]
            )
        )
    if "minimum_label_type" in value:
        import capo_quicksight.types.minimum_label_type

        out["MinimumLabelType"] = (
            capo_quicksight.types.minimum_label_type.serialize_json(
                value["minimum_label_type"]
            )
        )
    if "maximum_label_type" in value:
        import capo_quicksight.types.maximum_label_type

        out["MaximumLabelType"] = (
            capo_quicksight.types.maximum_label_type.serialize_json(
                value["maximum_label_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLabelType:
    out: DataLabelType = {}  # type: ignore[typeddict-item]
    if data.get("FieldLabelType") is not None:
        import capo_quicksight.types.field_label_type

        out["field_label_type"] = (
            capo_quicksight.types.field_label_type.deserialize_json(
                data["FieldLabelType"]
            )
        )
    if data.get("DataPathLabelType") is not None:
        import capo_quicksight.types.data_path_label_type

        out["data_path_label_type"] = (
            capo_quicksight.types.data_path_label_type.deserialize_json(
                data["DataPathLabelType"]
            )
        )
    if data.get("RangeEndsLabelType") is not None:
        import capo_quicksight.types.range_ends_label_type

        out["range_ends_label_type"] = (
            capo_quicksight.types.range_ends_label_type.deserialize_json(
                data["RangeEndsLabelType"]
            )
        )
    if data.get("MinimumLabelType") is not None:
        import capo_quicksight.types.minimum_label_type

        out["minimum_label_type"] = (
            capo_quicksight.types.minimum_label_type.deserialize_json(
                data["MinimumLabelType"]
            )
        )
    if data.get("MaximumLabelType") is not None:
        import capo_quicksight.types.maximum_label_type

        out["maximum_label_type"] = (
            capo_quicksight.types.maximum_label_type.deserialize_json(
                data["MaximumLabelType"]
            )
        )
    return out


def redact_sensitive(value: DataLabelType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_path_label_type" in value:
        import capo_quicksight.types.data_path_label_type

        out["data_path_label_type"] = (
            capo_quicksight.types.data_path_label_type.redact_sensitive(
                value["data_path_label_type"]
            )
        )
    return out
