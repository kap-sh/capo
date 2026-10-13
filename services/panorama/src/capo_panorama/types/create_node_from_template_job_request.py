"""Generated from Smithy shape ``com.amazonaws.panorama#CreateNodeFromTemplateJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.description
    import capo_panorama.types.job_tags_list
    import capo_panorama.types.node_name
    import capo_panorama.types.node_package_name
    import capo_panorama.types.node_package_version
    import capo_panorama.types.template_parameters_map
    import capo_panorama.types.template_type


class CreateNodeFromTemplateJobRequest(TypedDict, closed=True):
    template_type: "capo_panorama.types.template_type.TemplateType"
    """<p>The type of node.</p>"""
    output_package_name: "capo_panorama.types.node_package_name.NodePackageName"
    """<p>An output package name for the node.</p>"""
    output_package_version: (
        "capo_panorama.types.node_package_version.NodePackageVersion"
    )
    """<p>An output package version for the node.</p>"""
    node_name: "capo_panorama.types.node_name.NodeName"
    """<p>A name for the node.</p>"""
    node_description: NotRequired["capo_panorama.types.description.Description"]
    """<p>A description for the node.</p>"""
    template_parameters: (
        "capo_panorama.types.template_parameters_map.TemplateParametersMap"
    )
    """<p>Template parameters for the node.</p>"""
    job_tags: NotRequired["capo_panorama.types.job_tags_list.JobTagsList"]
    """<p>Tags for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodeFromTemplateJobRequest) -> dict:
    out: dict = {}
    out["TemplateType"] = value["template_type"]
    out["OutputPackageName"] = value["output_package_name"]
    out["OutputPackageVersion"] = value["output_package_version"]
    out["NodeName"] = value["node_name"]
    if "node_description" in value:
        out["NodeDescription"] = value["node_description"]
    import capo_panorama.types.template_parameters_map

    out["TemplateParameters"] = (
        capo_panorama.types.template_parameters_map.serialize_json(
            value["template_parameters"]
        )
    )
    if "job_tags" in value:
        import capo_panorama.types.job_tags_list

        out["JobTags"] = capo_panorama.types.job_tags_list.serialize_json(
            value["job_tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateNodeFromTemplateJobRequest:
    out: CreateNodeFromTemplateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("TemplateType") is not None:
        out["template_type"] = data["TemplateType"]
    else:
        raise DeserializationError(
            "CreateNodeFromTemplateJobRequest.template_type required"
        )
    if data.get("OutputPackageName") is not None:
        out["output_package_name"] = data["OutputPackageName"]
    else:
        raise DeserializationError(
            "CreateNodeFromTemplateJobRequest.output_package_name required"
        )
    if data.get("OutputPackageVersion") is not None:
        out["output_package_version"] = data["OutputPackageVersion"]
    else:
        raise DeserializationError(
            "CreateNodeFromTemplateJobRequest.output_package_version required"
        )
    if data.get("NodeName") is not None:
        out["node_name"] = data["NodeName"]
    else:
        raise DeserializationError(
            "CreateNodeFromTemplateJobRequest.node_name required"
        )
    if data.get("NodeDescription") is not None:
        out["node_description"] = data["NodeDescription"]
    if data.get("TemplateParameters") is not None:
        import capo_panorama.types.template_parameters_map

        out["template_parameters"] = (
            capo_panorama.types.template_parameters_map.deserialize_json(
                data["TemplateParameters"]
            )
        )
    else:
        raise DeserializationError(
            "CreateNodeFromTemplateJobRequest.template_parameters required"
        )
    if data.get("JobTags") is not None:
        import capo_panorama.types.job_tags_list

        out["job_tags"] = capo_panorama.types.job_tags_list.deserialize_json(
            data["JobTags"]
        )
    return out


def redact_sensitive(value: CreateNodeFromTemplateJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template_parameters" in value:
        import capo_panorama.types.template_parameters_map

        out["template_parameters"] = (
            capo_panorama.types.template_parameters_map.redact_sensitive(
                value["template_parameters"]
            )
        )
    return out
