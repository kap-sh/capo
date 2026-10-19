"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#InstanceUserSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.arn
    import capo_license_manager_user_subscriptions.types.identity_provider


class InstanceUserSummary(TypedDict, closed=True):
    username: "str"
    """<p>The user name from the identity provider for the user.</p>"""
    instance_id: "str"
    """<p>The ID of the EC2 instance that provides user-based subscriptions.</p>"""
    identity_provider: "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>The <code>IdentityProvider</code> resource specifies details about the identity provider.</p>"""
    status: "str"
    """<p>The status of a user associated with an EC2 instance.</p>"""
    instance_user_arn: NotRequired[
        "capo_license_manager_user_subscriptions.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the instance user.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message for users of an EC2 instance.</p>"""
    domain: NotRequired["str"]
    """<p>The domain name of the Active Directory that contains the user information for the product subscription.</p>"""
    association_date: NotRequired["str"]
    """<p>The date a user was associated with an EC2 instance.</p>"""
    disassociation_date: NotRequired["str"]
    """<p>The date a user was disassociated from an EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceUserSummary) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["InstanceId"] = value["instance_id"]
    import capo_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        capo_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    out["Status"] = value["status"]
    if "instance_user_arn" in value:
        out["InstanceUserArn"] = value["instance_user_arn"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "association_date" in value:
        out["AssociationDate"] = value["association_date"]
    if "disassociation_date" in value:
        out["DisassociationDate"] = value["disassociation_date"]
    return out


def deserialize_json(data: dict) -> InstanceUserSummary:
    out: InstanceUserSummary = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("IdentityProvider") is not None:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        import capo_license_manager_user_subscriptions.types._unknown

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types._unknown.UnknownUnionMember(
                ""
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("InstanceUserArn") is not None:
        out["instance_user_arn"] = data["InstanceUserArn"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("AssociationDate") is not None:
        out["association_date"] = data["AssociationDate"]
    if data.get("DisassociationDate") is not None:
        out["disassociation_date"] = data["DisassociationDate"]
    return out
