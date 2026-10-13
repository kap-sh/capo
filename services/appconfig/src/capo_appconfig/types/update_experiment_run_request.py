"""Generated from Smithy shape ``com.amazonaws.appconfig#UpdateExperimentRunRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.deployment_parameters
    import capo_appconfig.types.description
    import capo_appconfig.types.identifier
    import capo_appconfig.types.nullable_percentage
    import capo_appconfig.types.positive_integer
    import capo_appconfig.types.treatment_overrides


class UpdateExperimentRunRequest(TypedDict, closed=True):
    application_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The application ID or name.</p>"""
    experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The experiment definition ID or name.</p>"""
    run: "capo_appconfig.types.positive_integer.PositiveInteger"
    """<p>The run number to update.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>An updated description for the experiment run.</p>"""
    exposure_percentage: NotRequired[
        "capo_appconfig.types.nullable_percentage.NullablePercentage"
    ]
    """<p>The new exposure percentage. This value can only be increased from the current setting.</p>"""
    treatment_overrides: NotRequired[
        "capo_appconfig.types.treatment_overrides.TreatmentOverrides"
    ]
    """<p>The updated treatment assignment overrides that assign specific entity IDs to treatments, bypassing random assignment.</p>"""
    deployment_parameters: NotRequired[
        "capo_appconfig.types.deployment_parameters.DeploymentParameters"
    ]
    """<p>The updated deployment parameters for the experiment run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExperimentRunRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "exposure_percentage" in value:
        out["ExposurePercentage"] = (
            "NaN"
            if value["exposure_percentage"] != value["exposure_percentage"]
            else "Infinity"
            if value["exposure_percentage"] == float("inf")
            else "-Infinity"
            if value["exposure_percentage"] == float("-inf")
            else value["exposure_percentage"]
        )
    if "treatment_overrides" in value:
        import capo_appconfig.types.treatment_overrides

        out["TreatmentOverrides"] = (
            capo_appconfig.types.treatment_overrides.serialize_json(
                value["treatment_overrides"]
            )
        )
    if "deployment_parameters" in value:
        import capo_appconfig.types.deployment_parameters

        out["DeploymentParameters"] = (
            capo_appconfig.types.deployment_parameters.serialize_json(
                value["deployment_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateExperimentRunRequest:
    out: UpdateExperimentRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ExposurePercentage") is not None:
        out["exposure_percentage"] = float(data["ExposurePercentage"])
    if data.get("TreatmentOverrides") is not None:
        import capo_appconfig.types.treatment_overrides

        out["treatment_overrides"] = (
            capo_appconfig.types.treatment_overrides.deserialize_json(
                data["TreatmentOverrides"]
            )
        )
    if data.get("DeploymentParameters") is not None:
        import capo_appconfig.types.deployment_parameters

        out["deployment_parameters"] = (
            capo_appconfig.types.deployment_parameters.deserialize_json(
                data["DeploymentParameters"]
            )
        )
    return out


def redact_sensitive(value: UpdateExperimentRunRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "deployment_parameters" in value:
        import capo_appconfig.types.deployment_parameters

        out["deployment_parameters"] = (
            capo_appconfig.types.deployment_parameters.redact_sensitive(
                value["deployment_parameters"]
            )
        )
    return out
