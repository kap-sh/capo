"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.column_group_list
    import capo_quicksight.types.column_level_permission_rule_list
    import capo_quicksight.types.data_prep_configuration
    import capo_quicksight.types.data_set_import_mode
    import capo_quicksight.types.data_set_usage_configuration
    import capo_quicksight.types.data_set_use_as
    import capo_quicksight.types.dataset_parameter_list
    import capo_quicksight.types.field_folder_map
    import capo_quicksight.types.logical_table_map
    import capo_quicksight.types.long
    import capo_quicksight.types.output_column_list
    import capo_quicksight.types.performance_configuration
    import capo_quicksight.types.physical_table_map
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.row_level_permission_data_set
    import capo_quicksight.types.row_level_permission_tag_configuration
    import capo_quicksight.types.semantic_model_configuration
    import capo_quicksight.types.timestamp


class DataSet(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    data_set_id: NotRequired["capo_quicksight.types.resource_id.ResourceId"]
    """<p>The ID of the dataset. Limited to 96 characters.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A display name for the dataset.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this dataset was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this dataset was updated.</p>"""
    physical_table_map: NotRequired[
        "capo_quicksight.types.physical_table_map.PhysicalTableMap"
    ]
    """<p>Declares the physical tables that are available in the underlying data sources.</p>"""
    logical_table_map: NotRequired[
        "capo_quicksight.types.logical_table_map.LogicalTableMap"
    ]
    """<p>Configures the combination and transformation of the data from the physical tables.</p>"""
    output_columns: NotRequired[
        "capo_quicksight.types.output_column_list.OutputColumnList"
    ]
    """<p>The list of columns after all transforms. These columns are available in templates, analyses, and dashboards.</p>"""
    import_mode: NotRequired[
        "capo_quicksight.types.data_set_import_mode.DataSetImportMode"
    ]
    """<p>A value that indicates whether you want to import the data into SPICE.</p>"""
    consumed_spice_capacity_in_bytes: "capo_quicksight.types.long.Long"
    """<p>The amount of SPICE capacity used by this dataset. This is 0 if the dataset isn't imported into SPICE.</p>"""
    column_groups: NotRequired[
        "capo_quicksight.types.column_group_list.ColumnGroupList"
    ]
    """<p>Groupings of columns that work together in certain Quick Sight features. Currently, only geospatial hierarchy is supported.</p>"""
    field_folders: NotRequired["capo_quicksight.types.field_folder_map.FieldFolderMap"]
    """<p>The folder that contains fields and nested subfolders for your dataset.</p>"""
    row_level_permission_data_set: NotRequired[
        "capo_quicksight.types.row_level_permission_data_set.RowLevelPermissionDataSet"
    ]
    """<p>The row-level security configuration for the dataset.</p>"""
    row_level_permission_tag_configuration: NotRequired[
        "capo_quicksight.types.row_level_permission_tag_configuration.RowLevelPermissionTagConfiguration"
    ]
    """<p>The element you can use to define tags for row-level security.</p>"""
    column_level_permission_rules: NotRequired[
        "capo_quicksight.types.column_level_permission_rule_list.ColumnLevelPermissionRuleList"
    ]
    """<p>A set of one or more definitions of a <code> <a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnLevelPermissionRule.html">ColumnLevelPermissionRule</a> </code>.</p>"""
    data_set_usage_configuration: NotRequired[
        "capo_quicksight.types.data_set_usage_configuration.DataSetUsageConfiguration"
    ]
    """<p>The usage configuration to apply to child datasets that reference this dataset as a source.</p>"""
    dataset_parameters: NotRequired[
        "capo_quicksight.types.dataset_parameter_list.DatasetParameterList"
    ]
    """<p>The parameters that are declared in a dataset.</p>"""
    performance_configuration: NotRequired[
        "capo_quicksight.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>The performance optimization configuration of a dataset.</p>"""
    use_as: NotRequired["capo_quicksight.types.data_set_use_as.DataSetUseAs"]
    """<p>The usage of the dataset.</p>"""
    data_prep_configuration: NotRequired[
        "capo_quicksight.types.data_prep_configuration.DataPrepConfiguration"
    ]
    """<p>The data preparation configuration associated with this dataset.</p>"""
    semantic_model_configuration: NotRequired[
        "capo_quicksight.types.semantic_model_configuration.SemanticModelConfiguration"
    ]
    """<p>The semantic model configuration associated with this dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSet) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "data_set_id" in value:
        out["DataSetId"] = value["data_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "physical_table_map" in value:
        import capo_quicksight.types.physical_table_map

        out["PhysicalTableMap"] = (
            capo_quicksight.types.physical_table_map.serialize_json(
                value["physical_table_map"]
            )
        )
    if "logical_table_map" in value:
        import capo_quicksight.types.logical_table_map

        out["LogicalTableMap"] = capo_quicksight.types.logical_table_map.serialize_json(
            value["logical_table_map"]
        )
    if "output_columns" in value:
        import capo_quicksight.types.output_column_list

        out["OutputColumns"] = capo_quicksight.types.output_column_list.serialize_json(
            value["output_columns"]
        )
    if "import_mode" in value:
        import capo_quicksight.types.data_set_import_mode

        out["ImportMode"] = capo_quicksight.types.data_set_import_mode.serialize_json(
            value["import_mode"]
        )
    out["ConsumedSpiceCapacityInBytes"] = value.get(
        "consumed_spice_capacity_in_bytes", 0
    )
    if "column_groups" in value:
        import capo_quicksight.types.column_group_list

        out["ColumnGroups"] = capo_quicksight.types.column_group_list.serialize_json(
            value["column_groups"]
        )
    if "field_folders" in value:
        import capo_quicksight.types.field_folder_map

        out["FieldFolders"] = capo_quicksight.types.field_folder_map.serialize_json(
            value["field_folders"]
        )
    if "row_level_permission_data_set" in value:
        import capo_quicksight.types.row_level_permission_data_set

        out["RowLevelPermissionDataSet"] = (
            capo_quicksight.types.row_level_permission_data_set.serialize_json(
                value["row_level_permission_data_set"]
            )
        )
    if "row_level_permission_tag_configuration" in value:
        import capo_quicksight.types.row_level_permission_tag_configuration

        out["RowLevelPermissionTagConfiguration"] = (
            capo_quicksight.types.row_level_permission_tag_configuration.serialize_json(
                value["row_level_permission_tag_configuration"]
            )
        )
    if "column_level_permission_rules" in value:
        import capo_quicksight.types.column_level_permission_rule_list

        out["ColumnLevelPermissionRules"] = (
            capo_quicksight.types.column_level_permission_rule_list.serialize_json(
                value["column_level_permission_rules"]
            )
        )
    if "data_set_usage_configuration" in value:
        import capo_quicksight.types.data_set_usage_configuration

        out["DataSetUsageConfiguration"] = (
            capo_quicksight.types.data_set_usage_configuration.serialize_json(
                value["data_set_usage_configuration"]
            )
        )
    if "dataset_parameters" in value:
        import capo_quicksight.types.dataset_parameter_list

        out["DatasetParameters"] = (
            capo_quicksight.types.dataset_parameter_list.serialize_json(
                value["dataset_parameters"]
            )
        )
    if "performance_configuration" in value:
        import capo_quicksight.types.performance_configuration

        out["PerformanceConfiguration"] = (
            capo_quicksight.types.performance_configuration.serialize_json(
                value["performance_configuration"]
            )
        )
    if "use_as" in value:
        import capo_quicksight.types.data_set_use_as

        out["UseAs"] = capo_quicksight.types.data_set_use_as.serialize_json(
            value["use_as"]
        )
    if "data_prep_configuration" in value:
        import capo_quicksight.types.data_prep_configuration

        out["DataPrepConfiguration"] = (
            capo_quicksight.types.data_prep_configuration.serialize_json(
                value["data_prep_configuration"]
            )
        )
    if "semantic_model_configuration" in value:
        import capo_quicksight.types.semantic_model_configuration

        out["SemanticModelConfiguration"] = (
            capo_quicksight.types.semantic_model_configuration.serialize_json(
                value["semantic_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSet:
    out: DataSet = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if data.get("PhysicalTableMap") is not None:
        import capo_quicksight.types.physical_table_map

        out["physical_table_map"] = (
            capo_quicksight.types.physical_table_map.deserialize_json(
                data["PhysicalTableMap"]
            )
        )
    if data.get("LogicalTableMap") is not None:
        import capo_quicksight.types.logical_table_map

        out["logical_table_map"] = (
            capo_quicksight.types.logical_table_map.deserialize_json(
                data["LogicalTableMap"]
            )
        )
    if data.get("OutputColumns") is not None:
        import capo_quicksight.types.output_column_list

        out["output_columns"] = (
            capo_quicksight.types.output_column_list.deserialize_json(
                data["OutputColumns"]
            )
        )
    if data.get("ImportMode") is not None:
        import capo_quicksight.types.data_set_import_mode

        out["import_mode"] = (
            capo_quicksight.types.data_set_import_mode.deserialize_json(
                data["ImportMode"]
            )
        )
    if data.get("ConsumedSpiceCapacityInBytes") is not None:
        out["consumed_spice_capacity_in_bytes"] = data["ConsumedSpiceCapacityInBytes"]
    else:
        out["consumed_spice_capacity_in_bytes"] = 0
    if data.get("ColumnGroups") is not None:
        import capo_quicksight.types.column_group_list

        out["column_groups"] = capo_quicksight.types.column_group_list.deserialize_json(
            data["ColumnGroups"]
        )
    if data.get("FieldFolders") is not None:
        import capo_quicksight.types.field_folder_map

        out["field_folders"] = capo_quicksight.types.field_folder_map.deserialize_json(
            data["FieldFolders"]
        )
    if data.get("RowLevelPermissionDataSet") is not None:
        import capo_quicksight.types.row_level_permission_data_set

        out["row_level_permission_data_set"] = (
            capo_quicksight.types.row_level_permission_data_set.deserialize_json(
                data["RowLevelPermissionDataSet"]
            )
        )
    if data.get("RowLevelPermissionTagConfiguration") is not None:
        import capo_quicksight.types.row_level_permission_tag_configuration

        out["row_level_permission_tag_configuration"] = (
            capo_quicksight.types.row_level_permission_tag_configuration.deserialize_json(
                data["RowLevelPermissionTagConfiguration"]
            )
        )
    if data.get("ColumnLevelPermissionRules") is not None:
        import capo_quicksight.types.column_level_permission_rule_list

        out["column_level_permission_rules"] = (
            capo_quicksight.types.column_level_permission_rule_list.deserialize_json(
                data["ColumnLevelPermissionRules"]
            )
        )
    if data.get("DataSetUsageConfiguration") is not None:
        import capo_quicksight.types.data_set_usage_configuration

        out["data_set_usage_configuration"] = (
            capo_quicksight.types.data_set_usage_configuration.deserialize_json(
                data["DataSetUsageConfiguration"]
            )
        )
    if data.get("DatasetParameters") is not None:
        import capo_quicksight.types.dataset_parameter_list

        out["dataset_parameters"] = (
            capo_quicksight.types.dataset_parameter_list.deserialize_json(
                data["DatasetParameters"]
            )
        )
    if data.get("PerformanceConfiguration") is not None:
        import capo_quicksight.types.performance_configuration

        out["performance_configuration"] = (
            capo_quicksight.types.performance_configuration.deserialize_json(
                data["PerformanceConfiguration"]
            )
        )
    if data.get("UseAs") is not None:
        import capo_quicksight.types.data_set_use_as

        out["use_as"] = capo_quicksight.types.data_set_use_as.deserialize_json(
            data["UseAs"]
        )
    if data.get("DataPrepConfiguration") is not None:
        import capo_quicksight.types.data_prep_configuration

        out["data_prep_configuration"] = (
            capo_quicksight.types.data_prep_configuration.deserialize_json(
                data["DataPrepConfiguration"]
            )
        )
    if data.get("SemanticModelConfiguration") is not None:
        import capo_quicksight.types.semantic_model_configuration

        out["semantic_model_configuration"] = (
            capo_quicksight.types.semantic_model_configuration.deserialize_json(
                data["SemanticModelConfiguration"]
            )
        )
    return out
