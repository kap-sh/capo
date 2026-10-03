"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_interface_type


class ClusterNetworkInterface(TypedDict, closed=True):
    interface_type: NotRequired[
        "capo_sagemaker.types.cluster_interface_type.ClusterInterfaceType"
    ]
    """<p>The type of network interface for the instance group. Valid values:</p> <ul> <li> <p> <code>efa</code> – An EFA with ENA interface, which provides both the EFA device for low-latency, high-throughput communication and the ENA device for IP networking.</p> </li> <li> <p> <code>efa-only</code> – An EFA-only interface, which provides only the EFA device capabilities without the ENA device for traditional IP networking.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html">Elastic Fabric Adapter</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNetworkInterface) -> dict:
    out: dict = {}
    if "interface_type" in value:
        import capo_sagemaker.types.cluster_interface_type

        out["InterfaceType"] = (
            capo_sagemaker.types.cluster_interface_type.serialize_aws_json_1_1(
                value["interface_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterNetworkInterface:
    out: ClusterNetworkInterface = {}  # type: ignore[typeddict-item]
    if data.get("InterfaceType") is not None:
        import capo_sagemaker.types.cluster_interface_type

        out["interface_type"] = (
            capo_sagemaker.types.cluster_interface_type.deserialize_aws_json_1_1(
                data["InterfaceType"]
            )
        )
    return out
