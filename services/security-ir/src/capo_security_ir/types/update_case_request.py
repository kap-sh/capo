"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateCaseRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_security_ir.types.case_description
    import capo_security_ir.types.case_id
    import capo_security_ir.types.case_metadata
    import capo_security_ir.types.case_title
    import capo_security_ir.types.engagement_type
    import capo_security_ir.types.impacted_accounts
    import capo_security_ir.types.impacted_aws_region_list
    import capo_security_ir.types.impacted_services_list
    import capo_security_ir.types.threat_actor_ip_list
    import capo_security_ir.types.watchers


class UpdateCaseRequest(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Required element for UpdateCase to identify the case ID for updates.</p>"""
    title: NotRequired["capo_security_ir.types.case_title.CaseTitle"]
    """<p>Optional element for UpdateCase to provide content for the title field.</p>"""
    description: NotRequired["capo_security_ir.types.case_description.CaseDescription"]
    """<p>Optional element for UpdateCase to provide content for the description field.</p>"""
    reported_incident_start_date: NotRequired["datetime.datetime"]
    """<p>Optional element for UpdateCase to provide content for the customer reported incident start date field. </p>"""
    actual_incident_start_date: NotRequired["datetime.datetime"]
    """<p>Optional element for UpdateCase to provide content for the incident start date field.</p>"""
    engagement_type: NotRequired[
        "capo_security_ir.types.engagement_type.EngagementType"
    ]
    """<p>Optional element for UpdateCase to provide content for the engagement type field. <code>Available engagement types include Security Incident | Investigation</code>. </p>"""
    watchers_to_add: NotRequired["capo_security_ir.types.watchers.Watchers"]
    """<p>Optional element for UpdateCase to provide content to add additional watchers to a case.</p>"""
    watchers_to_delete: NotRequired["capo_security_ir.types.watchers.Watchers"]
    """<p>Optional element for UpdateCase to provide content to remove existing watchers from a case.</p>"""
    threat_actor_ip_addresses_to_add: NotRequired[
        "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
    ]
    """<p>Optional element for UpdateCase to provide content to add additional suspicious IP addresses related to a case. </p>"""
    threat_actor_ip_addresses_to_delete: NotRequired[
        "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
    ]
    """<p>Optional element for UpdateCase to provide content to remove suspicious IP addresses from a case.</p>"""
    impacted_services_to_add: NotRequired[
        "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
    ]
    """<p>Optional element for UpdateCase to provide content to add services impacted.</p>"""
    impacted_services_to_delete: NotRequired[
        "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
    ]
    """<p>Optional element for UpdateCase to provide content to remove services impacted.</p>"""
    impacted_aws_regions_to_add: NotRequired[
        "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
    ]
    """<p>Optional element for UpdateCase to provide content to add regions impacted.</p>"""
    impacted_aws_regions_to_delete: NotRequired[
        "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
    ]
    """<p>Optional element for UpdateCase to provide content to remove regions impacted.</p>"""
    impacted_accounts_to_add: NotRequired[
        "capo_security_ir.types.impacted_accounts.ImpactedAccounts"
    ]
    """<p>Optional element for UpdateCase to provide content to add accounts impacted.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>"""
    impacted_accounts_to_delete: NotRequired[
        "capo_security_ir.types.impacted_accounts.ImpactedAccounts"
    ]
    """<p>Optional element for UpdateCase to provide content to add accounts impacted.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>"""
    case_metadata: NotRequired["capo_security_ir.types.case_metadata.CaseMetadata"]
    """<p>Update the case request with case metadata</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCaseRequest) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "reported_incident_start_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["reportedIncidentStartDate"] = (
            capo_security_ir.types._prelude.timestamp.serialize_json(
                value["reported_incident_start_date"]
            )
        )
    if "actual_incident_start_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["actualIncidentStartDate"] = (
            capo_security_ir.types._prelude.timestamp.serialize_json(
                value["actual_incident_start_date"]
            )
        )
    if "engagement_type" in value:
        import capo_security_ir.types.engagement_type

        out["engagementType"] = capo_security_ir.types.engagement_type.serialize_json(
            value["engagement_type"]
        )
    if "watchers_to_add" in value:
        import capo_security_ir.types.watchers

        out["watchersToAdd"] = capo_security_ir.types.watchers.serialize_json(
            value["watchers_to_add"]
        )
    if "watchers_to_delete" in value:
        import capo_security_ir.types.watchers

        out["watchersToDelete"] = capo_security_ir.types.watchers.serialize_json(
            value["watchers_to_delete"]
        )
    if "threat_actor_ip_addresses_to_add" in value:
        import capo_security_ir.types.threat_actor_ip_list

        out["threatActorIpAddressesToAdd"] = (
            capo_security_ir.types.threat_actor_ip_list.serialize_json(
                value["threat_actor_ip_addresses_to_add"]
            )
        )
    if "threat_actor_ip_addresses_to_delete" in value:
        import capo_security_ir.types.threat_actor_ip_list

        out["threatActorIpAddressesToDelete"] = (
            capo_security_ir.types.threat_actor_ip_list.serialize_json(
                value["threat_actor_ip_addresses_to_delete"]
            )
        )
    if "impacted_services_to_add" in value:
        import capo_security_ir.types.impacted_services_list

        out["impactedServicesToAdd"] = (
            capo_security_ir.types.impacted_services_list.serialize_json(
                value["impacted_services_to_add"]
            )
        )
    if "impacted_services_to_delete" in value:
        import capo_security_ir.types.impacted_services_list

        out["impactedServicesToDelete"] = (
            capo_security_ir.types.impacted_services_list.serialize_json(
                value["impacted_services_to_delete"]
            )
        )
    if "impacted_aws_regions_to_add" in value:
        import capo_security_ir.types.impacted_aws_region_list

        out["impactedAwsRegionsToAdd"] = (
            capo_security_ir.types.impacted_aws_region_list.serialize_json(
                value["impacted_aws_regions_to_add"]
            )
        )
    if "impacted_aws_regions_to_delete" in value:
        import capo_security_ir.types.impacted_aws_region_list

        out["impactedAwsRegionsToDelete"] = (
            capo_security_ir.types.impacted_aws_region_list.serialize_json(
                value["impacted_aws_regions_to_delete"]
            )
        )
    if "impacted_accounts_to_add" in value:
        import capo_security_ir.types.impacted_accounts

        out["impactedAccountsToAdd"] = (
            capo_security_ir.types.impacted_accounts.serialize_json(
                value["impacted_accounts_to_add"]
            )
        )
    if "impacted_accounts_to_delete" in value:
        import capo_security_ir.types.impacted_accounts

        out["impactedAccountsToDelete"] = (
            capo_security_ir.types.impacted_accounts.serialize_json(
                value["impacted_accounts_to_delete"]
            )
        )
    if "case_metadata" in value:
        import capo_security_ir.types.case_metadata

        out["caseMetadata"] = capo_security_ir.types.case_metadata.serialize_json(
            value["case_metadata"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCaseRequest:
    out: UpdateCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("reportedIncidentStartDate") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["reported_incident_start_date"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["reportedIncidentStartDate"]
            )
        )
    if data.get("actualIncidentStartDate") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["actual_incident_start_date"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["actualIncidentStartDate"]
            )
        )
    if data.get("engagementType") is not None:
        import capo_security_ir.types.engagement_type

        out["engagement_type"] = (
            capo_security_ir.types.engagement_type.deserialize_json(
                data["engagementType"]
            )
        )
    if data.get("watchersToAdd") is not None:
        import capo_security_ir.types.watchers

        out["watchers_to_add"] = capo_security_ir.types.watchers.deserialize_json(
            data["watchersToAdd"]
        )
    if data.get("watchersToDelete") is not None:
        import capo_security_ir.types.watchers

        out["watchers_to_delete"] = capo_security_ir.types.watchers.deserialize_json(
            data["watchersToDelete"]
        )
    if data.get("threatActorIpAddressesToAdd") is not None:
        import capo_security_ir.types.threat_actor_ip_list

        out["threat_actor_ip_addresses_to_add"] = (
            capo_security_ir.types.threat_actor_ip_list.deserialize_json(
                data["threatActorIpAddressesToAdd"]
            )
        )
    if data.get("threatActorIpAddressesToDelete") is not None:
        import capo_security_ir.types.threat_actor_ip_list

        out["threat_actor_ip_addresses_to_delete"] = (
            capo_security_ir.types.threat_actor_ip_list.deserialize_json(
                data["threatActorIpAddressesToDelete"]
            )
        )
    if data.get("impactedServicesToAdd") is not None:
        import capo_security_ir.types.impacted_services_list

        out["impacted_services_to_add"] = (
            capo_security_ir.types.impacted_services_list.deserialize_json(
                data["impactedServicesToAdd"]
            )
        )
    if data.get("impactedServicesToDelete") is not None:
        import capo_security_ir.types.impacted_services_list

        out["impacted_services_to_delete"] = (
            capo_security_ir.types.impacted_services_list.deserialize_json(
                data["impactedServicesToDelete"]
            )
        )
    if data.get("impactedAwsRegionsToAdd") is not None:
        import capo_security_ir.types.impacted_aws_region_list

        out["impacted_aws_regions_to_add"] = (
            capo_security_ir.types.impacted_aws_region_list.deserialize_json(
                data["impactedAwsRegionsToAdd"]
            )
        )
    if data.get("impactedAwsRegionsToDelete") is not None:
        import capo_security_ir.types.impacted_aws_region_list

        out["impacted_aws_regions_to_delete"] = (
            capo_security_ir.types.impacted_aws_region_list.deserialize_json(
                data["impactedAwsRegionsToDelete"]
            )
        )
    if data.get("impactedAccountsToAdd") is not None:
        import capo_security_ir.types.impacted_accounts

        out["impacted_accounts_to_add"] = (
            capo_security_ir.types.impacted_accounts.deserialize_json(
                data["impactedAccountsToAdd"]
            )
        )
    if data.get("impactedAccountsToDelete") is not None:
        import capo_security_ir.types.impacted_accounts

        out["impacted_accounts_to_delete"] = (
            capo_security_ir.types.impacted_accounts.deserialize_json(
                data["impactedAccountsToDelete"]
            )
        )
    if data.get("caseMetadata") is not None:
        import capo_security_ir.types.case_metadata

        out["case_metadata"] = capo_security_ir.types.case_metadata.deserialize_json(
            data["caseMetadata"]
        )
    return out


def redact_sensitive(value: UpdateCaseRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "watchers_to_add" in value:
        import capo_security_ir.types.watchers

        out["watchers_to_add"] = capo_security_ir.types.watchers.redact_sensitive(
            value["watchers_to_add"]
        )
    if "watchers_to_delete" in value:
        import capo_security_ir.types.watchers

        out["watchers_to_delete"] = capo_security_ir.types.watchers.redact_sensitive(
            value["watchers_to_delete"]
        )
    if "threat_actor_ip_addresses_to_add" in value:
        import capo_security_ir.types.threat_actor_ip_list

        out["threat_actor_ip_addresses_to_add"] = (
            capo_security_ir.types.threat_actor_ip_list.redact_sensitive(
                value["threat_actor_ip_addresses_to_add"]
            )
        )
    if "threat_actor_ip_addresses_to_delete" in value:
        import capo_security_ir.types.threat_actor_ip_list

        out["threat_actor_ip_addresses_to_delete"] = (
            capo_security_ir.types.threat_actor_ip_list.redact_sensitive(
                value["threat_actor_ip_addresses_to_delete"]
            )
        )
    return out
