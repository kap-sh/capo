"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.data_partition_id
    import capo_iotfleetwise.types.max_sample_count
    import capo_iotfleetwise.types.uint32
    import capo_iotfleetwise.types.wildcard_signal_name


class SignalInformation(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.wildcard_signal_name.wildcardSignalName"
    """<p>The name of the signal.</p>"""
    max_sample_count: NotRequired[
        "capo_iotfleetwise.types.max_sample_count.maxSampleCount"
    ]
    """<p>The maximum number of samples to collect.</p>"""
    minimum_sampling_interval_ms: NotRequired["capo_iotfleetwise.types.uint32.uint32"]
    """<p>The minimum duration of time (in milliseconds) between two triggering events to collect data.</p> <note> <p>If a signal changes often, you might want to collect data at a slower rate.</p> </note>"""
    data_partition_id: NotRequired[
        "capo_iotfleetwise.types.data_partition_id.DataPartitionId"
    ]
    """<p>The ID of the data partition this signal is associated with.</p> <p>The ID must match one of the IDs provided in <code>dataPartitions</code>. This is accomplished either by specifying a particular data partition ID or by using <code>default</code> for an established default partition. You can establish a default partition in the <code>DataPartition</code> data type.</p> <note> <p>If you upload a signal as a condition for a campaign's data partition, the same signal must be included in <code>signalsToCollect</code>.</p> </note> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalInformation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "max_sample_count" in value:
        out["maxSampleCount"] = value["max_sample_count"]
    if "minimum_sampling_interval_ms" in value:
        out["minimumSamplingIntervalMs"] = value["minimum_sampling_interval_ms"]
    if "data_partition_id" in value:
        out["dataPartitionId"] = value["data_partition_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SignalInformation:
    out: SignalInformation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SignalInformation.name required")
    if data.get("maxSampleCount") is not None:
        out["max_sample_count"] = data["maxSampleCount"]
    if data.get("minimumSamplingIntervalMs") is not None:
        out["minimum_sampling_interval_ms"] = data["minimumSamplingIntervalMs"]
    if data.get("dataPartitionId") is not None:
        out["data_partition_id"] = data["dataPartitionId"]
    return out
