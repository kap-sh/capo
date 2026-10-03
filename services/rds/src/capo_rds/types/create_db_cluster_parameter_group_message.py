"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.tag_list


class CreateDBClusterParameterGroupMessage(TypedDict, closed=True):
    db_cluster_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must not match the name of an existing DB cluster parameter group.</p> </li> </ul> <note> <p>This value is stored as a lowercase string.</p> </note>"""
    db_parameter_group_family: NotRequired["capo_rds.types.string.String"]
    """<p>The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.</p> <p> <b>Aurora MySQL</b> </p> <p>Example: <code>aurora-mysql5.7</code>, <code>aurora-mysql8.0</code> </p> <p> <b>Aurora PostgreSQL</b> </p> <p>Example: <code>aurora-postgresql14</code> </p> <p> <b>RDS for MySQL</b> </p> <p>Example: <code>mysql8.0</code> </p> <p> <b>RDS for PostgreSQL</b> </p> <p>Example: <code>postgres13</code> </p> <p>To list all of the available parameter group families for a DB engine, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily" --engine &lt;engine&gt;</code> </p> <p>For example, to list all of the available parameter group families for the Aurora PostgreSQL DB engine, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily" --engine aurora-postgresql</code> </p> <note> <p>The output contains duplicates.</p> </note> <p>The following are the valid DB engine values:</p> <ul> <li> <p> <code>aurora-mysql</code> </p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> </ul>"""
    description: NotRequired["capo_rds.types.string.String"]
    """<p>The description for the DB cluster parameter group.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>Tags to assign to the DB cluster parameter group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterParameterGroupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterParameterGroupName",
                str(value["db_cluster_parameter_group_name"]),
            )
        )
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{key_prefix}DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateDBClusterParameterGroupMessage:
    out: CreateDBClusterParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_parameter_group_name = el.find("DBClusterParameterGroupName")
    if child_db_cluster_parameter_group_name is not None:
        out["db_cluster_parameter_group_name"] = str(
            child_db_cluster_parameter_group_name.text or ""
        )
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
