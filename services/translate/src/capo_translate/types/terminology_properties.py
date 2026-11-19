"""Generated from Smithy shape ``com.amazonaws.translate#TerminologyProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.description
    import capo_translate.types.directionality
    import capo_translate.types.encryption_key
    import capo_translate.types.integer
    import capo_translate.types.language_code_string
    import capo_translate.types.language_code_string_list
    import capo_translate.types.resource_name
    import capo_translate.types.terminology_arn
    import capo_translate.types.terminology_data_format
    import capo_translate.types.timestamp
    import capo_translate.types.unbounded_length_string


class TerminologyProperties(TypedDict, closed=True):
    name: NotRequired["capo_translate.types.resource_name.ResourceName"]
    """<p>The name of the custom terminology.</p>"""
    description: NotRequired["capo_translate.types.description.Description"]
    """<p>The description of the custom terminology properties.</p>"""
    arn: NotRequired["capo_translate.types.terminology_arn.TerminologyArn"]
    """<p> The Amazon Resource Name (ARN) of the custom terminology. </p>"""
    source_language_code: NotRequired[
        "capo_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>The language code for the source text of the translation request for which the custom terminology is being used.</p>"""
    target_language_codes: NotRequired[
        "capo_translate.types.language_code_string_list.LanguageCodeStringList"
    ]
    """<p>The language codes for the target languages available with the custom terminology resource. All possible target languages are returned in array.</p>"""
    encryption_key: NotRequired["capo_translate.types.encryption_key.EncryptionKey"]
    """<p>The encryption key for the custom terminology.</p>"""
    size_bytes: NotRequired["capo_translate.types.integer.Integer"]
    """<p>The size of the file used when importing a custom terminology.</p>"""
    term_count: NotRequired["capo_translate.types.integer.Integer"]
    """<p>The number of terms included in the custom terminology.</p>"""
    created_at: NotRequired["capo_translate.types.timestamp.Timestamp"]
    """<p>The time at which the custom terminology was created, based on the timestamp.</p>"""
    last_updated_at: NotRequired["capo_translate.types.timestamp.Timestamp"]
    """<p>The time at which the custom terminology was last update, based on the timestamp.</p>"""
    directionality: NotRequired["capo_translate.types.directionality.Directionality"]
    """<p>The directionality of your terminology resource indicates whether it has one source language (uni-directional) or multiple (multi-directional). </p> <dl> <dt>UNI</dt> <dd> <p>The terminology resource has one source language (the first column in a CSV file), and all of its other languages are target languages.</p> </dd> <dt>MULTI</dt> <dd> <p>Any language in the terminology resource can be the source language.</p> </dd> </dl>"""
    message: NotRequired[
        "capo_translate.types.unbounded_length_string.UnboundedLengthString"
    ]
    """<p>Additional information from Amazon Translate about the terminology resource.</p>"""
    skipped_term_count: NotRequired["capo_translate.types.integer.Integer"]
    """<p>The number of terms in the input file that Amazon Translate skipped when you created or updated the terminology resource.</p>"""
    format: NotRequired[
        "capo_translate.types.terminology_data_format.TerminologyDataFormat"
    ]
    """<p>The format of the custom terminology input file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminologyProperties) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "source_language_code" in value:
        out["SourceLanguageCode"] = value["source_language_code"]
    if "target_language_codes" in value:
        import capo_translate.types.language_code_string_list

        out["TargetLanguageCodes"] = (
            capo_translate.types.language_code_string_list.serialize_aws_json_1_1(
                value["target_language_codes"]
            )
        )
    if "encryption_key" in value:
        import capo_translate.types.encryption_key

        out["EncryptionKey"] = (
            capo_translate.types.encryption_key.serialize_aws_json_1_1(
                value["encryption_key"]
            )
        )
    if "size_bytes" in value:
        out["SizeBytes"] = value["size_bytes"]
    if "term_count" in value:
        out["TermCount"] = value["term_count"]
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
    if "directionality" in value:
        import capo_translate.types.directionality

        out["Directionality"] = (
            capo_translate.types.directionality.serialize_aws_json_1_1(
                value["directionality"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "skipped_term_count" in value:
        out["SkippedTermCount"] = value["skipped_term_count"]
    if "format" in value:
        import capo_translate.types.terminology_data_format

        out["Format"] = (
            capo_translate.types.terminology_data_format.serialize_aws_json_1_1(
                value["format"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminologyProperties:
    out: TerminologyProperties = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("SourceLanguageCode") is not None:
        out["source_language_code"] = data["SourceLanguageCode"]
    if data.get("TargetLanguageCodes") is not None:
        import capo_translate.types.language_code_string_list

        out["target_language_codes"] = (
            capo_translate.types.language_code_string_list.deserialize_aws_json_1_1(
                data["TargetLanguageCodes"]
            )
        )
    if data.get("EncryptionKey") is not None:
        import capo_translate.types.encryption_key

        out["encryption_key"] = (
            capo_translate.types.encryption_key.deserialize_aws_json_1_1(
                data["EncryptionKey"]
            )
        )
    if data.get("SizeBytes") is not None:
        out["size_bytes"] = data["SizeBytes"]
    if data.get("TermCount") is not None:
        out["term_count"] = data["TermCount"]
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
    if data.get("Directionality") is not None:
        import capo_translate.types.directionality

        out["directionality"] = (
            capo_translate.types.directionality.deserialize_aws_json_1_1(
                data["Directionality"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("SkippedTermCount") is not None:
        out["skipped_term_count"] = data["SkippedTermCount"]
    if data.get("Format") is not None:
        import capo_translate.types.terminology_data_format

        out["format"] = (
            capo_translate.types.terminology_data_format.deserialize_aws_json_1_1(
                data["Format"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TerminologyProperties) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "source_language_code" in value:
        out["SourceLanguageCode"] = value["source_language_code"]
    if "target_language_codes" in value:
        import capo_translate.types.language_code_string_list

        out["TargetLanguageCodes"] = (
            capo_translate.types.language_code_string_list.serialize_cbor(
                value["target_language_codes"]
            )
        )
    if "encryption_key" in value:
        import capo_translate.types.encryption_key

        out["EncryptionKey"] = capo_translate.types.encryption_key.serialize_cbor(
            value["encryption_key"]
        )
    if "size_bytes" in value:
        out["SizeBytes"] = value["size_bytes"]
    if "term_count" in value:
        out["TermCount"] = value["term_count"]
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
    if "directionality" in value:
        import capo_translate.types.directionality

        out["Directionality"] = capo_translate.types.directionality.serialize_cbor(
            value["directionality"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "skipped_term_count" in value:
        out["SkippedTermCount"] = value["skipped_term_count"]
    if "format" in value:
        import capo_translate.types.terminology_data_format

        out["Format"] = capo_translate.types.terminology_data_format.serialize_cbor(
            value["format"]
        )
    return out


def deserialize_cbor(data: dict) -> TerminologyProperties:
    out: TerminologyProperties = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("SourceLanguageCode") is not None:
        out["source_language_code"] = data["SourceLanguageCode"]
    if data.get("TargetLanguageCodes") is not None:
        import capo_translate.types.language_code_string_list

        out["target_language_codes"] = (
            capo_translate.types.language_code_string_list.deserialize_cbor(
                data["TargetLanguageCodes"]
            )
        )
    if data.get("EncryptionKey") is not None:
        import capo_translate.types.encryption_key

        out["encryption_key"] = capo_translate.types.encryption_key.deserialize_cbor(
            data["EncryptionKey"]
        )
    if data.get("SizeBytes") is not None:
        out["size_bytes"] = data["SizeBytes"]
    if data.get("TermCount") is not None:
        out["term_count"] = data["TermCount"]
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
    if data.get("Directionality") is not None:
        import capo_translate.types.directionality

        out["directionality"] = capo_translate.types.directionality.deserialize_cbor(
            data["Directionality"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("SkippedTermCount") is not None:
        out["skipped_term_count"] = data["SkippedTermCount"]
    if data.get("Format") is not None:
        import capo_translate.types.terminology_data_format

        out["format"] = capo_translate.types.terminology_data_format.deserialize_cbor(
            data["Format"]
        )
    return out
