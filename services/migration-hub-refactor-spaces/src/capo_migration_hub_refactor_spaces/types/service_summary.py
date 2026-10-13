"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ServiceSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.account_id
    import capo_migration_hub_refactor_spaces.types.application_id
    import capo_migration_hub_refactor_spaces.types.description
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.error_response
    import capo_migration_hub_refactor_spaces.types.lambda_endpoint_summary
    import capo_migration_hub_refactor_spaces.types.resource_arn
    import capo_migration_hub_refactor_spaces.types.service_endpoint_type
    import capo_migration_hub_refactor_spaces.types.service_id
    import capo_migration_hub_refactor_spaces.types.service_name
    import capo_migration_hub_refactor_spaces.types.service_state
    import capo_migration_hub_refactor_spaces.types.tag_map
    import capo_migration_hub_refactor_spaces.types.timestamp
    import capo_migration_hub_refactor_spaces.types.url_endpoint_summary
    import capo_migration_hub_refactor_spaces.types.vpc_id


class ServiceSummary(TypedDict, closed=True):
    service_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.service_id.ServiceId"
    ]
    """<p>The unique identifier of the service. </p>"""
    name: NotRequired[
        "capo_migration_hub_refactor_spaces.types.service_name.ServiceName"
    ]
    """<p>The name of the service. </p>"""
    arn: NotRequired[
        "capo_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service. </p>"""
    owner_account_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the service owner.</p>"""
    created_by_account_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the service creator. </p>"""
    description: NotRequired[
        "capo_migration_hub_refactor_spaces.types.description.Description"
    ]
    """<p>A description of the service. </p>"""
    environment_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    ]
    """<p>The unique identifier of the environment. </p>"""
    application_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p>The unique identifier of the application. </p>"""
    vpc_id: NotRequired["capo_migration_hub_refactor_spaces.types.vpc_id.VpcId"]
    """<p>The ID of the virtual private cloud (VPC). </p>"""
    endpoint_type: NotRequired[
        "capo_migration_hub_refactor_spaces.types.service_endpoint_type.ServiceEndpointType"
    ]
    """<p>The endpoint type of the service. </p>"""
    url_endpoint: NotRequired[
        "capo_migration_hub_refactor_spaces.types.url_endpoint_summary.UrlEndpointSummary"
    ]
    """<p>The summary of the configuration for the URL endpoint type. </p>"""
    lambda_endpoint: NotRequired[
        "capo_migration_hub_refactor_spaces.types.lambda_endpoint_summary.LambdaEndpointSummary"
    ]
    """<p>A summary of the configuration for the Lambda endpoint type. </p>"""
    state: NotRequired[
        "capo_migration_hub_refactor_spaces.types.service_state.ServiceState"
    ]
    """<p>The current state of the service. </p>"""
    tags: NotRequired["capo_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags assigned to the service. </p>"""
    error: NotRequired[
        "capo_migration_hub_refactor_spaces.types.error_response.ErrorResponse"
    ]
    """<p>Any error associated with the service resource. </p>"""
    last_updated_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the service was last updated. </p>"""
    created_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the service is created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceSummary) -> dict:
    out: dict = {}
    if "service_id" in value:
        out["ServiceId"] = value["service_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "created_by_account_id" in value:
        out["CreatedByAccountId"] = value["created_by_account_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "endpoint_type" in value:
        out["EndpointType"] = value["endpoint_type"]
    if "url_endpoint" in value:
        import capo_migration_hub_refactor_spaces.types.url_endpoint_summary

        out["UrlEndpoint"] = (
            capo_migration_hub_refactor_spaces.types.url_endpoint_summary.serialize_json(
                value["url_endpoint"]
            )
        )
    if "lambda_endpoint" in value:
        import capo_migration_hub_refactor_spaces.types.lambda_endpoint_summary

        out["LambdaEndpoint"] = (
            capo_migration_hub_refactor_spaces.types.lambda_endpoint_summary.serialize_json(
                value["lambda_endpoint"]
            )
        )
    if "state" in value:
        out["State"] = value["state"]
    if "tags" in value:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["Tags"] = capo_migration_hub_refactor_spaces.types.tag_map.serialize_json(
            value["tags"]
        )
    if "error" in value:
        import capo_migration_hub_refactor_spaces.types.error_response

        out["Error"] = (
            capo_migration_hub_refactor_spaces.types.error_response.serialize_json(
                value["error"]
            )
        )
    if "last_updated_time" in value:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["LastUpdatedTime"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    if "created_time" in value:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["CreatedTime"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["created_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceSummary:
    out: ServiceSummary = {}  # type: ignore[typeddict-item]
    if data.get("ServiceId") is not None:
        out["service_id"] = data["ServiceId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("CreatedByAccountId") is not None:
        out["created_by_account_id"] = data["CreatedByAccountId"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EnvironmentId") is not None:
        out["environment_id"] = data["EnvironmentId"]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("EndpointType") is not None:
        out["endpoint_type"] = data["EndpointType"]
    if data.get("UrlEndpoint") is not None:
        import capo_migration_hub_refactor_spaces.types.url_endpoint_summary

        out["url_endpoint"] = (
            capo_migration_hub_refactor_spaces.types.url_endpoint_summary.deserialize_json(
                data["UrlEndpoint"]
            )
        )
    if data.get("LambdaEndpoint") is not None:
        import capo_migration_hub_refactor_spaces.types.lambda_endpoint_summary

        out["lambda_endpoint"] = (
            capo_migration_hub_refactor_spaces.types.lambda_endpoint_summary.deserialize_json(
                data["LambdaEndpoint"]
            )
        )
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("Tags") is not None:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = capo_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("Error") is not None:
        import capo_migration_hub_refactor_spaces.types.error_response

        out["error"] = (
            capo_migration_hub_refactor_spaces.types.error_response.deserialize_json(
                data["Error"]
            )
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["last_updated_time"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["created_time"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["CreatedTime"]
            )
        )
    return out


def redact_sensitive(value: ServiceSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
