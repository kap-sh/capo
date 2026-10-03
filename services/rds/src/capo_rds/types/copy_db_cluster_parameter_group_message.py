"""Generated from Smithy shape ``com.amazonaws.rds#CopyDBClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.tag_list


class CopyDBClusterParameterGroupMessage(TypedDict, closed=True):
    source_db_cluster_parameter_group_identifier: NotRequired[
        "capo_rds.types.string.String"
    ]
    """<p>The identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group. For information about creating an ARN, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing"> Constructing an ARN for Amazon RDS</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid DB cluster parameter group.</p> </li> </ul>"""
    target_db_cluster_parameter_group_identifier: NotRequired[
        "capo_rds.types.string.String"
    ]
    """<p>The identifier for the copied DB cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Can't be null, empty, or blank</p> </li> <li> <p>Must contain from 1 to 255 letters, numbers, or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens</p> </li> </ul> <p>Example: <code>my-cluster-param-group1</code> </p>"""
    target_db_cluster_parameter_group_description: NotRequired[
        "capo_rds.types.string.String"
    ]
    """<p>A description for the copied DB cluster parameter group.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CopyDBClusterParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_db_cluster_parameter_group_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceDBClusterParameterGroupIdentifier",
                str(value["source_db_cluster_parameter_group_identifier"]),
            )
        )
    if "target_db_cluster_parameter_group_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}TargetDBClusterParameterGroupIdentifier",
                str(value["target_db_cluster_parameter_group_identifier"]),
            )
        )
    if "target_db_cluster_parameter_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}TargetDBClusterParameterGroupDescription",
                str(value["target_db_cluster_parameter_group_description"]),
            )
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CopyDBClusterParameterGroupMessage:
    out: CopyDBClusterParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_source_db_cluster_parameter_group_identifier = el.find(
        "SourceDBClusterParameterGroupIdentifier"
    )
    if child_source_db_cluster_parameter_group_identifier is not None:
        out["source_db_cluster_parameter_group_identifier"] = str(
            child_source_db_cluster_parameter_group_identifier.text or ""
        )
    child_target_db_cluster_parameter_group_identifier = el.find(
        "TargetDBClusterParameterGroupIdentifier"
    )
    if child_target_db_cluster_parameter_group_identifier is not None:
        out["target_db_cluster_parameter_group_identifier"] = str(
            child_target_db_cluster_parameter_group_identifier.text or ""
        )
    child_target_db_cluster_parameter_group_description = el.find(
        "TargetDBClusterParameterGroupDescription"
    )
    if child_target_db_cluster_parameter_group_description is not None:
        out["target_db_cluster_parameter_group_description"] = str(
            child_target_db_cluster_parameter_group_description.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
