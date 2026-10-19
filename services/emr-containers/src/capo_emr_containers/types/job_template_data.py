"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobTemplateData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.job_driver
    import capo_emr_containers.types.parametric_configuration_overrides
    import capo_emr_containers.types.parametric_iam_role_arn
    import capo_emr_containers.types.parametric_release_label
    import capo_emr_containers.types.tag_map
    import capo_emr_containers.types.template_parameter_configuration_map


class JobTemplateData(TypedDict, closed=True):
    execution_role_arn: (
        "capo_emr_containers.types.parametric_iam_role_arn.ParametricIAMRoleArn"
    )
    """<p>The execution role ARN of the job run.</p>"""
    release_label: (
        "capo_emr_containers.types.parametric_release_label.ParametricReleaseLabel"
    )
    """<p> The release version of Amazon EMR.</p>"""
    configuration_overrides: NotRequired[
        "capo_emr_containers.types.parametric_configuration_overrides.ParametricConfigurationOverrides"
    ]
    """<p> The configuration settings that are used to override defaults configuration.</p>"""
    job_driver: "capo_emr_containers.types.job_driver.JobDriver"
    parameter_configuration: NotRequired[
        "capo_emr_containers.types.template_parameter_configuration_map.TemplateParameterConfigurationMap"
    ]
    """<p>The configuration of parameters existing in the job template.</p>"""
    job_tags: NotRequired["capo_emr_containers.types.tag_map.TagMap"]
    """<p>The tags assigned to jobs started using the job template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplateData) -> dict:
    out: dict = {}
    out["executionRoleArn"] = value["execution_role_arn"]
    out["releaseLabel"] = value["release_label"]
    if "configuration_overrides" in value:
        import capo_emr_containers.types.parametric_configuration_overrides

        out["configurationOverrides"] = (
            capo_emr_containers.types.parametric_configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    import capo_emr_containers.types.job_driver

    out["jobDriver"] = capo_emr_containers.types.job_driver.serialize_json(
        value["job_driver"]
    )
    if "parameter_configuration" in value:
        import capo_emr_containers.types.template_parameter_configuration_map

        out["parameterConfiguration"] = (
            capo_emr_containers.types.template_parameter_configuration_map.serialize_json(
                value["parameter_configuration"]
            )
        )
    if "job_tags" in value:
        import capo_emr_containers.types.tag_map

        out["jobTags"] = capo_emr_containers.types.tag_map.serialize_json(
            value["job_tags"]
        )
    return out


def deserialize_json(data: dict) -> JobTemplateData:
    out: JobTemplateData = {}  # type: ignore[typeddict-item]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("releaseLabel") is not None:
        out["release_label"] = data["releaseLabel"]
    else:
        out["release_label"] = ""
    if data.get("configurationOverrides") is not None:
        import capo_emr_containers.types.parametric_configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_containers.types.parametric_configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if data.get("jobDriver") is not None:
        import capo_emr_containers.types.job_driver

        out["job_driver"] = capo_emr_containers.types.job_driver.deserialize_json(
            data["jobDriver"]
        )
    else:
        raise DeserializationError("JobTemplateData.job_driver required")
    if data.get("parameterConfiguration") is not None:
        import capo_emr_containers.types.template_parameter_configuration_map

        out["parameter_configuration"] = (
            capo_emr_containers.types.template_parameter_configuration_map.deserialize_json(
                data["parameterConfiguration"]
            )
        )
    if data.get("jobTags") is not None:
        import capo_emr_containers.types.tag_map

        out["job_tags"] = capo_emr_containers.types.tag_map.deserialize_json(
            data["jobTags"]
        )
    return out


def redact_sensitive(value: JobTemplateData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration_overrides" in value:
        import capo_emr_containers.types.parametric_configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_containers.types.parametric_configuration_overrides.redact_sensitive(
                value["configuration_overrides"]
            )
        )
    if "job_driver" in value:
        import capo_emr_containers.types.job_driver

        out["job_driver"] = capo_emr_containers.types.job_driver.redact_sensitive(
            value["job_driver"]
        )
    return out
