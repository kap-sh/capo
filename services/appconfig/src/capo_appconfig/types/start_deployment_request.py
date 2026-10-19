"""Generated from Smithy shape ``com.amazonaws.appconfig#StartDeploymentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.deployment_strategy_id
    import capo_appconfig.types.description
    import capo_appconfig.types.dynamic_parameter_map
    import capo_appconfig.types.integer
    import capo_appconfig.types.kms_key_identifier
    import capo_appconfig.types.long_name
    import capo_appconfig.types.name
    import capo_appconfig.types.tag_map
    import capo_appconfig.types.version


class StartDeploymentRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.name.Name"
    """<p>The application ID.</p>"""
    environment_id: "capo_appconfig.types.name.Name"
    """<p>The environment ID.</p>"""
    deployment_strategy_id: (
        "capo_appconfig.types.deployment_strategy_id.DeploymentStrategyId"
    )
    """<p>The deployment strategy ID.</p>"""
    configuration_profile_id: "capo_appconfig.types.long_name.LongName"
    """<p>The configuration profile ID.</p>"""
    configuration_version: "capo_appconfig.types.version.Version"
    """<p>The configuration version to deploy. If deploying an AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the deployment.</p>"""
    tags: NotRequired["capo_appconfig.types.tag_map.TagMap"]
    """<p>Metadata to assign to the deployment. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>"""
    kms_key_identifier: NotRequired[
        "capo_appconfig.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The KMS key identifier (key ID, key alias, or key ARN). AppConfig uses this ID to encrypt the configuration data using a customer managed key. </p>"""
    dynamic_extension_parameters: NotRequired[
        "capo_appconfig.types.dynamic_parameter_map.DynamicParameterMap"
    ]
    """<p>A map of dynamic extension parameter names to values to pass to associated extensions with <code>PRE_START_DEPLOYMENT</code> actions.</p>"""
    latest_deployment_number: NotRequired["capo_appconfig.types.integer.Integer"]
    """<p>The number of the latest deployment. Use this value to ensure that the deployment starts from the expected state and to prevent conflicting updates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDeploymentRequest) -> dict:
    out: dict = {}
    out["DeploymentStrategyId"] = value["deployment_strategy_id"]
    out["ConfigurationProfileId"] = value["configuration_profile_id"]
    out["ConfigurationVersion"] = value["configuration_version"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_appconfig.types.tag_map

        out["Tags"] = capo_appconfig.types.tag_map.serialize_json(value["tags"])
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    if "dynamic_extension_parameters" in value:
        import capo_appconfig.types.dynamic_parameter_map

        out["DynamicExtensionParameters"] = (
            capo_appconfig.types.dynamic_parameter_map.serialize_json(
                value["dynamic_extension_parameters"]
            )
        )
    if "latest_deployment_number" in value:
        out["LatestDeploymentNumber"] = value["latest_deployment_number"]
    return out


def deserialize_json(data: dict) -> StartDeploymentRequest:
    out: StartDeploymentRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeploymentStrategyId") is not None:
        out["deployment_strategy_id"] = data["DeploymentStrategyId"]
    else:
        out["deployment_strategy_id"] = ""
    if data.get("ConfigurationProfileId") is not None:
        out["configuration_profile_id"] = data["ConfigurationProfileId"]
    else:
        out["configuration_profile_id"] = ""
    if data.get("ConfigurationVersion") is not None:
        out["configuration_version"] = data["ConfigurationVersion"]
    else:
        out["configuration_version"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_appconfig.types.tag_map

        out["tags"] = capo_appconfig.types.tag_map.deserialize_json(data["Tags"])
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if data.get("DynamicExtensionParameters") is not None:
        import capo_appconfig.types.dynamic_parameter_map

        out["dynamic_extension_parameters"] = (
            capo_appconfig.types.dynamic_parameter_map.deserialize_json(
                data["DynamicExtensionParameters"]
            )
        )
    if data.get("LatestDeploymentNumber") is not None:
        out["latest_deployment_number"] = data["LatestDeploymentNumber"]
    return out


def redact_sensitive(value: StartDeploymentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dynamic_extension_parameters" in value:
        out["dynamic_extension_parameters"] = "*** Sensitive Data Redacted ***"
    return out
