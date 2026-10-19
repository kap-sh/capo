"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateInferenceProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.inference_profile_arn
    import capo_bedrock.types.inference_profile_status


class CreateInferenceProfileResponse(TypedDict, closed=True):
    inference_profile_arn: (
        "capo_bedrock.types.inference_profile_arn.InferenceProfileArn"
    )
    """<p>The ARN of the inference profile that you created.</p>"""
    status: NotRequired[
        "capo_bedrock.types.inference_profile_status.InferenceProfileStatus"
    ]
    """<p>The status of the inference profile. <code>ACTIVE</code> means that the inference profile is ready to be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInferenceProfileResponse) -> dict:
    out: dict = {}
    out["inferenceProfileArn"] = value["inference_profile_arn"]
    if "status" in value:
        import capo_bedrock.types.inference_profile_status

        out["status"] = capo_bedrock.types.inference_profile_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> CreateInferenceProfileResponse:
    out: CreateInferenceProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("inferenceProfileArn") is not None:
        out["inference_profile_arn"] = data["inferenceProfileArn"]
    else:
        out["inference_profile_arn"] = ""
    if data.get("status") is not None:
        import capo_bedrock.types.inference_profile_status

        out["status"] = capo_bedrock.types.inference_profile_status.deserialize_json(
            data["status"]
        )
    return out
