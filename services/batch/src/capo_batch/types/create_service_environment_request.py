"""Generated from Smithy shape ``com.amazonaws.batch#CreateServiceEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.capacity_limits
    import capo_batch.types.service_environment_state
    import capo_batch.types.service_environment_type
    import capo_batch.types.string
    import capo_batch.types.tagris_tags_map


class CreateServiceEnvironmentRequest(TypedDict, closed=True):
    service_environment_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name for the service environment. It can be up to 128 characters long and can contain letters, numbers, hyphens (-), and underscores (_).</p>"""
    service_environment_type: NotRequired[
        "capo_batch.types.service_environment_type.ServiceEnvironmentType"
    ]
    """<p>The type of service environment. For SageMaker Training jobs, specify <code>SAGEMAKER_TRAINING</code>.</p>"""
    state: NotRequired[
        "capo_batch.types.service_environment_state.ServiceEnvironmentState"
    ]
    """<p>The state of the service environment. Valid values are <code>ENABLED</code> and <code>DISABLED</code>. The default value is <code>ENABLED</code>.</p>"""
    capacity_limits: NotRequired["capo_batch.types.capacity_limits.CapacityLimits"]
    """<p>The capacity limits for the service environment. The number of instances a job consumes is the total number of instances requested in the submit training job request resource configuration.</p>"""
    tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that you apply to the service environment to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html">Tagging your Batch resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceEnvironmentRequest) -> dict:
    out: dict = {}
    if "service_environment_name" in value:
        out["serviceEnvironmentName"] = value["service_environment_name"]
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
    if "capacity_limits" in value:
        import capo_batch.types.capacity_limits

        out["capacityLimits"] = capo_batch.types.capacity_limits.serialize_json(
            value["capacity_limits"]
        )
    if "tags" in value:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateServiceEnvironmentRequest:
    out: CreateServiceEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceEnvironmentName") is not None:
        out["service_environment_name"] = data["serviceEnvironmentName"]
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
    if data.get("capacityLimits") is not None:
        import capo_batch.types.capacity_limits

        out["capacity_limits"] = capo_batch.types.capacity_limits.deserialize_json(
            data["capacityLimits"]
        )
    if data.get("tags") is not None:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    return out
