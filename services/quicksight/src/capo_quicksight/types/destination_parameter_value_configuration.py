"""Generated from Smithy shape ``com.amazonaws.quicksight#DestinationParameterValueConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.custom_values_configuration
    import capo_quicksight.types.field_id
    import capo_quicksight.types.select_all_value_options
    import capo_quicksight.types.string


class DestinationParameterValueConfiguration(TypedDict, closed=True):
    custom_values_configuration: NotRequired[
        "capo_quicksight.types.custom_values_configuration.CustomValuesConfiguration"
    ]
    """<p>The configuration of custom values for destination parameter in <code>DestinationParameterValueConfiguration</code>.</p>"""
    select_all_value_options: NotRequired[
        "capo_quicksight.types.select_all_value_options.SelectAllValueOptions"
    ]
    """<p>The configuration that selects all options.</p>"""
    source_parameter_name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The source parameter name of the destination parameter.</p>"""
    source_field: NotRequired["capo_quicksight.types.field_id.FieldId"]
    """<p>The source field ID of the destination parameter.</p>"""
    source_column: NotRequired[
        "capo_quicksight.types.column_identifier.ColumnIdentifier"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationParameterValueConfiguration) -> dict:
    out: dict = {}
    if "custom_values_configuration" in value:
        import capo_quicksight.types.custom_values_configuration

        out["CustomValuesConfiguration"] = (
            capo_quicksight.types.custom_values_configuration.serialize_json(
                value["custom_values_configuration"]
            )
        )
    if "select_all_value_options" in value:
        import capo_quicksight.types.select_all_value_options

        out["SelectAllValueOptions"] = (
            capo_quicksight.types.select_all_value_options.serialize_json(
                value["select_all_value_options"]
            )
        )
    if "source_parameter_name" in value:
        out["SourceParameterName"] = value["source_parameter_name"]
    if "source_field" in value:
        out["SourceField"] = value["source_field"]
    if "source_column" in value:
        import capo_quicksight.types.column_identifier

        out["SourceColumn"] = capo_quicksight.types.column_identifier.serialize_json(
            value["source_column"]
        )
    return out


def deserialize_json(data: dict) -> DestinationParameterValueConfiguration:
    out: DestinationParameterValueConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CustomValuesConfiguration") is not None:
        import capo_quicksight.types.custom_values_configuration

        out["custom_values_configuration"] = (
            capo_quicksight.types.custom_values_configuration.deserialize_json(
                data["CustomValuesConfiguration"]
            )
        )
    if data.get("SelectAllValueOptions") is not None:
        import capo_quicksight.types.select_all_value_options

        out["select_all_value_options"] = (
            capo_quicksight.types.select_all_value_options.deserialize_json(
                data["SelectAllValueOptions"]
            )
        )
    if data.get("SourceParameterName") is not None:
        out["source_parameter_name"] = data["SourceParameterName"]
    if data.get("SourceField") is not None:
        out["source_field"] = data["SourceField"]
    if data.get("SourceColumn") is not None:
        import capo_quicksight.types.column_identifier

        out["source_column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["SourceColumn"]
        )
    return out


def redact_sensitive(value: DestinationParameterValueConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_values_configuration" in value:
        import capo_quicksight.types.custom_values_configuration

        out["custom_values_configuration"] = (
            capo_quicksight.types.custom_values_configuration.redact_sensitive(
                value["custom_values_configuration"]
            )
        )
    return out
