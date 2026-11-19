"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceNetworkPerformanceOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.bandwidth_weighting_enum


class InstanceNetworkPerformanceOptionsRequest(TypedDict, closed=True):
    bandwidth_weighting: NotRequired[
        "capo_workspaces_instances.types.bandwidth_weighting_enum.BandwidthWeightingEnum"
    ]
    """<p>Defines bandwidth allocation strategy for network interfaces.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceNetworkPerformanceOptionsRequest) -> dict:
    out: dict = {}
    if "bandwidth_weighting" in value:
        import capo_workspaces_instances.types.bandwidth_weighting_enum

        out["BandwidthWeighting"] = (
            capo_workspaces_instances.types.bandwidth_weighting_enum.serialize_aws_json_1_0(
                value["bandwidth_weighting"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceNetworkPerformanceOptionsRequest:
    out: InstanceNetworkPerformanceOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("BandwidthWeighting") is not None:
        import capo_workspaces_instances.types.bandwidth_weighting_enum

        out["bandwidth_weighting"] = (
            capo_workspaces_instances.types.bandwidth_weighting_enum.deserialize_aws_json_1_0(
                data["BandwidthWeighting"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceNetworkPerformanceOptionsRequest) -> dict:
    out: dict = {}
    if "bandwidth_weighting" in value:
        import capo_workspaces_instances.types.bandwidth_weighting_enum

        out["BandwidthWeighting"] = (
            capo_workspaces_instances.types.bandwidth_weighting_enum.serialize_cbor(
                value["bandwidth_weighting"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> InstanceNetworkPerformanceOptionsRequest:
    out: InstanceNetworkPerformanceOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("BandwidthWeighting") is not None:
        import capo_workspaces_instances.types.bandwidth_weighting_enum

        out["bandwidth_weighting"] = (
            capo_workspaces_instances.types.bandwidth_weighting_enum.deserialize_cbor(
                data["BandwidthWeighting"]
            )
        )
    return out
