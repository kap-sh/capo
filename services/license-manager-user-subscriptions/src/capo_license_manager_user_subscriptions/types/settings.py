"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.security_group
    import capo_license_manager_user_subscriptions.types.subnets


class Settings(TypedDict, closed=True):
    subnets: "capo_license_manager_user_subscriptions.types.subnets.Subnets"
    """<p>The subnets defined for the registered identity provider.</p>"""
    security_group_id: (
        "capo_license_manager_user_subscriptions.types.security_group.SecurityGroup"
    )
    """<p>A security group ID that allows inbound TCP port 1688 communication between resources in your VPC and the VPC endpoint for activation servers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Settings) -> dict:
    out: dict = {}
    import capo_license_manager_user_subscriptions.types.subnets

    out["Subnets"] = (
        capo_license_manager_user_subscriptions.types.subnets.serialize_json(
            value["subnets"]
        )
    )
    out["SecurityGroupId"] = value["security_group_id"]
    return out


def deserialize_json(data: dict) -> Settings:
    out: Settings = {}  # type: ignore[typeddict-item]
    if data.get("Subnets") is not None:
        import capo_license_manager_user_subscriptions.types.subnets

        out["subnets"] = (
            capo_license_manager_user_subscriptions.types.subnets.deserialize_json(
                data["Subnets"]
            )
        )
    else:
        out["subnets"] = []
    if data.get("SecurityGroupId") is not None:
        out["security_group_id"] = data["SecurityGroupId"]
    else:
        out["security_group_id"] = ""
    return out
