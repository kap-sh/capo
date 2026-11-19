"""Generated from Smithy shape ``com.amazonaws.transcribe#CreateLanguageModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.base_model_name
    import capo_transcribe.types.clm_language_code
    import capo_transcribe.types.input_data_config
    import capo_transcribe.types.model_name
    import capo_transcribe.types.model_status


class CreateLanguageModelResponse(TypedDict, closed=True):
    language_code: NotRequired[
        "capo_transcribe.types.clm_language_code.CLMLanguageCode"
    ]
    """<p>The language code you selected for your custom language model.</p>"""
    base_model_name: NotRequired["capo_transcribe.types.base_model_name.BaseModelName"]
    """<p>The Amazon Transcribe standard language model, or base model, you specified when creating your custom language model.</p>"""
    model_name: NotRequired["capo_transcribe.types.model_name.ModelName"]
    """<p>The name of your custom language model.</p>"""
    input_data_config: NotRequired[
        "capo_transcribe.types.input_data_config.InputDataConfig"
    ]
    """<p>Lists your data access role ARN (Amazon Resource Name) and the Amazon S3 locations you provided for your training (<code>S3Uri</code>) and tuning (<code>TuningDataS3Uri</code>) data.</p>"""
    model_status: NotRequired["capo_transcribe.types.model_status.ModelStatus"]
    """<p>The status of your custom language model. When the status displays as <code>COMPLETED</code>, your model is ready to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLanguageModelResponse) -> dict:
    out: dict = {}
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
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "input_data_config" in value:
        import capo_transcribe.types.input_data_config

        out["InputDataConfig"] = (
            capo_transcribe.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "model_status" in value:
        import capo_transcribe.types.model_status

        out["ModelStatus"] = capo_transcribe.types.model_status.serialize_aws_json_1_1(
            value["model_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLanguageModelResponse:
    out: CreateLanguageModelResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("InputDataConfig") is not None:
        import capo_transcribe.types.input_data_config

        out["input_data_config"] = (
            capo_transcribe.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if data.get("ModelStatus") is not None:
        import capo_transcribe.types.model_status

        out["model_status"] = (
            capo_transcribe.types.model_status.deserialize_aws_json_1_1(
                data["ModelStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateLanguageModelResponse) -> dict:
    out: dict = {}
    if "language_code" in value:
        import capo_transcribe.types.clm_language_code

        out["LanguageCode"] = capo_transcribe.types.clm_language_code.serialize_cbor(
            value["language_code"]
        )
    if "base_model_name" in value:
        import capo_transcribe.types.base_model_name

        out["BaseModelName"] = capo_transcribe.types.base_model_name.serialize_cbor(
            value["base_model_name"]
        )
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "input_data_config" in value:
        import capo_transcribe.types.input_data_config

        out["InputDataConfig"] = capo_transcribe.types.input_data_config.serialize_cbor(
            value["input_data_config"]
        )
    if "model_status" in value:
        import capo_transcribe.types.model_status

        out["ModelStatus"] = capo_transcribe.types.model_status.serialize_cbor(
            value["model_status"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateLanguageModelResponse:
    out: CreateLanguageModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.clm_language_code

        out["language_code"] = capo_transcribe.types.clm_language_code.deserialize_cbor(
            data["LanguageCode"]
        )
    if data.get("BaseModelName") is not None:
        import capo_transcribe.types.base_model_name

        out["base_model_name"] = capo_transcribe.types.base_model_name.deserialize_cbor(
            data["BaseModelName"]
        )
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("InputDataConfig") is not None:
        import capo_transcribe.types.input_data_config

        out["input_data_config"] = (
            capo_transcribe.types.input_data_config.deserialize_cbor(
                data["InputDataConfig"]
            )
        )
    if data.get("ModelStatus") is not None:
        import capo_transcribe.types.model_status

        out["model_status"] = capo_transcribe.types.model_status.deserialize_cbor(
            data["ModelStatus"]
        )
    return out
