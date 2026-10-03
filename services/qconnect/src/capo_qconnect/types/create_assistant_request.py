"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAssistantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.assistant_type
    import capo_qconnect.types.client_token
    import capo_qconnect.types.description
    import capo_qconnect.types.name
    import capo_qconnect.types.server_side_encryption_configuration
    import capo_qconnect.types.tags


class CreateAssistantRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the assistant.</p>"""
    type: "capo_qconnect.types.assistant_type.AssistantType"
    """<p>The type of assistant.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the assistant.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>The configuration information for the customer managed key used for encryption. </p> <p>The customer managed key must have a policy that allows <code>kms:CreateGrant</code>, <code> kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect. To use Amazon Q in Connect with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html">Enable Amazon Q in Connect for your instance</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssistantRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    if "server_side_encryption_configuration" in value:
        import capo_qconnect.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            capo_qconnect.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAssistantRequest:
    out: CreateAssistantRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssistantRequest.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateAssistantRequest.type required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    if data.get("serverSideEncryptionConfiguration") is not None:
        import capo_qconnect.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_qconnect.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    return out
