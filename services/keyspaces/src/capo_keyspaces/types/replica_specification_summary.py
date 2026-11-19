"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicaSpecificationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.capacity_specification_summary
    import capo_keyspaces.types.region
    import capo_keyspaces.types.table_status
    import capo_keyspaces.types.warm_throughput_specification_summary


class ReplicaSpecificationSummary(TypedDict, closed=True):
    region: NotRequired["capo_keyspaces.types.region.region"]
    """<p>The Amazon Web Services Region.</p>"""
    status: NotRequired["capo_keyspaces.types.table_status.TableStatus"]
    """<p>The status of the multi-Region table in the specified Amazon Web Services Region.</p>"""
    capacity_specification: NotRequired[
        "capo_keyspaces.types.capacity_specification_summary.CapacitySpecificationSummary"
    ]
    warm_throughput_specification: NotRequired[
        "capo_keyspaces.types.warm_throughput_specification_summary.WarmThroughputSpecificationSummary"
    ]
    """<p>The warm throughput settings for this replica, including the current status and configured read and write capacity units.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaSpecificationSummary) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "status" in value:
        out["status"] = value["status"]
    if "capacity_specification" in value:
        import capo_keyspaces.types.capacity_specification_summary

        out["capacitySpecification"] = (
            capo_keyspaces.types.capacity_specification_summary.serialize_aws_json_1_0(
                value["capacity_specification"]
            )
        )
    if "warm_throughput_specification" in value:
        import capo_keyspaces.types.warm_throughput_specification_summary

        out["warmThroughputSpecification"] = (
            capo_keyspaces.types.warm_throughput_specification_summary.serialize_aws_json_1_0(
                value["warm_throughput_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaSpecificationSummary:
    out: ReplicaSpecificationSummary = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("capacitySpecification") is not None:
        import capo_keyspaces.types.capacity_specification_summary

        out["capacity_specification"] = (
            capo_keyspaces.types.capacity_specification_summary.deserialize_aws_json_1_0(
                data["capacitySpecification"]
            )
        )
    if data.get("warmThroughputSpecification") is not None:
        import capo_keyspaces.types.warm_throughput_specification_summary

        out["warm_throughput_specification"] = (
            capo_keyspaces.types.warm_throughput_specification_summary.deserialize_aws_json_1_0(
                data["warmThroughputSpecification"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReplicaSpecificationSummary) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "status" in value:
        out["status"] = value["status"]
    if "capacity_specification" in value:
        import capo_keyspaces.types.capacity_specification_summary

        out["capacitySpecification"] = (
            capo_keyspaces.types.capacity_specification_summary.serialize_cbor(
                value["capacity_specification"]
            )
        )
    if "warm_throughput_specification" in value:
        import capo_keyspaces.types.warm_throughput_specification_summary

        out["warmThroughputSpecification"] = (
            capo_keyspaces.types.warm_throughput_specification_summary.serialize_cbor(
                value["warm_throughput_specification"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ReplicaSpecificationSummary:
    out: ReplicaSpecificationSummary = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("capacitySpecification") is not None:
        import capo_keyspaces.types.capacity_specification_summary

        out["capacity_specification"] = (
            capo_keyspaces.types.capacity_specification_summary.deserialize_cbor(
                data["capacitySpecification"]
            )
        )
    if data.get("warmThroughputSpecification") is not None:
        import capo_keyspaces.types.warm_throughput_specification_summary

        out["warm_throughput_specification"] = (
            capo_keyspaces.types.warm_throughput_specification_summary.deserialize_cbor(
                data["warmThroughputSpecification"]
            )
        )
    return out
