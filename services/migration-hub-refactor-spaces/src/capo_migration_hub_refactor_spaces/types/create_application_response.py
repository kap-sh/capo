"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.account_id
    import capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input
    import capo_migration_hub_refactor_spaces.types.application_id
    import capo_migration_hub_refactor_spaces.types.application_name
    import capo_migration_hub_refactor_spaces.types.application_state
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.proxy_type
    import capo_migration_hub_refactor_spaces.types.resource_arn
    import capo_migration_hub_refactor_spaces.types.tag_map
    import capo_migration_hub_refactor_spaces.types.timestamp
    import capo_migration_hub_refactor_spaces.types.vpc_id


class CreateApplicationResponse(TypedDict, closed=True):
    name: NotRequired[
        "capo_migration_hub_refactor_spaces.types.application_name.ApplicationName"
    ]
    """<p>The name of the application.</p>"""
    arn: NotRequired[
        "capo_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the application. The format for this ARN is <code>arn:aws:refactor-spaces:<i>region</i>:<i>account-id</i>:<i>resource-type/resource-id</i> </code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    owner_account_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the application owner (which is always the same as the environment owner account ID).</p>"""
    created_by_account_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of application creator.</p>"""
    application_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p>The unique identifier of the application.</p>"""
    environment_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the environment in which the application is created.</p>"""
    vpc_id: NotRequired["capo_migration_hub_refactor_spaces.types.vpc_id.VpcId"]
    """<p>The ID of the Amazon VPC. </p>"""
    proxy_type: NotRequired[
        "capo_migration_hub_refactor_spaces.types.proxy_type.ProxyType"
    ]
    """<p>The proxy type of the proxy created within the application. </p>"""
    api_gateway_proxy: NotRequired[
        "capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input.ApiGatewayProxyInput"
    ]
    """<p>A wrapper object holding the API Gateway endpoint type and stage name for the proxy. </p>"""
    state: NotRequired[
        "capo_migration_hub_refactor_spaces.types.application_state.ApplicationState"
    ]
    """<p>The current state of the application. </p>"""
    tags: NotRequired["capo_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags assigned to the application. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair. </p>"""
    last_updated_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the application was last updated. </p>"""
    created_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the application is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "created_by_account_id" in value:
        out["CreatedByAccountId"] = value["created_by_account_id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "proxy_type" in value:
        out["ProxyType"] = value["proxy_type"]
    if "api_gateway_proxy" in value:
        import capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input

        out["ApiGatewayProxy"] = (
            capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input.serialize_json(
                value["api_gateway_proxy"]
            )
        )
    if "state" in value:
        out["State"] = value["state"]
    if "tags" in value:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["Tags"] = capo_migration_hub_refactor_spaces.types.tag_map.serialize_json(
            value["tags"]
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


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("CreatedByAccountId") is not None:
        out["created_by_account_id"] = data["CreatedByAccountId"]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("EnvironmentId") is not None:
        out["environment_id"] = data["EnvironmentId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("ProxyType") is not None:
        out["proxy_type"] = data["ProxyType"]
    if data.get("ApiGatewayProxy") is not None:
        import capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input

        out["api_gateway_proxy"] = (
            capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input.deserialize_json(
                data["ApiGatewayProxy"]
            )
        )
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("Tags") is not None:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = capo_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
            data["Tags"]
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
