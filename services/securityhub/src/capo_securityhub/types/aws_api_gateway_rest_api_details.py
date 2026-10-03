"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayRestApiDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_api_gateway_endpoint_configuration
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsApiGatewayRestApiDetails(TypedDict, closed=True):
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the REST API.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the REST API.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the REST API.</p>"""
    created_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the API was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    version: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The version identifier for the REST API.</p>"""
    binary_media_types: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The list of binary media types supported by the REST API.</p>"""
    minimum_compression_size: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The minimum size in bytes of a payload before compression is enabled.</p> <p>If <code>null</code>, then compression is disabled.</p> <p>If 0, then all payloads are compressed.</p>"""
    api_key_source: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The source of the API key for metering requests according to a usage plan.</p> <p> <code>HEADER</code> indicates whether to read the API key from the X-API-Key header of a request.</p> <p> <code>AUTHORIZER</code> indicates whether to read the API key from the <code>UsageIdentifierKey</code> from a custom authorizer.</p>"""
    endpoint_configuration: NotRequired[
        "capo_securityhub.types.aws_api_gateway_endpoint_configuration.AwsApiGatewayEndpointConfiguration"
    ]
    """<p>The endpoint configuration of the REST API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayRestApiDetails) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    if "version" in value:
        out["Version"] = value["version"]
    if "binary_media_types" in value:
        import capo_securityhub.types.non_empty_string_list

        out["BinaryMediaTypes"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["binary_media_types"]
            )
        )
    if "minimum_compression_size" in value:
        out["MinimumCompressionSize"] = value["minimum_compression_size"]
    if "api_key_source" in value:
        out["ApiKeySource"] = value["api_key_source"]
    if "endpoint_configuration" in value:
        import capo_securityhub.types.aws_api_gateway_endpoint_configuration

        out["EndpointConfiguration"] = (
            capo_securityhub.types.aws_api_gateway_endpoint_configuration.serialize_json(
                value["endpoint_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsApiGatewayRestApiDetails:
    out: AwsApiGatewayRestApiDetails = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedDate") is not None:
        out["created_date"] = data["CreatedDate"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("BinaryMediaTypes") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["binary_media_types"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["BinaryMediaTypes"]
            )
        )
    if data.get("MinimumCompressionSize") is not None:
        out["minimum_compression_size"] = data["MinimumCompressionSize"]
    if data.get("ApiKeySource") is not None:
        out["api_key_source"] = data["ApiKeySource"]
    if data.get("EndpointConfiguration") is not None:
        import capo_securityhub.types.aws_api_gateway_endpoint_configuration

        out["endpoint_configuration"] = (
            capo_securityhub.types.aws_api_gateway_endpoint_configuration.deserialize_json(
                data["EndpointConfiguration"]
            )
        )
    return out
