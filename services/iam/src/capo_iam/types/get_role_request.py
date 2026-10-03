"""Generated from Smithy shape ``com.amazonaws.iam#GetRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.role_name_type


class GetRoleRequest(TypedDict, closed=True):
    role_name: "capo_iam.types.role_name_type.roleNameType"
    """<p>The name of the IAM role to get information about.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))


def deserialize_query(el: Element) -> GetRoleRequest:
    out: GetRoleRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError("GetRoleRequest.role_name required")
    return out
