"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateDataSourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.data_source_credentials
    import capo_quicksight.types.data_source_parameters
    import capo_quicksight.types.data_source_type
    import capo_quicksight.types.folder_arn_list
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.ssl_properties
    import capo_quicksight.types.tag_list
    import capo_quicksight.types.vpc_connection_properties


class CreateDataSourceRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_source_id: "capo_quicksight.types.resource_id.ResourceId"
    """<p>An ID for the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account. </p>"""
    name: "capo_quicksight.types.resource_name.ResourceName"
    """<p>A display name for the data source.</p>"""
    type: "capo_quicksight.types.data_source_type.DataSourceType"
    """<p>The type of the data source. To return a list of all data sources, use <code>ListDataSources</code>.</p> <p>Use <code>AMAZON_ELASTICSEARCH</code> for Amazon OpenSearch Service.</p>"""
    data_source_parameters: NotRequired[
        "capo_quicksight.types.data_source_parameters.DataSourceParameters"
    ]
    """<p>The parameters that Amazon Quick Sight uses to connect to your underlying source.</p>"""
    credentials: NotRequired[
        "capo_quicksight.types.data_source_credentials.DataSourceCredentials"
    ]
    """<p>The credentials Amazon Quick Sight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A list of resource permissions on the data source.</p>"""
    vpc_connection_properties: NotRequired[
        "capo_quicksight.types.vpc_connection_properties.VpcConnectionProperties"
    ]
    """<p>Use this parameter only when you want Amazon Quick Sight to use a VPC connection when connecting to your underlying source.</p>"""
    ssl_properties: NotRequired["capo_quicksight.types.ssl_properties.SslProperties"]
    """<p>Secure Socket Layer (SSL) properties that apply when Amazon Quick Sight connects to your underlying source.</p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>"""
    folder_arns: NotRequired["capo_quicksight.types.folder_arn_list.FolderArnList"]
    """<p>When you create the data source, Amazon Quick Sight adds the data source to these folders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceRequest) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    out["Name"] = value["name"]
    import capo_quicksight.types.data_source_type

    out["Type"] = capo_quicksight.types.data_source_type.serialize_json(value["type"])
    if "data_source_parameters" in value:
        import capo_quicksight.types.data_source_parameters

        out["DataSourceParameters"] = (
            capo_quicksight.types.data_source_parameters.serialize_json(
                value["data_source_parameters"]
            )
        )
    if "credentials" in value:
        import capo_quicksight.types.data_source_credentials

        out["Credentials"] = (
            capo_quicksight.types.data_source_credentials.serialize_json(
                value["credentials"]
            )
        )
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
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
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    if "folder_arns" in value:
        import capo_quicksight.types.folder_arn_list

        out["FolderArns"] = capo_quicksight.types.folder_arn_list.serialize_json(
            value["folder_arns"]
        )
    return out


def deserialize_json(data: dict) -> CreateDataSourceRequest:
    out: CreateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    else:
        raise DeserializationError("CreateDataSourceRequest.data_source_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDataSourceRequest.name required")
    if data.get("Type") is not None:
        import capo_quicksight.types.data_source_type

        out["type"] = capo_quicksight.types.data_source_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateDataSourceRequest.type required")
    if data.get("DataSourceParameters") is not None:
        import capo_quicksight.types.data_source_parameters

        out["data_source_parameters"] = (
            capo_quicksight.types.data_source_parameters.deserialize_json(
                data["DataSourceParameters"]
            )
        )
    if data.get("Credentials") is not None:
        import capo_quicksight.types.data_source_credentials

        out["credentials"] = (
            capo_quicksight.types.data_source_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    if data.get("Permissions") is not None:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
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
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    if data.get("FolderArns") is not None:
        import capo_quicksight.types.folder_arn_list

        out["folder_arns"] = capo_quicksight.types.folder_arn_list.deserialize_json(
            data["FolderArns"]
        )
    return out


def redact_sensitive(value: CreateDataSourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        out["credentials"] = "*** Sensitive Data Redacted ***"
    return out
