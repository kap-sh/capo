"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.artifact_details
    import capo_codepipeline.types.rule_configuration_property_list
    import capo_codepipeline.types.rule_type_id
    import capo_codepipeline.types.rule_type_settings


class RuleType(TypedDict, closed=True):
    id: "capo_codepipeline.types.rule_type_id.RuleTypeId"
    """<p>Represents information about a rule type.</p>"""
    settings: NotRequired["capo_codepipeline.types.rule_type_settings.RuleTypeSettings"]
    """<p>Returns information about the settings for a rule type.</p>"""
    rule_configuration_properties: NotRequired[
        "capo_codepipeline.types.rule_configuration_property_list.RuleConfigurationPropertyList"
    ]
    """<p>The configuration properties for the rule type.</p>"""
    input_artifact_details: "capo_codepipeline.types.artifact_details.ArtifactDetails"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleType) -> dict:
    out: dict = {}
    import capo_codepipeline.types.rule_type_id

    out["id"] = capo_codepipeline.types.rule_type_id.serialize_aws_json_1_1(value["id"])
    if "settings" in value:
        import capo_codepipeline.types.rule_type_settings

        out["settings"] = (
            capo_codepipeline.types.rule_type_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "rule_configuration_properties" in value:
        import capo_codepipeline.types.rule_configuration_property_list

        out["ruleConfigurationProperties"] = (
            capo_codepipeline.types.rule_configuration_property_list.serialize_aws_json_1_1(
                value["rule_configuration_properties"]
            )
        )
    import capo_codepipeline.types.artifact_details

    out["inputArtifactDetails"] = (
        capo_codepipeline.types.artifact_details.serialize_aws_json_1_1(
            value["input_artifact_details"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleType:
    out: RuleType = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        import capo_codepipeline.types.rule_type_id

        out["id"] = capo_codepipeline.types.rule_type_id.deserialize_aws_json_1_1(
            data["id"]
        )
    else:
        raise DeserializationError("RuleType.id required")
    if data.get("settings") is not None:
        import capo_codepipeline.types.rule_type_settings

        out["settings"] = (
            capo_codepipeline.types.rule_type_settings.deserialize_aws_json_1_1(
                data["settings"]
            )
        )
    if data.get("ruleConfigurationProperties") is not None:
        import capo_codepipeline.types.rule_configuration_property_list

        out["rule_configuration_properties"] = (
            capo_codepipeline.types.rule_configuration_property_list.deserialize_aws_json_1_1(
                data["ruleConfigurationProperties"]
            )
        )
    if data.get("inputArtifactDetails") is not None:
        import capo_codepipeline.types.artifact_details

        out["input_artifact_details"] = (
            capo_codepipeline.types.artifact_details.deserialize_aws_json_1_1(
                data["inputArtifactDetails"]
            )
        )
    else:
        raise DeserializationError("RuleType.input_artifact_details required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleType) -> dict:
    out: dict = {}
    import capo_codepipeline.types.rule_type_id

    out["id"] = capo_codepipeline.types.rule_type_id.serialize_cbor(value["id"])
    if "settings" in value:
        import capo_codepipeline.types.rule_type_settings

        out["settings"] = capo_codepipeline.types.rule_type_settings.serialize_cbor(
            value["settings"]
        )
    if "rule_configuration_properties" in value:
        import capo_codepipeline.types.rule_configuration_property_list

        out["ruleConfigurationProperties"] = (
            capo_codepipeline.types.rule_configuration_property_list.serialize_cbor(
                value["rule_configuration_properties"]
            )
        )
    import capo_codepipeline.types.artifact_details

    out["inputArtifactDetails"] = (
        capo_codepipeline.types.artifact_details.serialize_cbor(
            value["input_artifact_details"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> RuleType:
    out: RuleType = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        import capo_codepipeline.types.rule_type_id

        out["id"] = capo_codepipeline.types.rule_type_id.deserialize_cbor(data["id"])
    else:
        raise DeserializationError("RuleType.id required")
    if data.get("settings") is not None:
        import capo_codepipeline.types.rule_type_settings

        out["settings"] = capo_codepipeline.types.rule_type_settings.deserialize_cbor(
            data["settings"]
        )
    if data.get("ruleConfigurationProperties") is not None:
        import capo_codepipeline.types.rule_configuration_property_list

        out["rule_configuration_properties"] = (
            capo_codepipeline.types.rule_configuration_property_list.deserialize_cbor(
                data["ruleConfigurationProperties"]
            )
        )
    if data.get("inputArtifactDetails") is not None:
        import capo_codepipeline.types.artifact_details

        out["input_artifact_details"] = (
            capo_codepipeline.types.artifact_details.deserialize_cbor(
                data["inputArtifactDetails"]
            )
        )
    else:
        raise DeserializationError("RuleType.input_artifact_details required")
    return out
