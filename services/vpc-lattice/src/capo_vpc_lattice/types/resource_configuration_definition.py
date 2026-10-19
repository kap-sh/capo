"""Generated from Smithy shape ``com.amazonaws.vpclattice#ResourceConfigurationDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_vpc_lattice.errors import DeserializationError, SerializationError
from capo_vpc_lattice.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_vpc_lattice.types.arn_resource
    import capo_vpc_lattice.types.cidr_resource
    import capo_vpc_lattice.types.dns_resource
    import capo_vpc_lattice.types.ip_resource


class _ResourceConfigurationDefinition_dnsResource(TypedDict, closed=True):
    dnsResource: "capo_vpc_lattice.types.dns_resource.DnsResource"


class _ResourceConfigurationDefinition_ipResource(TypedDict, closed=True):
    ipResource: "capo_vpc_lattice.types.ip_resource.IpResource"


class _ResourceConfigurationDefinition_arnResource(TypedDict, closed=True):
    arnResource: "capo_vpc_lattice.types.arn_resource.ArnResource"


class _ResourceConfigurationDefinition_cidrResource(TypedDict, closed=True):
    cidrResource: "capo_vpc_lattice.types.cidr_resource.CidrResource"


ResourceConfigurationDefinition: TypeAlias = (
    _ResourceConfigurationDefinition_dnsResource
    | _ResourceConfigurationDefinition_ipResource
    | _ResourceConfigurationDefinition_arnResource
    | _ResourceConfigurationDefinition_cidrResource
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfigurationDefinition) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ResourceConfigurationDefinition: cannot serialize unknown variant {value.name!r}"
        )
    elif "dnsResource" in value:
        import capo_vpc_lattice.types.dns_resource

        return {
            "dnsResource": capo_vpc_lattice.types.dns_resource.serialize_json(
                value["dnsResource"]
            )
        }
    elif "ipResource" in value:
        import capo_vpc_lattice.types.ip_resource

        return {
            "ipResource": capo_vpc_lattice.types.ip_resource.serialize_json(
                value["ipResource"]
            )
        }
    elif "arnResource" in value:
        import capo_vpc_lattice.types.arn_resource

        return {
            "arnResource": capo_vpc_lattice.types.arn_resource.serialize_json(
                value["arnResource"]
            )
        }
    elif "cidrResource" in value:
        import capo_vpc_lattice.types.cidr_resource

        return {
            "cidrResource": capo_vpc_lattice.types.cidr_resource.serialize_json(
                value["cidrResource"]
            )
        }
    else:
        raise SerializationError("ResourceConfigurationDefinition: no variant present")


def deserialize_json(data: dict) -> ResourceConfigurationDefinition:
    if data.get("dnsResource") is not None:
        import capo_vpc_lattice.types.dns_resource

        return {
            "dnsResource": capo_vpc_lattice.types.dns_resource.deserialize_json(
                data["dnsResource"]
            )
        }
    elif data.get("ipResource") is not None:
        import capo_vpc_lattice.types.ip_resource

        return {
            "ipResource": capo_vpc_lattice.types.ip_resource.deserialize_json(
                data["ipResource"]
            )
        }
    elif data.get("arnResource") is not None:
        import capo_vpc_lattice.types.arn_resource

        return {
            "arnResource": capo_vpc_lattice.types.arn_resource.deserialize_json(
                data["arnResource"]
            )
        }
    elif data.get("cidrResource") is not None:
        import capo_vpc_lattice.types.cidr_resource

        return {
            "cidrResource": capo_vpc_lattice.types.cidr_resource.deserialize_json(
                data["cidrResource"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "ResourceConfigurationDefinition: no recognized variant key"
        )
