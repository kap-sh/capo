"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.capacity_limits
    import capo_batch.types.service_environment_state
    import capo_batch.types.service_environment_status
    import capo_batch.types.service_environment_type
    import capo_batch.types.string
    import capo_batch.types.tagris_tags_map


class ServiceEnvironmentDetail(TypedDict, closed=True):
    service_environment_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the service environment.</p>"""
    service_environment_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service environment.</p>"""
    service_environment_type: NotRequired[
        "capo_batch.types.service_environment_type.ServiceEnvironmentType"
    ]
    """<p>The type of service environment. For SageMaker Training jobs, this value is <code>SAGEMAKER_TRAINING</code>.</p>"""
    state: NotRequired[
        "capo_batch.types.service_environment_state.ServiceEnvironmentState"
    ]
    """<p>The state of the service environment. Valid values are <code>ENABLED</code> and <code>DISABLED</code>.</p>"""
    status: NotRequired[
        "capo_batch.types.service_environment_status.ServiceEnvironmentStatus"
    ]
    """<p>The current status of the service environment.</p>"""
    capacity_limits: NotRequired["capo_batch.types.capacity_limits.CapacityLimits"]
    """<p>The capacity limits for the service environment. This defines the maximum resources that can be used by service jobs in this environment.</p>"""
    tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags associated with the service environment. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html">Tagging your Batch resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEnvironmentDetail) -> dict:
    out: dict = {}
    if "service_environment_name" in value:
        out["serviceEnvironmentName"] = value["service_environment_name"]
    if "service_environment_arn" in value:
        out["serviceEnvironmentArn"] = value["service_environment_arn"]
    if "service_environment_type" in value:
        import capo_batch.types.service_environment_type

        out["serviceEnvironmentType"] = (
            capo_batch.types.service_environment_type.serialize_json(
                value["service_environment_type"]
            )
        )
    if "state" in value:
        import capo_batch.types.service_environment_state

        out["state"] = capo_batch.types.service_environment_state.serialize_json(
            value["state"]
        )
    if "status" in value:
        import capo_batch.types.service_environment_status

        out["status"] = capo_batch.types.service_environment_status.serialize_json(
            value["status"]
        )
    if "capacity_limits" in value:
        import capo_batch.types.capacity_limits

        out["capacityLimits"] = capo_batch.types.capacity_limits.serialize_json(
            value["capacity_limits"]
        )
    if "tags" in value:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ServiceEnvironmentDetail:
    out: ServiceEnvironmentDetail = {}  # type: ignore[typeddict-item]
    if data.get("serviceEnvironmentName") is not None:
        out["service_environment_name"] = data["serviceEnvironmentName"]
    if data.get("serviceEnvironmentArn") is not None:
        out["service_environment_arn"] = data["serviceEnvironmentArn"]
    if data.get("serviceEnvironmentType") is not None:
        import capo_batch.types.service_environment_type

        out["service_environment_type"] = (
            capo_batch.types.service_environment_type.deserialize_json(
                data["serviceEnvironmentType"]
            )
        )
    if data.get("state") is not None:
        import capo_batch.types.service_environment_state

        out["state"] = capo_batch.types.service_environment_state.deserialize_json(
            data["state"]
        )
    if data.get("status") is not None:
        import capo_batch.types.service_environment_status

        out["status"] = capo_batch.types.service_environment_status.deserialize_json(
            data["status"]
        )
    if data.get("capacityLimits") is not None:
        import capo_batch.types.capacity_limits

        out["capacity_limits"] = capo_batch.types.capacity_limits.deserialize_json(
            data["capacityLimits"]
        )
    if data.get("tags") is not None:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    return out
