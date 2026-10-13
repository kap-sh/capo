"""Generated from Smithy shape ``com.amazonaws.pipes#SelfManagedKafkaAccessConfigurationVpc``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.security_group_ids
    import capo_pipes.types.subnet_ids


class SelfManagedKafkaAccessConfigurationVpc(TypedDict, closed=True):
    subnets: NotRequired["capo_pipes.types.subnet_ids.SubnetIds"]
    """<p>Specifies the subnets associated with the stream. These subnets must all be in the same VPC. You can specify as many as 16 subnets.</p>"""
    security_group: NotRequired["capo_pipes.types.security_group_ids.SecurityGroupIds"]
    """<p>Specifies the security groups associated with the stream. These security groups must all be in the same VPC. You can specify as many as five security groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedKafkaAccessConfigurationVpc) -> dict:
    out: dict = {}
    if "subnets" in value:
        import capo_pipes.types.subnet_ids

        out["Subnets"] = capo_pipes.types.subnet_ids.serialize_json(value["subnets"])
    if "security_group" in value:
        import capo_pipes.types.security_group_ids

        out["SecurityGroup"] = capo_pipes.types.security_group_ids.serialize_json(
            value["security_group"]
        )
    return out


def deserialize_json(data: dict) -> SelfManagedKafkaAccessConfigurationVpc:
    out: SelfManagedKafkaAccessConfigurationVpc = {}  # type: ignore[typeddict-item]
    if data.get("Subnets") is not None:
        import capo_pipes.types.subnet_ids

        out["subnets"] = capo_pipes.types.subnet_ids.deserialize_json(data["Subnets"])
    if data.get("SecurityGroup") is not None:
        import capo_pipes.types.security_group_ids

        out["security_group"] = capo_pipes.types.security_group_ids.deserialize_json(
            data["SecurityGroup"]
        )
    return out


def redact_sensitive(value: SelfManagedKafkaAccessConfigurationVpc) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "subnets" in value:
        import capo_pipes.types.subnet_ids

        out["subnets"] = capo_pipes.types.subnet_ids.redact_sensitive(value["subnets"])
    if "security_group" in value:
        import capo_pipes.types.security_group_ids

        out["security_group"] = capo_pipes.types.security_group_ids.redact_sensitive(
            value["security_group"]
        )
    return out
