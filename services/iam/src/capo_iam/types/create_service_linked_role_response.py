"""Generated from Smithy shape ``com.amazonaws.iam#CreateServiceLinkedRoleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.role


class CreateServiceLinkedRoleResponse(TypedDict, closed=True):
    role: NotRequired["capo_iam.types.role.Role"]
    """<p>A <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_Role.html">Role</a> object that contains details about the newly created role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateServiceLinkedRoleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "role" in value:
        import capo_iam.types.role

        capo_iam.types.role.serialize_query(value["role"], pairs, f"{key_prefix}Role")


def deserialize_query(el: Element) -> CreateServiceLinkedRoleResponse:
    out: CreateServiceLinkedRoleResponse = {}  # type: ignore[typeddict-item]
    child_role = el.find("Role")
    if child_role is not None:
        import capo_iam.types.role

        out["role"] = capo_iam.types.role.deserialize_query(child_role)
    return out
