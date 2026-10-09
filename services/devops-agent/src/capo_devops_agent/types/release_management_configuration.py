"""Generated from Smithy shape ``com.amazonaws.devopsagent#ReleaseManagementConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.display_name
    import capo_devops_agent.types.network_access_configuration


class ReleaseManagementConfiguration(TypedDict, closed=True):
    name: "capo_devops_agent.types.display_name.DisplayName"
    """<p>The name for this release management environment.</p>"""
    network_access: "capo_devops_agent.types.network_access_configuration.NetworkAccessConfiguration"
    """<p>Specifies how AWS DevOps Agent reaches your application using a Release Management Environment</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReleaseManagementConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_devops_agent.types.network_access_configuration

    out["networkAccess"] = (
        capo_devops_agent.types.network_access_configuration.serialize_json(
            value["network_access"]
        )
    )
    return out


def deserialize_json(data: dict) -> ReleaseManagementConfiguration:
    out: ReleaseManagementConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ReleaseManagementConfiguration.name required")
    if data.get("networkAccess") is not None:
        import capo_devops_agent.types.network_access_configuration

        out["network_access"] = (
            capo_devops_agent.types.network_access_configuration.deserialize_json(
                data["networkAccess"]
            )
        )
    else:
        raise DeserializationError(
            "ReleaseManagementConfiguration.network_access required"
        )
    return out
