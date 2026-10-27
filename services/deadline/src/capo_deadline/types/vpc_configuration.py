"""Generated from Smithy shape ``com.amazonaws.deadline#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.vpc_resource_configuration_arns


class VpcConfiguration(TypedDict, closed=True):
    resource_configuration_arns: NotRequired[
        "capo_deadline.types.vpc_resource_configuration_arns.VpcResourceConfigurationArns"
    ]
    """The ARNs of the VPC Lattice resource configurations attached to the fleet."""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfiguration) -> dict:
    out: dict = {}
    if "resource_configuration_arns" in value:
        import capo_deadline.types.vpc_resource_configuration_arns

        out["resourceConfigurationArns"] = (
            capo_deadline.types.vpc_resource_configuration_arns.serialize_json(
                value["resource_configuration_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("resourceConfigurationArns") is not None:
        import capo_deadline.types.vpc_resource_configuration_arns

        out["resource_configuration_arns"] = (
            capo_deadline.types.vpc_resource_configuration_arns.deserialize_json(
                data["resourceConfigurationArns"]
            )
        )
    return out
