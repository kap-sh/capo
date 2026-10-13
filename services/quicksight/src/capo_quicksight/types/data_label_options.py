"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_label_content
    import capo_quicksight.types.data_label_overlap
    import capo_quicksight.types.data_label_position
    import capo_quicksight.types.data_label_types
    import capo_quicksight.types.font_configuration
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.visibility


class DataLabelOptions(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Determines the visibility of the data labels.</p>"""
    category_label_visibility: NotRequired[
        "capo_quicksight.types.visibility.Visibility"
    ]
    """<p>Determines the visibility of the category field labels.</p>"""
    measure_label_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Determines the visibility of the measure field labels.</p>"""
    data_label_types: NotRequired[
        "capo_quicksight.types.data_label_types.DataLabelTypes"
    ]
    """<p>The option that determines the data label type.</p>"""
    position: NotRequired["capo_quicksight.types.data_label_position.DataLabelPosition"]
    """<p>Determines the position of the data labels.</p>"""
    label_content: NotRequired[
        "capo_quicksight.types.data_label_content.DataLabelContent"
    ]
    """<p>Determines the content of the data labels.</p>"""
    label_font_configuration: NotRequired[
        "capo_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>Determines the font configuration of the data labels.</p>"""
    label_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>Determines the color of the data labels.</p>"""
    overlap: NotRequired["capo_quicksight.types.data_label_overlap.DataLabelOverlap"]
    """<p>Determines whether overlap is enabled or disabled for the data labels.</p>"""
    totals_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Determines the visibility of the total.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLabelOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "category_label_visibility" in value:
        import capo_quicksight.types.visibility

        out["CategoryLabelVisibility"] = (
            capo_quicksight.types.visibility.serialize_json(
                value["category_label_visibility"]
            )
        )
    if "measure_label_visibility" in value:
        import capo_quicksight.types.visibility

        out["MeasureLabelVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["measure_label_visibility"]
        )
    if "data_label_types" in value:
        import capo_quicksight.types.data_label_types

        out["DataLabelTypes"] = capo_quicksight.types.data_label_types.serialize_json(
            value["data_label_types"]
        )
    if "position" in value:
        import capo_quicksight.types.data_label_position

        out["Position"] = capo_quicksight.types.data_label_position.serialize_json(
            value["position"]
        )
    if "label_content" in value:
        import capo_quicksight.types.data_label_content

        out["LabelContent"] = capo_quicksight.types.data_label_content.serialize_json(
            value["label_content"]
        )
    if "label_font_configuration" in value:
        import capo_quicksight.types.font_configuration

        out["LabelFontConfiguration"] = (
            capo_quicksight.types.font_configuration.serialize_json(
                value["label_font_configuration"]
            )
        )
    if "label_color" in value:
        out["LabelColor"] = value["label_color"]
    if "overlap" in value:
        import capo_quicksight.types.data_label_overlap

        out["Overlap"] = capo_quicksight.types.data_label_overlap.serialize_json(
            value["overlap"]
        )
    if "totals_visibility" in value:
        import capo_quicksight.types.visibility

        out["TotalsVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["totals_visibility"]
        )
    return out


def deserialize_json(data: dict) -> DataLabelOptions:
    out: DataLabelOptions = {}  # type: ignore[typeddict-item]
    if data.get("Visibility") is not None:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if data.get("CategoryLabelVisibility") is not None:
        import capo_quicksight.types.visibility

        out["category_label_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["CategoryLabelVisibility"]
            )
        )
    if data.get("MeasureLabelVisibility") is not None:
        import capo_quicksight.types.visibility

        out["measure_label_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["MeasureLabelVisibility"]
            )
        )
    if data.get("DataLabelTypes") is not None:
        import capo_quicksight.types.data_label_types

        out["data_label_types"] = (
            capo_quicksight.types.data_label_types.deserialize_json(
                data["DataLabelTypes"]
            )
        )
    if data.get("Position") is not None:
        import capo_quicksight.types.data_label_position

        out["position"] = capo_quicksight.types.data_label_position.deserialize_json(
            data["Position"]
        )
    if data.get("LabelContent") is not None:
        import capo_quicksight.types.data_label_content

        out["label_content"] = (
            capo_quicksight.types.data_label_content.deserialize_json(
                data["LabelContent"]
            )
        )
    if data.get("LabelFontConfiguration") is not None:
        import capo_quicksight.types.font_configuration

        out["label_font_configuration"] = (
            capo_quicksight.types.font_configuration.deserialize_json(
                data["LabelFontConfiguration"]
            )
        )
    if data.get("LabelColor") is not None:
        out["label_color"] = data["LabelColor"]
    if data.get("Overlap") is not None:
        import capo_quicksight.types.data_label_overlap

        out["overlap"] = capo_quicksight.types.data_label_overlap.deserialize_json(
            data["Overlap"]
        )
    if data.get("TotalsVisibility") is not None:
        import capo_quicksight.types.visibility

        out["totals_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["TotalsVisibility"]
        )
    return out


def redact_sensitive(value: DataLabelOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_label_types" in value:
        import capo_quicksight.types.data_label_types

        out["data_label_types"] = (
            capo_quicksight.types.data_label_types.redact_sensitive(
                value["data_label_types"]
            )
        )
    return out
