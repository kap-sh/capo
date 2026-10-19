"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#UpdateSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.security_group
    import capo_license_manager_user_subscriptions.types.subnets


class UpdateSettings(TypedDict, closed=True):
    add_subnets: "capo_license_manager_user_subscriptions.types.subnets.Subnets"
    """<p>The ID of one or more subnets in which License Manager will create a VPC endpoint for products that require connectivity to activation servers.</p>"""
    remove_subnets: "capo_license_manager_user_subscriptions.types.subnets.Subnets"
    """<p>The ID of one or more subnets to remove.</p>"""
    security_group_id: NotRequired[
        "capo_license_manager_user_subscriptions.types.security_group.SecurityGroup"
    ]
    """<p>A security group ID that allows inbound TCP port 1688 communication between resources in your VPC and the VPC endpoints for activation servers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSettings) -> dict:
    out: dict = {}
    import capo_license_manager_user_subscriptions.types.subnets

    out["AddSubnets"] = (
        capo_license_manager_user_subscriptions.types.subnets.serialize_json(
            value["add_subnets"]
        )
    )
    import capo_license_manager_user_subscriptions.types.subnets

    out["RemoveSubnets"] = (
        capo_license_manager_user_subscriptions.types.subnets.serialize_json(
            value["remove_subnets"]
        )
    )
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    return out


def deserialize_json(data: dict) -> UpdateSettings:
    out: UpdateSettings = {}  # type: ignore[typeddict-item]
    if data.get("AddSubnets") is not None:
        import capo_license_manager_user_subscriptions.types.subnets

        out["add_subnets"] = (
            capo_license_manager_user_subscriptions.types.subnets.deserialize_json(
                data["AddSubnets"]
            )
        )
    else:
        out["add_subnets"] = []
    if data.get("RemoveSubnets") is not None:
        import capo_license_manager_user_subscriptions.types.subnets

        out["remove_subnets"] = (
            capo_license_manager_user_subscriptions.types.subnets.deserialize_json(
                data["RemoveSubnets"]
            )
        )
    else:
        out["remove_subnets"] = []
    if data.get("SecurityGroupId") is not None:
        out["security_group_id"] = data["SecurityGroupId"]
    return out
