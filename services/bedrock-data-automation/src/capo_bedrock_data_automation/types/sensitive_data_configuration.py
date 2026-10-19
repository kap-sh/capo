"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#SensitiveDataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.pii_entities_configuration
    import capo_bedrock_data_automation.types.sensitive_data_detection_mode
    import capo_bedrock_data_automation.types.sensitive_data_detection_scope


class SensitiveDataConfiguration(TypedDict, closed=True):
    detection_mode: "capo_bedrock_data_automation.types.sensitive_data_detection_mode.SensitiveDataDetectionMode"
    """Mode for sensitive data detection"""
    detection_scope: NotRequired[
        "capo_bedrock_data_automation.types.sensitive_data_detection_scope.SensitiveDataDetectionScope"
    ]
    """Scope of detection - what types of sensitive data to detect"""
    pii_entities_configuration: NotRequired[
        "capo_bedrock_data_automation.types.pii_entities_configuration.PIIEntitiesConfiguration"
    ]
    """Configuration for PII entities detection and redaction"""


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDataConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.sensitive_data_detection_mode

    out["detectionMode"] = (
        capo_bedrock_data_automation.types.sensitive_data_detection_mode.serialize_json(
            value["detection_mode"]
        )
    )
    if "detection_scope" in value:
        import capo_bedrock_data_automation.types.sensitive_data_detection_scope

        out["detectionScope"] = (
            capo_bedrock_data_automation.types.sensitive_data_detection_scope.serialize_json(
                value["detection_scope"]
            )
        )
    if "pii_entities_configuration" in value:
        import capo_bedrock_data_automation.types.pii_entities_configuration

        out["piiEntitiesConfiguration"] = (
            capo_bedrock_data_automation.types.pii_entities_configuration.serialize_json(
                value["pii_entities_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SensitiveDataConfiguration:
    out: SensitiveDataConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("detectionMode") is not None:
        import capo_bedrock_data_automation.types.sensitive_data_detection_mode

        out["detection_mode"] = (
            capo_bedrock_data_automation.types.sensitive_data_detection_mode.deserialize_json(
                data["detectionMode"]
            )
        )
    else:
        import typing

        out["detection_mode"] = typing.cast(
            "capo_bedrock_data_automation.types.sensitive_data_detection_mode.SensitiveDataDetectionMode",
            "",
        )
    if data.get("detectionScope") is not None:
        import capo_bedrock_data_automation.types.sensitive_data_detection_scope

        out["detection_scope"] = (
            capo_bedrock_data_automation.types.sensitive_data_detection_scope.deserialize_json(
                data["detectionScope"]
            )
        )
    if data.get("piiEntitiesConfiguration") is not None:
        import capo_bedrock_data_automation.types.pii_entities_configuration

        out["pii_entities_configuration"] = (
            capo_bedrock_data_automation.types.pii_entities_configuration.deserialize_json(
                data["piiEntitiesConfiguration"]
            )
        )
    return out
