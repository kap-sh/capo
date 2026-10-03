"""Generated from Smithy shape ``com.amazonaws.iam#PolicyUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.id_type
    import capo_iam.types.user_name_type


class PolicyUser(TypedDict, closed=True):
    user_name: NotRequired["capo_iam.types.user_name_type.userNameType"]
    """<p>The name (friendly name, not ARN) identifying the user.</p>"""
    user_id: NotRequired["capo_iam.types.id_type.idType"]
    """<p>The stable and unique string identifying the user. For more information about IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyUser, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    if "user_id" in value:
        pairs.append((f"{key_prefix}UserId", str(value["user_id"])))


def deserialize_query(el: Element) -> PolicyUser:
    out: PolicyUser = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    return out
