"""Generated from Smithy shape ``com.amazonaws.s3control#CreateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.confirmation_required
    import capo_s3_control.types.iam_role_arn
    import capo_s3_control.types.job_manifest
    import capo_s3_control.types.job_manifest_generator
    import capo_s3_control.types.job_operation
    import capo_s3_control.types.job_priority
    import capo_s3_control.types.job_report
    import capo_s3_control.types.non_empty_max_length64_string
    import capo_s3_control.types.non_empty_max_length256_string
    import capo_s3_control.types.s3_tag_set


class CreateJobRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID that creates the job.</p>"""
    confirmation_required: NotRequired[
        "capo_s3_control.types.confirmation_required.ConfirmationRequired"
    ]
    """<p>Indicates whether confirmation is required before Amazon S3 runs the job. Confirmation is only required for jobs created through the Amazon S3 console.</p>"""
    operation: "capo_s3_control.types.job_operation.JobOperation"
    """<p>The action that you want this job to perform on every object listed in the manifest. For more information about the available actions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html">Operations</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    report: "capo_s3_control.types.job_report.JobReport"
    """<p>Configuration parameters for the optional job-completion report.</p>"""
    client_request_token: (
        "capo_s3_control.types.non_empty_max_length64_string.NonEmptyMaxLength64String"
    )
    """<p>An idempotency token to ensure that you don't accidentally submit the same request twice. You can use any string up to the maximum length.</p>"""
    manifest: NotRequired["capo_s3_control.types.job_manifest.JobManifest"]
    """<p>Configuration parameters for the manifest.</p>"""
    description: NotRequired[
        "capo_s3_control.types.non_empty_max_length256_string.NonEmptyMaxLength256String"
    ]
    """<p>A description for this job. You can use any string within the permitted length. Descriptions don't need to be unique and can be used for multiple jobs.</p>"""
    priority: "capo_s3_control.types.job_priority.JobPriority"
    """<p>The numerical priority for this job. Higher numbers indicate higher priority.</p>"""
    role_arn: "capo_s3_control.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) role that Batch Operations will use to run this job's action on every object in the manifest.</p>"""
    tags: NotRequired["capo_s3_control.types.s3_tag_set.S3TagSet"]
    """<p>A set of tags to associate with the S3 Batch Operations job. This is an optional parameter. </p>"""
    manifest_generator: NotRequired[
        "capo_s3_control.types.job_manifest_generator.JobManifestGenerator"
    ]
    """<p>The attribute container for the ManifestGenerator details. Jobs must be created with either a manifest file or a ManifestGenerator, but not both.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateJobRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "confirmation_required" in value:
        SubElement(el, "ConfirmationRequired").text = (
            "true" if value["confirmation_required"] else "false"
        )
    import capo_s3_control.types.job_operation

    capo_s3_control.types.job_operation.serialize_xml(
        value["operation"], el, "Operation"
    )
    import capo_s3_control.types.job_report

    capo_s3_control.types.job_report.serialize_xml(value["report"], el, "Report")
    SubElement(el, "ClientRequestToken").text = str(value["client_request_token"])
    if "manifest" in value:
        import capo_s3_control.types.job_manifest

        capo_s3_control.types.job_manifest.serialize_xml(
            value["manifest"], el, "Manifest"
        )
    if "description" in value:
        SubElement(el, "Description").text = str(value["description"])
    SubElement(el, "Priority").text = str(value["priority"])
    SubElement(el, "RoleArn").text = str(value["role_arn"])
    if "tags" in value:
        import capo_s3_control.types.s3_tag_set

        capo_s3_control.types.s3_tag_set.serialize_xml(value["tags"], el, "Tags")
    if "manifest_generator" in value:
        import capo_s3_control.types.job_manifest_generator

        capo_s3_control.types.job_manifest_generator.serialize_xml(
            value["manifest_generator"], el, "ManifestGenerator"
        )


def deserialize_xml(el: Element) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    child_confirmation_required = el.find("ConfirmationRequired")
    if child_confirmation_required is not None:
        out["confirmation_required"] = (
            child_confirmation_required.text or ""
        ).lower() == "true"
    child_operation = el.find("Operation")
    if child_operation is not None:
        import capo_s3_control.types.job_operation

        out["operation"] = capo_s3_control.types.job_operation.deserialize_xml(
            child_operation
        )
    else:
        raise DeserializationError("CreateJobRequest.operation required")
    child_report = el.find("Report")
    if child_report is not None:
        import capo_s3_control.types.job_report

        out["report"] = capo_s3_control.types.job_report.deserialize_xml(child_report)
    else:
        raise DeserializationError("CreateJobRequest.report required")
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    else:
        raise DeserializationError("CreateJobRequest.client_request_token required")
    child_manifest = el.find("Manifest")
    if child_manifest is not None:
        import capo_s3_control.types.job_manifest

        out["manifest"] = capo_s3_control.types.job_manifest.deserialize_xml(
            child_manifest
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    else:
        raise DeserializationError("CreateJobRequest.priority required")
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    else:
        raise DeserializationError("CreateJobRequest.role_arn required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.s3_tag_set

        out["tags"] = capo_s3_control.types.s3_tag_set.deserialize_xml(child_tags)
    child_manifest_generator = el.find("ManifestGenerator")
    if child_manifest_generator is not None:
        import capo_s3_control.types.job_manifest_generator

        out["manifest_generator"] = (
            capo_s3_control.types.job_manifest_generator.deserialize_xml(
                child_manifest_generator
            )
        )
    return out
