"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceOverrideParametersList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters

AssetBundleImportJobDataSourceOverrideParametersList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters.AssetBundleImportJobDataSourceOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSourceOverrideParametersList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleImportJobDataSourceOverrideParametersList:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters

    out: AssetBundleImportJobDataSourceOverrideParametersList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: AssetBundleImportJobDataSourceOverrideParametersList,
) -> list[Any]:
    import capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters

    return [
        capo_quicksight.types.asset_bundle_import_job_data_source_override_parameters.redact_sensitive(
            item
        )
        for item in value
    ]
