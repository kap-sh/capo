"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLine``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.reference_line_data_configuration
    import capo_quicksight.types.reference_line_label_configuration
    import capo_quicksight.types.reference_line_style_configuration
    import capo_quicksight.types.widget_status


class ReferenceLine(TypedDict, closed=True):
    status: NotRequired["capo_quicksight.types.widget_status.WidgetStatus"]
    """<p>The status of the reference line. Choose one of the following options:</p> <ul> <li> <p> <code>ENABLE</code> </p> </li> <li> <p> <code>DISABLE</code> </p> </li> </ul>"""
    data_configuration: "capo_quicksight.types.reference_line_data_configuration.ReferenceLineDataConfiguration"
    """<p>The data configuration of the reference line.</p>"""
    style_configuration: NotRequired[
        "capo_quicksight.types.reference_line_style_configuration.ReferenceLineStyleConfiguration"
    ]
    """<p>The style configuration of the reference line.</p>"""
    label_configuration: NotRequired[
        "capo_quicksight.types.reference_line_label_configuration.ReferenceLineLabelConfiguration"
    ]
    """<p>The label configuration of the reference line.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLine) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_quicksight.types.widget_status

        out["Status"] = capo_quicksight.types.widget_status.serialize_json(
            value["status"]
        )
    import capo_quicksight.types.reference_line_data_configuration

    out["DataConfiguration"] = (
        capo_quicksight.types.reference_line_data_configuration.serialize_json(
            value["data_configuration"]
        )
    )
    if "style_configuration" in value:
        import capo_quicksight.types.reference_line_style_configuration

        out["StyleConfiguration"] = (
            capo_quicksight.types.reference_line_style_configuration.serialize_json(
                value["style_configuration"]
            )
        )
    if "label_configuration" in value:
        import capo_quicksight.types.reference_line_label_configuration

        out["LabelConfiguration"] = (
            capo_quicksight.types.reference_line_label_configuration.serialize_json(
                value["label_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReferenceLine:
    out: ReferenceLine = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_quicksight.types.widget_status

        out["status"] = capo_quicksight.types.widget_status.deserialize_json(
            data["Status"]
        )
    if data.get("DataConfiguration") is not None:
        import capo_quicksight.types.reference_line_data_configuration

        out["data_configuration"] = (
            capo_quicksight.types.reference_line_data_configuration.deserialize_json(
                data["DataConfiguration"]
            )
        )
    else:
        raise DeserializationError("ReferenceLine.data_configuration required")
    if data.get("StyleConfiguration") is not None:
        import capo_quicksight.types.reference_line_style_configuration

        out["style_configuration"] = (
            capo_quicksight.types.reference_line_style_configuration.deserialize_json(
                data["StyleConfiguration"]
            )
        )
    if data.get("LabelConfiguration") is not None:
        import capo_quicksight.types.reference_line_label_configuration

        out["label_configuration"] = (
            capo_quicksight.types.reference_line_label_configuration.deserialize_json(
                data["LabelConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ReferenceLine) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_configuration" in value:
        import capo_quicksight.types.reference_line_data_configuration

        out["data_configuration"] = (
            capo_quicksight.types.reference_line_data_configuration.redact_sensitive(
                value["data_configuration"]
            )
        )
    if "label_configuration" in value:
        import capo_quicksight.types.reference_line_label_configuration

        out["label_configuration"] = (
            capo_quicksight.types.reference_line_label_configuration.redact_sensitive(
                value["label_configuration"]
            )
        )
    return out
