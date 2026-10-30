"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateConfigurationInheritance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.inheritance_mode


class UpdateConfigurationInheritance(TypedDict, closed=True):
    ec2_configuration: NotRequired[
        "capo_inspector2.types.inheritance_mode.InheritanceMode"
    ]
    """<p>The inheritance mode for Amazon EC2 scan configuration. Set to <code>INHERIT_FROM_ADMIN</code> to reset the member account's Amazon EC2 scan configuration to inherit from the delegated administrator. If omitted, the member account's existing Amazon EC2 scan configuration is not changed.</p>"""
    ecr_configuration: NotRequired[
        "capo_inspector2.types.inheritance_mode.InheritanceMode"
    ]
    """<p>The inheritance mode for Amazon ECR scan configuration. Set to <code>INHERIT_FROM_ADMIN</code> to reset the member account's Amazon ECR scan configuration to inherit from the delegated administrator. If omitted, the member account's existing Amazon ECR scan configuration is not changed.</p>"""
    ami_configuration: NotRequired[
        "capo_inspector2.types.inheritance_mode.InheritanceMode"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationInheritance) -> dict:
    out: dict = {}
    if "ec2_configuration" in value:
        out["ec2Configuration"] = value["ec2_configuration"]
    if "ecr_configuration" in value:
        out["ecrConfiguration"] = value["ecr_configuration"]
    if "ami_configuration" in value:
        out["amiConfiguration"] = value["ami_configuration"]
    return out


def deserialize_json(data: dict) -> UpdateConfigurationInheritance:
    out: UpdateConfigurationInheritance = {}  # type: ignore[typeddict-item]
    if data.get("ec2Configuration") is not None:
        out["ec2_configuration"] = data["ec2Configuration"]
    if data.get("ecrConfiguration") is not None:
        out["ecr_configuration"] = data["ecrConfiguration"]
    if data.get("amiConfiguration") is not None:
        out["ami_configuration"] = data["amiConfiguration"]
    return out
