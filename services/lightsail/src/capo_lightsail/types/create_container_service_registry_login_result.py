"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateContainerServiceRegistryLoginResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_registry_login


class CreateContainerServiceRegistryLoginResult(TypedDict, closed=True):
    registry_login: NotRequired[
        "capo_lightsail.types.container_service_registry_login.ContainerServiceRegistryLogin"
    ]
    """<p>An object that describes the log in information for the container service registry of your Lightsail account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerServiceRegistryLoginResult) -> dict:
    out: dict = {}
    if "registry_login" in value:
        import capo_lightsail.types.container_service_registry_login

        out["registryLogin"] = (
            capo_lightsail.types.container_service_registry_login.serialize_aws_json_1_1(
                value["registry_login"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerServiceRegistryLoginResult:
    out: CreateContainerServiceRegistryLoginResult = {}  # type: ignore[typeddict-item]
    if data.get("registryLogin") is not None:
        import capo_lightsail.types.container_service_registry_login

        out["registry_login"] = (
            capo_lightsail.types.container_service_registry_login.deserialize_aws_json_1_1(
                data["registryLogin"]
            )
        )
    return out


def redact_sensitive(
    value: CreateContainerServiceRegistryLoginResult,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "registry_login" in value:
        import capo_lightsail.types.container_service_registry_login

        out["registry_login"] = (
            capo_lightsail.types.container_service_registry_login.redact_sensitive(
                value["registry_login"]
            )
        )
    return out
