"""Generated from Smithy shape ``com.amazonaws.athena#DataCatalogSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.catalog_name_string
    import capo_athena.types.connection_type
    import capo_athena.types.data_catalog_status
    import capo_athena.types.data_catalog_type
    import capo_athena.types.error_message


class DataCatalogSummary(TypedDict, closed=True):
    catalog_name: NotRequired["capo_athena.types.catalog_name_string.CatalogNameString"]
    """<p>The name of the data catalog. The catalog name is unique for the Amazon Web Services account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.</p>"""
    type: NotRequired["capo_athena.types.data_catalog_type.DataCatalogType"]
    """<p>The data catalog type.</p>"""
    status: NotRequired["capo_athena.types.data_catalog_status.DataCatalogStatus"]
    """<p>The status of the creation or deletion of the data catalog.</p> <ul> <li> <p>The <code>LAMBDA</code>, <code>GLUE</code>, and <code>HIVE</code> data catalog types are created synchronously. Their status is either <code>CREATE_COMPLETE</code> or <code>CREATE_FAILED</code>.</p> </li> <li> <p>The <code>FEDERATED</code> data catalog type is created asynchronously.</p> </li> </ul> <p>Data catalog creation status:</p> <ul> <li> <p> <code>CREATE_IN_PROGRESS</code>: Federated data catalog creation in progress.</p> </li> <li> <p> <code>CREATE_COMPLETE</code>: Data catalog creation complete.</p> </li> <li> <p> <code>CREATE_FAILED</code>: Data catalog could not be created.</p> </li> <li> <p> <code>CREATE_FAILED_CLEANUP_IN_PROGRESS</code>: Federated data catalog creation failed and is being removed.</p> </li> <li> <p> <code>CREATE_FAILED_CLEANUP_COMPLETE</code>: Federated data catalog creation failed and was removed.</p> </li> <li> <p> <code>CREATE_FAILED_CLEANUP_FAILED</code>: Federated data catalog creation failed but could not be removed.</p> </li> </ul> <p>Data catalog deletion status:</p> <ul> <li> <p> <code>DELETE_IN_PROGRESS</code>: Federated data catalog deletion in progress.</p> </li> <li> <p> <code>DELETE_COMPLETE</code>: Federated data catalog deleted.</p> </li> <li> <p> <code>DELETE_FAILED</code>: Federated data catalog could not be deleted.</p> </li> </ul>"""
    connection_type: NotRequired["capo_athena.types.connection_type.ConnectionType"]
    """<p>The type of connection for a <code>FEDERATED</code> data catalog (for example, <code>REDSHIFT</code>, <code>MYSQL</code>, or <code>SQLSERVER</code>). For information about individual connectors, see <a href="https://docs.aws.amazon.com/athena/latest/ug/connectors-available.html">Available data source connectors</a>.</p>"""
    error: NotRequired["capo_athena.types.error_message.ErrorMessage"]
    """<p>Text of the error that occurred during data catalog creation or deletion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataCatalogSummary) -> dict:
    out: dict = {}
    if "catalog_name" in value:
        out["CatalogName"] = value["catalog_name"]
    if "type" in value:
        import capo_athena.types.data_catalog_type

        out["Type"] = capo_athena.types.data_catalog_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "status" in value:
        import capo_athena.types.data_catalog_status

        out["Status"] = capo_athena.types.data_catalog_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "connection_type" in value:
        import capo_athena.types.connection_type

        out["ConnectionType"] = (
            capo_athena.types.connection_type.serialize_aws_json_1_1(
                value["connection_type"]
            )
        )
    if "error" in value:
        out["Error"] = value["error"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataCatalogSummary:
    out: DataCatalogSummary = {}  # type: ignore[typeddict-item]
    if data.get("CatalogName") is not None:
        out["catalog_name"] = data["CatalogName"]
    if data.get("Type") is not None:
        import capo_athena.types.data_catalog_type

        out["type"] = capo_athena.types.data_catalog_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Status") is not None:
        import capo_athena.types.data_catalog_status

        out["status"] = capo_athena.types.data_catalog_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("ConnectionType") is not None:
        import capo_athena.types.connection_type

        out["connection_type"] = (
            capo_athena.types.connection_type.deserialize_aws_json_1_1(
                data["ConnectionType"]
            )
        )
    if data.get("Error") is not None:
        out["error"] = data["Error"]
    return out
