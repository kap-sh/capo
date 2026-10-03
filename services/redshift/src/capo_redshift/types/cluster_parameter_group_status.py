"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterParameterGroupStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_parameter_status_list
    import capo_redshift.types.string


class ClusterParameterGroupStatus(TypedDict, closed=True):
    parameter_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the cluster parameter group.</p>"""
    parameter_apply_status: NotRequired["capo_redshift.types.string.String"]
    """<p>The status of parameter updates.</p>"""
    cluster_parameter_status_list: NotRequired[
        "capo_redshift.types.cluster_parameter_status_list.ClusterParameterStatusList"
    ]
    """<p>The list of parameter statuses.</p> <p> For more information about parameters and parameter groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Amazon Redshift Parameter Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterParameterGroupStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}ParameterGroupName", str(value["parameter_group_name"]))
        )
    if "parameter_apply_status" in value:
        pairs.append(
            (f"{key_prefix}ParameterApplyStatus", str(value["parameter_apply_status"]))
        )
    if "cluster_parameter_status_list" in value:
        import capo_redshift.types.cluster_parameter_status_list

        capo_redshift.types.cluster_parameter_status_list.serialize_query(
            value["cluster_parameter_status_list"],
            pairs,
            f"{key_prefix}ClusterParameterStatusList",
        )


def deserialize_query(el: Element) -> ClusterParameterGroupStatus:
    out: ClusterParameterGroupStatus = {}  # type: ignore[typeddict-item]
    child_parameter_group_name = el.find("ParameterGroupName")
    if child_parameter_group_name is not None:
        out["parameter_group_name"] = str(child_parameter_group_name.text or "")
    child_parameter_apply_status = el.find("ParameterApplyStatus")
    if child_parameter_apply_status is not None:
        out["parameter_apply_status"] = str(child_parameter_apply_status.text or "")
    child_cluster_parameter_status_list = el.find("ClusterParameterStatusList")
    if child_cluster_parameter_status_list is not None:
        import capo_redshift.types.cluster_parameter_status_list

        out["cluster_parameter_status_list"] = (
            capo_redshift.types.cluster_parameter_status_list.deserialize_query(
                child_cluster_parameter_status_list
            )
        )
    return out
