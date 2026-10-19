"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateJobTemplateRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.client_token
    import capo_emr_containers.types.job_template_data
    import capo_emr_containers.types.kms_key_arn
    import capo_emr_containers.types.resource_name_string
    import capo_emr_containers.types.tag_map


class CreateJobTemplateRequest(TypedDict, closed=True):
    name: "capo_emr_containers.types.resource_name_string.ResourceNameString"
    """<p>The specified name of the job template.</p>"""
    client_token: "capo_emr_containers.types.client_token.ClientToken"
    """<p>The client token of the job template.</p>"""
    job_template_data: "capo_emr_containers.types.job_template_data.JobTemplateData"
    """<p>The job template data which holds values of StartJobRun API request.</p>"""
    tags: NotRequired["capo_emr_containers.types.tag_map.TagMap"]
    """<p>The tags that are associated with the job template.</p>"""
    kms_key_arn: NotRequired["capo_emr_containers.types.kms_key_arn.KmsKeyArn"]
    """<p>The KMS key ARN used to encrypt the job template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobTemplateRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["clientToken"] = value["client_token"]
    import capo_emr_containers.types.job_template_data

    out["jobTemplateData"] = capo_emr_containers.types.job_template_data.serialize_json(
        value["job_template_data"]
    )
    if "tags" in value:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.serialize_json(value["tags"])
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateJobTemplateRequest:
    out: CreateJobTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("jobTemplateData") is not None:
        import capo_emr_containers.types.job_template_data

        out["job_template_data"] = (
            capo_emr_containers.types.job_template_data.deserialize_json(
                data["jobTemplateData"]
            )
        )
    else:
        raise DeserializationError(
            "CreateJobTemplateRequest.job_template_data required"
        )
    if data.get("tags") is not None:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.deserialize_json(data["tags"])
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out


def redact_sensitive(value: CreateJobTemplateRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_template_data" in value:
        import capo_emr_containers.types.job_template_data

        out["job_template_data"] = (
            capo_emr_containers.types.job_template_data.redact_sensitive(
                value["job_template_data"]
            )
        )
    return out
