"""Generated from Smithy shape ``com.amazonaws.datazone#GetDomainOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.delete_progress
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_status
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.domain_version
    import capo_datazone.types.failure_reasons_list
    import capo_datazone.types.kms_key_arn
    import capo_datazone.types.role_arn
    import capo_datazone.types.single_sign_on
    import capo_datazone.types.tags
    import capo_datazone.types.updated_at


class GetDomainOutput(TypedDict, closed=True):
    id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the specified Amazon DataZone domain.</p>"""
    root_domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the root domain in Amazon Datazone.</p>"""
    name: NotRequired["str"]
    """<p>The name of the Amazon DataZone domain.</p>"""
    description: NotRequired["str"]
    """<p>The description of the Amazon DataZone domain.</p>"""
    single_sign_on: NotRequired["capo_datazone.types.single_sign_on.SingleSignOn"]
    """<p>The single sing-on option of the specified Amazon DataZone domain.</p>"""
    domain_execution_role: "capo_datazone.types.role_arn.RoleArn"
    """<p>The domain execution role with which the Amazon DataZone domain is created.</p>"""
    arn: NotRequired["str"]
    """<p>The ARN of the specified Amazon DataZone domain.</p>"""
    kms_key_identifier: NotRequired["capo_datazone.types.kms_key_arn.KmsKeyArn"]
    """<p>The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data. </p>"""
    status: "capo_datazone.types.domain_status.DomainStatus"
    """<p>The status of the specified Amazon DataZone domain.</p>"""
    portal_url: NotRequired["str"]
    """<p>The URL of the data portal for this Amazon DataZone domain.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the Amazon DataZone domain was created.</p>"""
    last_updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the Amazon DataZone domain was last updated.</p>"""
    tags: NotRequired["capo_datazone.types.tags.Tags"]
    """<p>The tags specified for the Amazon DataZone domain.</p>"""
    domain_version: NotRequired["capo_datazone.types.domain_version.DomainVersion"]
    """<p>The version of the domain.</p>"""
    service_role: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>The service role of the domain.</p>"""
    failure_reasons: NotRequired[
        "capo_datazone.types.failure_reasons_list.FailureReasonsList"
    ]
    """<p>The list of failure reasons for resources that Amazon DataZone could not delete during a cascade deletion of the domain.</p>"""
    delete_progress: NotRequired["capo_datazone.types.delete_progress.DeleteProgress"]
    """<p>The progress of the current domain deletion, including the number of projects that Amazon DataZone successfully deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "root_domain_unit_id" in value:
        out["rootDomainUnitId"] = value["root_domain_unit_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "single_sign_on" in value:
        import capo_datazone.types.single_sign_on

        out["singleSignOn"] = capo_datazone.types.single_sign_on.serialize_json(
            value["single_sign_on"]
        )
    out["domainExecutionRole"] = value["domain_execution_role"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "kms_key_identifier" in value:
        out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    import capo_datazone.types.domain_status

    out["status"] = capo_datazone.types.domain_status.serialize_json(value["status"])
    if "portal_url" in value:
        out["portalUrl"] = value["portal_url"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_datazone.types.updated_at

        out["lastUpdatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["last_updated_at"]
        )
    if "tags" in value:
        import capo_datazone.types.tags

        out["tags"] = capo_datazone.types.tags.serialize_json(value["tags"])
    if "domain_version" in value:
        import capo_datazone.types.domain_version

        out["domainVersion"] = capo_datazone.types.domain_version.serialize_json(
            value["domain_version"]
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "failure_reasons" in value:
        import capo_datazone.types.failure_reasons_list

        out["failureReasons"] = capo_datazone.types.failure_reasons_list.serialize_json(
            value["failure_reasons"]
        )
    if "delete_progress" in value:
        import capo_datazone.types.delete_progress

        out["deleteProgress"] = capo_datazone.types.delete_progress.serialize_json(
            value["delete_progress"]
        )
    return out


def deserialize_json(data: dict) -> GetDomainOutput:
    out: GetDomainOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("rootDomainUnitId") is not None:
        out["root_domain_unit_id"] = data["rootDomainUnitId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("singleSignOn") is not None:
        import capo_datazone.types.single_sign_on

        out["single_sign_on"] = capo_datazone.types.single_sign_on.deserialize_json(
            data["singleSignOn"]
        )
    if data.get("domainExecutionRole") is not None:
        out["domain_execution_role"] = data["domainExecutionRole"]
    else:
        out["domain_execution_role"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("kmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    if data.get("status") is not None:
        import capo_datazone.types.domain_status

        out["status"] = capo_datazone.types.domain_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.domain_status.DomainStatus", ""
        )
    if data.get("portalUrl") is not None:
        out["portal_url"] = data["portalUrl"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_datazone.types.updated_at

        out["last_updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["lastUpdatedAt"]
        )
    if data.get("tags") is not None:
        import capo_datazone.types.tags

        out["tags"] = capo_datazone.types.tags.deserialize_json(data["tags"])
    if data.get("domainVersion") is not None:
        import capo_datazone.types.domain_version

        out["domain_version"] = capo_datazone.types.domain_version.deserialize_json(
            data["domainVersion"]
        )
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("failureReasons") is not None:
        import capo_datazone.types.failure_reasons_list

        out["failure_reasons"] = (
            capo_datazone.types.failure_reasons_list.deserialize_json(
                data["failureReasons"]
            )
        )
    if data.get("deleteProgress") is not None:
        import capo_datazone.types.delete_progress

        out["delete_progress"] = capo_datazone.types.delete_progress.deserialize_json(
            data["deleteProgress"]
        )
    return out
