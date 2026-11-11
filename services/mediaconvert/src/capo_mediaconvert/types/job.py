"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Job``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer
    import capo_mediaconvert.types.__integer_min_negative50_max50
    import capo_mediaconvert.types.__list_of_hop_destination
    import capo_mediaconvert.types.__list_of_output_group_detail
    import capo_mediaconvert.types.__list_of_queue_transition
    import capo_mediaconvert.types.__list_of_warning_group
    import capo_mediaconvert.types.__map_of__string
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__timestamp_unix
    import capo_mediaconvert.types.acceleration_settings
    import capo_mediaconvert.types.acceleration_status
    import capo_mediaconvert.types.billing_tags_source
    import capo_mediaconvert.types.elemental_inference_configuration
    import capo_mediaconvert.types.elemental_inference_settings
    import capo_mediaconvert.types.job_messages
    import capo_mediaconvert.types.job_phase
    import capo_mediaconvert.types.job_settings
    import capo_mediaconvert.types.job_status
    import capo_mediaconvert.types.share_status
    import capo_mediaconvert.types.simulate_reserved_queue
    import capo_mediaconvert.types.status_update_interval
    import capo_mediaconvert.types.timing


class Job(TypedDict, closed=True):
    acceleration_settings: NotRequired[
        "capo_mediaconvert.types.acceleration_settings.AccelerationSettings"
    ]
    """Accelerated transcoding can significantly speed up jobs with long, visually complex content."""
    acceleration_status: NotRequired[
        "capo_mediaconvert.types.acceleration_status.AccelerationStatus"
    ]
    """Describes whether the current job is running with accelerated transcoding. For jobs that have Acceleration (AccelerationMode) set to DISABLED, AccelerationStatus is always NOT_APPLICABLE. For jobs that have Acceleration (AccelerationMode) set to ENABLED or PREFERRED, AccelerationStatus is one of the other states. AccelerationStatus is IN_PROGRESS initially, while the service determines whether the input files and job settings are compatible with accelerated transcoding. If they are, AcclerationStatus is ACCELERATED. If your input files and job settings aren't compatible with accelerated transcoding, the service either fails your job or runs it without accelerated transcoding, depending on how you set Acceleration (AccelerationMode). When the service runs your job without accelerated transcoding, AccelerationStatus is NOT_ACCELERATED."""
    arn: NotRequired["capo_mediaconvert.types.__string.__string"]
    """An identifier for this resource that is unique within all of AWS."""
    billing_tags_source: NotRequired[
        "capo_mediaconvert.types.billing_tags_source.BillingTagsSource"
    ]
    """The tag type that AWS Billing and Cost Management will use to sort your AWS Elemental MediaConvert costs on any billing report that you set up."""
    client_request_token: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Prevent duplicate jobs from being created and ensure idempotency for your requests. A client request token can be any string that includes up to 64 ASCII characters. If you reuse a client request token within one minute of a successful request, the API returns the job details of the original request instead. For more information see https://docs.aws.amazon.com/mediaconvert/latest/apireference/idempotency.html."""
    created_at: NotRequired["capo_mediaconvert.types.__timestamp_unix.__timestampUnix"]
    """The time, in Unix epoch format in seconds, when the job got created."""
    current_phase: NotRequired["capo_mediaconvert.types.job_phase.JobPhase"]
    """A job's phase can be PROBING, TRANSCODING OR UPLOADING"""
    elemental_inference_configuration: NotRequired[
        "capo_mediaconvert.types.elemental_inference_configuration.ElementalInferenceConfiguration"
    ]
    """The Elemental Inference configuration used in this job."""
    elemental_inference_settings: NotRequired[
        "capo_mediaconvert.types.elemental_inference_settings.ElementalInferenceSettings"
    ]
    """The Elemental Inference settings used in this job."""
    error_code: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Error code for the job"""
    error_message: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Error message of Job"""
    hop_destinations: NotRequired[
        "capo_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
    ]
    """Optional list of hop destinations."""
    id: NotRequired["capo_mediaconvert.types.__string.__string"]
    """A portion of the job's ARN, unique within your AWS Elemental MediaConvert resources"""
    job_engine_version_requested: NotRequired[
        "capo_mediaconvert.types.__string.__string"
    ]
    """The Job engine version that you requested for your job. Valid versions are in a YYYY-MM-DD format."""
    job_engine_version_used: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The Job engine version that your job used. Job engine versions are in a YYYY-MM-DD format. When you request an expired version, the response for this property will be empty. Requests to create jobs with an expired version result in a regular job, as if no specific Job engine version was requested. When you request an invalid version, the response for this property will be empty. Requests to create jobs with an invalid version result in a 400 error message, and no job is created."""
    job_percent_complete: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """An estimate of how far your job has progressed. This estimate is shown as a percentage of the total time from when your job leaves its queue to when your output files appear in your output Amazon S3 bucket. AWS Elemental MediaConvert provides jobPercentComplete in CloudWatch STATUS_UPDATE events and in the response to GetJob and ListJobs requests. The jobPercentComplete estimate is reliable for the following input containers: Quicktime, Transport Stream, MP4, and MXF. For some jobs, the service can't provide information about job progress. In those cases, jobPercentComplete returns a null value."""
    job_template: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The job template that the job is created from, if it is created from a job template."""
    last_share_details: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Contains information about the most recent share attempt for the job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/creating-resource-share.html"""
    messages: NotRequired["capo_mediaconvert.types.job_messages.JobMessages"]
    """Provides messages from the service about jobs that you have already successfully submitted."""
    output_group_details: NotRequired[
        "capo_mediaconvert.types.__list_of_output_group_detail.__listOfOutputGroupDetail"
    ]
    """List of output group details"""
    priority: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
    ]
    """Relative priority on the job."""
    queue: NotRequired["capo_mediaconvert.types.__string.__string"]
    """When you create a job, you can specify a queue to send it to. If you don't specify, the job will go to the default queue. For more about queues, see the User Guide topic at https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html"""
    queue_transitions: NotRequired[
        "capo_mediaconvert.types.__list_of_queue_transition.__listOfQueueTransition"
    ]
    """The job's queue hopping history."""
    retry_count: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The number of times that the service automatically attempted to process your job after encountering an error."""
    role: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The IAM role you use for creating this job. For details about permissions, see the User Guide topic at the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html"""
    settings: NotRequired["capo_mediaconvert.types.job_settings.JobSettings"]
    """JobSettings contains all the transcode settings for a job."""
    share_status: NotRequired["capo_mediaconvert.types.share_status.ShareStatus"]
    """A job's share status can be NOT_SHARED, INITIATED, or SHARED"""
    simulate_reserved_queue: NotRequired[
        "capo_mediaconvert.types.simulate_reserved_queue.SimulateReservedQueue"
    ]
    """Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default."""
    status: NotRequired["capo_mediaconvert.types.job_status.JobStatus"]
    """A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR."""
    status_update_interval: NotRequired[
        "capo_mediaconvert.types.status_update_interval.StatusUpdateInterval"
    ]
    """Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error."""
    timing: NotRequired["capo_mediaconvert.types.timing.Timing"]
    """Information about when jobs are submitted, started, and finished is specified in Unix epoch format in seconds."""
    user_metadata: NotRequired[
        "capo_mediaconvert.types.__map_of__string.__mapOf__string"
    ]
    """User-defined metadata that you want to associate with an MediaConvert job. You specify metadata in key/value pairs."""
    warnings: NotRequired[
        "capo_mediaconvert.types.__list_of_warning_group.__listOfWarningGroup"
    ]
    """Contains any warning messages for the job. Use to help identify potential issues with your input, output, or job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/warning_codes.html"""


# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    if "acceleration_settings" in value:
        import capo_mediaconvert.types.acceleration_settings

        out["accelerationSettings"] = (
            capo_mediaconvert.types.acceleration_settings.serialize_json(
                value["acceleration_settings"]
            )
        )
    if "acceleration_status" in value:
        import capo_mediaconvert.types.acceleration_status

        out["accelerationStatus"] = (
            capo_mediaconvert.types.acceleration_status.serialize_json(
                value["acceleration_status"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "billing_tags_source" in value:
        import capo_mediaconvert.types.billing_tags_source

        out["billingTagsSource"] = (
            capo_mediaconvert.types.billing_tags_source.serialize_json(
                value["billing_tags_source"]
            )
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "created_at" in value:
        import capo_mediaconvert.types.__timestamp_unix

        out["createdAt"] = capo_mediaconvert.types.__timestamp_unix.serialize_json(
            value["created_at"]
        )
    if "current_phase" in value:
        import capo_mediaconvert.types.job_phase

        out["currentPhase"] = capo_mediaconvert.types.job_phase.serialize_json(
            value["current_phase"]
        )
    if "elemental_inference_configuration" in value:
        import capo_mediaconvert.types.elemental_inference_configuration

        out["elementalInferenceConfiguration"] = (
            capo_mediaconvert.types.elemental_inference_configuration.serialize_json(
                value["elemental_inference_configuration"]
            )
        )
    if "elemental_inference_settings" in value:
        import capo_mediaconvert.types.elemental_inference_settings

        out["elementalInferenceSettings"] = (
            capo_mediaconvert.types.elemental_inference_settings.serialize_json(
                value["elemental_inference_settings"]
            )
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "hop_destinations" in value:
        import capo_mediaconvert.types.__list_of_hop_destination

        out["hopDestinations"] = (
            capo_mediaconvert.types.__list_of_hop_destination.serialize_json(
                value["hop_destinations"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "job_engine_version_requested" in value:
        out["jobEngineVersionRequested"] = value["job_engine_version_requested"]
    if "job_engine_version_used" in value:
        out["jobEngineVersionUsed"] = value["job_engine_version_used"]
    if "job_percent_complete" in value:
        out["jobPercentComplete"] = value["job_percent_complete"]
    if "job_template" in value:
        out["jobTemplate"] = value["job_template"]
    if "last_share_details" in value:
        out["lastShareDetails"] = value["last_share_details"]
    if "messages" in value:
        import capo_mediaconvert.types.job_messages

        out["messages"] = capo_mediaconvert.types.job_messages.serialize_json(
            value["messages"]
        )
    if "output_group_details" in value:
        import capo_mediaconvert.types.__list_of_output_group_detail

        out["outputGroupDetails"] = (
            capo_mediaconvert.types.__list_of_output_group_detail.serialize_json(
                value["output_group_details"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "queue" in value:
        out["queue"] = value["queue"]
    if "queue_transitions" in value:
        import capo_mediaconvert.types.__list_of_queue_transition

        out["queueTransitions"] = (
            capo_mediaconvert.types.__list_of_queue_transition.serialize_json(
                value["queue_transitions"]
            )
        )
    if "retry_count" in value:
        out["retryCount"] = value["retry_count"]
    if "role" in value:
        out["role"] = value["role"]
    if "settings" in value:
        import capo_mediaconvert.types.job_settings

        out["settings"] = capo_mediaconvert.types.job_settings.serialize_json(
            value["settings"]
        )
    if "share_status" in value:
        import capo_mediaconvert.types.share_status

        out["shareStatus"] = capo_mediaconvert.types.share_status.serialize_json(
            value["share_status"]
        )
    if "simulate_reserved_queue" in value:
        import capo_mediaconvert.types.simulate_reserved_queue

        out["simulateReservedQueue"] = (
            capo_mediaconvert.types.simulate_reserved_queue.serialize_json(
                value["simulate_reserved_queue"]
            )
        )
    if "status" in value:
        import capo_mediaconvert.types.job_status

        out["status"] = capo_mediaconvert.types.job_status.serialize_json(
            value["status"]
        )
    if "status_update_interval" in value:
        import capo_mediaconvert.types.status_update_interval

        out["statusUpdateInterval"] = (
            capo_mediaconvert.types.status_update_interval.serialize_json(
                value["status_update_interval"]
            )
        )
    if "timing" in value:
        import capo_mediaconvert.types.timing

        out["timing"] = capo_mediaconvert.types.timing.serialize_json(value["timing"])
    if "user_metadata" in value:
        import capo_mediaconvert.types.__map_of__string

        out["userMetadata"] = capo_mediaconvert.types.__map_of__string.serialize_json(
            value["user_metadata"]
        )
    if "warnings" in value:
        import capo_mediaconvert.types.__list_of_warning_group

        out["warnings"] = (
            capo_mediaconvert.types.__list_of_warning_group.serialize_json(
                value["warnings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if data.get("accelerationSettings") is not None:
        import capo_mediaconvert.types.acceleration_settings

        out["acceleration_settings"] = (
            capo_mediaconvert.types.acceleration_settings.deserialize_json(
                data["accelerationSettings"]
            )
        )
    if data.get("accelerationStatus") is not None:
        import capo_mediaconvert.types.acceleration_status

        out["acceleration_status"] = (
            capo_mediaconvert.types.acceleration_status.deserialize_json(
                data["accelerationStatus"]
            )
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("billingTagsSource") is not None:
        import capo_mediaconvert.types.billing_tags_source

        out["billing_tags_source"] = (
            capo_mediaconvert.types.billing_tags_source.deserialize_json(
                data["billingTagsSource"]
            )
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("createdAt") is not None:
        import capo_mediaconvert.types.__timestamp_unix

        out["created_at"] = capo_mediaconvert.types.__timestamp_unix.deserialize_json(
            data["createdAt"]
        )
    if data.get("currentPhase") is not None:
        import capo_mediaconvert.types.job_phase

        out["current_phase"] = capo_mediaconvert.types.job_phase.deserialize_json(
            data["currentPhase"]
        )
    if data.get("elementalInferenceConfiguration") is not None:
        import capo_mediaconvert.types.elemental_inference_configuration

        out["elemental_inference_configuration"] = (
            capo_mediaconvert.types.elemental_inference_configuration.deserialize_json(
                data["elementalInferenceConfiguration"]
            )
        )
    if data.get("elementalInferenceSettings") is not None:
        import capo_mediaconvert.types.elemental_inference_settings

        out["elemental_inference_settings"] = (
            capo_mediaconvert.types.elemental_inference_settings.deserialize_json(
                data["elementalInferenceSettings"]
            )
        )
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("hopDestinations") is not None:
        import capo_mediaconvert.types.__list_of_hop_destination

        out["hop_destinations"] = (
            capo_mediaconvert.types.__list_of_hop_destination.deserialize_json(
                data["hopDestinations"]
            )
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("jobEngineVersionRequested") is not None:
        out["job_engine_version_requested"] = data["jobEngineVersionRequested"]
    if data.get("jobEngineVersionUsed") is not None:
        out["job_engine_version_used"] = data["jobEngineVersionUsed"]
    if data.get("jobPercentComplete") is not None:
        out["job_percent_complete"] = data["jobPercentComplete"]
    if data.get("jobTemplate") is not None:
        out["job_template"] = data["jobTemplate"]
    if data.get("lastShareDetails") is not None:
        out["last_share_details"] = data["lastShareDetails"]
    if data.get("messages") is not None:
        import capo_mediaconvert.types.job_messages

        out["messages"] = capo_mediaconvert.types.job_messages.deserialize_json(
            data["messages"]
        )
    if data.get("outputGroupDetails") is not None:
        import capo_mediaconvert.types.__list_of_output_group_detail

        out["output_group_details"] = (
            capo_mediaconvert.types.__list_of_output_group_detail.deserialize_json(
                data["outputGroupDetails"]
            )
        )
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("queue") is not None:
        out["queue"] = data["queue"]
    if data.get("queueTransitions") is not None:
        import capo_mediaconvert.types.__list_of_queue_transition

        out["queue_transitions"] = (
            capo_mediaconvert.types.__list_of_queue_transition.deserialize_json(
                data["queueTransitions"]
            )
        )
    if data.get("retryCount") is not None:
        out["retry_count"] = data["retryCount"]
    if data.get("role") is not None:
        out["role"] = data["role"]
    if data.get("settings") is not None:
        import capo_mediaconvert.types.job_settings

        out["settings"] = capo_mediaconvert.types.job_settings.deserialize_json(
            data["settings"]
        )
    if data.get("shareStatus") is not None:
        import capo_mediaconvert.types.share_status

        out["share_status"] = capo_mediaconvert.types.share_status.deserialize_json(
            data["shareStatus"]
        )
    if data.get("simulateReservedQueue") is not None:
        import capo_mediaconvert.types.simulate_reserved_queue

        out["simulate_reserved_queue"] = (
            capo_mediaconvert.types.simulate_reserved_queue.deserialize_json(
                data["simulateReservedQueue"]
            )
        )
    if data.get("status") is not None:
        import capo_mediaconvert.types.job_status

        out["status"] = capo_mediaconvert.types.job_status.deserialize_json(
            data["status"]
        )
    if data.get("statusUpdateInterval") is not None:
        import capo_mediaconvert.types.status_update_interval

        out["status_update_interval"] = (
            capo_mediaconvert.types.status_update_interval.deserialize_json(
                data["statusUpdateInterval"]
            )
        )
    if data.get("timing") is not None:
        import capo_mediaconvert.types.timing

        out["timing"] = capo_mediaconvert.types.timing.deserialize_json(data["timing"])
    if data.get("userMetadata") is not None:
        import capo_mediaconvert.types.__map_of__string

        out["user_metadata"] = (
            capo_mediaconvert.types.__map_of__string.deserialize_json(
                data["userMetadata"]
            )
        )
    if data.get("warnings") is not None:
        import capo_mediaconvert.types.__list_of_warning_group

        out["warnings"] = (
            capo_mediaconvert.types.__list_of_warning_group.deserialize_json(
                data["warnings"]
            )
        )
    return out
