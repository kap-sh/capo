"""Generated from Smithy shape ``com.amazonaws.transcribe#UpdateVocabularyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.data_access_role_arn
    import capo_transcribe.types.encryption_configuration
    import capo_transcribe.types.language_code
    import capo_transcribe.types.phrases
    import capo_transcribe.types.uri
    import capo_transcribe.types.vocabulary_name


class UpdateVocabularyRequest(TypedDict, closed=True):
    vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName"
    """<p>The name of the custom vocabulary you want to update. Custom vocabulary names are case sensitive.</p>"""
    language_code: "capo_transcribe.types.language_code.LanguageCode"
    """<p>The language code that represents the language of the entries in the custom vocabulary you want to update. Each custom vocabulary must contain terms in only one language.</p> <p>A custom vocabulary can only be used to transcribe files in the same language as the custom vocabulary. For example, if you create a custom vocabulary using US English (<code>en-US</code>), you can only apply this custom vocabulary to files that contain English audio.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p>"""
    phrases: NotRequired["capo_transcribe.types.phrases.Phrases"]
    """<p>Use this parameter if you want to update your custom vocabulary by including all desired terms, as comma-separated values, within your request. The other option for updating your custom vocabulary is to save your entries in a text file and upload them to an Amazon S3 bucket, then specify the location of your file using the <code>VocabularyFileUri</code> parameter.</p> <p>Note that if you include <code>Phrases</code> in your request, you cannot use <code>VocabularyFileUri</code>; you must choose one or the other.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p>"""
    vocabulary_file_uri: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location of the text file that contains your custom vocabulary. The URI must be located in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-file.txt</code> </p> <p>Note that if you include <code>VocabularyFileUri</code> in your request, you cannot use the <code>Phrases</code> flag; you must choose one or the other.</p>"""
    data_access_role_arn: NotRequired[
        "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files (in this case, your custom vocabulary). If you include <code>EncryptionConfiguration</code> in your request, this role must also have permissions to access the specified KMS key. If the role that you specify doesn’t have the appropriate permissions, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>"""
    encryption_configuration: NotRequired[
        "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Specifies the new encryption configuration for your custom vocabulary. The vocabulary artifacts are re-encrypted in place using the specified KMS key or with an AWS-owned key if a key is not supplied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVocabularyRequest) -> dict:
    out: dict = {}
    out["VocabularyName"] = value["vocabulary_name"]
    import capo_transcribe.types.language_code

    out["LanguageCode"] = capo_transcribe.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "phrases" in value:
        import capo_transcribe.types.phrases

        out["Phrases"] = capo_transcribe.types.phrases.serialize_aws_json_1_1(
            value["phrases"]
        )
    if "vocabulary_file_uri" in value:
        out["VocabularyFileUri"] = value["vocabulary_file_uri"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateVocabularyRequest:
    out: UpdateVocabularyRequest = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    else:
        raise DeserializationError("UpdateVocabularyRequest.vocabulary_name required")
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = (
            capo_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("UpdateVocabularyRequest.language_code required")
    if data.get("Phrases") is not None:
        import capo_transcribe.types.phrases

        out["phrases"] = capo_transcribe.types.phrases.deserialize_aws_json_1_1(
            data["Phrases"]
        )
    if data.get("VocabularyFileUri") is not None:
        out["vocabulary_file_uri"] = data["VocabularyFileUri"]
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
