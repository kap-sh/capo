"""Generated from Smithy shape ``com.amazonaws.transcribe#LanguageModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.base_model_name
    import capo_transcribe.types.boolean
    import capo_transcribe.types.clm_language_code
    import capo_transcribe.types.date_time
    import capo_transcribe.types.encryption_configuration
    import capo_transcribe.types.failure_reason
    import capo_transcribe.types.input_data_config
    import capo_transcribe.types.model_name
    import capo_transcribe.types.model_status


class LanguageModel(TypedDict, closed=True):
    model_name: NotRequired["capo_transcribe.types.model_name.ModelName"]
    """<p>A unique name, chosen by you, for your custom language model.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account.</p>"""
    create_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom language model was created.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    last_modified_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom language model was last modified.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    language_code: NotRequired[
        "capo_transcribe.types.clm_language_code.CLMLanguageCode"
    ]
    """<p>The language code used to create your custom language model. Each custom language model must contain terms in only one language, and the language you select for your custom language model must match the language of your training and tuning data.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table. Note that US English (<code>en-US</code>) is the only language supported with Amazon Transcribe Medical.</p>"""
    base_model_name: NotRequired["capo_transcribe.types.base_model_name.BaseModelName"]
    """<p>The Amazon Transcribe standard language model, or base model, used to create your custom language model.</p>"""
    model_status: NotRequired["capo_transcribe.types.model_status.ModelStatus"]
    """<p>The status of the specified custom language model. When the status displays as <code>COMPLETED</code> the model is ready for use.</p>"""
    upgrade_availability: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Shows if a more current base model is available for use with the specified custom language model.</p> <p>If <code>false</code>, your custom language model is using the most up-to-date base model.</p> <p>If <code>true</code>, there is a newer base model available than the one your language model is using.</p> <p>Note that to update a base model, you must recreate the custom language model using the new base model. Base model upgrades for existing custom language models are not supported.</p>"""
    failure_reason: NotRequired["capo_transcribe.types.failure_reason.FailureReason"]
    """<p>If <code>ModelStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the custom language model request failed. See also: <a href="https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html">Common Errors</a>.</p>"""
    input_data_config: NotRequired[
        "capo_transcribe.types.input_data_config.InputDataConfig"
    ]
    """<p>The Amazon S3 location of the input files used to train and tune your custom language model, in addition to the data access role ARN (Amazon Resource Name) that has permissions to access these data.</p>"""
    encryption_configuration: NotRequired[
        "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration used for your custom language model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageModel) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "create_time" in value:
        import capo_transcribe.types.date_time

        out["CreateTime"] = capo_transcribe.types.date_time.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "last_modified_time" in value:
        import capo_transcribe.types.date_time

        out["LastModifiedTime"] = (
            capo_transcribe.types.date_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "language_code" in value:
        import capo_transcribe.types.clm_language_code

        out["LanguageCode"] = (
            capo_transcribe.types.clm_language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "base_model_name" in value:
        import capo_transcribe.types.base_model_name

        out["BaseModelName"] = (
            capo_transcribe.types.base_model_name.serialize_aws_json_1_1(
                value["base_model_name"]
            )
        )
    if "model_status" in value:
        import capo_transcribe.types.model_status

        out["ModelStatus"] = capo_transcribe.types.model_status.serialize_aws_json_1_1(
            value["model_status"]
        )
    if "upgrade_availability" in value:
        out["UpgradeAvailability"] = value["upgrade_availability"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "input_data_config" in value:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> LanguageModel:
    out: LanguageModel = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("CreateTime") is not None:
        import capo_transcribe.types.date_time

        out["create_time"] = capo_transcribe.types.date_time.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_transcribe.types.date_time

        out["last_modified_time"] = (
            capo_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.clm_language_code

        out["language_code"] = (
            capo_transcribe.types.clm_language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("BaseModelName") is not None:
        import capo_transcribe.types.base_model_name

        out["base_model_name"] = (
            capo_transcribe.types.base_model_name.deserialize_aws_json_1_1(
                data["BaseModelName"]
            )
        )
    if data.get("ModelStatus") is not None:
        import capo_transcribe.types.model_status

        out["model_status"] = (
            capo_transcribe.types.model_status.deserialize_aws_json_1_1(
                data["ModelStatus"]
            )
        )
    if data.get("UpgradeAvailability") is not None:
        out["upgrade_availability"] = data["UpgradeAvailability"]
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("InputDataConfig") is not None:
        import capo_transcribe.types.input_data_config

        out["input_data_config"] = (
            capo_transcribe.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_transcribe.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_transcribe.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    return out
