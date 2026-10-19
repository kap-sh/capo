"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceProfileSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.inference_profile_arn
    import capo_bedrock.types.inference_profile_description
    import capo_bedrock.types.inference_profile_id
    import capo_bedrock.types.inference_profile_models
    import capo_bedrock.types.inference_profile_name
    import capo_bedrock.types.inference_profile_status
    import capo_bedrock.types.inference_profile_type
    import capo_bedrock.types.timestamp


class InferenceProfileSummary(TypedDict, closed=True):
    inference_profile_name: (
        "capo_bedrock.types.inference_profile_name.InferenceProfileName"
    )
    """<p>The name of the inference profile.</p>"""
    description: NotRequired[
        "capo_bedrock.types.inference_profile_description.InferenceProfileDescription"
    ]
    """<p>The description of the inference profile.</p>"""
    created_at: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the inference profile was created.</p>"""
    updated_at: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the inference profile was last updated.</p>"""
    inference_profile_arn: (
        "capo_bedrock.types.inference_profile_arn.InferenceProfileArn"
    )
    """<p>The Amazon Resource Name (ARN) of the inference profile.</p>"""
    models: "capo_bedrock.types.inference_profile_models.InferenceProfileModels"
    """<p>A list of information about each model in the inference profile.</p>"""
    inference_profile_id: "capo_bedrock.types.inference_profile_id.InferenceProfileId"
    """<p>The unique identifier of the inference profile.</p>"""
    status: "capo_bedrock.types.inference_profile_status.InferenceProfileStatus"
    """<p>The status of the inference profile. <code>ACTIVE</code> means that the inference profile is ready to be used.</p>"""
    type: "capo_bedrock.types.inference_profile_type.InferenceProfileType"
    """<p>The type of the inference profile. The following types are possible:</p> <ul> <li> <p> <code>SYSTEM_DEFINED</code> – The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles.</p> </li> <li> <p> <code>APPLICATION</code> – The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceProfileSummary) -> dict:
    out: dict = {}
    out["inferenceProfileName"] = value["inference_profile_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_bedrock.types.timestamp

        out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_bedrock.types.timestamp

        out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(
            value["updated_at"]
        )
    out["inferenceProfileArn"] = value["inference_profile_arn"]
    import capo_bedrock.types.inference_profile_models

    out["models"] = capo_bedrock.types.inference_profile_models.serialize_json(
        value["models"]
    )
    out["inferenceProfileId"] = value["inference_profile_id"]
    import capo_bedrock.types.inference_profile_status

    out["status"] = capo_bedrock.types.inference_profile_status.serialize_json(
        value["status"]
    )
    import capo_bedrock.types.inference_profile_type

    out["type"] = capo_bedrock.types.inference_profile_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> InferenceProfileSummary:
    out: InferenceProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("inferenceProfileName") is not None:
        out["inference_profile_name"] = data["inferenceProfileName"]
    else:
        out["inference_profile_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("inferenceProfileArn") is not None:
        out["inference_profile_arn"] = data["inferenceProfileArn"]
    else:
        out["inference_profile_arn"] = ""
    if data.get("models") is not None:
        import capo_bedrock.types.inference_profile_models

        out["models"] = capo_bedrock.types.inference_profile_models.deserialize_json(
            data["models"]
        )
    else:
        out["models"] = []
    if data.get("inferenceProfileId") is not None:
        out["inference_profile_id"] = data["inferenceProfileId"]
    else:
        out["inference_profile_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock.types.inference_profile_status

        out["status"] = capo_bedrock.types.inference_profile_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock.types.inference_profile_status.InferenceProfileStatus", ""
        )
    if data.get("type") is not None:
        import capo_bedrock.types.inference_profile_type

        out["type"] = capo_bedrock.types.inference_profile_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock.types.inference_profile_type.InferenceProfileType", ""
        )
    return out


def redact_sensitive(value: InferenceProfileSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
