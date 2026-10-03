"""Generated from Smithy shape ``com.amazonaws.iam#PolicyGrantingServiceAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.entity_name_type
    import capo_iam.types.policy_name_type
    import capo_iam.types.policy_owner_entity_type
    import capo_iam.types.policy_type


class PolicyGrantingServiceAccess(TypedDict, closed=True):
    policy_name: "capo_iam.types.policy_name_type.policyNameType"
    """<p>The policy name.</p>"""
    policy_type: "capo_iam.types.policy_type.policyType"
    """<p>The policy type. For more information about these policy types, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html">Managed policies and inline policies</a> in the <i>IAM User Guide</i>.</p>"""
    policy_arn: NotRequired["capo_iam.types.arn_type.arnType"]
    entity_type: NotRequired[
        "capo_iam.types.policy_owner_entity_type.policyOwnerEntityType"
    ]
    """<p>The type of entity (user or role) that used the policy to access the service to which the inline policy is attached.</p> <p>This field is null for managed policies. For more information about these policy types, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html">Managed policies and inline policies</a> in the <i>IAM User Guide</i>.</p>"""
    entity_name: NotRequired["capo_iam.types.entity_name_type.entityNameType"]
    """<p>The name of the entity (user or role) to which the inline policy is attached.</p> <p>This field is null for managed policies. For more information about these policy types, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html">Managed policies and inline policies</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyGrantingServiceAccess, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))
    import capo_iam.types.policy_type

    capo_iam.types.policy_type.serialize_query(
        value["policy_type"], pairs, f"{key_prefix}PolicyType"
    )
    if "policy_arn" in value:
        pairs.append((f"{key_prefix}PolicyArn", str(value["policy_arn"])))
    if "entity_type" in value:
        import capo_iam.types.policy_owner_entity_type

        capo_iam.types.policy_owner_entity_type.serialize_query(
            value["entity_type"], pairs, f"{key_prefix}EntityType"
        )
    if "entity_name" in value:
        pairs.append((f"{key_prefix}EntityName", str(value["entity_name"])))


def deserialize_query(el: Element) -> PolicyGrantingServiceAccess:
    out: PolicyGrantingServiceAccess = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        raise DeserializationError("PolicyGrantingServiceAccess.policy_name required")
    child_policy_type = el.find("PolicyType")
    if child_policy_type is not None:
        import capo_iam.types.policy_type

        out["policy_type"] = capo_iam.types.policy_type.deserialize_query(
            child_policy_type
        )
    else:
        raise DeserializationError("PolicyGrantingServiceAccess.policy_type required")
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    child_entity_type = el.find("EntityType")
    if child_entity_type is not None:
        import capo_iam.types.policy_owner_entity_type

        out["entity_type"] = capo_iam.types.policy_owner_entity_type.deserialize_query(
            child_entity_type
        )
    child_entity_name = el.find("EntityName")
    if child_entity_name is not None:
        out["entity_name"] = str(child_entity_name.text or "")
    return out
