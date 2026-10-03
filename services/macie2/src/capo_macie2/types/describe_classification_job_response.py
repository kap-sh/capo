"""Generated from Smithy shape ``com.amazonaws.macie2#DescribeClassificationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__boolean
    import capo_macie2.types.__integer
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.__string
    import capo_macie2.types.__timestamp_iso8601
    import capo_macie2.types.job_schedule_frequency
    import capo_macie2.types.job_status
    import capo_macie2.types.job_type
    import capo_macie2.types.last_run_error_status
    import capo_macie2.types.managed_data_identifier_selector
    import capo_macie2.types.s3_job_definition
    import capo_macie2.types.statistics
    import capo_macie2.types.tag_map
    import capo_macie2.types.user_paused_details


class DescribeClassificationJobResponse(TypedDict, closed=True):
    allow_list_ids: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array of unique identifiers, one for each allow list that the job is configured to use when it analyzes data.</p>"""
    client_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The token that was provided to ensure the idempotency of the request to create the job.</p>"""
    created_at: NotRequired["capo_macie2.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the job was created.</p>"""
    custom_data_identifier_ids: NotRequired[
        "capo_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of unique identifiers, one for each custom data identifier that the job is configured to use when it analyzes data. This value is null if the job is configured to use only managed data identifiers to analyze data.</p>"""
    description: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The custom description of the job.</p>"""
    initial_run: NotRequired["capo_macie2.types.__boolean.__boolean"]
    """<p>For a recurring job, specifies whether you configured the job to analyze all existing, eligible objects immediately after the job was created (true). If you configured the job to analyze only those objects that were created or changed after the job was created and before the job's first scheduled run, this value is false. This value is also false for a one-time job.</p>"""
    job_arn: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the job.</p>"""
    job_status: NotRequired["capo_macie2.types.job_status.JobStatus"]
    """<p>The current status of the job. Possible values are:</p> <ul><li><p>CANCELLED - You cancelled the job or, if it's a one-time job, you paused the job and didn't resume it within 30 days.</p></li> <li><p>COMPLETE - For a one-time job, Amazon Macie finished processing the data specified for the job. This value doesn't apply to recurring jobs.</p></li> <li><p>IDLE - For a recurring job, the previous scheduled run is complete and the next scheduled run is pending. This value doesn't apply to one-time jobs.</p></li> <li><p>PAUSED - Macie started running the job but additional processing would exceed the monthly sensitive data discovery quota for your account or one or more member accounts that the job analyzes data for.</p></li> <li><p>RUNNING - For a one-time job, the job is in progress. For a recurring job, a scheduled run is in progress.</p></li> <li><p>USER_PAUSED - You paused the job. If you paused the job while it had a status of RUNNING and you don't resume it within 30 days of pausing it, the job or job run will expire and be cancelled, depending on the job's type. To check the expiration date, refer to the UserPausedDetails.jobExpiresAt property.</p></li></ul>"""
    job_type: NotRequired["capo_macie2.types.job_type.JobType"]
    """<p>The schedule for running the job. Possible values are:</p> <ul><li><p>ONE_TIME - The job runs only once.</p></li> <li><p>SCHEDULED - The job runs on a daily, weekly, or monthly basis. The scheduleFrequency property indicates the recurrence pattern for the job.</p></li></ul>"""
    last_run_error_status: NotRequired[
        "capo_macie2.types.last_run_error_status.LastRunErrorStatus"
    ]
    """<p>Specifies whether any account- or bucket-level access errors occurred when the job ran. For a recurring job, this value indicates the error status of the job's most recent run.</p>"""
    last_run_time: NotRequired[
        "capo_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the job started. If the job is a recurring job, this value indicates when the most recent run started or, if the job hasn't run yet, when the job was created.</p>"""
    managed_data_identifier_ids: NotRequired[
        "capo_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of unique identifiers, one for each managed data identifier that the job is explicitly configured to include (use) or exclude (not use) when it analyzes data. Inclusion or exclusion depends on the managed data identifier selection type specified for the job (managedDataIdentifierSelector).</p><p>This value is null if the job's managed data identifier selection type is ALL, NONE, or RECOMMENDED.</p>"""
    managed_data_identifier_selector: NotRequired[
        "capo_macie2.types.managed_data_identifier_selector.ManagedDataIdentifierSelector"
    ]
    """<p>The selection type that determines which managed data identifiers the job uses when it analyzes data. Possible values are:</p> <ul><li><p>ALL - Use all managed data identifiers.</p></li> <li><p>EXCLUDE - Use all managed data identifiers except the ones specified by the managedDataIdentifierIds property.</p></li> <li><p>INCLUDE - Use only the managed data identifiers specified by the managedDataIdentifierIds property.</p></li> <li><p>NONE - Don't use any managed data identifiers. Use only custom data identifiers (customDataIdentifierIds).</p></li> <li><p>RECOMMENDED (default) - Use the recommended set of managed data identifiers.</p></li></ul> <p>If this value is null, the job uses the recommended set of managed data identifiers.</p> <p>If the job is a recurring job and this value is ALL or EXCLUDE, each job run automatically uses new managed data identifiers that are released. If this value is null or RECOMMENDED for a recurring job, each job run uses all the managed data identifiers that are in the recommended set when the run starts.</p> <p>To learn about individual managed data identifiers or determine which ones are in the recommended set, see <a href="https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html">Using managed data identifiers</a> or <a href="https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-mdis-recommended.html">Recommended managed data identifiers</a> in the <i>Amazon Macie User Guide</i>.</p>"""
    name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The custom name of the job.</p>"""
    s3_job_definition: NotRequired[
        "capo_macie2.types.s3_job_definition.S3JobDefinition"
    ]
    """<p>The S3 buckets that contain the objects to analyze, and the scope of that analysis.</p>"""
    sampling_percentage: NotRequired["capo_macie2.types.__integer.__integer"]
    """<p>The sampling depth, as a percentage, that determines the percentage of eligible objects that the job analyzes.</p>"""
    schedule_frequency: NotRequired[
        "capo_macie2.types.job_schedule_frequency.JobScheduleFrequency"
    ]
    """<p>The recurrence pattern for running the job. This value is null if the job is configured to run only once.</p>"""
    statistics: NotRequired["capo_macie2.types.statistics.Statistics"]
    """<p>The number of times that the job has run and processing statistics for the job's current run.</p>"""
    tags: NotRequired["capo_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies which tags (keys and values) are associated with the job.</p>"""
    user_paused_details: NotRequired[
        "capo_macie2.types.user_paused_details.UserPausedDetails"
    ]
    """<p>If the current status of the job is USER_PAUSED, specifies when the job was paused and when the job or job run will expire and be cancelled if it isn't resumed. This value is present only if the value for jobStatus is USER_PAUSED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClassificationJobResponse) -> dict:
    out: dict = {}
    if "allow_list_ids" in value:
        import capo_macie2.types.__list_of__string

        out["allowListIds"] = capo_macie2.types.__list_of__string.serialize_json(
            value["allow_list_ids"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "created_at" in value:
        import capo_macie2.types.__timestamp_iso8601

        out["createdAt"] = capo_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "custom_data_identifier_ids" in value:
        import capo_macie2.types.__list_of__string

        out["customDataIdentifierIds"] = (
            capo_macie2.types.__list_of__string.serialize_json(
                value["custom_data_identifier_ids"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "initial_run" in value:
        out["initialRun"] = value["initial_run"]
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_status" in value:
        import capo_macie2.types.job_status

        out["jobStatus"] = capo_macie2.types.job_status.serialize_json(
            value["job_status"]
        )
    if "job_type" in value:
        import capo_macie2.types.job_type

        out["jobType"] = capo_macie2.types.job_type.serialize_json(value["job_type"])
    if "last_run_error_status" in value:
        import capo_macie2.types.last_run_error_status

        out["lastRunErrorStatus"] = (
            capo_macie2.types.last_run_error_status.serialize_json(
                value["last_run_error_status"]
            )
        )
    if "last_run_time" in value:
        import capo_macie2.types.__timestamp_iso8601

        out["lastRunTime"] = capo_macie2.types.__timestamp_iso8601.serialize_json(
            value["last_run_time"]
        )
    if "managed_data_identifier_ids" in value:
        import capo_macie2.types.__list_of__string

        out["managedDataIdentifierIds"] = (
            capo_macie2.types.__list_of__string.serialize_json(
                value["managed_data_identifier_ids"]
            )
        )
    if "managed_data_identifier_selector" in value:
        import capo_macie2.types.managed_data_identifier_selector

        out["managedDataIdentifierSelector"] = (
            capo_macie2.types.managed_data_identifier_selector.serialize_json(
                value["managed_data_identifier_selector"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "s3_job_definition" in value:
        import capo_macie2.types.s3_job_definition

        out["s3JobDefinition"] = capo_macie2.types.s3_job_definition.serialize_json(
            value["s3_job_definition"]
        )
    if "sampling_percentage" in value:
        out["samplingPercentage"] = value["sampling_percentage"]
    if "schedule_frequency" in value:
        import capo_macie2.types.job_schedule_frequency

        out["scheduleFrequency"] = (
            capo_macie2.types.job_schedule_frequency.serialize_json(
                value["schedule_frequency"]
            )
        )
    if "statistics" in value:
        import capo_macie2.types.statistics

        out["statistics"] = capo_macie2.types.statistics.serialize_json(
            value["statistics"]
        )
    if "tags" in value:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.serialize_json(value["tags"])
    if "user_paused_details" in value:
        import capo_macie2.types.user_paused_details

        out["userPausedDetails"] = capo_macie2.types.user_paused_details.serialize_json(
            value["user_paused_details"]
        )
    return out


def deserialize_json(data: dict) -> DescribeClassificationJobResponse:
    out: DescribeClassificationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("allowListIds") is not None:
        import capo_macie2.types.__list_of__string

        out["allow_list_ids"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["allowListIds"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("createdAt") is not None:
        import capo_macie2.types.__timestamp_iso8601

        out["created_at"] = capo_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if data.get("customDataIdentifierIds") is not None:
        import capo_macie2.types.__list_of__string

        out["custom_data_identifier_ids"] = (
            capo_macie2.types.__list_of__string.deserialize_json(
                data["customDataIdentifierIds"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("initialRun") is not None:
        out["initial_run"] = data["initialRun"]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("jobStatus") is not None:
        import capo_macie2.types.job_status

        out["job_status"] = capo_macie2.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    if data.get("jobType") is not None:
        import capo_macie2.types.job_type

        out["job_type"] = capo_macie2.types.job_type.deserialize_json(data["jobType"])
    if data.get("lastRunErrorStatus") is not None:
        import capo_macie2.types.last_run_error_status

        out["last_run_error_status"] = (
            capo_macie2.types.last_run_error_status.deserialize_json(
                data["lastRunErrorStatus"]
            )
        )
    if data.get("lastRunTime") is not None:
        import capo_macie2.types.__timestamp_iso8601

        out["last_run_time"] = capo_macie2.types.__timestamp_iso8601.deserialize_json(
            data["lastRunTime"]
        )
    if data.get("managedDataIdentifierIds") is not None:
        import capo_macie2.types.__list_of__string

        out["managed_data_identifier_ids"] = (
            capo_macie2.types.__list_of__string.deserialize_json(
                data["managedDataIdentifierIds"]
            )
        )
    if data.get("managedDataIdentifierSelector") is not None:
        import capo_macie2.types.managed_data_identifier_selector

        out["managed_data_identifier_selector"] = (
            capo_macie2.types.managed_data_identifier_selector.deserialize_json(
                data["managedDataIdentifierSelector"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("s3JobDefinition") is not None:
        import capo_macie2.types.s3_job_definition

        out["s3_job_definition"] = capo_macie2.types.s3_job_definition.deserialize_json(
            data["s3JobDefinition"]
        )
    if data.get("samplingPercentage") is not None:
        out["sampling_percentage"] = data["samplingPercentage"]
    if data.get("scheduleFrequency") is not None:
        import capo_macie2.types.job_schedule_frequency

        out["schedule_frequency"] = (
            capo_macie2.types.job_schedule_frequency.deserialize_json(
                data["scheduleFrequency"]
            )
        )
    if data.get("statistics") is not None:
        import capo_macie2.types.statistics

        out["statistics"] = capo_macie2.types.statistics.deserialize_json(
            data["statistics"]
        )
    if data.get("tags") is not None:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.deserialize_json(data["tags"])
    if data.get("userPausedDetails") is not None:
        import capo_macie2.types.user_paused_details

        out["user_paused_details"] = (
            capo_macie2.types.user_paused_details.deserialize_json(
                data["userPausedDetails"]
            )
        )
    return out
