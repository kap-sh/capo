"""Generated from Smithy shape ``com.amazonaws.redshift#NodeConfigurationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.double_optional
    import capo_redshift.types.integer
    import capo_redshift.types.mode
    import capo_redshift.types.string


class NodeConfigurationOption(TypedDict, closed=True):
    node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The node type, such as, "ra3.4xlarge".</p>"""
    number_of_nodes: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The number of nodes.</p>"""
    estimated_disk_utilization_percent: NotRequired[
        "capo_redshift.types.double_optional.DoubleOptional"
    ]
    """<p>The estimated disk utilizaton percentage.</p>"""
    mode: NotRequired["capo_redshift.types.mode.Mode"]
    """<p>The category of the node configuration recommendation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeConfigurationOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "node_type" in value:
        pairs.append((f"{key_prefix}NodeType", str(value["node_type"])))
    if "number_of_nodes" in value:
        pairs.append((f"{key_prefix}NumberOfNodes", str(value["number_of_nodes"])))
    if "estimated_disk_utilization_percent" in value:
        pairs.append(
            (
                f"{key_prefix}EstimatedDiskUtilizationPercent",
                (
                    "NaN"
                    if value["estimated_disk_utilization_percent"]
                    != value["estimated_disk_utilization_percent"]
                    else "Infinity"
                    if value["estimated_disk_utilization_percent"] == float("inf")
                    else "-Infinity"
                    if value["estimated_disk_utilization_percent"] == float("-inf")
                    else str(value["estimated_disk_utilization_percent"])
                ),
            )
        )
    if "mode" in value:
        import capo_redshift.types.mode

        capo_redshift.types.mode.serialize_query(
            value["mode"], pairs, f"{key_prefix}Mode"
        )


def deserialize_query(el: Element) -> NodeConfigurationOption:
    out: NodeConfigurationOption = {}  # type: ignore[typeddict-item]
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_number_of_nodes = el.find("NumberOfNodes")
    if child_number_of_nodes is not None:
        out["number_of_nodes"] = int(child_number_of_nodes.text or "")
    child_estimated_disk_utilization_percent = el.find(
        "EstimatedDiskUtilizationPercent"
    )
    if child_estimated_disk_utilization_percent is not None:
        out["estimated_disk_utilization_percent"] = float(
            child_estimated_disk_utilization_percent.text or ""
        )
    child_mode = el.find("Mode")
    if child_mode is not None:
        import capo_redshift.types.mode

        out["mode"] = capo_redshift.types.mode.deserialize_query(child_mode)
    return out
