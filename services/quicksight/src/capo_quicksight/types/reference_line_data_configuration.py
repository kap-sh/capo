"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineDataConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_binding
    import capo_quicksight.types.reference_line_dynamic_data_configuration
    import capo_quicksight.types.reference_line_series_type
    import capo_quicksight.types.reference_line_static_data_configuration


class ReferenceLineDataConfiguration(TypedDict, closed=True):
    static_configuration: NotRequired[
        "capo_quicksight.types.reference_line_static_data_configuration.ReferenceLineStaticDataConfiguration"
    ]
    """<p>The static data configuration of the reference line data configuration.</p>"""
    dynamic_configuration: NotRequired[
        "capo_quicksight.types.reference_line_dynamic_data_configuration.ReferenceLineDynamicDataConfiguration"
    ]
    """<p>The dynamic configuration of the reference line data configuration.</p>"""
    axis_binding: NotRequired["capo_quicksight.types.axis_binding.AxisBinding"]
    """<p>The axis binding type of the reference line. Choose one of the following options:</p> <ul> <li> <p> <code>PrimaryY</code> </p> </li> <li> <p> <code>SecondaryY</code> </p> </li> </ul>"""
    series_type: NotRequired[
        "capo_quicksight.types.reference_line_series_type.ReferenceLineSeriesType"
    ]
    """<p>The series type of the reference line data configuration. Choose one of the following options:</p> <ul> <li> <p> <code>BAR</code> </p> </li> <li> <p> <code>LINE</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineDataConfiguration) -> dict:
    out: dict = {}
    if "static_configuration" in value:
        import capo_quicksight.types.reference_line_static_data_configuration

        out["StaticConfiguration"] = (
            capo_quicksight.types.reference_line_static_data_configuration.serialize_json(
                value["static_configuration"]
            )
        )
    if "dynamic_configuration" in value:
        import capo_quicksight.types.reference_line_dynamic_data_configuration

        out["DynamicConfiguration"] = (
            capo_quicksight.types.reference_line_dynamic_data_configuration.serialize_json(
                value["dynamic_configuration"]
            )
        )
    if "axis_binding" in value:
        import capo_quicksight.types.axis_binding

        out["AxisBinding"] = capo_quicksight.types.axis_binding.serialize_json(
            value["axis_binding"]
        )
    if "series_type" in value:
        import capo_quicksight.types.reference_line_series_type

        out["SeriesType"] = (
            capo_quicksight.types.reference_line_series_type.serialize_json(
                value["series_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReferenceLineDataConfiguration:
    out: ReferenceLineDataConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StaticConfiguration") is not None:
        import capo_quicksight.types.reference_line_static_data_configuration

        out["static_configuration"] = (
            capo_quicksight.types.reference_line_static_data_configuration.deserialize_json(
                data["StaticConfiguration"]
            )
        )
    if data.get("DynamicConfiguration") is not None:
        import capo_quicksight.types.reference_line_dynamic_data_configuration

        out["dynamic_configuration"] = (
            capo_quicksight.types.reference_line_dynamic_data_configuration.deserialize_json(
                data["DynamicConfiguration"]
            )
        )
    if data.get("AxisBinding") is not None:
        import capo_quicksight.types.axis_binding

        out["axis_binding"] = capo_quicksight.types.axis_binding.deserialize_json(
            data["AxisBinding"]
        )
    if data.get("SeriesType") is not None:
        import capo_quicksight.types.reference_line_series_type

        out["series_type"] = (
            capo_quicksight.types.reference_line_series_type.deserialize_json(
                data["SeriesType"]
            )
        )
    return out


def redact_sensitive(value: ReferenceLineDataConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "static_configuration" in value:
        import capo_quicksight.types.reference_line_static_data_configuration

        out["static_configuration"] = (
            capo_quicksight.types.reference_line_static_data_configuration.redact_sensitive(
                value["static_configuration"]
            )
        )
    return out
