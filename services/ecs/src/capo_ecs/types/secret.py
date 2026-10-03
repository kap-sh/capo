"""Generated from Smithy shape ``com.amazonaws.ecs#Secret``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.string


class Secret(TypedDict, closed=True):
    name: "capo_ecs.types.string.String"
    """<p>The name of the secret.</p>"""
    value_from: "capo_ecs.types.string.String"
    """<p>The secret to expose to the container. The supported values are either the full ARN of the Secrets Manager secret or the full ARN of the parameter in the SSM Parameter Store.</p> <p>For information about the require Identity and Access Management permissions, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-secrets.html#secrets-iam">Required IAM permissions for Amazon ECS secrets</a> (for Secrets Manager) or <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-parameters.html">Required IAM permissions for Amazon ECS secrets</a> (for Systems Manager Parameter store) in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>If the SSM Parameter Store parameter exists in the same Region as the task you're launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Secret) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["valueFrom"] = value["value_from"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Secret:
    out: Secret = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Secret.name required")
    if data.get("valueFrom") is not None:
        out["value_from"] = data["valueFrom"]
    else:
        raise DeserializationError("Secret.value_from required")
    return out
