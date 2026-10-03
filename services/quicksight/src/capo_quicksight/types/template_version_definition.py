"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateVersionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_defaults
    import capo_quicksight.types.asset_options
    import capo_quicksight.types.calculated_fields
    import capo_quicksight.types.column_configuration_list
    import capo_quicksight.types.data_set_configuration_list
    import capo_quicksight.types.filter_group_list
    import capo_quicksight.types.parameter_declaration_list
    import capo_quicksight.types.query_execution_options
    import capo_quicksight.types.sheet_definition_list
    import capo_quicksight.types.static_file_list
    import capo_quicksight.types.tooltip_sheet_definition_list
    import capo_quicksight.types.topic_configuration_list


class TemplateVersionDefinition(TypedDict, closed=True):
    data_set_configurations: (
        "capo_quicksight.types.data_set_configuration_list.DataSetConfigurationList"
    )
    """<p>An array of dataset configurations. These configurations define the required columns for each dataset used within a template.</p>"""
    topic_configurations: NotRequired[
        "capo_quicksight.types.topic_configuration_list.TopicConfigurationList"
    ]
    """<p>An array of topic configurations. These configurations define the required columns for each topic used within a template.</p>"""
    sheets: NotRequired[
        "capo_quicksight.types.sheet_definition_list.SheetDefinitionList"
    ]
    """<p>An array of sheet definitions for a template.</p>"""
    tooltip_sheets: NotRequired[
        "capo_quicksight.types.tooltip_sheet_definition_list.TooltipSheetDefinitionList"
    ]
    """<p>An array of tooltip sheet definitions for a template.</p>"""
    calculated_fields: NotRequired[
        "capo_quicksight.types.calculated_fields.CalculatedFields"
    ]
    """<p>An array of calculated field definitions for the template.</p>"""
    parameter_declarations: NotRequired[
        "capo_quicksight.types.parameter_declaration_list.ParameterDeclarationList"
    ]
    """<p>An array of parameter declarations for a template.</p> <p> <i>Parameters</i> are named variables that can transfer a value for use by an action or an object.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html">Parameters in Amazon Quick Sight</a> in the <i>Amazon Quick Suite User Guide</i>. </p>"""
    filter_groups: NotRequired[
        "capo_quicksight.types.filter_group_list.FilterGroupList"
    ]
    """<p>Filter definitions for a template.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/filtering-visual-data.html">Filtering Data</a> in the <i>Amazon Quick Suite User Guide</i>. </p>"""
    column_configurations: NotRequired[
        "capo_quicksight.types.column_configuration_list.ColumnConfigurationList"
    ]
    """<p> An array of template-level column configurations. Column configurations are used to set default formatting for a column that's used throughout a template. </p>"""
    analysis_defaults: NotRequired[
        "capo_quicksight.types.analysis_defaults.AnalysisDefaults"
    ]
    options: NotRequired["capo_quicksight.types.asset_options.AssetOptions"]
    """<p>An array of option definitions for a template.</p>"""
    query_execution_options: NotRequired[
        "capo_quicksight.types.query_execution_options.QueryExecutionOptions"
    ]
    static_files: NotRequired["capo_quicksight.types.static_file_list.StaticFileList"]
    """<p>The static files for the definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateVersionDefinition) -> dict:
    out: dict = {}
    import capo_quicksight.types.data_set_configuration_list

    out["DataSetConfigurations"] = (
        capo_quicksight.types.data_set_configuration_list.serialize_json(
            value["data_set_configurations"]
        )
    )
    if "topic_configurations" in value:
        import capo_quicksight.types.topic_configuration_list

        out["TopicConfigurations"] = (
            capo_quicksight.types.topic_configuration_list.serialize_json(
                value["topic_configurations"]
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
    if "query_execution_options" in value:
        import capo_quicksight.types.query_execution_options

        out["QueryExecutionOptions"] = (
            capo_quicksight.types.query_execution_options.serialize_json(
                value["query_execution_options"]
            )
        )
    if "static_files" in value:
        import capo_quicksight.types.static_file_list

        out["StaticFiles"] = capo_quicksight.types.static_file_list.serialize_json(
            value["static_files"]
        )
    return out


def deserialize_json(data: dict) -> TemplateVersionDefinition:
    out: TemplateVersionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("DataSetConfigurations") is not None:
        import capo_quicksight.types.data_set_configuration_list

        out["data_set_configurations"] = (
            capo_quicksight.types.data_set_configuration_list.deserialize_json(
                data["DataSetConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "TemplateVersionDefinition.data_set_configurations required"
        )
    if data.get("TopicConfigurations") is not None:
        import capo_quicksight.types.topic_configuration_list

        out["topic_configurations"] = (
            capo_quicksight.types.topic_configuration_list.deserialize_json(
                data["TopicConfigurations"]
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
    if data.get("QueryExecutionOptions") is not None:
        import capo_quicksight.types.query_execution_options

        out["query_execution_options"] = (
            capo_quicksight.types.query_execution_options.deserialize_json(
                data["QueryExecutionOptions"]
            )
        )
    if data.get("StaticFiles") is not None:
        import capo_quicksight.types.static_file_list

        out["static_files"] = capo_quicksight.types.static_file_list.deserialize_json(
            data["StaticFiles"]
        )
    return out
