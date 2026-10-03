"""Generated from Smithy shape ``com.amazonaws.athena#CreateDataCatalogInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.catalog_name_string
    import capo_athena.types.data_catalog_type
    import capo_athena.types.description_string
    import capo_athena.types.parameters_map
    import capo_athena.types.tag_list


class CreateDataCatalogInput(TypedDict, closed=True):
    name: "capo_athena.types.catalog_name_string.CatalogNameString"
    r"""<p>The name of the data catalog to create. The catalog name must be unique for the Amazon Web Services account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.</p> <p>For <code>FEDERATED</code> type the catalog name has following considerations and limits:</p> <ul> <li> <p>The catalog name allows special characters such as <code>_ , @ , \ , - </code>. These characters are replaced with a hyphen (-) when creating the CFN Stack Name and with an underscore (_) when creating the Lambda Function and Glue Connection Name.</p> </li> <li> <p>The catalog name has a theoretical limit of 128 characters. However, since we use it to create other resources that allow less characters and we prepend a prefix to it, the actual catalog name limit for <code>FEDERATED</code> catalog is 64 - 23 = 41 characters.</p> </li> </ul>"""
    type: "capo_athena.types.data_catalog_type.DataCatalogType"
    """<p>The type of data catalog to create: <code>LAMBDA</code> for a federated catalog, <code>GLUE</code> for an Glue Data Catalog, and <code>HIVE</code> for an external Apache Hive metastore. <code>FEDERATED</code> is a federated catalog for which Athena creates the connection and the Lambda function for you based on the parameters that you pass.</p> <p>For <code>FEDERATED</code> type, we do not support IAM identity center.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>A description of the data catalog to be created.</p>"""
    parameters: NotRequired["capo_athena.types.parameters_map.ParametersMap"]
    r"""<p>Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type. </p> <ul> <li> <p>For the <code>HIVE</code> data catalog type, use the following syntax. The <code>metadata-function</code> parameter is required. <code>The sdk-version</code> parameter is optional and defaults to the currently supported version.</p> <p> <code>metadata-function=<i>lambda_arn</i>, sdk-version=<i>version_number</i> </code> </p> </li> <li> <p>For the <code>LAMBDA</code> data catalog type, use one of the following sets of required parameters, but not both.</p> <ul> <li> <p>If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.</p> <p> <code>metadata-function=<i>lambda_arn</i>, record-function=<i>lambda_arn</i> </code> </p> </li> <li> <p> If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.</p> <p> <code>function=<i>lambda_arn</i> </code> </p> </li> </ul> </li> <li> <p>The <code>GLUE</code> type takes a catalog ID parameter and is required. The <code> <i>catalog_id</i> </code> is the account ID of the Amazon Web Services account to which the Glue Data Catalog belongs.</p> <p> <code>catalog-id=<i>catalog_id</i> </code> </p> <ul> <li> <p>The <code>GLUE</code> data catalog type also applies to the default <code>AwsDataCatalog</code> that already exists in your account, of which you can have only one and cannot modify.</p> </li> </ul> </li> <li> <p>The <code>FEDERATED</code> data catalog type uses one of the following parameters, but not both. Use <code>connection-arn</code> for an existing Glue connection. Use <code>connection-type</code> and <code>connection-properties</code> to specify the configuration setting for a new connection.</p> <ul> <li> <p> <code>connection-arn:<i><glue_connection_arn_to_reuse></i> </code> </p> </li> <li> <p> <code>lambda-role-arn</code> (optional): The execution role to use for the Lambda function. If not provided, one is created.</p> </li> <li> <p> <code>connection-type:MYSQL|REDSHIFT|...., connection-properties:"<i><json_string></i>"</code> </p> <p>For <i> <code><json_string></code> </i>, use escaped JSON text, as in the following example.</p> <p> <code>"{\"spill_bucket\":\"my_spill\",\"spill_prefix\":\"athena-spill\",\"host\":\"abc12345.snowflakecomputing.com\",\"port\":\"1234\",\"warehouse\":\"DEV_WH\",\"database\":\"TEST\",\"schema\":\"PUBLIC\",\"SecretArn\":\"arn:aws:secretsmanager:ap-south-1:111122223333:secret:snowflake-XHb67j\"}"</code> </p> </li> </ul> </li> </ul>"""
    tags: NotRequired["capo_athena.types.tag_list.TagList"]
    """<p>A list of comma separated tags to add to the data catalog that is created. All the resources that are created by the <code>CreateDataCatalog</code> API operation with <code>FEDERATED</code> type will have the tag <code>federated_athena_datacatalog="true"</code>. This includes the CFN Stack, Glue Connection, Athena DataCatalog, and all the resources created as part of the CFN Stack (Lambda Function, IAM policies/roles).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataCatalogInput) -> dict:
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
    if "tags" in value:
        import capo_athena.types.tag_list

        out["Tags"] = capo_athena.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataCatalogInput:
    out: CreateDataCatalogInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDataCatalogInput.name required")
    if data.get("Type") is not None:
        import capo_athena.types.data_catalog_type

        out["type"] = capo_athena.types.data_catalog_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateDataCatalogInput.type required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Parameters") is not None:
        import capo_athena.types.parameters_map

        out["parameters"] = capo_athena.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if data.get("Tags") is not None:
        import capo_athena.types.tag_list

        out["tags"] = capo_athena.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
