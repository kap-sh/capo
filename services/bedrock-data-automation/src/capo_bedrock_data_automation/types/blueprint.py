"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#Blueprint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_name
    import capo_bedrock_data_automation.types.blueprint_optimization_samples
    import capo_bedrock_data_automation.types.blueprint_schema
    import capo_bedrock_data_automation.types.blueprint_stage
    import capo_bedrock_data_automation.types.blueprint_version
    import capo_bedrock_data_automation.types.date_timestamp
    import capo_bedrock_data_automation.types.kms_encryption_context
    import capo_bedrock_data_automation.types.kms_key_id
    import capo_bedrock_data_automation.types.type


class Blueprint(TypedDict, closed=True):
    blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    schema: "capo_bedrock_data_automation.types.blueprint_schema.BlueprintSchema"
    type: "capo_bedrock_data_automation.types.type.Type"
    creation_time: "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    last_modified_time: (
        "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    )
    blueprint_name: "capo_bedrock_data_automation.types.blueprint_name.BlueprintName"
    blueprint_version: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
    ]
    blueprint_stage: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    kms_key_id: NotRequired["capo_bedrock_data_automation.types.kms_key_id.KmsKeyId"]
    kms_encryption_context: NotRequired[
        "capo_bedrock_data_automation.types.kms_encryption_context.KmsEncryptionContext"
    ]
    optimization_samples: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_optimization_samples.BlueprintOptimizationSamples"
    ]
    optimization_time: NotRequired[
        "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Blueprint) -> dict:
    out: dict = {}
    out["blueprintArn"] = value["blueprint_arn"]
    out["schema"] = value["schema"]
    import capo_bedrock_data_automation.types.type

    out["type"] = capo_bedrock_data_automation.types.type.serialize_json(value["type"])
    import capo_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        capo_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    import capo_bedrock_data_automation.types.date_timestamp

    out["lastModifiedTime"] = (
        capo_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    out["blueprintName"] = value["blueprint_name"]
    if "blueprint_version" in value:
        out["blueprintVersion"] = value["blueprint_version"]
    if "blueprint_stage" in value:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["blueprintStage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["blueprint_stage"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "kms_encryption_context" in value:
        import capo_bedrock_data_automation.types.kms_encryption_context

        out["kmsEncryptionContext"] = (
            capo_bedrock_data_automation.types.kms_encryption_context.serialize_json(
                value["kms_encryption_context"]
            )
        )
    if "optimization_samples" in value:
        import capo_bedrock_data_automation.types.blueprint_optimization_samples

        out["optimizationSamples"] = (
            capo_bedrock_data_automation.types.blueprint_optimization_samples.serialize_json(
                value["optimization_samples"]
            )
        )
    if "optimization_time" in value:
        import capo_bedrock_data_automation.types.date_timestamp

        out["optimizationTime"] = (
            capo_bedrock_data_automation.types.date_timestamp.serialize_json(
                value["optimization_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> Blueprint:
    out: Blueprint = {}  # type: ignore[typeddict-item]
    if data.get("blueprintArn") is not None:
        out["blueprint_arn"] = data["blueprintArn"]
    else:
        raise DeserializationError("Blueprint.blueprint_arn required")
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    else:
        raise DeserializationError("Blueprint.schema required")
    if data.get("type") is not None:
        import capo_bedrock_data_automation.types.type

        out["type"] = capo_bedrock_data_automation.types.type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("Blueprint.type required")
    if data.get("creationTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("Blueprint.creation_time required")
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["last_modified_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("Blueprint.last_modified_time required")
    if data.get("blueprintName") is not None:
        out["blueprint_name"] = data["blueprintName"]
    else:
        raise DeserializationError("Blueprint.blueprint_name required")
    if data.get("blueprintVersion") is not None:
        out["blueprint_version"] = data["blueprintVersion"]
    if data.get("blueprintStage") is not None:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["blueprint_stage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["blueprintStage"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("kmsEncryptionContext") is not None:
        import capo_bedrock_data_automation.types.kms_encryption_context

        out["kms_encryption_context"] = (
            capo_bedrock_data_automation.types.kms_encryption_context.deserialize_json(
                data["kmsEncryptionContext"]
            )
        )
    if data.get("optimizationSamples") is not None:
        import capo_bedrock_data_automation.types.blueprint_optimization_samples

        out["optimization_samples"] = (
            capo_bedrock_data_automation.types.blueprint_optimization_samples.deserialize_json(
                data["optimizationSamples"]
            )
        )
    if data.get("optimizationTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["optimization_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["optimizationTime"]
            )
        )
    return out


def redact_sensitive(value: Blueprint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "schema" in value:
        out["schema"] = "*** Sensitive Data Redacted ***"
    if "blueprint_name" in value:
        out["blueprint_name"] = "*** Sensitive Data Redacted ***"
    return out
