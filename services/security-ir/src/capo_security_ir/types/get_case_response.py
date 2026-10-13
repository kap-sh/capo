"""Generated from Smithy shape ``com.amazonaws.securityir#GetCaseResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_security_ir.types.case_arn
    import capo_security_ir.types.case_attachments_list
    import capo_security_ir.types.case_description
    import capo_security_ir.types.case_metadata
    import capo_security_ir.types.case_status
    import capo_security_ir.types.case_title
    import capo_security_ir.types.closure_code
    import capo_security_ir.types.engagement_type
    import capo_security_ir.types.impacted_accounts
    import capo_security_ir.types.impacted_aws_region_list
    import capo_security_ir.types.impacted_services_list
    import capo_security_ir.types.pending_action
    import capo_security_ir.types.resolver_type
    import capo_security_ir.types.threat_actor_ip_list
    import capo_security_ir.types.watchers


class GetCaseResponse(TypedDict, closed=True):
    title: NotRequired["capo_security_ir.types.case_title.CaseTitle"]
    """<p>Response element for GetCase that provides the case title.</p>"""
    case_arn: NotRequired["capo_security_ir.types.case_arn.CaseArn"]
    """<p>Response element for GetCase that provides the case ARN</p>"""
    description: NotRequired["capo_security_ir.types.case_description.CaseDescription"]
    """<p>Response element for GetCase that provides contents of the case description.</p>"""
    case_status: NotRequired["capo_security_ir.types.case_status.CaseStatus"]
    """<p>Response element for GetCase that provides the case status. Options for statuses include <code>Submitted | Detection and Analysis | Eradication, Containment and Recovery | Post-Incident Activities | Closed </code> </p>"""
    engagement_type: NotRequired[
        "capo_security_ir.types.engagement_type.EngagementType"
    ]
    """<p>Response element for GetCase that provides the engagement type. Options for engagement type include <code>Active Security Event | Investigations</code> </p>"""
    reported_incident_start_date: NotRequired["datetime.datetime"]
    """<p>Response element for GetCase that provides the customer provided incident start date.</p>"""
    actual_incident_start_date: NotRequired["datetime.datetime"]
    """<p>Response element for GetCase that provides the actual incident start date as identified by data analysis during the investigation. </p>"""
    impacted_aws_regions: NotRequired[
        "capo_security_ir.types.impacted_aws_region_list.ImpactedAwsRegionList"
    ]
    """<p>Response element for GetCase that provides the impacted regions.</p>"""
    threat_actor_ip_addresses: NotRequired[
        "capo_security_ir.types.threat_actor_ip_list.ThreatActorIpList"
    ]
    """<p>Response element for GetCase that provides a list of suspicious IP addresses associated with unauthorized activity. </p>"""
    pending_action: NotRequired["capo_security_ir.types.pending_action.PendingAction"]
    """<p>Response element for GetCase that identifies the case is waiting on customer input.</p>"""
    impacted_accounts: NotRequired[
        "capo_security_ir.types.impacted_accounts.ImpactedAccounts"
    ]
    """<p>Response element for GetCase that provides a list of impacted accounts.</p>"""
    watchers: NotRequired["capo_security_ir.types.watchers.Watchers"]
    """<p>Response element for GetCase that provides a list of Watchers added to the case.</p>"""
    created_date: NotRequired["datetime.datetime"]
    """<p>Response element for GetCase that provides the date the case was created.</p>"""
    last_updated_date: NotRequired["datetime.datetime"]
    """<p>Response element for GetCase that provides the date a case was last modified.</p>"""
    closure_code: NotRequired["capo_security_ir.types.closure_code.ClosureCode"]
    """<p>Response element for GetCase that provides the summary code for why a case was closed.</p>"""
    resolver_type: NotRequired["capo_security_ir.types.resolver_type.ResolverType"]
    """<p>Response element for GetCase that provides the current resolver types.</p>"""
    impacted_services: NotRequired[
        "capo_security_ir.types.impacted_services_list.ImpactedServicesList"
    ]
    """<p>Response element for GetCase that provides a list of impacted services.</p>"""
    case_attachments: NotRequired[
        "capo_security_ir.types.case_attachments_list.CaseAttachmentsList"
    ]
    """<p>Response element for GetCase that provides a list of current case attachments.</p>"""
    closed_date: NotRequired["datetime.datetime"]
    """<p>Response element for GetCase that provides the date a specified case was closed.</p>"""
    case_metadata: NotRequired["capo_security_ir.types.case_metadata.CaseMetadata"]
    """<p>Case response metadata</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseResponse) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "case_arn" in value:
        out["caseArn"] = value["case_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "case_status" in value:
        import capo_security_ir.types.case_status

        out["caseStatus"] = capo_security_ir.types.case_status.serialize_json(
            value["case_status"]
        )
    if "engagement_type" in value:
        import capo_security_ir.types.engagement_type

        out["engagementType"] = capo_security_ir.types.engagement_type.serialize_json(
            value["engagement_type"]
        )
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
    if "impacted_aws_regions" in value:
        import capo_security_ir.types.impacted_aws_region_list

        out["impactedAwsRegions"] = (
            capo_security_ir.types.impacted_aws_region_list.serialize_json(
                value["impacted_aws_regions"]
            )
        )
    if "threat_actor_ip_addresses" in value:
        import capo_security_ir.types.threat_actor_ip_list

        out["threatActorIpAddresses"] = (
            capo_security_ir.types.threat_actor_ip_list.serialize_json(
                value["threat_actor_ip_addresses"]
            )
        )
    if "pending_action" in value:
        import capo_security_ir.types.pending_action

        out["pendingAction"] = capo_security_ir.types.pending_action.serialize_json(
            value["pending_action"]
        )
    if "impacted_accounts" in value:
        import capo_security_ir.types.impacted_accounts

        out["impactedAccounts"] = (
            capo_security_ir.types.impacted_accounts.serialize_json(
                value["impacted_accounts"]
            )
        )
    if "watchers" in value:
        import capo_security_ir.types.watchers

        out["watchers"] = capo_security_ir.types.watchers.serialize_json(
            value["watchers"]
        )
    if "created_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["createdDate"] = capo_security_ir.types._prelude.timestamp.serialize_json(
            value["created_date"]
        )
    if "last_updated_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["lastUpdatedDate"] = (
            capo_security_ir.types._prelude.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "closure_code" in value:
        import capo_security_ir.types.closure_code

        out["closureCode"] = capo_security_ir.types.closure_code.serialize_json(
            value["closure_code"]
        )
    if "resolver_type" in value:
        import capo_security_ir.types.resolver_type

        out["resolverType"] = capo_security_ir.types.resolver_type.serialize_json(
            value["resolver_type"]
        )
    if "impacted_services" in value:
        import capo_security_ir.types.impacted_services_list

        out["impactedServices"] = (
            capo_security_ir.types.impacted_services_list.serialize_json(
                value["impacted_services"]
            )
        )
    if "case_attachments" in value:
        import capo_security_ir.types.case_attachments_list

        out["caseAttachments"] = (
            capo_security_ir.types.case_attachments_list.serialize_json(
                value["case_attachments"]
            )
        )
    if "closed_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["closedDate"] = capo_security_ir.types._prelude.timestamp.serialize_json(
            value["closed_date"]
        )
    if "case_metadata" in value:
        import capo_security_ir.types.case_metadata

        out["caseMetadata"] = capo_security_ir.types.case_metadata.serialize_json(
            value["case_metadata"]
        )
    return out


def deserialize_json(data: dict) -> GetCaseResponse:
    out: GetCaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("caseArn") is not None:
        out["case_arn"] = data["caseArn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("caseStatus") is not None:
        import capo_security_ir.types.case_status

        out["case_status"] = capo_security_ir.types.case_status.deserialize_json(
            data["caseStatus"]
        )
    if data.get("engagementType") is not None:
        import capo_security_ir.types.engagement_type

        out["engagement_type"] = (
            capo_security_ir.types.engagement_type.deserialize_json(
                data["engagementType"]
            )
        )
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
    if data.get("impactedAwsRegions") is not None:
        import capo_security_ir.types.impacted_aws_region_list

        out["impacted_aws_regions"] = (
            capo_security_ir.types.impacted_aws_region_list.deserialize_json(
                data["impactedAwsRegions"]
            )
        )
    if data.get("threatActorIpAddresses") is not None:
        import capo_security_ir.types.threat_actor_ip_list

        out["threat_actor_ip_addresses"] = (
            capo_security_ir.types.threat_actor_ip_list.deserialize_json(
                data["threatActorIpAddresses"]
            )
        )
    if data.get("pendingAction") is not None:
        import capo_security_ir.types.pending_action

        out["pending_action"] = capo_security_ir.types.pending_action.deserialize_json(
            data["pendingAction"]
        )
    if data.get("impactedAccounts") is not None:
        import capo_security_ir.types.impacted_accounts

        out["impacted_accounts"] = (
            capo_security_ir.types.impacted_accounts.deserialize_json(
                data["impactedAccounts"]
            )
        )
    if data.get("watchers") is not None:
        import capo_security_ir.types.watchers

        out["watchers"] = capo_security_ir.types.watchers.deserialize_json(
            data["watchers"]
        )
    if data.get("createdDate") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["created_date"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if data.get("lastUpdatedDate") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["last_updated_date"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if data.get("closureCode") is not None:
        import capo_security_ir.types.closure_code

        out["closure_code"] = capo_security_ir.types.closure_code.deserialize_json(
            data["closureCode"]
        )
    if data.get("resolverType") is not None:
        import capo_security_ir.types.resolver_type

        out["resolver_type"] = capo_security_ir.types.resolver_type.deserialize_json(
            data["resolverType"]
        )
    if data.get("impactedServices") is not None:
        import capo_security_ir.types.impacted_services_list

        out["impacted_services"] = (
            capo_security_ir.types.impacted_services_list.deserialize_json(
                data["impactedServices"]
            )
        )
    if data.get("caseAttachments") is not None:
        import capo_security_ir.types.case_attachments_list

        out["case_attachments"] = (
            capo_security_ir.types.case_attachments_list.deserialize_json(
                data["caseAttachments"]
            )
        )
    if data.get("closedDate") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["closed_date"] = capo_security_ir.types._prelude.timestamp.deserialize_json(
            data["closedDate"]
        )
    if data.get("caseMetadata") is not None:
        import capo_security_ir.types.case_metadata

        out["case_metadata"] = capo_security_ir.types.case_metadata.deserialize_json(
            data["caseMetadata"]
        )
    return out


def redact_sensitive(value: GetCaseResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "threat_actor_ip_addresses" in value:
        import capo_security_ir.types.threat_actor_ip_list

        out["threat_actor_ip_addresses"] = (
            capo_security_ir.types.threat_actor_ip_list.redact_sensitive(
                value["threat_actor_ip_addresses"]
            )
        )
    if "watchers" in value:
        import capo_security_ir.types.watchers

        out["watchers"] = capo_security_ir.types.watchers.redact_sensitive(
            value["watchers"]
        )
    if "case_attachments" in value:
        import capo_security_ir.types.case_attachments_list

        out["case_attachments"] = (
            capo_security_ir.types.case_attachments_list.redact_sensitive(
                value["case_attachments"]
            )
        )
    return out
