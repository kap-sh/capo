"""Generated from Smithy shape ``com.amazonaws.iam#PolicyUsageType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

"""<p>The policy usage type that indicates whether the policy is used as a permissions policy or as the permissions boundary for an entity.</p> <p>For more information about permissions boundaries, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html">Permissions boundaries for IAM identities </a> in the <i>IAM User Guide</i>.</p>"""
PolicyUsageType: TypeAlias = Literal[
    "PermissionsPolicy",
    "PermissionsBoundary",
]


# --- awsQuery ser/de ---
def to_query_text(value: PolicyUsageType) -> str:
    return value


def from_query_text(text: str) -> PolicyUsageType:
    return cast(PolicyUsageType, text)


def serialize_query(
    value: PolicyUsageType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PolicyUsageType:
    return from_query_text(el.text or "")
