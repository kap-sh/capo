"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentFrameworkShareRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.account_id
    import capo_auditmanager.types.compliance_type
    import capo_auditmanager.types.framework_description
    import capo_auditmanager.types.framework_name
    import capo_auditmanager.types.nullable_integer
    import capo_auditmanager.types.region
    import capo_auditmanager.types.share_request_comment
    import capo_auditmanager.types.share_request_status
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.uuid


class AssessmentFrameworkShareRequest(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the share request. </p>"""
    framework_id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p>The unique identifier for the shared custom framework. </p>"""
    framework_name: NotRequired["capo_auditmanager.types.framework_name.FrameworkName"]
    """<p> The name of the custom framework that the share request is for. </p>"""
    framework_description: NotRequired[
        "capo_auditmanager.types.framework_description.FrameworkDescription"
    ]
    """<p>The description of the shared custom framework.</p>"""
    status: NotRequired[
        "capo_auditmanager.types.share_request_status.ShareRequestStatus"
    ]
    """<p> The status of the share request. </p>"""
    source_account: NotRequired["capo_auditmanager.types.account_id.AccountId"]
    """<p> The Amazon Web Services account of the sender. </p>"""
    destination_account: NotRequired["capo_auditmanager.types.account_id.AccountId"]
    """<p> The Amazon Web Services account of the recipient. </p>"""
    destination_region: NotRequired["capo_auditmanager.types.region.Region"]
    """<p> The Amazon Web Services Region of the recipient. </p>"""
    expiration_time: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the share request expires. </p>"""
    creation_time: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the share request was created. </p>"""
    last_updated: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> Specifies when the share request was last updated. </p>"""
    comment: NotRequired[
        "capo_auditmanager.types.share_request_comment.ShareRequestComment"
    ]
    """<p> An optional comment from the sender about the share request. </p>"""
    standard_controls_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of standard controls that are part of the shared custom framework. </p>"""
    custom_controls_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of custom controls that are part of the shared custom framework.</p>"""
    compliance_type: NotRequired[
        "capo_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p>The compliance type that the shared custom framework supports, such as CIS or HIPAA.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentFrameworkShareRequest) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "framework_id" in value:
        out["frameworkId"] = value["framework_id"]
    if "framework_name" in value:
        out["frameworkName"] = value["framework_name"]
    if "framework_description" in value:
        out["frameworkDescription"] = value["framework_description"]
    if "status" in value:
        import capo_auditmanager.types.share_request_status

        out["status"] = capo_auditmanager.types.share_request_status.serialize_json(
            value["status"]
        )
    if "source_account" in value:
        out["sourceAccount"] = value["source_account"]
    if "destination_account" in value:
        out["destinationAccount"] = value["destination_account"]
    if "destination_region" in value:
        out["destinationRegion"] = value["destination_region"]
    if "expiration_time" in value:
        import capo_auditmanager.types.timestamp

        out["expirationTime"] = capo_auditmanager.types.timestamp.serialize_json(
            value["expiration_time"]
        )
    if "creation_time" in value:
        import capo_auditmanager.types.timestamp

        out["creationTime"] = capo_auditmanager.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated" in value:
        import capo_auditmanager.types.timestamp

        out["lastUpdated"] = capo_auditmanager.types.timestamp.serialize_json(
            value["last_updated"]
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    if "standard_controls_count" in value:
        out["standardControlsCount"] = value["standard_controls_count"]
    if "custom_controls_count" in value:
        out["customControlsCount"] = value["custom_controls_count"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    return out


def deserialize_json(data: dict) -> AssessmentFrameworkShareRequest:
    out: AssessmentFrameworkShareRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("frameworkId") is not None:
        out["framework_id"] = data["frameworkId"]
    if data.get("frameworkName") is not None:
        out["framework_name"] = data["frameworkName"]
    if data.get("frameworkDescription") is not None:
        out["framework_description"] = data["frameworkDescription"]
    if data.get("status") is not None:
        import capo_auditmanager.types.share_request_status

        out["status"] = capo_auditmanager.types.share_request_status.deserialize_json(
            data["status"]
        )
    if data.get("sourceAccount") is not None:
        out["source_account"] = data["sourceAccount"]
    if data.get("destinationAccount") is not None:
        out["destination_account"] = data["destinationAccount"]
    if data.get("destinationRegion") is not None:
        out["destination_region"] = data["destinationRegion"]
    if data.get("expirationTime") is not None:
        import capo_auditmanager.types.timestamp

        out["expiration_time"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["expirationTime"]
        )
    if data.get("creationTime") is not None:
        import capo_auditmanager.types.timestamp

        out["creation_time"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("lastUpdated") is not None:
        import capo_auditmanager.types.timestamp

        out["last_updated"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdated"]
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("standardControlsCount") is not None:
        out["standard_controls_count"] = data["standardControlsCount"]
    if data.get("customControlsCount") is not None:
        out["custom_controls_count"] = data["customControlsCount"]
    if data.get("complianceType") is not None:
        out["compliance_type"] = data["complianceType"]
    return out


def redact_sensitive(value: AssessmentFrameworkShareRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "compliance_type" in value:
        out["compliance_type"] = "*** Sensitive Data Redacted ***"
    return out
