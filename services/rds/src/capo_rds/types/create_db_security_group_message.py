"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBSecurityGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.tag_list


class CreateDBSecurityGroupMessage(TypedDict, closed=True):
    db_security_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name for the DB security group. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> <li> <p>Must not be "Default"</p> </li> </ul> <p>Example: <code>mysecuritygroup</code> </p>"""
    db_security_group_description: NotRequired["capo_rds.types.string.String"]
    """<p>The description for the DB security group.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>Tags to assign to the DB security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBSecurityGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_security_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSecurityGroupName", str(value["db_security_group_name"]))
        )
    if "db_security_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}DBSecurityGroupDescription",
                str(value["db_security_group_description"]),
            )
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateDBSecurityGroupMessage:
    out: CreateDBSecurityGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_security_group_name = el.find("DBSecurityGroupName")
    if child_db_security_group_name is not None:
        out["db_security_group_name"] = str(child_db_security_group_name.text or "")
    child_db_security_group_description = el.find("DBSecurityGroupDescription")
    if child_db_security_group_description is not None:
        out["db_security_group_description"] = str(
            child_db_security_group_description.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
