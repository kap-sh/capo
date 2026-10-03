"""Generated from Smithy shape ``com.amazonaws.iam#PolicyRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.id_type
    import capo_iam.types.role_name_type


class PolicyRole(TypedDict, closed=True):
    role_name: NotRequired["capo_iam.types.role_name_type.roleNameType"]
    """<p>The name (friendly name, not ARN) identifying the role.</p>"""
    role_id: NotRequired["capo_iam.types.id_type.idType"]
    """<p>The stable and unique string identifying the role. For more information about IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "role_name" in value:
        pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))
    if "role_id" in value:
        pairs.append((f"{key_prefix}RoleId", str(value["role_id"])))


def deserialize_query(el: Element) -> PolicyRole:
    out: PolicyRole = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    child_role_id = el.find("RoleId")
    if child_role_id is not None:
        out["role_id"] = str(child_role_id.text or "")
    return out
