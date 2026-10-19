"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderVpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_security_group_ids
    import capo_lambda.types.capacity_provider_subnet_ids


class CapacityProviderVpcConfig(TypedDict, closed=True):
    subnet_ids: (
        "capo_lambda.types.capacity_provider_subnet_ids.CapacityProviderSubnetIds"
    )
    """<p>A list of subnet IDs where the capacity provider launches compute instances.</p>"""
    security_group_ids: "capo_lambda.types.capacity_provider_security_group_ids.CapacityProviderSecurityGroupIds"
    """<p>A list of security group IDs that control network access for compute instances managed by the capacity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderVpcConfig) -> dict:
    out: dict = {}
    import capo_lambda.types.capacity_provider_subnet_ids

    out["SubnetIds"] = capo_lambda.types.capacity_provider_subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    import capo_lambda.types.capacity_provider_security_group_ids

    out["SecurityGroupIds"] = (
        capo_lambda.types.capacity_provider_security_group_ids.serialize_json(
            value["security_group_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> CapacityProviderVpcConfig:
    out: CapacityProviderVpcConfig = {}  # type: ignore[typeddict-item]
    if data.get("SubnetIds") is not None:
        import capo_lambda.types.capacity_provider_subnet_ids

        out["subnet_ids"] = (
            capo_lambda.types.capacity_provider_subnet_ids.deserialize_json(
                data["SubnetIds"]
            )
        )
    else:
        out["subnet_ids"] = []
    if data.get("SecurityGroupIds") is not None:
        import capo_lambda.types.capacity_provider_security_group_ids

        out["security_group_ids"] = (
            capo_lambda.types.capacity_provider_security_group_ids.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    return out
