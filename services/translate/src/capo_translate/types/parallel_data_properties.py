"""Generated from Smithy shape ``com.amazonaws.translate#ParallelDataProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.description
    import capo_translate.types.encryption_key
    import capo_translate.types.language_code_string
    import capo_translate.types.language_code_string_list
    import capo_translate.types.long
    import capo_translate.types.parallel_data_arn
    import capo_translate.types.parallel_data_config
    import capo_translate.types.parallel_data_status
    import capo_translate.types.resource_name
    import capo_translate.types.timestamp
    import capo_translate.types.unbounded_length_string


class ParallelDataProperties(TypedDict, closed=True):
    name: NotRequired["capo_translate.types.resource_name.ResourceName"]
    """<p>The custom name assigned to the parallel data resource.</p>"""
    arn: NotRequired["capo_translate.types.parallel_data_arn.ParallelDataArn"]
    """<p>The Amazon Resource Name (ARN) of the parallel data resource.</p>"""
    description: NotRequired["capo_translate.types.description.Description"]
    """<p>The description assigned to the parallel data resource.</p>"""
    status: NotRequired["capo_translate.types.parallel_data_status.ParallelDataStatus"]
    """<p>The status of the parallel data resource. When the parallel data is ready for you to use, the status is <code>ACTIVE</code>.</p>"""
    source_language_code: NotRequired[
        "capo_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>The source language of the translations in the parallel data file.</p>"""
    target_language_codes: NotRequired[
        "capo_translate.types.language_code_string_list.LanguageCodeStringList"
    ]
    """<p>The language codes for the target languages available in the parallel data file. All possible target languages are returned as an array.</p>"""
    parallel_data_config: NotRequired[
        "capo_translate.types.parallel_data_config.ParallelDataConfig"
    ]
    """<p>Specifies the format and S3 location of the parallel data input file.</p>"""
    message: NotRequired[
        "capo_translate.types.unbounded_length_string.UnboundedLengthString"
    ]
    """<p>Additional information from Amazon Translate about the parallel data resource. </p>"""
    imported_data_size: NotRequired["capo_translate.types.long.Long"]
    """<p>The number of UTF-8 characters that Amazon Translate imported from the parallel data input file. This number includes only the characters in your translation examples. It does not include characters that are used to format your file. For example, if you provided a Translation Memory Exchange (.tmx) file, this number does not include the tags.</p>"""
    imported_record_count: NotRequired["capo_translate.types.long.Long"]
    """<p>The number of records successfully imported from the parallel data input file.</p>"""
    failed_record_count: NotRequired["capo_translate.types.long.Long"]
    """<p>The number of records unsuccessfully imported from the parallel data input file.</p>"""
    skipped_record_count: NotRequired["capo_translate.types.long.Long"]
    """<p>The number of items in the input file that Amazon Translate skipped when you created or updated the parallel data resource. For example, Amazon Translate skips empty records, empty target texts, and empty lines.</p>"""
    encryption_key: NotRequired["capo_translate.types.encryption_key.EncryptionKey"]
    created_at: NotRequired["capo_translate.types.timestamp.Timestamp"]
    """<p>The time at which the parallel data resource was created.</p>"""
    last_updated_at: NotRequired["capo_translate.types.timestamp.Timestamp"]
    """<p>The time at which the parallel data resource was last updated.</p>"""
    latest_update_attempt_status: NotRequired[
        "capo_translate.types.parallel_data_status.ParallelDataStatus"
    ]
    """<p>The status of the most recent update attempt for the parallel data resource.</p>"""
    latest_update_attempt_at: NotRequired["capo_translate.types.timestamp.Timestamp"]
    """<p>The time that the most recent update was attempted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelDataProperties) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_translate.types.parallel_data_status

        out["Status"] = (
            capo_translate.types.parallel_data_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "source_language_code" in value:
        out["SourceLanguageCode"] = value["source_language_code"]
    if "target_language_codes" in value:
        import capo_translate.types.language_code_string_list

        out["TargetLanguageCodes"] = (
            capo_translate.types.language_code_string_list.serialize_aws_json_1_1(
                value["target_language_codes"]
            )
        )
    if "parallel_data_config" in value:
        import capo_translate.types.parallel_data_config

        out["ParallelDataConfig"] = (
            capo_translate.types.parallel_data_config.serialize_aws_json_1_1(
                value["parallel_data_config"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "imported_data_size" in value:
        out["ImportedDataSize"] = value["imported_data_size"]
    if "imported_record_count" in value:
        out["ImportedRecordCount"] = value["imported_record_count"]
    if "failed_record_count" in value:
        out["FailedRecordCount"] = value["failed_record_count"]
    if "skipped_record_count" in value:
        out["SkippedRecordCount"] = value["skipped_record_count"]
    if "encryption_key" in value:
        import capo_translate.types.encryption_key

        out["EncryptionKey"] = (
            capo_translate.types.encryption_key.serialize_aws_json_1_1(
                value["encryption_key"]
            )
        )
    if "created_at" in value:
        import capo_translate.types.timestamp

        out["CreatedAt"] = capo_translate.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_translate.types.timestamp

        out["LastUpdatedAt"] = capo_translate.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_at"]
        )
    if "latest_update_attempt_status" in value:
        import capo_translate.types.parallel_data_status

        out["LatestUpdateAttemptStatus"] = (
            capo_translate.types.parallel_data_status.serialize_aws_json_1_1(
                value["latest_update_attempt_status"]
            )
        )
    if "latest_update_attempt_at" in value:
        import capo_translate.types.timestamp

        out["LatestUpdateAttemptAt"] = (
            capo_translate.types.timestamp.serialize_aws_json_1_1(
                value["latest_update_attempt_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParallelDataProperties:
    out: ParallelDataProperties = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_translate.types.parallel_data_status

        out["status"] = (
            capo_translate.types.parallel_data_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("SourceLanguageCode") is not None:
        out["source_language_code"] = data["SourceLanguageCode"]
    if data.get("TargetLanguageCodes") is not None:
        import capo_translate.types.language_code_string_list

        out["target_language_codes"] = (
            capo_translate.types.language_code_string_list.deserialize_aws_json_1_1(
                data["TargetLanguageCodes"]
            )
        )
    if data.get("ParallelDataConfig") is not None:
        import capo_translate.types.parallel_data_config

        out["parallel_data_config"] = (
            capo_translate.types.parallel_data_config.deserialize_aws_json_1_1(
                data["ParallelDataConfig"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ImportedDataSize") is not None:
        out["imported_data_size"] = data["ImportedDataSize"]
    if data.get("ImportedRecordCount") is not None:
        out["imported_record_count"] = data["ImportedRecordCount"]
    if data.get("FailedRecordCount") is not None:
        out["failed_record_count"] = data["FailedRecordCount"]
    if data.get("SkippedRecordCount") is not None:
        out["skipped_record_count"] = data["SkippedRecordCount"]
    if data.get("EncryptionKey") is not None:
        import capo_translate.types.encryption_key

        out["encryption_key"] = (
            capo_translate.types.encryption_key.deserialize_aws_json_1_1(
                data["EncryptionKey"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_translate.types.timestamp

        out["created_at"] = capo_translate.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_translate.types.timestamp

        out["last_updated_at"] = (
            capo_translate.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedAt"]
            )
        )
    if data.get("LatestUpdateAttemptStatus") is not None:
        import capo_translate.types.parallel_data_status

        out["latest_update_attempt_status"] = (
            capo_translate.types.parallel_data_status.deserialize_aws_json_1_1(
                data["LatestUpdateAttemptStatus"]
            )
        )
    if data.get("LatestUpdateAttemptAt") is not None:
        import capo_translate.types.timestamp

        out["latest_update_attempt_at"] = (
            capo_translate.types.timestamp.deserialize_aws_json_1_1(
                data["LatestUpdateAttemptAt"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ParallelDataProperties) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_translate.types.parallel_data_status

        out["Status"] = capo_translate.types.parallel_data_status.serialize_cbor(
            value["status"]
        )
    if "source_language_code" in value:
        out["SourceLanguageCode"] = value["source_language_code"]
    if "target_language_codes" in value:
        import capo_translate.types.language_code_string_list

        out["TargetLanguageCodes"] = (
            capo_translate.types.language_code_string_list.serialize_cbor(
                value["target_language_codes"]
            )
        )
    if "parallel_data_config" in value:
        import capo_translate.types.parallel_data_config

        out["ParallelDataConfig"] = (
            capo_translate.types.parallel_data_config.serialize_cbor(
                value["parallel_data_config"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "imported_data_size" in value:
        out["ImportedDataSize"] = value["imported_data_size"]
    if "imported_record_count" in value:
        out["ImportedRecordCount"] = value["imported_record_count"]
    if "failed_record_count" in value:
        out["FailedRecordCount"] = value["failed_record_count"]
    if "skipped_record_count" in value:
        out["SkippedRecordCount"] = value["skipped_record_count"]
    if "encryption_key" in value:
        import capo_translate.types.encryption_key

        out["EncryptionKey"] = capo_translate.types.encryption_key.serialize_cbor(
            value["encryption_key"]
        )
    if "created_at" in value:
        import capo_translate.types.timestamp

        out["CreatedAt"] = capo_translate.types.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_translate.types.timestamp

        out["LastUpdatedAt"] = capo_translate.types.timestamp.serialize_cbor(
            value["last_updated_at"]
        )
    if "latest_update_attempt_status" in value:
        import capo_translate.types.parallel_data_status

        out["LatestUpdateAttemptStatus"] = (
            capo_translate.types.parallel_data_status.serialize_cbor(
                value["latest_update_attempt_status"]
            )
        )
    if "latest_update_attempt_at" in value:
        import capo_translate.types.timestamp

        out["LatestUpdateAttemptAt"] = capo_translate.types.timestamp.serialize_cbor(
            value["latest_update_attempt_at"]
        )
    return out


def deserialize_cbor(data: dict) -> ParallelDataProperties:
    out: ParallelDataProperties = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_translate.types.parallel_data_status

        out["status"] = capo_translate.types.parallel_data_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("SourceLanguageCode") is not None:
        out["source_language_code"] = data["SourceLanguageCode"]
    if data.get("TargetLanguageCodes") is not None:
        import capo_translate.types.language_code_string_list

        out["target_language_codes"] = (
            capo_translate.types.language_code_string_list.deserialize_cbor(
                data["TargetLanguageCodes"]
            )
        )
    if data.get("ParallelDataConfig") is not None:
        import capo_translate.types.parallel_data_config

        out["parallel_data_config"] = (
            capo_translate.types.parallel_data_config.deserialize_cbor(
                data["ParallelDataConfig"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ImportedDataSize") is not None:
        out["imported_data_size"] = data["ImportedDataSize"]
    if data.get("ImportedRecordCount") is not None:
        out["imported_record_count"] = data["ImportedRecordCount"]
    if data.get("FailedRecordCount") is not None:
        out["failed_record_count"] = data["FailedRecordCount"]
    if data.get("SkippedRecordCount") is not None:
        out["skipped_record_count"] = data["SkippedRecordCount"]
    if data.get("EncryptionKey") is not None:
        import capo_translate.types.encryption_key

        out["encryption_key"] = capo_translate.types.encryption_key.deserialize_cbor(
            data["EncryptionKey"]
        )
    if data.get("CreatedAt") is not None:
        import capo_translate.types.timestamp

        out["created_at"] = capo_translate.types.timestamp.deserialize_cbor(
            data["CreatedAt"]
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_translate.types.timestamp

        out["last_updated_at"] = capo_translate.types.timestamp.deserialize_cbor(
            data["LastUpdatedAt"]
        )
    if data.get("LatestUpdateAttemptStatus") is not None:
        import capo_translate.types.parallel_data_status

        out["latest_update_attempt_status"] = (
            capo_translate.types.parallel_data_status.deserialize_cbor(
                data["LatestUpdateAttemptStatus"]
            )
        )
    if data.get("LatestUpdateAttemptAt") is not None:
        import capo_translate.types.timestamp

        out["latest_update_attempt_at"] = (
            capo_translate.types.timestamp.deserialize_cbor(
                data["LatestUpdateAttemptAt"]
            )
        )
    return out
