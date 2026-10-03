"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.recommendation_job_compiled_output_config


class RecommendationJobOutputConfig(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt your output artifacts with Amazon S3 server-side encryption. The SageMaker execution role must have <code>kms:GenerateDataKey</code> permission.</p> <p>The <code>KmsKeyId</code> can be any of the following formats:</p> <ul> <li> <p>// KMS Key ID</p> <p> <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>// Amazon Resource Name (ARN) of a KMS Key</p> <p> <code>"arn:aws:kms:&lt;region&gt;:&lt;account&gt;:key/&lt;key-id-12ab-34cd-56ef-1234567890ab&gt;"</code> </p> </li> <li> <p>// KMS Key Alias</p> <p> <code>"alias/ExampleAlias"</code> </p> </li> <li> <p>// Amazon Resource Name (ARN) of a KMS Key Alias</p> <p> <code>"arn:aws:kms:&lt;region&gt;:&lt;account&gt;:alias/&lt;ExampleAlias&gt;"</code> </p> </li> </ul> <p>For more information about key identifiers, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id">Key identifiers (KeyID)</a> in the Amazon Web Services Key Management Service (Amazon Web Services KMS) documentation.</p>"""
    compiled_output_config: NotRequired[
        "capo_sagemaker.types.recommendation_job_compiled_output_config.RecommendationJobCompiledOutputConfig"
    ]
    """<p>Provides information about the output configuration for the compiled model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobOutputConfig) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "compiled_output_config" in value:
        import capo_sagemaker.types.recommendation_job_compiled_output_config

        out["CompiledOutputConfig"] = (
            capo_sagemaker.types.recommendation_job_compiled_output_config.serialize_aws_json_1_1(
                value["compiled_output_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationJobOutputConfig:
    out: RecommendationJobOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("CompiledOutputConfig") is not None:
        import capo_sagemaker.types.recommendation_job_compiled_output_config

        out["compiled_output_config"] = (
            capo_sagemaker.types.recommendation_job_compiled_output_config.deserialize_aws_json_1_1(
                data["CompiledOutputConfig"]
            )
        )
    return out
