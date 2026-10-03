"""Generated from Smithy shape ``com.amazonaws.iam#PolicyGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.group_name_type
    import capo_iam.types.id_type


class PolicyGroup(TypedDict, closed=True):
    group_name: NotRequired["capo_iam.types.group_name_type.groupNameType"]
    """<p>The name (friendly name, not ARN) identifying the group.</p>"""
    group_id: NotRequired["capo_iam.types.id_type.idType"]
    """<p>The stable and unique string identifying the group. For more information about IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))


def deserialize_query(el: Element) -> PolicyGroup:
    out: PolicyGroup = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    return out
