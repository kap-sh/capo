"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardVersionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_defaults
    import capo_quicksight.types.asset_options
    import capo_quicksight.types.calculated_fields
    import capo_quicksight.types.column_configuration_list
    import capo_quicksight.types.data_set_identifier_declaration_list
    import capo_quicksight.types.filter_group_list
    import capo_quicksight.types.parameter_declaration_list
    import capo_quicksight.types.sheet_definition_list
    import capo_quicksight.types.static_file_list
    import capo_quicksight.types.tooltip_sheet_definition_list
    import capo_quicksight.types.topic_identifier_declaration_list


class DashboardVersionDefinition(TypedDict, closed=True):
    data_set_identifier_declarations: "capo_quicksight.types.data_set_identifier_declaration_list.DataSetIdentifierDeclarationList"
    """<p>An array of dataset identifier declarations. With this mapping,you can use dataset identifiers instead of dataset Amazon Resource Names (ARNs) throughout the dashboard's sub-structures.</p>"""
    topic_identifier_declarations: NotRequired[
        "capo_quicksight.types.topic_identifier_declaration_list.TopicIdentifierDeclarationList"
    ]
    """<p>An array of topic identifier declarations. With this mapping, you can use topic identifiers instead of topic Amazon Resource Names (ARNs) throughout the dashboard's sub-structures.</p>"""
    sheets: NotRequired[
        "capo_quicksight.types.sheet_definition_list.SheetDefinitionList"
    ]
    """<p>An array of sheet definitions for a dashboard.</p>"""
    tooltip_sheets: NotRequired[
        "capo_quicksight.types.tooltip_sheet_definition_list.TooltipSheetDefinitionList"
    ]
    """<p>An array of tooltip sheet definitions for a dashboard.</p>"""
    calculated_fields: NotRequired[
        "capo_quicksight.types.calculated_fields.CalculatedFields"
    ]
    """<p>An array of calculated field definitions for the dashboard.</p>"""
    parameter_declarations: NotRequired[
        "capo_quicksight.types.parameter_declaration_list.ParameterDeclarationList"
    ]
    """<p>The parameter declarations for a dashboard. Parameters are named variables that can transfer a value for use by an action or an object.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html">Parameters in Amazon Quick Sight</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    filter_groups: NotRequired[
        "capo_quicksight.types.filter_group_list.FilterGroupList"
    ]
    """<p>The filter definitions for a dashboard.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/adding-a-filter.html">Filtering Data in Amazon Quick Sight</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    column_configurations: NotRequired[
        "capo_quicksight.types.column_configuration_list.ColumnConfigurationList"
    ]
    """<p>An array of dashboard-level column configurations. Column configurations are used to set the default formatting for a column that is used throughout a dashboard. </p>"""
    analysis_defaults: NotRequired[
        "capo_quicksight.types.analysis_defaults.AnalysisDefaults"
    ]
    options: NotRequired["capo_quicksight.types.asset_options.AssetOptions"]
    """<p>An array of option definitions for a dashboard.</p>"""
    static_files: NotRequired["capo_quicksight.types.static_file_list.StaticFileList"]
    """<p>The static files for the definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardVersionDefinition) -> dict:
    out: dict = {}
    import capo_quicksight.types.data_set_identifier_declaration_list

    out["DataSetIdentifierDeclarations"] = (
        capo_quicksight.types.data_set_identifier_declaration_list.serialize_json(
            value["data_set_identifier_declarations"]
        )
    )
    if "topic_identifier_declarations" in value:
        import capo_quicksight.types.topic_identifier_declaration_list

        out["TopicIdentifierDeclarations"] = (
            capo_quicksight.types.topic_identifier_declaration_list.serialize_json(
                value["topic_identifier_declarations"]
            )
        )
    if "sheets" in value:
        import capo_quicksight.types.sheet_definition_list

        out["Sheets"] = capo_quicksight.types.sheet_definition_list.serialize_json(
            value["sheets"]
        )
    if "tooltip_sheets" in value:
        import capo_quicksight.types.tooltip_sheet_definition_list

        out["TooltipSheets"] = (
            capo_quicksight.types.tooltip_sheet_definition_list.serialize_json(
                value["tooltip_sheets"]
            )
        )
    if "calculated_fields" in value:
        import capo_quicksight.types.calculated_fields

        out["CalculatedFields"] = (
            capo_quicksight.types.calculated_fields.serialize_json(
                value["calculated_fields"]
            )
        )
    if "parameter_declarations" in value:
        import capo_quicksight.types.parameter_declaration_list

        out["ParameterDeclarations"] = (
            capo_quicksight.types.parameter_declaration_list.serialize_json(
                value["parameter_declarations"]
            )
        )
    if "filter_groups" in value:
        import capo_quicksight.types.filter_group_list

        out["FilterGroups"] = capo_quicksight.types.filter_group_list.serialize_json(
            value["filter_groups"]
        )
    if "column_configurations" in value:
        import capo_quicksight.types.column_configuration_list

        out["ColumnConfigurations"] = (
            capo_quicksight.types.column_configuration_list.serialize_json(
                value["column_configurations"]
            )
        )
    if "analysis_defaults" in value:
        import capo_quicksight.types.analysis_defaults

        out["AnalysisDefaults"] = (
            capo_quicksight.types.analysis_defaults.serialize_json(
                value["analysis_defaults"]
            )
        )
    if "options" in value:
        import capo_quicksight.types.asset_options

        out["Options"] = capo_quicksight.types.asset_options.serialize_json(
            value["options"]
        )
    if "static_files" in value:
        import capo_quicksight.types.static_file_list

        out["StaticFiles"] = capo_quicksight.types.static_file_list.serialize_json(
            value["static_files"]
        )
    return out


def deserialize_json(data: dict) -> DashboardVersionDefinition:
    out: DashboardVersionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("DataSetIdentifierDeclarations") is not None:
        import capo_quicksight.types.data_set_identifier_declaration_list

        out["data_set_identifier_declarations"] = (
            capo_quicksight.types.data_set_identifier_declaration_list.deserialize_json(
                data["DataSetIdentifierDeclarations"]
            )
        )
    else:
        raise DeserializationError(
            "DashboardVersionDefinition.data_set_identifier_declarations required"
        )
    if data.get("TopicIdentifierDeclarations") is not None:
        import capo_quicksight.types.topic_identifier_declaration_list

        out["topic_identifier_declarations"] = (
            capo_quicksight.types.topic_identifier_declaration_list.deserialize_json(
                data["TopicIdentifierDeclarations"]
            )
        )
    if data.get("Sheets") is not None:
        import capo_quicksight.types.sheet_definition_list

        out["sheets"] = capo_quicksight.types.sheet_definition_list.deserialize_json(
            data["Sheets"]
        )
    if data.get("TooltipSheets") is not None:
        import capo_quicksight.types.tooltip_sheet_definition_list

        out["tooltip_sheets"] = (
            capo_quicksight.types.tooltip_sheet_definition_list.deserialize_json(
                data["TooltipSheets"]
            )
        )
    if data.get("CalculatedFields") is not None:
        import capo_quicksight.types.calculated_fields

        out["calculated_fields"] = (
            capo_quicksight.types.calculated_fields.deserialize_json(
                data["CalculatedFields"]
            )
        )
    if data.get("ParameterDeclarations") is not None:
        import capo_quicksight.types.parameter_declaration_list

        out["parameter_declarations"] = (
            capo_quicksight.types.parameter_declaration_list.deserialize_json(
                data["ParameterDeclarations"]
            )
        )
    if data.get("FilterGroups") is not None:
        import capo_quicksight.types.filter_group_list

        out["filter_groups"] = capo_quicksight.types.filter_group_list.deserialize_json(
            data["FilterGroups"]
        )
    if data.get("ColumnConfigurations") is not None:
        import capo_quicksight.types.column_configuration_list

        out["column_configurations"] = (
            capo_quicksight.types.column_configuration_list.deserialize_json(
                data["ColumnConfigurations"]
            )
        )
    if data.get("AnalysisDefaults") is not None:
        import capo_quicksight.types.analysis_defaults

        out["analysis_defaults"] = (
            capo_quicksight.types.analysis_defaults.deserialize_json(
                data["AnalysisDefaults"]
            )
        )
    if data.get("Options") is not None:
        import capo_quicksight.types.asset_options

        out["options"] = capo_quicksight.types.asset_options.deserialize_json(
            data["Options"]
        )
    if data.get("StaticFiles") is not None:
        import capo_quicksight.types.static_file_list

        out["static_files"] = capo_quicksight.types.static_file_list.deserialize_json(
            data["StaticFiles"]
        )
    return out
