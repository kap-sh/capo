"""Generated from Smithy shape ``com.amazonaws.iam#UpdateRoleDescriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.role_description_type
    import capo_iam.types.role_name_type


class UpdateRoleDescriptionRequest(TypedDict, closed=True):
    role_name: "capo_iam.types.role_name_type.roleNameType"
    """<p>The name of the role that you want to modify.</p>"""
    description: "capo_iam.types.role_description_type.roleDescriptionType"
    """<p>The new description that you want to apply to the specified role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateRoleDescriptionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))
    pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_query(el: Element) -> UpdateRoleDescriptionRequest:
    out: UpdateRoleDescriptionRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        out["role_name"] = ""
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    else:
        out["description"] = ""
    return out
