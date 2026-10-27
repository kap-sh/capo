"""Generated from Smithy shape ``com.amazonaws.deadline#Statistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.fleet_id
    import capo_deadline.types.instance_type
    import capo_deadline.types.integer
    import capo_deadline.types.job_id
    import capo_deadline.types.job_name
    import capo_deadline.types.license_product
    import capo_deadline.types.queue_id
    import capo_deadline.types.stats
    import capo_deadline.types.timestamp
    import capo_deadline.types.usage_type
    import capo_deadline.types.user_id


class Statistics(TypedDict, closed=True):
    queue_id: NotRequired["capo_deadline.types.queue_id.QueueId"]
    """The queue ID."""
    fleet_id: NotRequired["capo_deadline.types.fleet_id.FleetId"]
    """The fleet ID."""
    job_id: NotRequired["capo_deadline.types.job_id.JobId"]
    """The job ID."""
    job_name: NotRequired["capo_deadline.types.job_name.JobName"]
    """The job name."""
    user_id: NotRequired["capo_deadline.types.user_id.UserId"]
    """The user ID."""
    usage_type: NotRequired["capo_deadline.types.usage_type.UsageType"]
    """The type of usage for the statistics."""
    license_product: NotRequired["capo_deadline.types.license_product.LicenseProduct"]
    """The licensed product."""
    instance_type: NotRequired["capo_deadline.types.instance_type.InstanceType"]
    """The type of instance."""
    count: "capo_deadline.types.integer.Integer"
    """The number of instances in a list of statistics."""
    cost_in_usd: "capo_deadline.types.stats.Stats"
    """How the statistics should appear in USD. Options include: minimum, maximum, average or sum."""
    runtime_in_seconds: "capo_deadline.types.stats.Stats"
    """The total aggregated runtime."""
    aggregation_start_time: NotRequired["capo_deadline.types.timestamp.Timestamp"]
    """The start time for the aggregation."""
    aggregation_end_time: NotRequired["capo_deadline.types.timestamp.Timestamp"]
    """The end time for the aggregation."""


# --- restJson1 ser/de ---
def serialize_json(value: Statistics) -> dict:
    out: dict = {}
    if "queue_id" in value:
        out["queueId"] = value["queue_id"]
    if "fleet_id" in value:
        out["fleetId"] = value["fleet_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "usage_type" in value:
        import capo_deadline.types.usage_type

        out["usageType"] = capo_deadline.types.usage_type.serialize_json(
            value["usage_type"]
        )
    if "license_product" in value:
        out["licenseProduct"] = value["license_product"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    out["count"] = value["count"]
    import capo_deadline.types.stats

    out["costInUsd"] = capo_deadline.types.stats.serialize_json(value["cost_in_usd"])
    import capo_deadline.types.stats

    out["runtimeInSeconds"] = capo_deadline.types.stats.serialize_json(
        value["runtime_in_seconds"]
    )
    if "aggregation_start_time" in value:
        import capo_deadline._protocol.serialize

        out["aggregationStartTime"] = capo_deadline._protocol.serialize.fmt_date_time(
            value["aggregation_start_time"]
        )
    if "aggregation_end_time" in value:
        import capo_deadline._protocol.serialize

        out["aggregationEndTime"] = capo_deadline._protocol.serialize.fmt_date_time(
            value["aggregation_end_time"]
        )
    return out


def deserialize_json(data: dict) -> Statistics:
    out: Statistics = {}  # type: ignore[typeddict-item]
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("usageType") is not None:
        import capo_deadline.types.usage_type

        out["usage_type"] = capo_deadline.types.usage_type.deserialize_json(
            data["usageType"]
        )
    if data.get("licenseProduct") is not None:
        out["license_product"] = data["licenseProduct"]
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if data.get("costInUsd") is not None:
        import capo_deadline.types.stats

        out["cost_in_usd"] = capo_deadline.types.stats.deserialize_json(
            data["costInUsd"]
        )
    else:
        raise DeserializationError("Statistics.cost_in_usd required")
    if data.get("runtimeInSeconds") is not None:
        import capo_deadline.types.stats

        out["runtime_in_seconds"] = capo_deadline.types.stats.deserialize_json(
            data["runtimeInSeconds"]
        )
    else:
        raise DeserializationError("Statistics.runtime_in_seconds required")
    if data.get("aggregationStartTime") is not None:
        import datetime

        out["aggregation_start_time"] = datetime.datetime.fromisoformat(
            data["aggregationStartTime"].replace("Z", "+00:00")
        )
    if data.get("aggregationEndTime") is not None:
        import datetime

        out["aggregation_end_time"] = datetime.datetime.fromisoformat(
            data["aggregationEndTime"].replace("Z", "+00:00")
        )
    return out
