"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDomainOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_status
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.domain_version
    import capo_datazone.types.kms_key_arn
    import capo_datazone.types.role_arn
    import capo_datazone.types.single_sign_on
    import capo_datazone.types.tags


class CreateDomainOutput(TypedDict, closed=True):
    id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    root_domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the root domain unit.</p>"""
    name: NotRequired["str"]
    """<p>The name of the Amazon DataZone domain.</p>"""
    description: NotRequired["str"]
    """<p>The description of the Amazon DataZone domain.</p>"""
    single_sign_on: NotRequired["capo_datazone.types.single_sign_on.SingleSignOn"]
    """<p>The single-sign on configuration of the Amazon DataZone domain.</p>"""
    domain_execution_role: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the Amazon Web Services account that houses the Amazon DataZone domain.</p>"""
    arn: NotRequired["str"]
    """<p>The ARN of the Amazon DataZone domain.</p>"""
    kms_key_identifier: NotRequired["capo_datazone.types.kms_key_arn.KmsKeyArn"]
    """<p>The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data. </p>"""
    status: NotRequired["capo_datazone.types.domain_status.DomainStatus"]
    """<p>The status of the Amazon DataZone domain.</p>"""
    portal_url: NotRequired["str"]
    """<p>The URL of the data portal for this Amazon DataZone domain.</p>"""
    tags: NotRequired["capo_datazone.types.tags.Tags"]
    """<p>The tags specified for the Amazon DataZone domain.</p>"""
    domain_version: NotRequired["capo_datazone.types.domain_version.DomainVersion"]
    """<p>The version of the domain that is created.</p>"""
    service_role: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>Te service role of the domain that is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainOutput) -> dict:
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
    if "domain_execution_role" in value:
        out["domainExecutionRole"] = value["domain_execution_role"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "kms_key_identifier" in value:
        out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    if "status" in value:
        import capo_datazone.types.domain_status

        out["status"] = capo_datazone.types.domain_status.serialize_json(
            value["status"]
        )
    if "portal_url" in value:
        out["portalUrl"] = value["portal_url"]
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
    return out


def deserialize_json(data: dict) -> CreateDomainOutput:
    out: CreateDomainOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("kmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    if data.get("status") is not None:
        import capo_datazone.types.domain_status

        out["status"] = capo_datazone.types.domain_status.deserialize_json(
            data["status"]
        )
    if data.get("portalUrl") is not None:
        out["portal_url"] = data["portalUrl"]
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
    return out
