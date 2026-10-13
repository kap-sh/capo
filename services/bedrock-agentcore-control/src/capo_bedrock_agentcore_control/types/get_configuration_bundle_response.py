"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetConfigurationBundleResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.component_configuration_map
    import capo_bedrock_agentcore_control.types.configuration_bundle_arn
    import capo_bedrock_agentcore_control.types.configuration_bundle_description
    import capo_bedrock_agentcore_control.types.configuration_bundle_id
    import capo_bedrock_agentcore_control.types.configuration_bundle_name
    import capo_bedrock_agentcore_control.types.configuration_bundle_version
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.version_lineage_metadata


class GetConfigurationBundleResponse(TypedDict, closed=True):
    bundle_arn: "capo_bedrock_agentcore_control.types.configuration_bundle_arn.ConfigurationBundleArn"
    """<p>The Amazon Resource Name (ARN) of the configuration bundle.</p>"""
    bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the configuration bundle.</p>"""
    bundle_name: "capo_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName"
    """<p>The name of the configuration bundle.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
    ]
    """<p>The description of the configuration bundle.</p>"""
    version_id: "capo_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion"
    """<p>The version identifier of this configuration bundle.</p>"""
    components: "capo_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap"
    """<p>A map of component identifiers to their configurations for this version.</p>"""
    lineage_metadata: NotRequired[
        "capo_bedrock_agentcore_control.types.version_lineage_metadata.VersionLineageMetadata"
    ]
    """<p>The version lineage metadata, including parent versions, branch name, and creation source.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the configuration bundle was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the configuration bundle was last updated.</p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>KMS key ARN used to encrypt component configurations, if CMK was provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationBundleResponse) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["bundleId"] = value["bundle_id"]
    out["bundleName"] = value["bundle_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["versionId"] = value["version_id"]
    import capo_bedrock_agentcore_control.types.component_configuration_map

    out["components"] = (
        capo_bedrock_agentcore_control.types.component_configuration_map.serialize_json(
            value["components"]
        )
    )
    if "lineage_metadata" in value:
        import capo_bedrock_agentcore_control.types.version_lineage_metadata

        out["lineageMetadata"] = (
            capo_bedrock_agentcore_control.types.version_lineage_metadata.serialize_json(
                value["lineage_metadata"]
            )
        )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetConfigurationBundleResponse:
    out: GetConfigurationBundleResponse = {}  # type: ignore[typeddict-item]
    if data.get("bundleArn") is not None:
        out["bundle_arn"] = data["bundleArn"]
    else:
        raise DeserializationError("GetConfigurationBundleResponse.bundle_arn required")
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError("GetConfigurationBundleResponse.bundle_id required")
    if data.get("bundleName") is not None:
        out["bundle_name"] = data["bundleName"]
    else:
        raise DeserializationError(
            "GetConfigurationBundleResponse.bundle_name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError("GetConfigurationBundleResponse.version_id required")
    if data.get("components") is not None:
        import capo_bedrock_agentcore_control.types.component_configuration_map

        out["components"] = (
            capo_bedrock_agentcore_control.types.component_configuration_map.deserialize_json(
                data["components"]
            )
        )
    else:
        raise DeserializationError("GetConfigurationBundleResponse.components required")
    if data.get("lineageMetadata") is not None:
        import capo_bedrock_agentcore_control.types.version_lineage_metadata

        out["lineage_metadata"] = (
            capo_bedrock_agentcore_control.types.version_lineage_metadata.deserialize_json(
                data["lineageMetadata"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetConfigurationBundleResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetConfigurationBundleResponse.updated_at required")
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out


def redact_sensitive(value: GetConfigurationBundleResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "components" in value:
        import capo_bedrock_agentcore_control.types.component_configuration_map

        out["components"] = (
            capo_bedrock_agentcore_control.types.component_configuration_map.redact_sensitive(
                value["components"]
            )
        )
    return out
