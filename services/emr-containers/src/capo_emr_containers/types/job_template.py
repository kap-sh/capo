"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobTemplate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.date
    import capo_emr_containers.types.job_template_arn
    import capo_emr_containers.types.job_template_data
    import capo_emr_containers.types.kms_key_arn
    import capo_emr_containers.types.request_identity_user_arn
    import capo_emr_containers.types.resource_id_string
    import capo_emr_containers.types.resource_name_string
    import capo_emr_containers.types.string2048
    import capo_emr_containers.types.tag_map


class JobTemplate(TypedDict, closed=True):
    name: NotRequired[
        "capo_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The name of the job template.</p>"""
    id: NotRequired["capo_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The ID of the job template.</p>"""
    arn: NotRequired["capo_emr_containers.types.job_template_arn.JobTemplateArn"]
    """<p>The ARN of the job template.</p>"""
    created_at: NotRequired["capo_emr_containers.types.date.Date"]
    """<p> The date and time when the job template was created.</p>"""
    created_by: NotRequired[
        "capo_emr_containers.types.request_identity_user_arn.RequestIdentityUserArn"
    ]
    """<p> The user who created the job template.</p>"""
    tags: NotRequired["capo_emr_containers.types.tag_map.TagMap"]
    """<p>The tags assigned to the job template.</p>"""
    job_template_data: "capo_emr_containers.types.job_template_data.JobTemplateData"
    """<p>The job template data which holds values of StartJobRun API request.</p>"""
    kms_key_arn: NotRequired["capo_emr_containers.types.kms_key_arn.KmsKeyArn"]
    """<p> The KMS key ARN used to encrypt the job template.</p>"""
    decryption_error: NotRequired["capo_emr_containers.types.string2048.String2048"]
    """<p>The error message in case the decryption of job template fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplate) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_emr_containers.types.date

        out["createdAt"] = capo_emr_containers.types.date.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "tags" in value:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.serialize_json(value["tags"])
    import capo_emr_containers.types.job_template_data

    out["jobTemplateData"] = capo_emr_containers.types.job_template_data.serialize_json(
        value["job_template_data"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "decryption_error" in value:
        out["decryptionError"] = value["decryption_error"]
    return out


def deserialize_json(data: dict) -> JobTemplate:
    out: JobTemplate = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("createdAt") is not None:
        import capo_emr_containers.types.date

        out["created_at"] = capo_emr_containers.types.date.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("tags") is not None:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.deserialize_json(data["tags"])
    if data.get("jobTemplateData") is not None:
        import capo_emr_containers.types.job_template_data

        out["job_template_data"] = (
            capo_emr_containers.types.job_template_data.deserialize_json(
                data["jobTemplateData"]
            )
        )
    else:
        raise DeserializationError("JobTemplate.job_template_data required")
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("decryptionError") is not None:
        out["decryption_error"] = data["decryptionError"]
    return out


def redact_sensitive(value: JobTemplate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_template_data" in value:
        import capo_emr_containers.types.job_template_data

        out["job_template_data"] = (
            capo_emr_containers.types.job_template_data.redact_sensitive(
                value["job_template_data"]
            )
        )
    return out
