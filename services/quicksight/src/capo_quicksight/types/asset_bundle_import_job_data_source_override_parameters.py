"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceOverrideParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_data_source_credentials
    import capo_quicksight.types.data_source_parameters
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.ssl_properties
    import capo_quicksight.types.vpc_connection_properties


class AssetBundleImportJobDataSourceOverrideParameters(TypedDict, closed=True):
    data_source_id: "capo_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the data source to apply overrides to.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the data source.</p>"""
    data_source_parameters: NotRequired[
        "capo_quicksight.types.data_source_parameters.DataSourceParameters"
    ]
    vpc_connection_properties: NotRequired[
        "capo_quicksight.types.vpc_connection_properties.VpcConnectionProperties"
    ]
    ssl_properties: NotRequired["capo_quicksight.types.ssl_properties.SslProperties"]
    credentials: NotRequired[
        "capo_quicksight.types.asset_bundle_import_job_data_source_credentials.AssetBundleImportJobDataSourceCredentials"
    ]
    """<p>An optional structure that provides the credentials to be used to create the imported data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSourceOverrideParameters) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "data_source_parameters" in value:
        import capo_quicksight.types.data_source_parameters

        out["DataSourceParameters"] = (
            capo_quicksight.types.data_source_parameters.serialize_json(
                value["data_source_parameters"]
            )
        )
    if "vpc_connection_properties" in value:
        import capo_quicksight.types.vpc_connection_properties

        out["VpcConnectionProperties"] = (
            capo_quicksight.types.vpc_connection_properties.serialize_json(
                value["vpc_connection_properties"]
            )
        )
    if "ssl_properties" in value:
        import capo_quicksight.types.ssl_properties

        out["SslProperties"] = capo_quicksight.types.ssl_properties.serialize_json(
            value["ssl_properties"]
        )
    if "credentials" in value:
        import capo_quicksight.types.asset_bundle_import_job_data_source_credentials

        out["Credentials"] = (
            capo_quicksight.types.asset_bundle_import_job_data_source_credentials.serialize_json(
                value["credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSourceOverrideParameters:
    out: AssetBundleImportJobDataSourceOverrideParameters = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    else:
        out["data_source_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DataSourceParameters") is not None:
        import capo_quicksight.types.data_source_parameters

        out["data_source_parameters"] = (
            capo_quicksight.types.data_source_parameters.deserialize_json(
                data["DataSourceParameters"]
            )
        )
    if data.get("VpcConnectionProperties") is not None:
        import capo_quicksight.types.vpc_connection_properties

        out["vpc_connection_properties"] = (
            capo_quicksight.types.vpc_connection_properties.deserialize_json(
                data["VpcConnectionProperties"]
            )
        )
    if data.get("SslProperties") is not None:
        import capo_quicksight.types.ssl_properties

        out["ssl_properties"] = capo_quicksight.types.ssl_properties.deserialize_json(
            data["SslProperties"]
        )
    if data.get("Credentials") is not None:
        import capo_quicksight.types.asset_bundle_import_job_data_source_credentials

        out["credentials"] = (
            capo_quicksight.types.asset_bundle_import_job_data_source_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    return out


def redact_sensitive(
    value: AssetBundleImportJobDataSourceOverrideParameters,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        import capo_quicksight.types.asset_bundle_import_job_data_source_credentials

        out["credentials"] = (
            capo_quicksight.types.asset_bundle_import_job_data_source_credentials.redact_sensitive(
                value["credentials"]
            )
        )
    return out
