"""Generated from Smithy shape ``com.amazonaws.wisdom#AssistantSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.arn
    import capo_wisdom.types.assistant_integration_configuration
    import capo_wisdom.types.assistant_status
    import capo_wisdom.types.assistant_type
    import capo_wisdom.types.description
    import capo_wisdom.types.name
    import capo_wisdom.types.server_side_encryption_configuration
    import capo_wisdom.types.tags
    import capo_wisdom.types.uuid


class AssistantSummary(TypedDict, closed=True):
    assistant_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the Wisdom assistant.</p>"""
    assistant_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Wisdom assistant.</p>"""
    name: "capo_wisdom.types.name.Name"
    """<p>The name of the assistant.</p>"""
    type: "capo_wisdom.types.assistant_type.AssistantType"
    """<p>The type of the assistant.</p>"""
    status: "capo_wisdom.types.assistant_status.AssistantStatus"
    """<p>The status of the assistant.</p>"""
    description: NotRequired["capo_wisdom.types.description.Description"]
    """<p>The description of the assistant.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Wisdom, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html">Enable Amazon Connect Wisdom for your instance</a>.</p>"""
    integration_configuration: NotRequired[
        "capo_wisdom.types.assistant_integration_configuration.AssistantIntegrationConfiguration"
    ]
    """<p>The configuration information for the Wisdom assistant integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssistantSummary) -> dict:
    out: dict = {}
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["status"] = value["status"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
    if "server_side_encryption_configuration" in value:
        import capo_wisdom.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            capo_wisdom.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "integration_configuration" in value:
        import capo_wisdom.types.assistant_integration_configuration

        out["integrationConfiguration"] = (
            capo_wisdom.types.assistant_integration_configuration.serialize_json(
                value["integration_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssistantSummary:
    out: AssistantSummary = {}  # type: ignore[typeddict-item]
    if data.get("assistantId") is not None:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("AssistantSummary.assistant_id required")
    if data.get("assistantArn") is not None:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("AssistantSummary.assistant_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssistantSummary.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AssistantSummary.type required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("AssistantSummary.status required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    if data.get("serverSideEncryptionConfiguration") is not None:
        import capo_wisdom.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_wisdom.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if data.get("integrationConfiguration") is not None:
        import capo_wisdom.types.assistant_integration_configuration

        out["integration_configuration"] = (
            capo_wisdom.types.assistant_integration_configuration.deserialize_json(
                data["integrationConfiguration"]
            )
        )
    return out
