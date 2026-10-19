"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.account_pool_list
    import capo_datazone.types.aws_account
    import capo_datazone.types.deployment_mode
    import capo_datazone.types.deployment_order
    import capo_datazone.types.description
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.environment_configuration_id
    import capo_datazone.types.environment_configuration_name
    import capo_datazone.types.environment_configuration_parameters_details
    import capo_datazone.types.region


class EnvironmentConfiguration(TypedDict, closed=True):
    name: "capo_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    """<p>The environment name.</p>"""
    id: NotRequired[
        "capo_datazone.types.environment_configuration_id.EnvironmentConfigurationId"
    ]
    """<p>The environment ID.</p>"""
    environment_blueprint_id: (
        "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The environment blueprint ID.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The environment description.</p>"""
    deployment_mode: NotRequired["capo_datazone.types.deployment_mode.DeploymentMode"]
    """<p>The deployment mode of the environment.</p>"""
    configuration_parameters: NotRequired[
        "capo_datazone.types.environment_configuration_parameters_details.EnvironmentConfigurationParametersDetails"
    ]
    """<p>The configuration parameters of the environment.</p>"""
    aws_account: NotRequired["capo_datazone.types.aws_account.AwsAccount"]
    """<p>The Amazon Web Services account of the environment.</p>"""
    account_pools: NotRequired["capo_datazone.types.account_pool_list.AccountPoolList"]
    """<p>The account pools used by a custom project profile.</p>"""
    aws_region: NotRequired["capo_datazone.types.region.Region"]
    """<p>The Amazon Web Services Region of the environment.</p>"""
    deployment_order: NotRequired[
        "capo_datazone.types.deployment_order.DeploymentOrder"
    ]
    """<p>The deployment order of the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    out["environmentBlueprintId"] = value["environment_blueprint_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "deployment_mode" in value:
        import capo_datazone.types.deployment_mode

        out["deploymentMode"] = capo_datazone.types.deployment_mode.serialize_json(
            value["deployment_mode"]
        )
    if "configuration_parameters" in value:
        import capo_datazone.types.environment_configuration_parameters_details

        out["configurationParameters"] = (
            capo_datazone.types.environment_configuration_parameters_details.serialize_json(
                value["configuration_parameters"]
            )
        )
    if "aws_account" in value:
        import capo_datazone.types.aws_account

        out["awsAccount"] = capo_datazone.types.aws_account.serialize_json(
            value["aws_account"]
        )
    if "account_pools" in value:
        import capo_datazone.types.account_pool_list

        out["accountPools"] = capo_datazone.types.account_pool_list.serialize_json(
            value["account_pools"]
        )
    if "aws_region" in value:
        import capo_datazone.types.region

        out["awsRegion"] = capo_datazone.types.region.serialize_json(
            value["aws_region"]
        )
    if "deployment_order" in value:
        out["deploymentOrder"] = value["deployment_order"]
    return out


def deserialize_json(data: dict) -> EnvironmentConfiguration:
    out: EnvironmentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("environmentBlueprintId") is not None:
        out["environment_blueprint_id"] = data["environmentBlueprintId"]
    else:
        out["environment_blueprint_id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("deploymentMode") is not None:
        import capo_datazone.types.deployment_mode

        out["deployment_mode"] = capo_datazone.types.deployment_mode.deserialize_json(
            data["deploymentMode"]
        )
    if data.get("configurationParameters") is not None:
        import capo_datazone.types.environment_configuration_parameters_details

        out["configuration_parameters"] = (
            capo_datazone.types.environment_configuration_parameters_details.deserialize_json(
                data["configurationParameters"]
            )
        )
    if data.get("awsAccount") is not None:
        import capo_datazone.types.aws_account

        out["aws_account"] = capo_datazone.types.aws_account.deserialize_json(
            data["awsAccount"]
        )
    if data.get("accountPools") is not None:
        import capo_datazone.types.account_pool_list

        out["account_pools"] = capo_datazone.types.account_pool_list.deserialize_json(
            data["accountPools"]
        )
    if data.get("awsRegion") is not None:
        import capo_datazone.types.region

        out["aws_region"] = capo_datazone.types.region.deserialize_json(
            data["awsRegion"]
        )
    if data.get("deploymentOrder") is not None:
        out["deployment_order"] = data["deploymentOrder"]
    return out


def redact_sensitive(value: EnvironmentConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "id" in value:
        out["id"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
