"""Generated from Smithy shape ``com.amazonaws.iam#Group``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.date_type
    import capo_iam.types.group_name_type
    import capo_iam.types.id_type
    import capo_iam.types.path_type


class Group(TypedDict, closed=True):
    path: "capo_iam.types.path_type.pathType"
    """<p>The path to the group. For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    group_name: "capo_iam.types.group_name_type.groupNameType"
    """<p>The friendly name that identifies the group.</p>"""
    group_id: "capo_iam.types.id_type.idType"
    """<p> The stable and unique string identifying the group. For more information about IDs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    arn: "capo_iam.types.arn_type.arnType"
    """<p> The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and how to use them in policies, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    create_date: "capo_iam.types.date_type.dateType"
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the group was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Group, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Path", str(value["path"])))
    pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    import capo_iam.types.date_type

    capo_iam.types.date_type.serialize_query(
        value["create_date"], pairs, f"{key_prefix}CreateDate"
    )


def deserialize_query(el: Element) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    else:
        raise DeserializationError("Group.path required")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    else:
        raise DeserializationError("Group.group_name required")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    else:
        raise DeserializationError("Group.group_id required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("Group.arn required")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_iam.types.date_type

        out["create_date"] = capo_iam.types.date_type.deserialize_query(
            child_create_date
        )
    else:
        raise DeserializationError("Group.create_date required")
    return out
