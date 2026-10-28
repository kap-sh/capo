"""Generated from Smithy shape ``com.amazonaws.iam#PolicyIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError, SerializationError
from capo_iam.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.inline_policy_identifier_type
    import capo_iam.types.policy_identifier_policy_type


class PolicyIdentifierPolicyTypeMember(TypedDict, closed=True):
    PolicyType: (
        "capo_iam.types.policy_identifier_policy_type.PolicyIdentifierPolicyType"
    )


class PolicyIdentifierPolicyArnMember(TypedDict, closed=True):
    PolicyArn: "capo_iam.types.arn_type.arnType"


class PolicyIdentifierInlinePolicyIdentifierMember(TypedDict, closed=True):
    InlinePolicyIdentifier: (
        "capo_iam.types.inline_policy_identifier_type.InlinePolicyIdentifierType"
    )


PolicyIdentifier: TypeAlias = (
    PolicyIdentifierPolicyTypeMember
    | PolicyIdentifierPolicyArnMember
    | PolicyIdentifierInlinePolicyIdentifierMember
    | UnknownUnionMember
)


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyIdentifier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "$unknown" in value:
        raise SerializationError(
            f"PolicyIdentifier: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PolicyType" in value:
        import capo_iam.types.policy_identifier_policy_type

        capo_iam.types.policy_identifier_policy_type.serialize_query(
            value["PolicyType"], pairs, f"{prefix}.PolicyType"
        )
    elif "PolicyArn" in value:
        pairs.append((f"{prefix}.PolicyArn", str(value["PolicyArn"])))
    elif "InlinePolicyIdentifier" in value:
        import capo_iam.types.inline_policy_identifier_type

        capo_iam.types.inline_policy_identifier_type.serialize_query(
            value["InlinePolicyIdentifier"], pairs, f"{prefix}.InlinePolicyIdentifier"
        )
    else:
        raise SerializationError("PolicyIdentifier: no variant present")


def deserialize_query(el: Element) -> PolicyIdentifier:
    for child in el:
        if child.tag == "PolicyType":
            import capo_iam.types.policy_identifier_policy_type

            return {
                "PolicyType": capo_iam.types.policy_identifier_policy_type.deserialize_query(
                    child
                )
            }
        elif child.tag == "PolicyArn":
            return {"PolicyArn": str(child.text or "")}
        elif child.tag == "InlinePolicyIdentifier":
            import capo_iam.types.inline_policy_identifier_type

            return {
                "InlinePolicyIdentifier": capo_iam.types.inline_policy_identifier_type.deserialize_query(
                    child
                )
            }
        else:
            return {"$unknown": {"name": child.tag}}
    raise DeserializationError("PolicyIdentifier: no recognized variant element")
