"""Generated from Smithy shape ``com.amazonaws.transcribe#CreateVocabularyFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.data_access_role_arn
    import capo_transcribe.types.encryption_configuration
    import capo_transcribe.types.language_code
    import capo_transcribe.types.tag_list
    import capo_transcribe.types.uri
    import capo_transcribe.types.vocabulary_filter_name
    import capo_transcribe.types.words


class CreateVocabularyFilterRequest(TypedDict, closed=True):
    vocabulary_filter_name: (
        "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    )
    """<p>A unique name, chosen by you, for your new custom vocabulary filter.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new custom vocabulary filter with the same name as an existing custom vocabulary filter, you get a <code>ConflictException</code> error.</p>"""
    language_code: "capo_transcribe.types.language_code.LanguageCode"
    """<p>The language code that represents the language of the entries in your vocabulary filter. Each custom vocabulary filter must contain terms in only one language.</p> <p>A custom vocabulary filter can only be used to transcribe files in the same language as the filter. For example, if you create a custom vocabulary filter using US English (<code>en-US</code>), you can only apply this filter to files that contain English audio.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p>"""
    words: NotRequired["capo_transcribe.types.words.Words"]
    """<p>Use this parameter if you want to create your custom vocabulary filter by including all desired terms, as comma-separated values, within your request. The other option for creating your vocabulary filter is to save your entries in a text file and upload them to an Amazon S3 bucket, then specify the location of your file using the <code>VocabularyFilterFileUri</code> parameter.</p> <p>Note that if you include <code>Words</code> in your request, you cannot use <code>VocabularyFilterFileUri</code>; you must choose one or the other.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p>"""
    vocabulary_filter_file_uri: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location of the text file that contains your custom vocabulary filter terms. The URI must be located in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-filter-file.txt</code> </p> <p>Note that if you include <code>VocabularyFilterFileUri</code> in your request, you cannot use <code>Words</code>; you must choose one or the other.</p>"""
    tags: NotRequired["capo_transcribe.types.tag_list.TagList"]
    """<p>Adds one or more custom tags, each in the form of a key:value pair, to a new custom vocabulary filter at the time you create this new vocabulary filter.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>"""
    data_access_role_arn: NotRequired[
        "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files (in this case, your custom vocabulary filter). If you include <code>EncryptionConfiguration</code> in your request, this role must also have permissions to access the specified KMS key. If the role that you specify doesn’t have the appropriate permissions, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>"""
    encryption_configuration: NotRequired[
        "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Specifies the encryption configuration for your custom vocabulary filter. Your vocabulary filter artifacts are encrypted with the specified KMS key or with an AWS-owned key if a key is not supplied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVocabularyFilterRequest) -> dict:
    out: dict = {}
    out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    import capo_transcribe.types.language_code

    out["LanguageCode"] = capo_transcribe.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "words" in value:
        import capo_transcribe.types.words

        out["Words"] = capo_transcribe.types.words.serialize_aws_json_1_1(
            value["words"]
        )
    if "vocabulary_filter_file_uri" in value:
        out["VocabularyFilterFileUri"] = value["vocabulary_filter_file_uri"]
    if "tags" in value:
        import capo_transcribe.types.tag_list

        out["Tags"] = capo_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
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


def deserialize_aws_json_1_1(data: dict) -> CreateVocabularyFilterRequest:
    out: CreateVocabularyFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyFilterName") is not None:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    else:
        raise DeserializationError(
            "CreateVocabularyFilterRequest.vocabulary_filter_name required"
        )
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = (
            capo_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "CreateVocabularyFilterRequest.language_code required"
        )
    if data.get("Words") is not None:
        import capo_transcribe.types.words

        out["words"] = capo_transcribe.types.words.deserialize_aws_json_1_1(
            data["Words"]
        )
    if data.get("VocabularyFilterFileUri") is not None:
        out["vocabulary_filter_file_uri"] = data["VocabularyFilterFileUri"]
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
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
