"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mediapackagev2.types.destination
    import capo_mediapackagev2.types.entity_tag
    import capo_mediapackagev2.types.harvest_job_status
    import capo_mediapackagev2.types.harvested_manifests
    import capo_mediapackagev2.types.harvester_schedule_configuration
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.resource_name


class HarvestJob(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel group containing the channel associated with this harvest job.</p>"""
    channel_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel associated with this harvest job.</p>"""
    origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the origin endpoint associated with this harvest job.</p>"""
    destination: "capo_mediapackagev2.types.destination.Destination"
    """<p>The S3 destination where the harvested content will be placed.</p>"""
    harvest_job_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the harvest job.</p>"""
    harvested_manifests: (
        "capo_mediapackagev2.types.harvested_manifests.HarvestedManifests"
    )
    """<p>A list of manifests that are being or have been harvested.</p>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description of the harvest job.</p>"""
    schedule_configuration: "capo_mediapackagev2.types.harvester_schedule_configuration.HarvesterScheduleConfiguration"
    """<p>The configuration for when the harvest job is scheduled to run.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the harvest job.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the harvest job was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time when the harvest job was last modified.</p>"""
    status: "capo_mediapackagev2.types.harvest_job_status.HarvestJobStatus"
    """<p>The current status of the harvest job (e.g., QUEUED, IN_PROGRESS, CANCELLED, COMPLETED, FAILED).</p>"""
    error_message: NotRequired["str"]
    """<p>An error message if the harvest job encountered any issues.</p>"""
    e_tag: NotRequired["capo_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The current version of the harvest job. Used for concurrency control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarvestJob) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    out["ChannelName"] = value["channel_name"]
    out["OriginEndpointName"] = value["origin_endpoint_name"]
    import capo_mediapackagev2.types.destination

    out["Destination"] = capo_mediapackagev2.types.destination.serialize_json(
        value["destination"]
    )
    out["HarvestJobName"] = value["harvest_job_name"]
    import capo_mediapackagev2.types.harvested_manifests

    out["HarvestedManifests"] = (
        capo_mediapackagev2.types.harvested_manifests.serialize_json(
            value["harvested_manifests"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    import capo_mediapackagev2.types.harvester_schedule_configuration

    out["ScheduleConfiguration"] = (
        capo_mediapackagev2.types.harvester_schedule_configuration.serialize_json(
            value["schedule_configuration"]
        )
    )
    out["Arn"] = value["arn"]
    import capo_mediapackagev2.types._prelude.timestamp

    out["CreatedAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_mediapackagev2.types._prelude.timestamp

    out["ModifiedAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    import capo_mediapackagev2.types.harvest_job_status

    out["Status"] = capo_mediapackagev2.types.harvest_job_status.serialize_json(
        value["status"]
    )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    return out


def deserialize_json(data: dict) -> HarvestJob:
    out: HarvestJob = {}  # type: ignore[typeddict-item]
    if data.get("ChannelGroupName") is not None:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        out["channel_group_name"] = ""
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        out["channel_name"] = ""
    if data.get("OriginEndpointName") is not None:
        out["origin_endpoint_name"] = data["OriginEndpointName"]
    else:
        out["origin_endpoint_name"] = ""
    if data.get("Destination") is not None:
        import capo_mediapackagev2.types.destination

        out["destination"] = capo_mediapackagev2.types.destination.deserialize_json(
            data["Destination"]
        )
    else:
        raise DeserializationError("HarvestJob.destination required")
    if data.get("HarvestJobName") is not None:
        out["harvest_job_name"] = data["HarvestJobName"]
    else:
        out["harvest_job_name"] = ""
    if data.get("HarvestedManifests") is not None:
        import capo_mediapackagev2.types.harvested_manifests

        out["harvested_manifests"] = (
            capo_mediapackagev2.types.harvested_manifests.deserialize_json(
                data["HarvestedManifests"]
            )
        )
    else:
        raise DeserializationError("HarvestJob.harvested_manifests required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ScheduleConfiguration") is not None:
        import capo_mediapackagev2.types.harvester_schedule_configuration

        out["schedule_configuration"] = (
            capo_mediapackagev2.types.harvester_schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    else:
        raise DeserializationError("HarvestJob.schedule_configuration required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("CreatedAt") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["created_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("ModifiedAt") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["modified_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    else:
        import datetime

        out["modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Status") is not None:
        import capo_mediapackagev2.types.harvest_job_status

        out["status"] = capo_mediapackagev2.types.harvest_job_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_mediapackagev2.types.harvest_job_status.HarvestJobStatus", ""
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("ETag") is not None:
        out["e_tag"] = data["ETag"]
    return out
