"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxClusterDatabasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.client_token_string
    import capo_finspace.types.kx_cluster_name
    import capo_finspace.types.kx_database_configurations
    import capo_finspace.types.kx_deployment_configuration
    import capo_finspace.types.kx_environment_id


class UpdateKxClusterDatabasesRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>The unique identifier of a kdb environment.</p>"""
    cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName"
    """<p>A unique name for the cluster that you want to modify.</p>"""
    client_token: NotRequired[
        "capo_finspace.types.client_token_string.ClientTokenString"
    ]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    databases: "capo_finspace.types.kx_database_configurations.KxDatabaseConfigurations"
    """<p> The structure of databases mounted on the cluster.</p>"""
    deployment_configuration: NotRequired[
        "capo_finspace.types.kx_deployment_configuration.KxDeploymentConfiguration"
    ]
    """<p> The configuration that allows you to choose how you want to update the databases on a cluster. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxClusterDatabasesRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_finspace.types.kx_database_configurations

    out["databases"] = capo_finspace.types.kx_database_configurations.serialize_json(
        value["databases"]
    )
    if "deployment_configuration" in value:
        import capo_finspace.types.kx_deployment_configuration

        out["deploymentConfiguration"] = (
            capo_finspace.types.kx_deployment_configuration.serialize_json(
                value["deployment_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKxClusterDatabasesRequest:
    out: UpdateKxClusterDatabasesRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("databases") is not None:
        import capo_finspace.types.kx_database_configurations

        out["databases"] = (
            capo_finspace.types.kx_database_configurations.deserialize_json(
                data["databases"]
            )
        )
    else:
        out["databases"] = []
    if data.get("deploymentConfiguration") is not None:
        import capo_finspace.types.kx_deployment_configuration

        out["deployment_configuration"] = (
            capo_finspace.types.kx_deployment_configuration.deserialize_json(
                data["deploymentConfiguration"]
            )
        )
    return out
