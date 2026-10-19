"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.float_version_string
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.model_identifier
    import capo_frauddetector.types.model_type_enum


class ModelVersion(TypedDict, closed=True):
    model_id: "capo_frauddetector.types.model_identifier.modelIdentifier"
    """<p>The model ID.</p>"""
    model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum"
    """<p>The model type.</p>"""
    model_version_number: (
        "capo_frauddetector.types.float_version_string.floatVersionString"
    )
    """<p>The model version number.</p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The model version ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelVersion) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import capo_frauddetector.types.model_type_enum

    out["modelType"] = capo_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
        value["model_type"]
    )
    out["modelVersionNumber"] = value["model_version_number"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelVersion:
    out: ModelVersion = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("modelType") is not None:
        import capo_frauddetector.types.model_type_enum

        out["model_type"] = (
            capo_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    else:
        import typing

        out["model_type"] = typing.cast(
            "capo_frauddetector.types.model_type_enum.ModelTypeEnum", ""
        )
    if data.get("modelVersionNumber") is not None:
        out["model_version_number"] = data["modelVersionNumber"]
    else:
        out["model_version_number"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
