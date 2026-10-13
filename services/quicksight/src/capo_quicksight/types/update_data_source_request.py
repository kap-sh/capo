"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDataSourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.data_source_credentials
    import capo_quicksight.types.data_source_parameters
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.ssl_properties
    import capo_quicksight.types.vpc_connection_properties


class UpdateDataSourceRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_source_id: "capo_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account. </p>"""
    name: "capo_quicksight.types.resource_name.ResourceName"
    """<p>A display name for the data source.</p>"""
    data_source_parameters: NotRequired[
        "capo_quicksight.types.data_source_parameters.DataSourceParameters"
    ]
    """<p>The parameters that Amazon Quick Sight uses to connect to your underlying source.</p>"""
    credentials: NotRequired[
        "capo_quicksight.types.data_source_credentials.DataSourceCredentials"
    ]
    """<p>The credentials that Amazon Quick Sight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.</p>"""
    vpc_connection_properties: NotRequired[
        "capo_quicksight.types.vpc_connection_properties.VpcConnectionProperties"
    ]
    """<p>Use this parameter only when you want Amazon Quick Sight to use a VPC connection when connecting to your underlying source.</p>"""
    ssl_properties: NotRequired["capo_quicksight.types.ssl_properties.SslProperties"]
    """<p>Secure Socket Layer (SSL) properties that apply when Amazon Quick Sight connects to your underlying source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
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
    return out


def deserialize_json(data: dict) -> UpdateDataSourceRequest:
    out: UpdateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDataSourceRequest.name required")
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
    return out


def redact_sensitive(value: UpdateDataSourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        out["credentials"] = "*** Sensitive Data Redacted ***"
    return out
