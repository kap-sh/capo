"""Generated from Smithy shape ``com.amazonaws.transcribe#GetVocabularyFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.data_access_role_arn
    import capo_transcribe.types.date_time
    import capo_transcribe.types.encryption_configuration
    import capo_transcribe.types.language_code
    import capo_transcribe.types.uri
    import capo_transcribe.types.vocabulary_filter_name


class GetVocabularyFilterResponse(TypedDict, closed=True):
    vocabulary_filter_name: NotRequired[
        "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>The name of the custom vocabulary filter you requested information about.</p>"""
    language_code: NotRequired["capo_transcribe.types.language_code.LanguageCode"]
    """<p>The language code you selected for your custom vocabulary filter.</p>"""
    last_modified_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom vocabulary filter was last modified.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    download_uri: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location where the custom vocabulary filter is stored; use this URI to view or download the custom vocabulary filter.</p>"""
    data_access_role_arn: NotRequired[
        "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role used to access the Amazon S3 bucket that contains your input files and, if applicable, the KMS key specified in <code>EncryptionConfiguration</code>.</p>"""
    encryption_configuration: NotRequired[
        "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration used for your custom vocabulary filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetVocabularyFilterResponse) -> dict:
    out: dict = {}
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    if "language_code" in value:
        import capo_transcribe.types.language_code

        out["LanguageCode"] = (
            capo_transcribe.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "last_modified_time" in value:
        import capo_transcribe.types.date_time

        out["LastModifiedTime"] = (
            capo_transcribe.types.date_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "download_uri" in value:
        out["DownloadUri"] = value["download_uri"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "encryption_configuration" in value:
        import capo_transcribe.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_transcribe.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetVocabularyFilterResponse:
    out: GetVocabularyFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyFilterName") is not None:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = (
            capo_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_transcribe.types.date_time

        out["last_modified_time"] = (
            capo_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("DownloadUri") is not None:
        out["download_uri"] = data["DownloadUri"]
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_transcribe.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_transcribe.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetVocabularyFilterResponse) -> dict:
    out: dict = {}
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    if "language_code" in value:
        import capo_transcribe.types.language_code

        out["LanguageCode"] = capo_transcribe.types.language_code.serialize_cbor(
            value["language_code"]
        )
    if "last_modified_time" in value:
        import capo_transcribe.types.date_time

        out["LastModifiedTime"] = capo_transcribe.types.date_time.serialize_cbor(
            value["last_modified_time"]
        )
    if "download_uri" in value:
        out["DownloadUri"] = value["download_uri"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "encryption_configuration" in value:
        import capo_transcribe.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_transcribe.types.encryption_configuration.serialize_cbor(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetVocabularyFilterResponse:
    out: GetVocabularyFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyFilterName") is not None:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = capo_transcribe.types.language_code.deserialize_cbor(
            data["LanguageCode"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_transcribe.types.date_time

        out["last_modified_time"] = capo_transcribe.types.date_time.deserialize_cbor(
            data["LastModifiedTime"]
        )
    if data.get("DownloadUri") is not None:
        out["download_uri"] = data["DownloadUri"]
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_transcribe.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_transcribe.types.encryption_configuration.deserialize_cbor(
                data["EncryptionConfiguration"]
            )
        )
    return out
