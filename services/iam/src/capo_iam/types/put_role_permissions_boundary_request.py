"""Generated from Smithy shape ``com.amazonaws.iam#PutRolePermissionsBoundaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.role_name_type


class PutRolePermissionsBoundaryRequest(TypedDict, closed=True):
    role_name: "capo_iam.types.role_name_type.roleNameType"
    """<p>The name (friendly name, not ARN) of the IAM role for which you want to set the permissions boundary.</p>"""
    permissions_boundary: "capo_iam.types.arn_type.arnType"
    """<p>The ARN of the managed policy that is used to set the permissions boundary for the role.</p> <p>A permissions boundary policy defines the maximum permissions that identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity. To learn more, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html">Permissions boundaries for IAM entities</a> in the <i>IAM User Guide</i>.</p> <p>For more information about policy types, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types">Policy types </a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutRolePermissionsBoundaryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))
    pairs.append(
        (f"{key_prefix}PermissionsBoundary", str(value["permissions_boundary"]))
    )


def deserialize_query(el: Element) -> PutRolePermissionsBoundaryRequest:
    out: PutRolePermissionsBoundaryRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError(
            "PutRolePermissionsBoundaryRequest.role_name required"
        )
    child_permissions_boundary = el.find("PermissionsBoundary")
    if child_permissions_boundary is not None:
        out["permissions_boundary"] = str(child_permissions_boundary.text or "")
    else:
        raise DeserializationError(
            "PutRolePermissionsBoundaryRequest.permissions_boundary required"
        )
    return out
