"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateSubdomainAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.string
    import capo_lightsail.types.subdomain_association_action


class UpdateSubdomainAssociationRequest(TypedDict, closed=True):
    subdomain_name: "capo_lightsail.types.string.string"
    """<p>The subdomain to update (for example, <code>mysite</code> or <code>blog.mysite</code>), not its web address.</p>"""
    action: (
        "capo_lightsail.types.subdomain_association_action.SubdomainAssociationAction"
    )
    """<p>The association change to make.</p> <p>The following actions are possible:</p> <ul> <li> <p> <code>ASSOCIATE</code> – Associates the subdomain with the resource that you specify in the <code>targetResourceArn</code> parameter. The subdomain must be in the <code>UNATTACHED</code> state.</p> </li> <li> <p> <code>DISASSOCIATE</code> – Disassociates the subdomain from its current resource. The subdomain must be in the <code>ATTACHED</code> state.</p> </li> <li> <p> <code>TRANSFER</code> – Moves the subdomain from its current resource to the resource that you specify in the <code>targetResourceArn</code> parameter. The subdomain must be in the <code>ATTACHED</code> state. You can transfer each subdomain only once in a 24-hour period.</p> </li> </ul>"""
    target_resource_arn: NotRequired["capo_lightsail.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the resource to associate the subdomain with. The resource must be in your account.</p> <p>This parameter is required when the <code>action</code> is <code>ASSOCIATE</code> or <code>TRANSFER</code>. It's ignored when the <code>action</code> is <code>DISASSOCIATE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSubdomainAssociationRequest) -> dict:
    out: dict = {}
    out["subdomainName"] = value["subdomain_name"]
    import capo_lightsail.types.subdomain_association_action

    out["action"] = (
        capo_lightsail.types.subdomain_association_action.serialize_aws_json_1_1(
            value["action"]
        )
    )
    if "target_resource_arn" in value:
        out["targetResourceArn"] = value["target_resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSubdomainAssociationRequest:
    out: UpdateSubdomainAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("subdomainName") is not None:
        out["subdomain_name"] = data["subdomainName"]
    else:
        out["subdomain_name"] = ""
    if data.get("action") is not None:
        import capo_lightsail.types.subdomain_association_action

        out["action"] = (
            capo_lightsail.types.subdomain_association_action.deserialize_aws_json_1_1(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_lightsail.types.subdomain_association_action.SubdomainAssociationAction",
            "",
        )
    if data.get("targetResourceArn") is not None:
        out["target_resource_arn"] = data["targetResourceArn"]
    return out
