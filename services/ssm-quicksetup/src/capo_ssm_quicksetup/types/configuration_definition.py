"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.configuration_parameters_map
    import capo_ssm_quicksetup.types.iam_role_arn


class ConfigurationDefinition(TypedDict, closed=True):
    type: "str"
    """<p>The type of the Quick Setup configuration.</p>"""
    parameters: "capo_ssm_quicksetup.types.configuration_parameters_map.ConfigurationParametersMap"
    """<p>A list of key-value pairs containing the required parameters for the configuration type.</p>"""
    type_version: NotRequired["str"]
    """<p>The version of the Quick Setup type used.</p>"""
    local_deployment_execution_role_name: NotRequired["str"]
    """<p>The name of the IAM role used to deploy local configurations.</p>"""
    local_deployment_administration_role_arn: NotRequired[
        "capo_ssm_quicksetup.types.iam_role_arn.IAMRoleArn"
    ]
    """<p>The ARN of the IAM role used to administrate local configuration deployments.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the configuration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationDefinition) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    import capo_ssm_quicksetup.types.configuration_parameters_map

    out["Parameters"] = (
        capo_ssm_quicksetup.types.configuration_parameters_map.serialize_json(
            value["parameters"]
        )
    )
    if "type_version" in value:
        out["TypeVersion"] = value["type_version"]
    if "local_deployment_execution_role_name" in value:
        out["LocalDeploymentExecutionRoleName"] = value[
            "local_deployment_execution_role_name"
        ]
    if "local_deployment_administration_role_arn" in value:
        out["LocalDeploymentAdministrationRoleArn"] = value[
            "local_deployment_administration_role_arn"
        ]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ConfigurationDefinition:
    out: ConfigurationDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("Parameters") is not None:
        import capo_ssm_quicksetup.types.configuration_parameters_map

        out["parameters"] = (
            capo_ssm_quicksetup.types.configuration_parameters_map.deserialize_json(
                data["Parameters"]
            )
        )
    else:
        out["parameters"] = {}
    if data.get("TypeVersion") is not None:
        out["type_version"] = data["TypeVersion"]
    if data.get("LocalDeploymentExecutionRoleName") is not None:
        out["local_deployment_execution_role_name"] = data[
            "LocalDeploymentExecutionRoleName"
        ]
    if data.get("LocalDeploymentAdministrationRoleArn") is not None:
        out["local_deployment_administration_role_arn"] = data[
            "LocalDeploymentAdministrationRoleArn"
        ]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
