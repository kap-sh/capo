"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateCrossAccountAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.attachment_name
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.principals
    import capo_global_accelerator.types.resources


class UpdateCrossAccountAttachmentRequest(TypedDict, closed=True):
    attachment_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the cross-account attachment to update.</p>"""
    name: NotRequired["capo_global_accelerator.types.attachment_name.AttachmentName"]
    """<p>The name of the cross-account attachment. </p>"""
    add_principals: NotRequired["capo_global_accelerator.types.principals.Principals"]
    """<p>The principals to add to the cross-account attachment. A principal is an account or the Amazon Resource Name (ARN) of an accelerator that the attachment gives permission to work with resources from another account. The resources are also listed in the attachment.</p> <p>To add more than one principal, separate the account numbers or accelerator ARNs, or both, with commas.</p>"""
    remove_principals: NotRequired[
        "capo_global_accelerator.types.principals.Principals"
    ]
    """<p>The principals to remove from the cross-account attachment. A principal is an account or the Amazon Resource Name (ARN) of an accelerator that the attachment gives permission to work with resources from another account. The resources are also listed in the attachment.</p> <p>To remove more than one principal, separate the account numbers or accelerator ARNs, or both, with commas.</p>"""
    add_resources: NotRequired["capo_global_accelerator.types.resources.Resources"]
    """<p>The resources to add to the cross-account attachment. A resource listed in a cross-account attachment can be used with an accelerator by the principals that are listed in the attachment.</p> <p>To add more than one resource, separate the resource ARNs with commas.</p>"""
    remove_resources: NotRequired["capo_global_accelerator.types.resources.Resources"]
    """<p>The resources to remove from the cross-account attachment. A resource listed in a cross-account attachment can be used with an accelerator by the principals that are listed in the attachment.</p> <p>To remove more than one resource, separate the resource ARNs with commas.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCrossAccountAttachmentRequest) -> dict:
    out: dict = {}
    out["AttachmentArn"] = value["attachment_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "add_principals" in value:
        import capo_global_accelerator.types.principals

        out["AddPrincipals"] = (
            capo_global_accelerator.types.principals.serialize_aws_json_1_1(
                value["add_principals"]
            )
        )
    if "remove_principals" in value:
        import capo_global_accelerator.types.principals

        out["RemovePrincipals"] = (
            capo_global_accelerator.types.principals.serialize_aws_json_1_1(
                value["remove_principals"]
            )
        )
    if "add_resources" in value:
        import capo_global_accelerator.types.resources

        out["AddResources"] = (
            capo_global_accelerator.types.resources.serialize_aws_json_1_1(
                value["add_resources"]
            )
        )
    if "remove_resources" in value:
        import capo_global_accelerator.types.resources

        out["RemoveResources"] = (
            capo_global_accelerator.types.resources.serialize_aws_json_1_1(
                value["remove_resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCrossAccountAttachmentRequest:
    out: UpdateCrossAccountAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AttachmentArn") is not None:
        out["attachment_arn"] = data["AttachmentArn"]
    else:
        out["attachment_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AddPrincipals") is not None:
        import capo_global_accelerator.types.principals

        out["add_principals"] = (
            capo_global_accelerator.types.principals.deserialize_aws_json_1_1(
                data["AddPrincipals"]
            )
        )
    if data.get("RemovePrincipals") is not None:
        import capo_global_accelerator.types.principals

        out["remove_principals"] = (
            capo_global_accelerator.types.principals.deserialize_aws_json_1_1(
                data["RemovePrincipals"]
            )
        )
    if data.get("AddResources") is not None:
        import capo_global_accelerator.types.resources

        out["add_resources"] = (
            capo_global_accelerator.types.resources.deserialize_aws_json_1_1(
                data["AddResources"]
            )
        )
    if data.get("RemoveResources") is not None:
        import capo_global_accelerator.types.resources

        out["remove_resources"] = (
            capo_global_accelerator.types.resources.deserialize_aws_json_1_1(
                data["RemoveResources"]
            )
        )
    return out
