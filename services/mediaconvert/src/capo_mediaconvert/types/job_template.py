"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min_negative50_max50
    import capo_mediaconvert.types.__list_of_hop_destination
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__timestamp_unix
    import capo_mediaconvert.types.acceleration_settings
    import capo_mediaconvert.types.elemental_inference_settings
    import capo_mediaconvert.types.job_template_settings
    import capo_mediaconvert.types.status_update_interval
    import capo_mediaconvert.types.type


class JobTemplate(TypedDict, closed=True):
    acceleration_settings: NotRequired[
        "capo_mediaconvert.types.acceleration_settings.AccelerationSettings"
    ]
    """Accelerated transcoding can significantly speed up jobs with long, visually complex content."""
    arn: NotRequired["capo_mediaconvert.types.__string.__string"]
    """An identifier for this resource that is unique within all of AWS."""
    category: NotRequired["capo_mediaconvert.types.__string.__string"]
    """An optional category you create to organize your job templates."""
    created_at: NotRequired["capo_mediaconvert.types.__timestamp_unix.__timestampUnix"]
    """The timestamp in epoch seconds for Job template creation."""
    description: NotRequired["capo_mediaconvert.types.__string.__string"]
    """An optional description you create for each job template."""
    elemental_inference_settings: NotRequired[
        "capo_mediaconvert.types.elemental_inference_settings.ElementalInferenceSettings"
    ]
    """The Elemental Inference settings used in this job."""
    hop_destinations: NotRequired[
        "capo_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
    ]
    """Optional list of hop destinations."""
    last_updated: NotRequired[
        "capo_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The timestamp in epoch seconds when the Job template was last updated."""
    name: NotRequired["capo_mediaconvert.types.__string.__string"]
    """A name you create for each job template. Each name must be unique within your account."""
    priority: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
    ]
    """Relative priority on the job."""
    queue: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Optional. The queue that jobs created from this template are assigned to. If you don't specify this, jobs will go to the default queue."""
    settings: NotRequired[
        "capo_mediaconvert.types.job_template_settings.JobTemplateSettings"
    ]
    """JobTemplateSettings contains all the transcode settings saved in the template that will be applied to jobs created from it."""
    status_update_interval: NotRequired[
        "capo_mediaconvert.types.status_update_interval.StatusUpdateInterval"
    ]
    """Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error."""
    type: NotRequired["capo_mediaconvert.types.type.Type"]
    """A job template can be of two types: system or custom. System or built-in job templates can't be modified or deleted by the user."""


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplate) -> dict:
    out: dict = {}
    if "acceleration_settings" in value:
        import capo_mediaconvert.types.acceleration_settings

        out["accelerationSettings"] = (
            capo_mediaconvert.types.acceleration_settings.serialize_json(
                value["acceleration_settings"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "category" in value:
        out["category"] = value["category"]
    if "created_at" in value:
        import capo_mediaconvert.types.__timestamp_unix

        out["createdAt"] = capo_mediaconvert.types.__timestamp_unix.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "elemental_inference_settings" in value:
        import capo_mediaconvert.types.elemental_inference_settings

        out["elementalInferenceSettings"] = (
            capo_mediaconvert.types.elemental_inference_settings.serialize_json(
                value["elemental_inference_settings"]
            )
        )
    if "hop_destinations" in value:
        import capo_mediaconvert.types.__list_of_hop_destination

        out["hopDestinations"] = (
            capo_mediaconvert.types.__list_of_hop_destination.serialize_json(
                value["hop_destinations"]
            )
        )
    if "last_updated" in value:
        import capo_mediaconvert.types.__timestamp_unix

        out["lastUpdated"] = capo_mediaconvert.types.__timestamp_unix.serialize_json(
            value["last_updated"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "queue" in value:
        out["queue"] = value["queue"]
    if "settings" in value:
        import capo_mediaconvert.types.job_template_settings

        out["settings"] = capo_mediaconvert.types.job_template_settings.serialize_json(
            value["settings"]
        )
    if "status_update_interval" in value:
        import capo_mediaconvert.types.status_update_interval

        out["statusUpdateInterval"] = (
            capo_mediaconvert.types.status_update_interval.serialize_json(
                value["status_update_interval"]
            )
        )
    if "type" in value:
        import capo_mediaconvert.types.type

        out["type"] = capo_mediaconvert.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> JobTemplate:
    out: JobTemplate = {}  # type: ignore[typeddict-item]
    if data.get("accelerationSettings") is not None:
        import capo_mediaconvert.types.acceleration_settings

        out["acceleration_settings"] = (
            capo_mediaconvert.types.acceleration_settings.deserialize_json(
                data["accelerationSettings"]
            )
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("category") is not None:
        out["category"] = data["category"]
    if data.get("createdAt") is not None:
        import capo_mediaconvert.types.__timestamp_unix

        out["created_at"] = capo_mediaconvert.types.__timestamp_unix.deserialize_json(
            data["createdAt"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("elementalInferenceSettings") is not None:
        import capo_mediaconvert.types.elemental_inference_settings

        out["elemental_inference_settings"] = (
            capo_mediaconvert.types.elemental_inference_settings.deserialize_json(
                data["elementalInferenceSettings"]
            )
        )
    if data.get("hopDestinations") is not None:
        import capo_mediaconvert.types.__list_of_hop_destination

        out["hop_destinations"] = (
            capo_mediaconvert.types.__list_of_hop_destination.deserialize_json(
                data["hopDestinations"]
            )
        )
    if data.get("lastUpdated") is not None:
        import capo_mediaconvert.types.__timestamp_unix

        out["last_updated"] = capo_mediaconvert.types.__timestamp_unix.deserialize_json(
            data["lastUpdated"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("queue") is not None:
        out["queue"] = data["queue"]
    if data.get("settings") is not None:
        import capo_mediaconvert.types.job_template_settings

        out["settings"] = (
            capo_mediaconvert.types.job_template_settings.deserialize_json(
                data["settings"]
            )
        )
    if data.get("statusUpdateInterval") is not None:
        import capo_mediaconvert.types.status_update_interval

        out["status_update_interval"] = (
            capo_mediaconvert.types.status_update_interval.deserialize_json(
                data["statusUpdateInterval"]
            )
        )
    if data.get("type") is not None:
        import capo_mediaconvert.types.type

        out["type"] = capo_mediaconvert.types.type.deserialize_json(data["type"])
    return out
