"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateCrossAccountAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.attachment_name
    import capo_global_accelerator.types.idempotency_token
    import capo_global_accelerator.types.principals
    import capo_global_accelerator.types.resources
    import capo_global_accelerator.types.tags


class CreateCrossAccountAttachmentRequest(TypedDict, closed=True):
    name: "capo_global_accelerator.types.attachment_name.AttachmentName"
    """<p>The name of the cross-account attachment. </p>"""
    principals: NotRequired["capo_global_accelerator.types.principals.Principals"]
    """<p>The principals to include in the cross-account attachment. A principal can be an Amazon Web Services account number or the Amazon Resource Name (ARN) for an accelerator. </p>"""
    resources: NotRequired["capo_global_accelerator.types.resources.Resources"]
    """<p>The Amazon Resource Names (ARNs) for the resources to include in the cross-account attachment. A resource can be any supported Amazon Web Services resource type for Global Accelerator or a CIDR range for a bring your own IP address (BYOIP) address pool. </p>"""
    idempotency_token: (
        "capo_global_accelerator.types.idempotency_token.IdempotencyToken"
    )
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>"""
    tags: NotRequired["capo_global_accelerator.types.tags.Tags"]
    """<p>Add tags for a cross-account attachment.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html">Tagging in Global Accelerator</a> in the <i>Global Accelerator Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCrossAccountAttachmentRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "principals" in value:
        import capo_global_accelerator.types.principals

        out["Principals"] = (
            capo_global_accelerator.types.principals.serialize_aws_json_1_1(
                value["principals"]
            )
        )
    if "resources" in value:
        import capo_global_accelerator.types.resources

        out["Resources"] = (
            capo_global_accelerator.types.resources.serialize_aws_json_1_1(
                value["resources"]
            )
        )
    out["IdempotencyToken"] = value["idempotency_token"]
    if "tags" in value:
        import capo_global_accelerator.types.tags

        out["Tags"] = capo_global_accelerator.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCrossAccountAttachmentRequest:
    out: CreateCrossAccountAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateCrossAccountAttachmentRequest.name required")
    if data.get("Principals") is not None:
        import capo_global_accelerator.types.principals

        out["principals"] = (
            capo_global_accelerator.types.principals.deserialize_aws_json_1_1(
                data["Principals"]
            )
        )
    if data.get("Resources") is not None:
        import capo_global_accelerator.types.resources

        out["resources"] = (
            capo_global_accelerator.types.resources.deserialize_aws_json_1_1(
                data["Resources"]
            )
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "CreateCrossAccountAttachmentRequest.idempotency_token required"
        )
    if data.get("Tags") is not None:
        import capo_global_accelerator.types.tags

        out["tags"] = capo_global_accelerator.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
