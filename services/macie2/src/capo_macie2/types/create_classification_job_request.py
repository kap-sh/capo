"""Generated from Smithy shape ``com.amazonaws.macie2#CreateClassificationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__boolean
    import capo_macie2.types.__integer
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.__string
    import capo_macie2.types.job_schedule_frequency
    import capo_macie2.types.job_type
    import capo_macie2.types.managed_data_identifier_selector
    import capo_macie2.types.s3_job_definition
    import capo_macie2.types.tag_map


class CreateClassificationJobRequest(TypedDict, closed=True):
    allow_list_ids: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array of unique identifiers, one for each allow list for the job to use when it analyzes data.</p>"""
    client_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>"""
    custom_data_identifier_ids: NotRequired[
        "capo_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of unique identifiers, one for each custom data identifier for the job to use when it analyzes data. To use only managed data identifiers, don't specify a value for this property and specify a value other than NONE for the managedDataIdentifierSelector property.</p>"""
    description: NotRequired["capo_macie2.types.__string.__string"]
    """<p>A custom description of the job. The description can contain as many as 200 characters.</p>"""
    initial_run: NotRequired["capo_macie2.types.__boolean.__boolean"]
    """<p>For a recurring job, specifies whether to analyze all existing, eligible objects immediately after the job is created (true). To analyze only those objects that are created or changed after you create the job and before the job's first scheduled run, set this value to false.</p> <p>If you configure the job to run only once, don't specify a value for this property.</p>"""
    job_type: NotRequired["capo_macie2.types.job_type.JobType"]
    """<p>The schedule for running the job. Valid values are:</p> <ul><li><p>ONE_TIME - Run the job only once. If you specify this value, don't specify a value for the scheduleFrequency property.</p></li> <li><p>SCHEDULED - Run the job on a daily, weekly, or monthly basis. If you specify this value, use the scheduleFrequency property to specify the recurrence pattern for the job.</p></li></ul>"""
    managed_data_identifier_ids: NotRequired[
        "capo_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of unique identifiers, one for each managed data identifier for the job to include (use) or exclude (not use) when it analyzes data. Inclusion or exclusion depends on the managed data identifier selection type that you specify for the job (managedDataIdentifierSelector).</p> <p>To retrieve a list of valid values for this property, use the ListManagedDataIdentifiers operation.</p>"""
    managed_data_identifier_selector: NotRequired[
        "capo_macie2.types.managed_data_identifier_selector.ManagedDataIdentifierSelector"
    ]
    """<p>The selection type to apply when determining which managed data identifiers the job uses to analyze data. Valid values are:</p> <ul><li><p>ALL - Use all managed data identifiers. If you specify this value, don't specify any values for the managedDataIdentifierIds property.</p></li> <li><p>EXCLUDE - Use all managed data identifiers except the ones specified by the managedDataIdentifierIds property.</p></li> <li><p>INCLUDE - Use only the managed data identifiers specified by the managedDataIdentifierIds property.</p></li> <li><p>NONE - Don't use any managed data identifiers. If you specify this value, specify at least one value for the customDataIdentifierIds property and don't specify any values for the managedDataIdentifierIds property.</p></li> <li><p>RECOMMENDED (default) - Use the recommended set of managed data identifiers. If you specify this value, don't specify any values for the managedDataIdentifierIds property.</p></li></ul> <p>If you don't specify a value for this property, the job uses the recommended set of managed data identifiers.</p> <p>If the job is a recurring job and you specify ALL or EXCLUDE, each job run automatically uses new managed data identifiers that are released. If you don't specify a value for this property or you specify RECOMMENDED for a recurring job, each job run automatically uses all the managed data identifiers that are in the recommended set when the run starts.</p> <p>To learn about individual managed data identifiers or determine which ones are in the recommended set, see <a href="https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html">Using managed data identifiers</a> or <a href="https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-mdis-recommended.html">Recommended managed data identifiers</a> in the <i>Amazon Macie User Guide</i>.</p>"""
    name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>A custom name for the job. The name can contain as many as 500 characters.</p>"""
    s3_job_definition: NotRequired[
        "capo_macie2.types.s3_job_definition.S3JobDefinition"
    ]
    """<p>The S3 buckets that contain the objects to analyze, and the scope of that analysis.</p>"""
    sampling_percentage: NotRequired["capo_macie2.types.__integer.__integer"]
    """<p>The sampling depth, as a percentage, for the job to apply when processing objects. This value determines the percentage of eligible objects that the job analyzes. If this value is less than 100, Amazon Macie selects the objects to analyze at random, up to the specified percentage, and analyzes all the data in those objects.</p>"""
    schedule_frequency: NotRequired[
        "capo_macie2.types.job_schedule_frequency.JobScheduleFrequency"
    ]
    """<p>The recurrence pattern for running the job. To run the job only once, don't specify a value for this property and set the value for the jobType property to ONE_TIME.</p>"""
    tags: NotRequired["capo_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies the tags to associate with the job.</p> <p>A job can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClassificationJobRequest) -> dict:
    out: dict = {}
    if "allow_list_ids" in value:
        import capo_macie2.types.__list_of__string

        out["allowListIds"] = capo_macie2.types.__list_of__string.serialize_json(
            value["allow_list_ids"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
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
    if "job_type" in value:
        import capo_macie2.types.job_type

        out["jobType"] = capo_macie2.types.job_type.serialize_json(value["job_type"])
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
    if "tags" in value:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateClassificationJobRequest:
    out: CreateClassificationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("allowListIds") is not None:
        import capo_macie2.types.__list_of__string

        out["allow_list_ids"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["allowListIds"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
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
    if data.get("jobType") is not None:
        import capo_macie2.types.job_type

        out["job_type"] = capo_macie2.types.job_type.deserialize_json(data["jobType"])
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
    if data.get("tags") is not None:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.deserialize_json(data["tags"])
    return out
