"""Generated from Smithy shape ``com.amazonaws.appmesh#ServiceDiscovery``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.aws_cloud_map_service_discovery
    import capo_app_mesh.types.dns_service_discovery


class _ServiceDiscovery_dns(TypedDict, closed=True):
    dns: "capo_app_mesh.types.dns_service_discovery.DnsServiceDiscovery"


class _ServiceDiscovery_awsCloudMap(TypedDict, closed=True):
    awsCloudMap: "capo_app_mesh.types.aws_cloud_map_service_discovery.AwsCloudMapServiceDiscovery"


ServiceDiscovery: TypeAlias = (
    _ServiceDiscovery_dns | _ServiceDiscovery_awsCloudMap | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ServiceDiscovery) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ServiceDiscovery: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "dns" in value:
        import capo_app_mesh.types.dns_service_discovery

        return {
            "dns": capo_app_mesh.types.dns_service_discovery.serialize_json(
                value["dns"]
            )
        }
    elif "awsCloudMap" in value:
        import capo_app_mesh.types.aws_cloud_map_service_discovery

        return {
            "awsCloudMap": capo_app_mesh.types.aws_cloud_map_service_discovery.serialize_json(
                value["awsCloudMap"]
            )
        }
    else:
        raise SerializationError("ServiceDiscovery: no variant present")


def deserialize_json(data: dict) -> ServiceDiscovery:
    if data.get("dns") is not None:
        import capo_app_mesh.types.dns_service_discovery

        return {
            "dns": capo_app_mesh.types.dns_service_discovery.deserialize_json(
                data["dns"]
            )
        }
    elif data.get("awsCloudMap") is not None:
        import capo_app_mesh.types.aws_cloud_map_service_discovery

        return {
            "awsCloudMap": capo_app_mesh.types.aws_cloud_map_service_discovery.deserialize_json(
                data["awsCloudMap"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ServiceDiscovery: no recognized variant key")
