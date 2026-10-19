"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.custom_label
    import capo_quicksight.types.field_id
    import capo_quicksight.types.pixel_length
    import capo_quicksight.types.table_field_url_configuration
    import capo_quicksight.types.visibility


class TableFieldOption(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field ID for a table field.</p>"""
    width: NotRequired["capo_quicksight.types.pixel_length.PixelLength"]
    """<p>The width for a table field.</p>"""
    custom_label: NotRequired["capo_quicksight.types.custom_label.CustomLabel"]
    """<p>The custom label for a table field.</p>"""
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of a table field.</p>"""
    url_styling: NotRequired[
        "capo_quicksight.types.table_field_url_configuration.TableFieldURLConfiguration"
    ]
    """<p>The URL configuration for a table field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldOption) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "width" in value:
        out["Width"] = value["width"]
    if "custom_label" in value:
        out["CustomLabel"] = value["custom_label"]
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "url_styling" in value:
        import capo_quicksight.types.table_field_url_configuration

        out["URLStyling"] = (
            capo_quicksight.types.table_field_url_configuration.serialize_json(
                value["url_styling"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableFieldOption:
    out: TableFieldOption = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("Width") is not None:
        out["width"] = data["Width"]
    if data.get("CustomLabel") is not None:
        out["custom_label"] = data["CustomLabel"]
    if data.get("Visibility") is not None:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if data.get("URLStyling") is not None:
        import capo_quicksight.types.table_field_url_configuration

        out["url_styling"] = (
            capo_quicksight.types.table_field_url_configuration.deserialize_json(
                data["URLStyling"]
            )
        )
    return out
