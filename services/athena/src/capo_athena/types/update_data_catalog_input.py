"""Generated from Smithy shape ``com.amazonaws.athena#UpdateDataCatalogInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.catalog_name_string
    import capo_athena.types.data_catalog_type
    import capo_athena.types.description_string
    import capo_athena.types.parameters_map


class UpdateDataCatalogInput(TypedDict, closed=True):
    name: "capo_athena.types.catalog_name_string.CatalogNameString"
    """<p>The name of the data catalog to update. The catalog name must be unique for the Amazon Web Services account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.</p>"""
    type: "capo_athena.types.data_catalog_type.DataCatalogType"
    """<p>Specifies the type of data catalog to update. Specify <code>LAMBDA</code> for a federated catalog, <code>HIVE</code> for an external hive metastore, or <code>GLUE</code> for an Glue Data Catalog.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>New or modified text that describes the data catalog.</p>"""
    parameters: NotRequired["capo_athena.types.parameters_map.ParametersMap"]
    """<p>Specifies the Lambda function or functions to use for updating the data catalog. This is a mapping whose values depend on the catalog type. </p> <ul> <li> <p>For the <code>HIVE</code> data catalog type, use the following syntax. The <code>metadata-function</code> parameter is required. <code>The sdk-version</code> parameter is optional and defaults to the currently supported version.</p> <p> <code>metadata-function=<i>lambda_arn</i>, sdk-version=<i>version_number</i> </code> </p> </li> <li> <p>For the <code>LAMBDA</code> data catalog type, use one of the following sets of required parameters, but not both.</p> <ul> <li> <p>If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.</p> <p> <code>metadata-function=<i>lambda_arn</i>, record-function=<i>lambda_arn</i> </code> </p> </li> <li> <p> If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.</p> <p> <code>function=<i>lambda_arn</i> </code> </p> </li> </ul> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDataCatalogInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_athena.types.data_catalog_type

    out["Type"] = capo_athena.types.data_catalog_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "parameters" in value:
        import capo_athena.types.parameters_map

        out["Parameters"] = capo_athena.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDataCatalogInput:
    out: UpdateDataCatalogInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        import capo_athena.types.data_catalog_type

        out["type"] = capo_athena.types.data_catalog_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_athena.types.data_catalog_type.DataCatalogType", ""
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Parameters") is not None:
        import capo_athena.types.parameters_map

        out["parameters"] = capo_athena.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    return out
