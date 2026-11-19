"""Generated from Smithy shape ``com.amazonaws.translate#TextTranslationJobProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.iam_role_arn
    import capo_translate.types.input_data_config
    import capo_translate.types.job_details
    import capo_translate.types.job_id
    import capo_translate.types.job_name
    import capo_translate.types.job_status
    import capo_translate.types.language_code_string
    import capo_translate.types.output_data_config
    import capo_translate.types.resource_name_list
    import capo_translate.types.target_language_code_string_list
    import capo_translate.types.timestamp
    import capo_translate.types.translation_settings
    import capo_translate.types.unbounded_length_string


class TextTranslationJobProperties(TypedDict, closed=True):
    job_id: NotRequired["capo_translate.types.job_id.JobId"]
    """<p>The ID of the translation job.</p>"""
    job_name: NotRequired["capo_translate.types.job_name.JobName"]
    """<p>The user-defined name of the translation job.</p>"""
    job_status: NotRequired["capo_translate.types.job_status.JobStatus"]
    """<p>The status of the translation job.</p>"""
    job_details: NotRequired["capo_translate.types.job_details.JobDetails"]
    """<p>The number of documents successfully and unsuccessfully processed during the translation job.</p>"""
    source_language_code: NotRequired[
        "capo_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>The language code of the language of the source text. The language must be a language supported by Amazon Translate.</p>"""
    target_language_codes: NotRequired[
        "capo_translate.types.target_language_code_string_list.TargetLanguageCodeStringList"
    ]
    """<p>The language code of the language of the target text. The language must be a language supported by Amazon Translate.</p>"""
    terminology_names: NotRequired[
        "capo_translate.types.resource_name_list.ResourceNameList"
    ]
    """<p>A list containing the names of the terminologies applied to a translation job. Only one terminology can be applied per <a>StartTextTranslationJob</a> request at this time.</p>"""
    parallel_data_names: NotRequired[
        "capo_translate.types.resource_name_list.ResourceNameList"
    ]
    """<p>A list containing the names of the parallel data resources applied to the translation job.</p>"""
    message: NotRequired[
        "capo_translate.types.unbounded_length_string.UnboundedLengthString"
    ]
    """<p>An explanation of any errors that may have occurred during the translation job.</p>"""
    submitted_time: NotRequired["capo_translate.types.timestamp.Timestamp"]
    """<p>The time at which the translation job was submitted.</p>"""
    end_time: NotRequired["capo_translate.types.timestamp.Timestamp"]
    """<p>The time at which the translation job ended.</p>"""
    input_data_config: NotRequired[
        "capo_translate.types.input_data_config.InputDataConfig"
    ]
    """<p>The input configuration properties that were specified when the job was requested.</p>"""
    output_data_config: NotRequired[
        "capo_translate.types.output_data_config.OutputDataConfig"
    ]
    """<p>The output configuration properties that were specified when the job was requested.</p>"""
    data_access_role_arn: NotRequired["capo_translate.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of an AWS Identity Access and Management (IAM) role that granted Amazon Translate read access to the job's input data.</p>"""
    settings: NotRequired[
        "capo_translate.types.translation_settings.TranslationSettings"
    ]
    """<p>Settings that modify the translation output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTranslationJobProperties) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import capo_translate.types.job_status

        out["JobStatus"] = capo_translate.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    if "job_details" in value:
        import capo_translate.types.job_details

        out["JobDetails"] = capo_translate.types.job_details.serialize_aws_json_1_1(
            value["job_details"]
        )
    if "source_language_code" in value:
        out["SourceLanguageCode"] = value["source_language_code"]
    if "target_language_codes" in value:
        import capo_translate.types.target_language_code_string_list

        out["TargetLanguageCodes"] = (
            capo_translate.types.target_language_code_string_list.serialize_aws_json_1_1(
                value["target_language_codes"]
            )
        )
    if "terminology_names" in value:
        import capo_translate.types.resource_name_list

        out["TerminologyNames"] = (
            capo_translate.types.resource_name_list.serialize_aws_json_1_1(
                value["terminology_names"]
            )
        )
    if "parallel_data_names" in value:
        import capo_translate.types.resource_name_list

        out["ParallelDataNames"] = (
            capo_translate.types.resource_name_list.serialize_aws_json_1_1(
                value["parallel_data_names"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "submitted_time" in value:
        import capo_translate.types.timestamp

        out["SubmittedTime"] = capo_translate.types.timestamp.serialize_aws_json_1_1(
            value["submitted_time"]
        )
    if "end_time" in value:
        import capo_translate.types.timestamp

        out["EndTime"] = capo_translate.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "input_data_config" in value:
        import capo_translate.types.input_data_config

        out["InputDataConfig"] = (
            capo_translate.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import capo_translate.types.output_data_config

        out["OutputDataConfig"] = (
            capo_translate.types.output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "settings" in value:
        import capo_translate.types.translation_settings

        out["Settings"] = (
            capo_translate.types.translation_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TextTranslationJobProperties:
    out: TextTranslationJobProperties = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobStatus") is not None:
        import capo_translate.types.job_status

        out["job_status"] = capo_translate.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    if data.get("JobDetails") is not None:
        import capo_translate.types.job_details

        out["job_details"] = capo_translate.types.job_details.deserialize_aws_json_1_1(
            data["JobDetails"]
        )
    if data.get("SourceLanguageCode") is not None:
        out["source_language_code"] = data["SourceLanguageCode"]
    if data.get("TargetLanguageCodes") is not None:
        import capo_translate.types.target_language_code_string_list

        out["target_language_codes"] = (
            capo_translate.types.target_language_code_string_list.deserialize_aws_json_1_1(
                data["TargetLanguageCodes"]
            )
        )
    if data.get("TerminologyNames") is not None:
        import capo_translate.types.resource_name_list

        out["terminology_names"] = (
            capo_translate.types.resource_name_list.deserialize_aws_json_1_1(
                data["TerminologyNames"]
            )
        )
    if data.get("ParallelDataNames") is not None:
        import capo_translate.types.resource_name_list

        out["parallel_data_names"] = (
            capo_translate.types.resource_name_list.deserialize_aws_json_1_1(
                data["ParallelDataNames"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("SubmittedTime") is not None:
        import capo_translate.types.timestamp

        out["submitted_time"] = capo_translate.types.timestamp.deserialize_aws_json_1_1(
            data["SubmittedTime"]
        )
    if data.get("EndTime") is not None:
        import capo_translate.types.timestamp

        out["end_time"] = capo_translate.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("InputDataConfig") is not None:
        import capo_translate.types.input_data_config

        out["input_data_config"] = (
            capo_translate.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_translate.types.output_data_config

        out["output_data_config"] = (
            capo_translate.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("Settings") is not None:
        import capo_translate.types.translation_settings

        out["settings"] = (
            capo_translate.types.translation_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TextTranslationJobProperties) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import capo_translate.types.job_status

        out["JobStatus"] = capo_translate.types.job_status.serialize_cbor(
            value["job_status"]
        )
    if "job_details" in value:
        import capo_translate.types.job_details

        out["JobDetails"] = capo_translate.types.job_details.serialize_cbor(
            value["job_details"]
        )
    if "source_language_code" in value:
        out["SourceLanguageCode"] = value["source_language_code"]
    if "target_language_codes" in value:
        import capo_translate.types.target_language_code_string_list

        out["TargetLanguageCodes"] = (
            capo_translate.types.target_language_code_string_list.serialize_cbor(
                value["target_language_codes"]
            )
        )
    if "terminology_names" in value:
        import capo_translate.types.resource_name_list

        out["TerminologyNames"] = (
            capo_translate.types.resource_name_list.serialize_cbor(
                value["terminology_names"]
            )
        )
    if "parallel_data_names" in value:
        import capo_translate.types.resource_name_list

        out["ParallelDataNames"] = (
            capo_translate.types.resource_name_list.serialize_cbor(
                value["parallel_data_names"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "submitted_time" in value:
        import capo_translate.types.timestamp

        out["SubmittedTime"] = capo_translate.types.timestamp.serialize_cbor(
            value["submitted_time"]
        )
    if "end_time" in value:
        import capo_translate.types.timestamp

        out["EndTime"] = capo_translate.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "input_data_config" in value:
        import capo_translate.types.input_data_config

        out["InputDataConfig"] = capo_translate.types.input_data_config.serialize_cbor(
            value["input_data_config"]
        )
    if "output_data_config" in value:
        import capo_translate.types.output_data_config

        out["OutputDataConfig"] = (
            capo_translate.types.output_data_config.serialize_cbor(
                value["output_data_config"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "settings" in value:
        import capo_translate.types.translation_settings

        out["Settings"] = capo_translate.types.translation_settings.serialize_cbor(
            value["settings"]
        )
    return out


def deserialize_cbor(data: dict) -> TextTranslationJobProperties:
    out: TextTranslationJobProperties = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobStatus") is not None:
        import capo_translate.types.job_status

        out["job_status"] = capo_translate.types.job_status.deserialize_cbor(
            data["JobStatus"]
        )
    if data.get("JobDetails") is not None:
        import capo_translate.types.job_details

        out["job_details"] = capo_translate.types.job_details.deserialize_cbor(
            data["JobDetails"]
        )
    if data.get("SourceLanguageCode") is not None:
        out["source_language_code"] = data["SourceLanguageCode"]
    if data.get("TargetLanguageCodes") is not None:
        import capo_translate.types.target_language_code_string_list

        out["target_language_codes"] = (
            capo_translate.types.target_language_code_string_list.deserialize_cbor(
                data["TargetLanguageCodes"]
            )
        )
    if data.get("TerminologyNames") is not None:
        import capo_translate.types.resource_name_list

        out["terminology_names"] = (
            capo_translate.types.resource_name_list.deserialize_cbor(
                data["TerminologyNames"]
            )
        )
    if data.get("ParallelDataNames") is not None:
        import capo_translate.types.resource_name_list

        out["parallel_data_names"] = (
            capo_translate.types.resource_name_list.deserialize_cbor(
                data["ParallelDataNames"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("SubmittedTime") is not None:
        import capo_translate.types.timestamp

        out["submitted_time"] = capo_translate.types.timestamp.deserialize_cbor(
            data["SubmittedTime"]
        )
    if data.get("EndTime") is not None:
        import capo_translate.types.timestamp

        out["end_time"] = capo_translate.types.timestamp.deserialize_cbor(
            data["EndTime"]
        )
    if data.get("InputDataConfig") is not None:
        import capo_translate.types.input_data_config

        out["input_data_config"] = (
            capo_translate.types.input_data_config.deserialize_cbor(
                data["InputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_translate.types.output_data_config

        out["output_data_config"] = (
            capo_translate.types.output_data_config.deserialize_cbor(
                data["OutputDataConfig"]
            )
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("Settings") is not None:
        import capo_translate.types.translation_settings

        out["settings"] = capo_translate.types.translation_settings.deserialize_cbor(
            data["Settings"]
        )
    return out
