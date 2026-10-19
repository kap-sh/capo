"""Generated from Smithy shape ``com.amazonaws.iam#DeleteUserPermissionsBoundaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.user_name_type


class DeleteUserPermissionsBoundaryRequest(TypedDict, closed=True):
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name (friendly name, not ARN) of the IAM user from which you want to remove the permissions boundary.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteUserPermissionsBoundaryRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))


def deserialize_query(el: Element) -> DeleteUserPermissionsBoundaryRequest:
    out: DeleteUserPermissionsBoundaryRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        out["user_name"] = ""
    return out
