"""Generated from Smithy shape ``com.amazonaws.transcribe#UpdateLanguageModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.date_time
    import capo_transcribe.types.model_name
    import capo_transcribe.types.model_status


class UpdateLanguageModelResponse(TypedDict, closed=True):
    model_name: NotRequired["capo_transcribe.types.model_name.ModelName"]
    """<p>The name of the custom language model that was updated.</p>"""
    model_status: NotRequired["capo_transcribe.types.model_status.ModelStatus"]
    """<p>The status of the specified custom language model.</p>"""
    last_modified_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom language model was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLanguageModelResponse) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_status" in value:
        import capo_transcribe.types.model_status

        out["ModelStatus"] = capo_transcribe.types.model_status.serialize_aws_json_1_1(
            value["model_status"]
        )
    if "last_modified_time" in value:
        import capo_transcribe.types.date_time

        out["LastModifiedTime"] = (
            capo_transcribe.types.date_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLanguageModelResponse:
    out: UpdateLanguageModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("ModelStatus") is not None:
        import capo_transcribe.types.model_status

        out["model_status"] = (
            capo_transcribe.types.model_status.deserialize_aws_json_1_1(
                data["ModelStatus"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_transcribe.types.date_time

        out["last_modified_time"] = (
            capo_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateLanguageModelResponse) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_status" in value:
        import capo_transcribe.types.model_status

        out["ModelStatus"] = capo_transcribe.types.model_status.serialize_cbor(
            value["model_status"]
        )
    if "last_modified_time" in value:
        import capo_transcribe.types.date_time

        out["LastModifiedTime"] = capo_transcribe.types.date_time.serialize_cbor(
            value["last_modified_time"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdateLanguageModelResponse:
    out: UpdateLanguageModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("ModelStatus") is not None:
        import capo_transcribe.types.model_status

        out["model_status"] = capo_transcribe.types.model_status.deserialize_cbor(
            data["ModelStatus"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_transcribe.types.date_time

        out["last_modified_time"] = capo_transcribe.types.date_time.deserialize_cbor(
            data["LastModifiedTime"]
        )
    return out
