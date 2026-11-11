"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CreateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min_negative50_max50
    import capo_mediaconvert.types.__list_of_hop_destination
    import capo_mediaconvert.types.__map_of__string
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.acceleration_settings
    import capo_mediaconvert.types.billing_tags_source
    import capo_mediaconvert.types.elemental_inference_settings
    import capo_mediaconvert.types.job_settings
    import capo_mediaconvert.types.simulate_reserved_queue
    import capo_mediaconvert.types.status_update_interval


class CreateJobRequest(TypedDict, closed=True):
    acceleration_settings: NotRequired[
        "capo_mediaconvert.types.acceleration_settings.AccelerationSettings"
    ]
    """Optional. Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, see the AWS Elemental MediaConvert User Guide."""
    billing_tags_source: NotRequired[
        "capo_mediaconvert.types.billing_tags_source.BillingTagsSource"
    ]
    """Optionally choose a Billing tags source that AWS Billing and Cost Management will use to display tags for individual output costs on any billing report that you set up. Leave blank to use the default value, Job."""
    client_request_token: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Prevent duplicate jobs from being created and ensure idempotency for your requests. A client request token can be any string that includes up to 64 ASCII characters. If you reuse a client request token within one minute of a successful request, the API returns the job details of the original request instead. For more information see https://docs.aws.amazon.com/mediaconvert/latest/apireference/idempotency.html."""
    elemental_inference_settings: NotRequired[
        "capo_mediaconvert.types.elemental_inference_settings.ElementalInferenceSettings"
    ]
    """The Elemental Inference settings used in this job."""
    hop_destinations: NotRequired[
        "capo_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
    ]
    """Optional. Use queue hopping to avoid overly long waits in the backlog of the queue that you submit your job to. Specify an alternate queue and the maximum time that your job will wait in the initial queue before hopping. For more information about this feature, see the AWS Elemental MediaConvert User Guide."""
    job_engine_version: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Use Job engine versions to run jobs for your production workflow on one version, while you test and validate the latest version. Job engine versions represent periodically grouped MediaConvert releases with new features, updates, improvements, and fixes. Job engine versions are in a YYYY-MM-DD format. Note that the Job engine version feature is not publicly available at this time. To request access, contact AWS support."""
    job_template: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Optional. When you create a job, you can either specify a job template or specify the transcoding settings individually."""
    priority: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
    ]
    """Optional. Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0."""
    queue: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Optional. When you create a job, you can specify a queue to send it to. If you don't specify, the job will go to the default queue. For more about queues, see the User Guide topic at https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html."""
    role: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Required. The IAM role you use for creating this job. For details about permissions, see the User Guide topic at the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html."""
    settings: NotRequired["capo_mediaconvert.types.job_settings.JobSettings"]
    """JobSettings contains all the transcode settings for a job."""
    simulate_reserved_queue: NotRequired[
        "capo_mediaconvert.types.simulate_reserved_queue.SimulateReservedQueue"
    ]
    """Optional. Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default."""
    status_update_interval: NotRequired[
        "capo_mediaconvert.types.status_update_interval.StatusUpdateInterval"
    ]
    """Optional. Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error."""
    tags: NotRequired["capo_mediaconvert.types.__map_of__string.__mapOf__string"]
    """Optional. The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key. Use standard AWS tags on your job for automatic integration with AWS services and for custom integrations and workflows."""
    user_metadata: NotRequired[
        "capo_mediaconvert.types.__map_of__string.__mapOf__string"
    ]
    """Optional. User-defined metadata that you want to associate with an MediaConvert job. You specify metadata in key/value pairs. Use only for existing integrations or workflows that rely on job metadata tags. Otherwise, we recommend that you use standard AWS tags."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobRequest) -> dict:
    out: dict = {}
    if "acceleration_settings" in value:
        import capo_mediaconvert.types.acceleration_settings

        out["accelerationSettings"] = (
            capo_mediaconvert.types.acceleration_settings.serialize_json(
                value["acceleration_settings"]
            )
        )
    if "billing_tags_source" in value:
        import capo_mediaconvert.types.billing_tags_source

        out["billingTagsSource"] = (
            capo_mediaconvert.types.billing_tags_source.serialize_json(
                value["billing_tags_source"]
            )
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
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
    if "job_engine_version" in value:
        out["jobEngineVersion"] = value["job_engine_version"]
    if "job_template" in value:
        out["jobTemplate"] = value["job_template"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "queue" in value:
        out["queue"] = value["queue"]
    if "role" in value:
        out["role"] = value["role"]
    if "settings" in value:
        import capo_mediaconvert.types.job_settings

        out["settings"] = capo_mediaconvert.types.job_settings.serialize_json(
            value["settings"]
        )
    if "simulate_reserved_queue" in value:
        import capo_mediaconvert.types.simulate_reserved_queue

        out["simulateReservedQueue"] = (
            capo_mediaconvert.types.simulate_reserved_queue.serialize_json(
                value["simulate_reserved_queue"]
            )
        )
    if "status_update_interval" in value:
        import capo_mediaconvert.types.status_update_interval

        out["statusUpdateInterval"] = (
            capo_mediaconvert.types.status_update_interval.serialize_json(
                value["status_update_interval"]
            )
        )
    if "tags" in value:
        import capo_mediaconvert.types.__map_of__string

        out["tags"] = capo_mediaconvert.types.__map_of__string.serialize_json(
            value["tags"]
        )
    if "user_metadata" in value:
        import capo_mediaconvert.types.__map_of__string

        out["userMetadata"] = capo_mediaconvert.types.__map_of__string.serialize_json(
            value["user_metadata"]
        )
    return out


def deserialize_json(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("accelerationSettings") is not None:
        import capo_mediaconvert.types.acceleration_settings

        out["acceleration_settings"] = (
            capo_mediaconvert.types.acceleration_settings.deserialize_json(
                data["accelerationSettings"]
            )
        )
    if data.get("billingTagsSource") is not None:
        import capo_mediaconvert.types.billing_tags_source

        out["billing_tags_source"] = (
            capo_mediaconvert.types.billing_tags_source.deserialize_json(
                data["billingTagsSource"]
            )
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
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
    if data.get("jobEngineVersion") is not None:
        out["job_engine_version"] = data["jobEngineVersion"]
    if data.get("jobTemplate") is not None:
        out["job_template"] = data["jobTemplate"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("queue") is not None:
        out["queue"] = data["queue"]
    if data.get("role") is not None:
        out["role"] = data["role"]
    if data.get("settings") is not None:
        import capo_mediaconvert.types.job_settings

        out["settings"] = capo_mediaconvert.types.job_settings.deserialize_json(
            data["settings"]
        )
    if data.get("simulateReservedQueue") is not None:
        import capo_mediaconvert.types.simulate_reserved_queue

        out["simulate_reserved_queue"] = (
            capo_mediaconvert.types.simulate_reserved_queue.deserialize_json(
                data["simulateReservedQueue"]
            )
        )
    if data.get("statusUpdateInterval") is not None:
        import capo_mediaconvert.types.status_update_interval

        out["status_update_interval"] = (
            capo_mediaconvert.types.status_update_interval.deserialize_json(
                data["statusUpdateInterval"]
            )
        )
    if data.get("tags") is not None:
        import capo_mediaconvert.types.__map_of__string

        out["tags"] = capo_mediaconvert.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if data.get("userMetadata") is not None:
        import capo_mediaconvert.types.__map_of__string

        out["user_metadata"] = (
            capo_mediaconvert.types.__map_of__string.deserialize_json(
                data["userMetadata"]
            )
        )
    return out
