"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#CreateServiceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.application_id
    import capo_migration_hub_refactor_spaces.types.client_token
    import capo_migration_hub_refactor_spaces.types.description
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.lambda_endpoint_input
    import capo_migration_hub_refactor_spaces.types.service_endpoint_type
    import capo_migration_hub_refactor_spaces.types.service_name
    import capo_migration_hub_refactor_spaces.types.tag_map
    import capo_migration_hub_refactor_spaces.types.url_endpoint_input
    import capo_migration_hub_refactor_spaces.types.vpc_id


class CreateServiceRequest(TypedDict, closed=True):
    name: "capo_migration_hub_refactor_spaces.types.service_name.ServiceName"
    """<p>The name of the service.</p>"""
    description: NotRequired[
        "capo_migration_hub_refactor_spaces.types.description.Description"
    ]
    """<p>The description of the service.</p>"""
    environment_identifier: (
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The ID of the environment in which the service is created.</p>"""
    application_identifier: (
        "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    )
    """<p>The ID of the application which the service is created.</p>"""
    vpc_id: NotRequired["capo_migration_hub_refactor_spaces.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    endpoint_type: "capo_migration_hub_refactor_spaces.types.service_endpoint_type.ServiceEndpointType"
    """<p>The type of endpoint to use for the service. The type can be a URL in a VPC or an Lambda function.</p>"""
    url_endpoint: NotRequired[
        "capo_migration_hub_refactor_spaces.types.url_endpoint_input.UrlEndpointInput"
    ]
    """<p>The configuration for the URL endpoint type. When creating a route to a service, Refactor Spaces automatically resolves the address in the <code>UrlEndpointInput</code> object URL when the Domain Name System (DNS) time-to-live (TTL) expires, or every 60 seconds for TTLs less than 60 seconds.</p>"""
    lambda_endpoint: NotRequired[
        "capo_migration_hub_refactor_spaces.types.lambda_endpoint_input.LambdaEndpointInput"
    ]
    """<p>The configuration for the Lambda endpoint type.</p>"""
    tags: NotRequired["capo_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags to assign to the service. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.. </p>"""
    client_token: NotRequired[
        "capo_migration_hub_refactor_spaces.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    out["EndpointType"] = value["endpoint_type"]
    if "url_endpoint" in value:
        import capo_migration_hub_refactor_spaces.types.url_endpoint_input

        out["UrlEndpoint"] = (
            capo_migration_hub_refactor_spaces.types.url_endpoint_input.serialize_json(
                value["url_endpoint"]
            )
        )
    if "lambda_endpoint" in value:
        import capo_migration_hub_refactor_spaces.types.lambda_endpoint_input

        out["LambdaEndpoint"] = (
            capo_migration_hub_refactor_spaces.types.lambda_endpoint_input.serialize_json(
                value["lambda_endpoint"]
            )
        )
    if "tags" in value:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["Tags"] = capo_migration_hub_refactor_spaces.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateServiceRequest:
    out: CreateServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("EndpointType") is not None:
        out["endpoint_type"] = data["EndpointType"]
    else:
        out["endpoint_type"] = ""
    if data.get("UrlEndpoint") is not None:
        import capo_migration_hub_refactor_spaces.types.url_endpoint_input

        out["url_endpoint"] = (
            capo_migration_hub_refactor_spaces.types.url_endpoint_input.deserialize_json(
                data["UrlEndpoint"]
            )
        )
    if data.get("LambdaEndpoint") is not None:
        import capo_migration_hub_refactor_spaces.types.lambda_endpoint_input

        out["lambda_endpoint"] = (
            capo_migration_hub_refactor_spaces.types.lambda_endpoint_input.deserialize_json(
                data["LambdaEndpoint"]
            )
        )
    if data.get("Tags") is not None:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = capo_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: CreateServiceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
