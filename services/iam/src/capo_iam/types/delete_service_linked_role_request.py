"""Generated from Smithy shape ``com.amazonaws.iam#DeleteServiceLinkedRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.role_name_type


class DeleteServiceLinkedRoleRequest(TypedDict, closed=True):
    role_name: "capo_iam.types.role_name_type.roleNameType"
    """<p>The name of the service-linked role to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteServiceLinkedRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))


def deserialize_query(el: Element) -> DeleteServiceLinkedRoleRequest:
    out: DeleteServiceLinkedRoleRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        out["role_name"] = ""
    return out
