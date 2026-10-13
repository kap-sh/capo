"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobOverrideParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list
    import capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list
    import capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list
    import capo_quicksight.types.asset_bundle_import_job_folder_override_parameters_list
    import capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list
    import capo_quicksight.types.asset_bundle_import_job_resource_id_override_configuration
    import capo_quicksight.types.asset_bundle_import_job_theme_override_parameters_list
    import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters_list
    import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list


class AssetBundleImportJobOverrideParameters(TypedDict, closed=True):
    resource_id_override_configuration: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_resource_id_override_configuration.AssetBundleImportJobResourceIdOverrideConfiguration"
    ]
    """<p>An optional structure that configures resource ID overrides to be applied within the import job.</p>"""
    vpc_connections: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list.AssetBundleImportJobVPCConnectionOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>VPCConnection</code> resources that are present in the asset bundle that is imported.</p>"""
    refresh_schedules: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list.AssetBundleImportJobRefreshScheduleOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>RefreshSchedule</code> resources that are present in the asset bundle that is imported.</p>"""
    data_sources: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list.AssetBundleImportJobDataSourceOverrideParametersList"
    ]
    """<p> A list of overrides for any <code>DataSource</code> resources that are present in the asset bundle that is imported.</p>"""
    data_sets: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list.AssetBundleImportJobDataSetOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>DataSet</code> resources that are present in the asset bundle that is imported.</p>"""
    themes: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_theme_override_parameters_list.AssetBundleImportJobThemeOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>Theme</code> resources that are present in the asset bundle that is imported.</p>"""
    analyses: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list.AssetBundleImportJobAnalysisOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>Analysis</code> resources that are present in the asset bundle that is imported.</p>"""
    dashboards: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list.AssetBundleImportJobDashboardOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>Dashboard</code> resources that are present in the asset bundle that is imported.</p>"""
    folders: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_folder_override_parameters_list.AssetBundleImportJobFolderOverrideParametersList"
    ]
    """<p>A list of overrides for any <code>Folder</code> resources that are present in the asset bundle that is imported.</p>"""
    topics_v2: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters_list.AssetBundleImportJobTopicV2OverrideParametersList"
    ]
    """<p>A list of overrides for any <code>Topic</code> resources that are present in the asset bundle that is imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobOverrideParameters) -> dict:
    out: dict = {}
    if "resource_id_override_configuration" in value:
        import capo_quicksight.types.asset_bundle_import_job_resource_id_override_configuration

        out["ResourceIdOverrideConfiguration"] = (
            capo_quicksight.types.asset_bundle_import_job_resource_id_override_configuration.serialize_json(
                value["resource_id_override_configuration"]
            )
        )
    if "vpc_connections" in value:
        import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list

        out["VPCConnections"] = (
            capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list.serialize_json(
                value["vpc_connections"]
            )
        )
    if "refresh_schedules" in value:
        import capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list

        out["RefreshSchedules"] = (
            capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list.serialize_json(
                value["refresh_schedules"]
            )
        )
    if "data_sources" in value:
        import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list

        out["DataSources"] = (
            capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list.serialize_json(
                value["data_sources"]
            )
        )
    if "data_sets" in value:
        import capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list

        out["DataSets"] = (
            capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list.serialize_json(
                value["data_sets"]
            )
        )
    if "themes" in value:
        import capo_quicksight.types.asset_bundle_import_job_theme_override_parameters_list

        out["Themes"] = (
            capo_quicksight.types.asset_bundle_import_job_theme_override_parameters_list.serialize_json(
                value["themes"]
            )
        )
    if "analyses" in value:
        import capo_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list

        out["Analyses"] = (
            capo_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list.serialize_json(
                value["analyses"]
            )
        )
    if "dashboards" in value:
        import capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list

        out["Dashboards"] = (
            capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list.serialize_json(
                value["dashboards"]
            )
        )
    if "folders" in value:
        import capo_quicksight.types.asset_bundle_import_job_folder_override_parameters_list

        out["Folders"] = (
            capo_quicksight.types.asset_bundle_import_job_folder_override_parameters_list.serialize_json(
                value["folders"]
            )
        )
    if "topics_v2" in value:
        import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters_list

        out["TopicsV2"] = (
            capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters_list.serialize_json(
                value["topics_v2"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobOverrideParameters:
    out: AssetBundleImportJobOverrideParameters = {}  # type: ignore[typeddict-item]
    if data.get("ResourceIdOverrideConfiguration") is not None:
        import capo_quicksight.types.asset_bundle_import_job_resource_id_override_configuration

        out["resource_id_override_configuration"] = (
            capo_quicksight.types.asset_bundle_import_job_resource_id_override_configuration.deserialize_json(
                data["ResourceIdOverrideConfiguration"]
            )
        )
    if data.get("VPCConnections") is not None:
        import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list

        out["vpc_connections"] = (
            capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters_list.deserialize_json(
                data["VPCConnections"]
            )
        )
    if data.get("RefreshSchedules") is not None:
        import capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list

        out["refresh_schedules"] = (
            capo_quicksight.types.asset_bundle_import_job_refresh_schedule_override_parameters_list.deserialize_json(
                data["RefreshSchedules"]
            )
        )
    if data.get("DataSources") is not None:
        import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list

        out["data_sources"] = (
            capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list.deserialize_json(
                data["DataSources"]
            )
        )
    if data.get("DataSets") is not None:
        import capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list

        out["data_sets"] = (
            capo_quicksight.types.asset_bundle_import_job_data_set_override_parameters_list.deserialize_json(
                data["DataSets"]
            )
        )
    if data.get("Themes") is not None:
        import capo_quicksight.types.asset_bundle_import_job_theme_override_parameters_list

        out["themes"] = (
            capo_quicksight.types.asset_bundle_import_job_theme_override_parameters_list.deserialize_json(
                data["Themes"]
            )
        )
    if data.get("Analyses") is not None:
        import capo_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list

        out["analyses"] = (
            capo_quicksight.types.asset_bundle_import_job_analysis_override_parameters_list.deserialize_json(
                data["Analyses"]
            )
        )
    if data.get("Dashboards") is not None:
        import capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list

        out["dashboards"] = (
            capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters_list.deserialize_json(
                data["Dashboards"]
            )
        )
    if data.get("Folders") is not None:
        import capo_quicksight.types.asset_bundle_import_job_folder_override_parameters_list

        out["folders"] = (
            capo_quicksight.types.asset_bundle_import_job_folder_override_parameters_list.deserialize_json(
                data["Folders"]
            )
        )
    if data.get("TopicsV2") is not None:
        import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters_list

        out["topics_v2"] = (
            capo_quicksight.types.asset_bundle_import_job_topic_v2_override_parameters_list.deserialize_json(
                data["TopicsV2"]
            )
        )
    return out


def redact_sensitive(value: AssetBundleImportJobOverrideParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_sources" in value:
        import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list

        out["data_sources"] = (
            capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters_list.redact_sensitive(
                value["data_sources"]
            )
        )
    return out
