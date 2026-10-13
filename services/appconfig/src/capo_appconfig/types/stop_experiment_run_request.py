"""Generated from Smithy shape ``com.amazonaws.appconfig#StopExperimentRunRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.deployment_parameters
    import capo_appconfig.types.experiment_run_result
    import capo_appconfig.types.identifier
    import capo_appconfig.types.positive_integer


class StopExperimentRunRequest(TypedDict, closed=True):
    application_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The application ID or name.</p>"""
    experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The experiment definition ID or name.</p>"""
    run: "capo_appconfig.types.positive_integer.PositiveInteger"
    """<p>The run number to stop.</p>"""
    result: NotRequired[
        "capo_appconfig.types.experiment_run_result.ExperimentRunResult"
    ]
    """<p>The result of the experiment run, including an executive summary and reasons for or against launching.</p>"""
    deployment_parameters: NotRequired[
        "capo_appconfig.types.deployment_parameters.DeploymentParameters"
    ]
    """<p>The deployment parameters for the stop operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopExperimentRunRequest) -> dict:
    out: dict = {}
    if "result" in value:
        import capo_appconfig.types.experiment_run_result

        out["Result"] = capo_appconfig.types.experiment_run_result.serialize_json(
            value["result"]
        )
    if "deployment_parameters" in value:
        import capo_appconfig.types.deployment_parameters

        out["DeploymentParameters"] = (
            capo_appconfig.types.deployment_parameters.serialize_json(
                value["deployment_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> StopExperimentRunRequest:
    out: StopExperimentRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("Result") is not None:
        import capo_appconfig.types.experiment_run_result

        out["result"] = capo_appconfig.types.experiment_run_result.deserialize_json(
            data["Result"]
        )
    if data.get("DeploymentParameters") is not None:
        import capo_appconfig.types.deployment_parameters

        out["deployment_parameters"] = (
            capo_appconfig.types.deployment_parameters.deserialize_json(
                data["DeploymentParameters"]
            )
        )
    return out


def redact_sensitive(value: StopExperimentRunRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "deployment_parameters" in value:
        import capo_appconfig.types.deployment_parameters

        out["deployment_parameters"] = (
            capo_appconfig.types.deployment_parameters.redact_sensitive(
                value["deployment_parameters"]
            )
        )
    return out
