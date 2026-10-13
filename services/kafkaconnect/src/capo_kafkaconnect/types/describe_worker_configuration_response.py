"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DescribeWorkerConfigurationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.__timestamp_iso8601
    import capo_kafkaconnect.types.worker_configuration_revision_description
    import capo_kafkaconnect.types.worker_configuration_state


class DescribeWorkerConfigurationResponse(TypedDict, closed=True):
    creation_time: NotRequired[
        "capo_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that the worker configuration was created.</p>"""
    description: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The description of the worker configuration.</p>"""
    latest_revision: NotRequired[
        "capo_kafkaconnect.types.worker_configuration_revision_description.WorkerConfigurationRevisionDescription"
    ]
    """<p>The latest revision of the custom configuration.</p>"""
    name: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The name of the worker configuration.</p>"""
    worker_configuration_arn: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the custom configuration.</p>"""
    worker_configuration_state: NotRequired[
        "capo_kafkaconnect.types.worker_configuration_state.WorkerConfigurationState"
    ]
    """<p>The state of the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkerConfigurationResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "latest_revision" in value:
        import capo_kafkaconnect.types.worker_configuration_revision_description

        out["latestRevision"] = (
            capo_kafkaconnect.types.worker_configuration_revision_description.serialize_json(
                value["latest_revision"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "worker_configuration_arn" in value:
        out["workerConfigurationArn"] = value["worker_configuration_arn"]
    if "worker_configuration_state" in value:
        out["workerConfigurationState"] = value["worker_configuration_state"]
    return out


def deserialize_json(data: dict) -> DescribeWorkerConfigurationResponse:
    out: DescribeWorkerConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("creationTime") is not None:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("latestRevision") is not None:
        import capo_kafkaconnect.types.worker_configuration_revision_description

        out["latest_revision"] = (
            capo_kafkaconnect.types.worker_configuration_revision_description.deserialize_json(
                data["latestRevision"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("workerConfigurationArn") is not None:
        out["worker_configuration_arn"] = data["workerConfigurationArn"]
    if data.get("workerConfigurationState") is not None:
        out["worker_configuration_state"] = data["workerConfigurationState"]
    return out


def redact_sensitive(value: DescribeWorkerConfigurationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "latest_revision" in value:
        import capo_kafkaconnect.types.worker_configuration_revision_description

        out["latest_revision"] = (
            capo_kafkaconnect.types.worker_configuration_revision_description.redact_sensitive(
                value["latest_revision"]
            )
        )
    return out
