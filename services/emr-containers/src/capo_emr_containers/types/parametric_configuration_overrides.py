"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ParametricConfigurationOverrides``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.configuration_list
    import capo_emr_containers.types.parametric_monitoring_configuration


class ParametricConfigurationOverrides(TypedDict, closed=True):
    application_configuration: NotRequired[
        "capo_emr_containers.types.configuration_list.ConfigurationList"
    ]
    """<p> The configurations for the application running by the job run.</p>"""
    monitoring_configuration: NotRequired[
        "capo_emr_containers.types.parametric_monitoring_configuration.ParametricMonitoringConfiguration"
    ]
    """<p> The configurations for monitoring. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParametricConfigurationOverrides) -> dict:
    out: dict = {}
    if "application_configuration" in value:
        import capo_emr_containers.types.configuration_list

        out["applicationConfiguration"] = (
            capo_emr_containers.types.configuration_list.serialize_json(
                value["application_configuration"]
            )
        )
    if "monitoring_configuration" in value:
        import capo_emr_containers.types.parametric_monitoring_configuration

        out["monitoringConfiguration"] = (
            capo_emr_containers.types.parametric_monitoring_configuration.serialize_json(
                value["monitoring_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParametricConfigurationOverrides:
    out: ParametricConfigurationOverrides = {}  # type: ignore[typeddict-item]
    if data.get("applicationConfiguration") is not None:
        import capo_emr_containers.types.configuration_list

        out["application_configuration"] = (
            capo_emr_containers.types.configuration_list.deserialize_json(
                data["applicationConfiguration"]
            )
        )
    if data.get("monitoringConfiguration") is not None:
        import capo_emr_containers.types.parametric_monitoring_configuration

        out["monitoring_configuration"] = (
            capo_emr_containers.types.parametric_monitoring_configuration.deserialize_json(
                data["monitoringConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ParametricConfigurationOverrides) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "application_configuration" in value:
        import capo_emr_containers.types.configuration_list

        out["application_configuration"] = (
            capo_emr_containers.types.configuration_list.redact_sensitive(
                value["application_configuration"]
            )
        )
    return out
