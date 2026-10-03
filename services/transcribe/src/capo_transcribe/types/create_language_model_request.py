"""Generated from Smithy shape ``com.amazonaws.transcribe#CreateLanguageModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.base_model_name
    import capo_transcribe.types.clm_language_code
    import capo_transcribe.types.encryption_configuration
    import capo_transcribe.types.input_data_config
    import capo_transcribe.types.model_name
    import capo_transcribe.types.tag_list


class CreateLanguageModelRequest(TypedDict, closed=True):
    language_code: "capo_transcribe.types.clm_language_code.CLMLanguageCode"
    """<p>The language code that represents the language of your model. Each custom language model must contain terms in only one language, and the language you select for your custom language model must match the language of your training and tuning data.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table. Note that US English (<code>en-US</code>) is the only language supported with Amazon Transcribe Medical.</p> <p>A custom language model can only be used to transcribe files in the same language as the model. For example, if you create a custom language model using US English (<code>en-US</code>), you can only apply this model to files that contain English audio.</p>"""
    base_model_name: "capo_transcribe.types.base_model_name.BaseModelName"
    """<p>The Amazon Transcribe standard language model, or base model, used to create your custom language model. Amazon Transcribe offers two options for base models: Wideband and Narrowband.</p> <p>If the audio you want to transcribe has a sample rate of 16,000 Hz or greater, choose <code>WideBand</code>. To transcribe audio with a sample rate less than 16,000 Hz, choose <code>NarrowBand</code>.</p>"""
    model_name: "capo_transcribe.types.model_name.ModelName"
    """<p>A unique name, chosen by you, for your custom language model.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new custom language model with the same name as an existing custom language model, you get a <code>ConflictException</code> error.</p>"""
    input_data_config: "capo_transcribe.types.input_data_config.InputDataConfig"
    """<p>Contains the Amazon S3 location of the training data you want to use to create a new custom language model, and permissions to access this location.</p> <p>When using <code>InputDataConfig</code>, you must include these sub-parameters: <code>S3Uri</code>, which is the Amazon S3 location of your training data, and <code>DataAccessRoleArn</code>, which is the Amazon Resource Name (ARN) of the role that has permission to access your specified Amazon S3 location. You can optionally include <code>TuningDataS3Uri</code>, which is the Amazon S3 location of your tuning data. If you specify different Amazon S3 locations for training and tuning data, the ARN you use must have permissions to access both locations.</p>"""
    encryption_configuration: NotRequired[
        "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Specifies the encryption configuration for your custom language model. Your model artifacts are encrypted with the specified KMS key or with an AWS-owned key if a key is not supplied.</p>"""
    tags: NotRequired["capo_transcribe.types.tag_list.TagList"]
    """<p>Adds one or more custom tags, each in the form of a key:value pair, to a new custom language model at the time you create this new model.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLanguageModelRequest) -> dict:
    out: dict = {}
    import capo_transcribe.types.clm_language_code

    out["LanguageCode"] = (
        capo_transcribe.types.clm_language_code.serialize_aws_json_1_1(
            value["language_code"]
        )
    )
    import capo_transcribe.types.base_model_name

    out["BaseModelName"] = capo_transcribe.types.base_model_name.serialize_aws_json_1_1(
        value["base_model_name"]
    )
    out["ModelName"] = value["model_name"]
    import capo_transcribe.types.input_data_config

    out["InputDataConfig"] = (
        capo_transcribe.types.input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    if "encryption_configuration" in value:
        import capo_transcribe.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_transcribe.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import capo_transcribe.types.tag_list

        out["Tags"] = capo_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLanguageModelRequest:
    out: CreateLanguageModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.clm_language_code

        out["language_code"] = (
            capo_transcribe.types.clm_language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("CreateLanguageModelRequest.language_code required")
    if data.get("BaseModelName") is not None:
        import capo_transcribe.types.base_model_name

        out["base_model_name"] = (
            capo_transcribe.types.base_model_name.deserialize_aws_json_1_1(
                data["BaseModelName"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLanguageModelRequest.base_model_name required"
        )
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError("CreateLanguageModelRequest.model_name required")
    if data.get("InputDataConfig") is not None:
        import capo_transcribe.types.input_data_config

        out["input_data_config"] = (
            capo_transcribe.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLanguageModelRequest.input_data_config required"
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_transcribe.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_transcribe.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
