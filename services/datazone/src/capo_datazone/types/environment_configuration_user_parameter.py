"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfigurationUserParameter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.environment_configuration_name
    import capo_datazone.types.environment_id
    import capo_datazone.types.environment_parameters_list
    import capo_datazone.types.environment_resolved_account


class EnvironmentConfigurationUserParameter(TypedDict, closed=True):
    environment_id: NotRequired["capo_datazone.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment.</p>"""
    environment_resolved_account: NotRequired[
        "capo_datazone.types.environment_resolved_account.EnvironmentResolvedAccount"
    ]
    """<p>Specifies the account/Region that is to be used during project creation for a particular blueprint.</p>"""
    environment_configuration_name: NotRequired[
        "capo_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    ]
    """<p>The environment configuration name.</p>"""
    environment_parameters: NotRequired[
        "capo_datazone.types.environment_parameters_list.EnvironmentParametersList"
    ]
    """<p>The environment parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationUserParameter) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "environment_resolved_account" in value:
        import capo_datazone.types.environment_resolved_account

        out["environmentResolvedAccount"] = (
            capo_datazone.types.environment_resolved_account.serialize_json(
                value["environment_resolved_account"]
            )
        )
    if "environment_configuration_name" in value:
        out["environmentConfigurationName"] = value["environment_configuration_name"]
    if "environment_parameters" in value:
        import capo_datazone.types.environment_parameters_list

        out["environmentParameters"] = (
            capo_datazone.types.environment_parameters_list.serialize_json(
                value["environment_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentConfigurationUserParameter:
    out: EnvironmentConfigurationUserParameter = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("environmentResolvedAccount") is not None:
        import capo_datazone.types.environment_resolved_account

        out["environment_resolved_account"] = (
            capo_datazone.types.environment_resolved_account.deserialize_json(
                data["environmentResolvedAccount"]
            )
        )
    if data.get("environmentConfigurationName") is not None:
        out["environment_configuration_name"] = data["environmentConfigurationName"]
    if data.get("environmentParameters") is not None:
        import capo_datazone.types.environment_parameters_list

        out["environment_parameters"] = (
            capo_datazone.types.environment_parameters_list.deserialize_json(
                data["environmentParameters"]
            )
        )
    return out


def redact_sensitive(value: EnvironmentConfigurationUserParameter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_configuration_name" in value:
        out["environment_configuration_name"] = "*** Sensitive Data Redacted ***"
    return out
