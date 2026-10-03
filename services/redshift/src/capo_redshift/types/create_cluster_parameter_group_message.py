"""Generated from Smithy shape ``com.amazonaws.redshift#CreateClusterParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.tag_list


class CreateClusterParameterGroupMessage(TypedDict, closed=True):
    parameter_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the cluster parameter group.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters or hyphens</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique withing your Amazon Web Services account.</p> </li> </ul> <note> <p>This value is stored as a lower-case string.</p> </note>"""
    parameter_group_family: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.</p> <p>To get a list of valid parameter group family names, you can call <a>DescribeClusterParameterGroups</a>. By default, Amazon Redshift returns a list of all the parameter groups that are owned by your Amazon Web Services account, including the default parameter groups for each Amazon Redshift engine version. The parameter group family names associated with the default parameter groups provide you the valid values. For example, a valid family name is "redshift-1.0". </p>"""
    description: NotRequired["capo_redshift.types.string.String"]
    """<p>A description of the parameter group.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>A list of tag instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateClusterParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}ParameterGroupName", str(value["parameter_group_name"]))
        )
    if "parameter_group_family" in value:
        pairs.append(
            (f"{key_prefix}ParameterGroupFamily", str(value["parameter_group_family"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateClusterParameterGroupMessage:
    out: CreateClusterParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_parameter_group_name = el.find("ParameterGroupName")
    if child_parameter_group_name is not None:
        out["parameter_group_name"] = str(child_parameter_group_name.text or "")
    child_parameter_group_family = el.find("ParameterGroupFamily")
    if child_parameter_group_family is not None:
        out["parameter_group_family"] = str(child_parameter_group_family.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    return out
