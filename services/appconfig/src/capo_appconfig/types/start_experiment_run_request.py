"""Generated from Smithy shape ``com.amazonaws.appconfig#StartExperimentRunRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.deployment_parameters
    import capo_appconfig.types.description
    import capo_appconfig.types.identifier
    import capo_appconfig.types.nullable_percentage
    import capo_appconfig.types.tag_map
    import capo_appconfig.types.treatment_overrides


class StartExperimentRunRequest(TypedDict, closed=True):
    application_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The application ID or name.</p>"""
    experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The experiment definition ID or name.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of this experiment run.</p>"""
    exposure_percentage: NotRequired[
        "capo_appconfig.types.nullable_percentage.NullablePercentage"
    ]
    """<p>The percentage of the target audience to expose to treatments. Set to 0 to validate the experiment before exposing production users.</p>"""
    treatment_overrides: NotRequired[
        "capo_appconfig.types.treatment_overrides.TreatmentOverrides"
    ]
    """<p>Treatment assignment overrides that assign specific entity IDs to treatments directly, bypassing random assignment.</p>"""
    tags: NotRequired["capo_appconfig.types.tag_map.TagMap"]
    """<p>The tags to assign to the experiment run.</p>"""
    deployment_parameters: NotRequired[
        "capo_appconfig.types.deployment_parameters.DeploymentParameters"
    ]
    """<p>The deployment parameters for the experiment run, including a KMS key identifier for encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExperimentRunRequest) -> dict:
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
    if "tags" in value:
        import capo_appconfig.types.tag_map

        out["Tags"] = capo_appconfig.types.tag_map.serialize_json(value["tags"])
    if "deployment_parameters" in value:
        import capo_appconfig.types.deployment_parameters

        out["DeploymentParameters"] = (
            capo_appconfig.types.deployment_parameters.serialize_json(
                value["deployment_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartExperimentRunRequest:
    out: StartExperimentRunRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Tags") is not None:
        import capo_appconfig.types.tag_map

        out["tags"] = capo_appconfig.types.tag_map.deserialize_json(data["Tags"])
    if data.get("DeploymentParameters") is not None:
        import capo_appconfig.types.deployment_parameters

        out["deployment_parameters"] = (
            capo_appconfig.types.deployment_parameters.deserialize_json(
                data["DeploymentParameters"]
            )
        )
    return out


def redact_sensitive(value: StartExperimentRunRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "deployment_parameters" in value:
        import capo_appconfig.types.deployment_parameters

        out["deployment_parameters"] = (
            capo_appconfig.types.deployment_parameters.redact_sensitive(
                value["deployment_parameters"]
            )
        )
    return out
