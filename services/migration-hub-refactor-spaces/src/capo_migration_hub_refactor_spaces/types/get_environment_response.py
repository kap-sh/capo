"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#GetEnvironmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.account_id
    import capo_migration_hub_refactor_spaces.types.description
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.environment_name
    import capo_migration_hub_refactor_spaces.types.environment_state
    import capo_migration_hub_refactor_spaces.types.error_response
    import capo_migration_hub_refactor_spaces.types.network_fabric_type
    import capo_migration_hub_refactor_spaces.types.resource_arn
    import capo_migration_hub_refactor_spaces.types.tag_map
    import capo_migration_hub_refactor_spaces.types.timestamp
    import capo_migration_hub_refactor_spaces.types.transit_gateway_id


class GetEnvironmentResponse(TypedDict, closed=True):
    name: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment.</p>"""
    arn: NotRequired[
        "capo_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the environment.</p>"""
    description: NotRequired[
        "capo_migration_hub_refactor_spaces.types.description.Description"
    ]
    """<p>The description of the environment. </p>"""
    environment_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    ]
    """<p>The unique identifier of the environment. </p>"""
    network_fabric_type: NotRequired[
        "capo_migration_hub_refactor_spaces.types.network_fabric_type.NetworkFabricType"
    ]
    """<p>The network fabric type of the environment. </p>"""
    owner_account_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.account_id.AccountId"
    ]
    """<p>The Amazon Web Services account ID of the environment owner.</p>"""
    transit_gateway_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the Transit Gateway set up by the environment, if applicable.</p>"""
    state: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_state.EnvironmentState"
    ]
    """<p>The current state of the environment. </p>"""
    tags: NotRequired["capo_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags to assign to the environment. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair. </p>"""
    error: NotRequired[
        "capo_migration_hub_refactor_spaces.types.error_response.ErrorResponse"
    ]
    """<p>Any error associated with the environment resource. </p>"""
    last_updated_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the environment was last updated. </p>"""
    created_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the environment is created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "network_fabric_type" in value:
        out["NetworkFabricType"] = value["network_fabric_type"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "transit_gateway_id" in value:
        out["TransitGatewayId"] = value["transit_gateway_id"]
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


def deserialize_json(data: dict) -> GetEnvironmentResponse:
    out: GetEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EnvironmentId") is not None:
        out["environment_id"] = data["EnvironmentId"]
    if data.get("NetworkFabricType") is not None:
        out["network_fabric_type"] = data["NetworkFabricType"]
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("TransitGatewayId") is not None:
        out["transit_gateway_id"] = data["TransitGatewayId"]
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


def redact_sensitive(value: GetEnvironmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
