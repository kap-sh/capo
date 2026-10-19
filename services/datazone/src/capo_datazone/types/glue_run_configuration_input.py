"""Generated from Smithy shape ``com.amazonaws.datazone#GlueRunConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.relational_filter_configurations


class GlueRunConfigurationInput(TypedDict, closed=True):
    data_access_role: NotRequired["str"]
    """<p>The data access role included in the configuration details of the Amazon Web Services Glue data source.</p>"""
    relational_filter_configurations: "capo_datazone.types.relational_filter_configurations.RelationalFilterConfigurations"
    """<p>The relational filter configurations included in the configuration details of the Amazon Web Services Glue data source.</p>"""
    auto_import_data_quality_result: NotRequired["bool"]
    """<p>Specifies whether to automatically import data quality metrics as part of the data source run.</p>"""
    catalog_name: NotRequired["str"]
    """<p>The catalog name in the Amazon Web Services Glue run configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueRunConfigurationInput) -> dict:
    out: dict = {}
    if "data_access_role" in value:
        out["dataAccessRole"] = value["data_access_role"]
    import capo_datazone.types.relational_filter_configurations

    out["relationalFilterConfigurations"] = (
        capo_datazone.types.relational_filter_configurations.serialize_json(
            value["relational_filter_configurations"]
        )
    )
    if "auto_import_data_quality_result" in value:
        out["autoImportDataQualityResult"] = value["auto_import_data_quality_result"]
    if "catalog_name" in value:
        out["catalogName"] = value["catalog_name"]
    return out


def deserialize_json(data: dict) -> GlueRunConfigurationInput:
    out: GlueRunConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("dataAccessRole") is not None:
        out["data_access_role"] = data["dataAccessRole"]
    if data.get("relationalFilterConfigurations") is not None:
        import capo_datazone.types.relational_filter_configurations

        out["relational_filter_configurations"] = (
            capo_datazone.types.relational_filter_configurations.deserialize_json(
                data["relationalFilterConfigurations"]
            )
        )
    else:
        out["relational_filter_configurations"] = []
    if data.get("autoImportDataQualityResult") is not None:
        out["auto_import_data_quality_result"] = data["autoImportDataQualityResult"]
    if data.get("catalogName") is not None:
        out["catalog_name"] = data["catalogName"]
    return out
