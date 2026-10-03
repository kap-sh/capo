"""Generated from Smithy shape ``com.amazonaws.transcribe#StartMedicalTranscriptionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.kms_encryption_context_map
    import capo_transcribe.types.kms_key_id
    import capo_transcribe.types.language_code
    import capo_transcribe.types.media
    import capo_transcribe.types.media_format
    import capo_transcribe.types.medical_content_identification_type
    import capo_transcribe.types.medical_media_sample_rate_hertz
    import capo_transcribe.types.medical_transcription_setting
    import capo_transcribe.types.output_bucket_name
    import capo_transcribe.types.output_key
    import capo_transcribe.types.specialty
    import capo_transcribe.types.tag_list
    import capo_transcribe.types.transcription_job_name
    import capo_transcribe.types.type


class StartMedicalTranscriptionJobRequest(TypedDict, closed=True):
    medical_transcription_job_name: (
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    )
    """<p>A unique name, chosen by you, for your medical transcription job. The name that you specify is also used as the default name of your transcription output file. If you want to specify a different name for your transcription output, use the <code>OutputKey</code> parameter.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new job with the same name as an existing job, you get a <code>ConflictException</code> error.</p>"""
    language_code: "capo_transcribe.types.language_code.LanguageCode"
    """<p>The language code that represents the language spoken in the input media file. US English (<code>en-US</code>) is the only valid value for medical transcription jobs. Any other value you enter for language code results in a <code>BadRequestException</code> error.</p>"""
    media_sample_rate_hertz: NotRequired[
        "capo_transcribe.types.medical_media_sample_rate_hertz.MedicalMediaSampleRateHertz"
    ]
    """<p>The sample rate, in hertz, of the audio track in your input media file.</p> <p>If you do not specify the media sample rate, Amazon Transcribe Medical determines it for you. If you specify the sample rate, it must match the rate detected by Amazon Transcribe Medical; if there's a mismatch between the value that you specify and the value detected, your job fails. Therefore, in most cases, it's advised to omit <code>MediaSampleRateHertz</code> and let Amazon Transcribe Medical determine the sample rate.</p>"""
    media_format: NotRequired["capo_transcribe.types.media_format.MediaFormat"]
    """<p>Specify the format of your input media file.</p>"""
    media: "capo_transcribe.types.media.Media"
    output_bucket_name: "capo_transcribe.types.output_bucket_name.OutputBucketName"
    """<p>The name of the Amazon S3 bucket where you want your medical transcription output stored. Do not include the <code>S3://</code> prefix of the specified bucket.</p> <p>If you want your output to go to a sub-folder of this bucket, specify it using the <code>OutputKey</code> parameter; <code>OutputBucketName</code> only accepts the name of a bucket.</p> <p>For example, if you want your output stored in <code>S3://DOC-EXAMPLE-BUCKET</code>, set <code>OutputBucketName</code> to <code>DOC-EXAMPLE-BUCKET</code>. However, if you want your output stored in <code>S3://DOC-EXAMPLE-BUCKET/test-files/</code>, set <code>OutputBucketName</code> to <code>DOC-EXAMPLE-BUCKET</code> and <code>OutputKey</code> to <code>test-files/</code>.</p> <p>Note that Amazon Transcribe must have permission to use the specified location. You can change Amazon S3 permissions using the <a href="https://console.aws.amazon.com/s3">Amazon Web Services Management Console</a>. See also <a href="https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user">Permissions Required for IAM User Roles</a>.</p>"""
    output_key: NotRequired["capo_transcribe.types.output_key.OutputKey"]
    """<p>Use in combination with <code>OutputBucketName</code> to specify the output location of your transcript and, optionally, a unique name for your output file. The default name for your transcription output is the same as the name you specified for your medical transcription job (<code>MedicalTranscriptionJobName</code>).</p> <p>Here are some examples of how you can use <code>OutputKey</code>:</p> <ul> <li> <p>If you specify 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code> and 'my-transcript.json' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/my-transcript.json</code>.</p> </li> <li> <p>If you specify 'my-first-transcription' as the <code>MedicalTranscriptionJobName</code>, 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code>, and 'my-transcript' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/my-transcript/my-first-transcription.json</code>.</p> </li> <li> <p>If you specify 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code> and 'test-files/my-transcript.json' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript.json</code>.</p> </li> <li> <p>If you specify 'my-first-transcription' as the <code>MedicalTranscriptionJobName</code>, 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code>, and 'test-files/my-transcript' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript/my-first-transcription.json</code>.</p> </li> </ul> <p>If you specify the name of an Amazon S3 bucket sub-folder that doesn't exist, one is created for you.</p>"""
    output_encryption_kms_key_id: NotRequired[
        "capo_transcribe.types.kms_key_id.KMSKeyId"
    ]
    """<p>The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your medical transcription output.</p> <p>KMS key ARNs have the format <code>arn:partition:kms:region:account:key/key-id</code>. For example: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN"> KMS key ARNs</a>.</p> <p>If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).</p> <p>Note that the role making the request and the role specified in the <code>DataAccessRoleArn</code> request parameter (if present) must have permission to use the specified KMS key.</p>"""
    kms_encryption_context: NotRequired[
        "capo_transcribe.types.kms_encryption_context_map.KMSEncryptionContextMap"
    ]
    """<p>A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context">KMS encryption context</a> and <a href="https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html">Asymmetric keys in KMS</a>.</p>"""
    settings: NotRequired[
        "capo_transcribe.types.medical_transcription_setting.MedicalTranscriptionSetting"
    ]
    """<p>Specify additional optional settings in your request, including channel identification, alternative transcriptions, and speaker partitioning. You can use that to apply custom vocabularies to your transcription job.</p>"""
    content_identification_type: NotRequired[
        "capo_transcribe.types.medical_content_identification_type.MedicalContentIdentificationType"
    ]
    """<p>Labels all personal health information (PHI) identified in your transcript. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html">Identifying personal health information (PHI) in a transcription</a>.</p>"""
    specialty: "capo_transcribe.types.specialty.Specialty"
    """<p>Specify the predominant medical specialty represented in your media. For batch transcriptions, <code>PRIMARYCARE</code> is the only valid value. If you require additional specialties, refer to .</p>"""
    type: "capo_transcribe.types.type.Type"
    """<p>Specify whether your input media contains only one person (<code>DICTATION</code>) or contains a conversation between two people (<code>CONVERSATION</code>).</p> <p>For example, <code>DICTATION</code> could be used for a medical professional wanting to transcribe voice memos; <code>CONVERSATION</code> could be used for transcribing the doctor-patient dialogue during the patient's office visit.</p>"""
    tags: NotRequired["capo_transcribe.types.tag_list.TagList"]
    """<p>Adds one or more custom tags, each in the form of a key:value pair, to a new medical transcription job at the time you start this new job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMedicalTranscriptionJobRequest) -> dict:
    out: dict = {}
    out["MedicalTranscriptionJobName"] = value["medical_transcription_job_name"]
    import capo_transcribe.types.language_code

    out["LanguageCode"] = capo_transcribe.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    if "media_sample_rate_hertz" in value:
        out["MediaSampleRateHertz"] = value["media_sample_rate_hertz"]
    if "media_format" in value:
        import capo_transcribe.types.media_format

        out["MediaFormat"] = capo_transcribe.types.media_format.serialize_aws_json_1_1(
            value["media_format"]
        )
    import capo_transcribe.types.media

    out["Media"] = capo_transcribe.types.media.serialize_aws_json_1_1(value["media"])
    out["OutputBucketName"] = value["output_bucket_name"]
    if "output_key" in value:
        out["OutputKey"] = value["output_key"]
    if "output_encryption_kms_key_id" in value:
        out["OutputEncryptionKMSKeyId"] = value["output_encryption_kms_key_id"]
    if "kms_encryption_context" in value:
        import capo_transcribe.types.kms_encryption_context_map

        out["KMSEncryptionContext"] = (
            capo_transcribe.types.kms_encryption_context_map.serialize_aws_json_1_1(
                value["kms_encryption_context"]
            )
        )
    if "settings" in value:
        import capo_transcribe.types.medical_transcription_setting

        out["Settings"] = (
            capo_transcribe.types.medical_transcription_setting.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "content_identification_type" in value:
        import capo_transcribe.types.medical_content_identification_type

        out["ContentIdentificationType"] = (
            capo_transcribe.types.medical_content_identification_type.serialize_aws_json_1_1(
                value["content_identification_type"]
            )
        )
    import capo_transcribe.types.specialty

    out["Specialty"] = capo_transcribe.types.specialty.serialize_aws_json_1_1(
        value["specialty"]
    )
    import capo_transcribe.types.type

    out["Type"] = capo_transcribe.types.type.serialize_aws_json_1_1(value["type"])
    if "tags" in value:
        import capo_transcribe.types.tag_list

        out["Tags"] = capo_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMedicalTranscriptionJobRequest:
    out: StartMedicalTranscriptionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("MedicalTranscriptionJobName") is not None:
        out["medical_transcription_job_name"] = data["MedicalTranscriptionJobName"]
    else:
        raise DeserializationError(
            "StartMedicalTranscriptionJobRequest.medical_transcription_job_name required"
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
            "StartMedicalTranscriptionJobRequest.language_code required"
        )
    if data.get("MediaSampleRateHertz") is not None:
        out["media_sample_rate_hertz"] = data["MediaSampleRateHertz"]
    if data.get("MediaFormat") is not None:
        import capo_transcribe.types.media_format

        out["media_format"] = (
            capo_transcribe.types.media_format.deserialize_aws_json_1_1(
                data["MediaFormat"]
            )
        )
    if data.get("Media") is not None:
        import capo_transcribe.types.media

        out["media"] = capo_transcribe.types.media.deserialize_aws_json_1_1(
            data["Media"]
        )
    else:
        raise DeserializationError("StartMedicalTranscriptionJobRequest.media required")
    if data.get("OutputBucketName") is not None:
        out["output_bucket_name"] = data["OutputBucketName"]
    else:
        raise DeserializationError(
            "StartMedicalTranscriptionJobRequest.output_bucket_name required"
        )
    if data.get("OutputKey") is not None:
        out["output_key"] = data["OutputKey"]
    if data.get("OutputEncryptionKMSKeyId") is not None:
        out["output_encryption_kms_key_id"] = data["OutputEncryptionKMSKeyId"]
    if data.get("KMSEncryptionContext") is not None:
        import capo_transcribe.types.kms_encryption_context_map

        out["kms_encryption_context"] = (
            capo_transcribe.types.kms_encryption_context_map.deserialize_aws_json_1_1(
                data["KMSEncryptionContext"]
            )
        )
    if data.get("Settings") is not None:
        import capo_transcribe.types.medical_transcription_setting

        out["settings"] = (
            capo_transcribe.types.medical_transcription_setting.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if data.get("ContentIdentificationType") is not None:
        import capo_transcribe.types.medical_content_identification_type

        out["content_identification_type"] = (
            capo_transcribe.types.medical_content_identification_type.deserialize_aws_json_1_1(
                data["ContentIdentificationType"]
            )
        )
    if data.get("Specialty") is not None:
        import capo_transcribe.types.specialty

        out["specialty"] = capo_transcribe.types.specialty.deserialize_aws_json_1_1(
            data["Specialty"]
        )
    else:
        raise DeserializationError(
            "StartMedicalTranscriptionJobRequest.specialty required"
        )
    if data.get("Type") is not None:
        import capo_transcribe.types.type

        out["type"] = capo_transcribe.types.type.deserialize_aws_json_1_1(data["Type"])
    else:
        raise DeserializationError("StartMedicalTranscriptionJobRequest.type required")
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
