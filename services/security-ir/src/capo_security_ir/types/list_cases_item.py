"""Generated from Smithy shape ``com.amazonaws.securityir#ListCasesItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_security_ir.types.case_arn
    import capo_security_ir.types.case_id
    import capo_security_ir.types.case_status
    import capo_security_ir.types.case_title
    import capo_security_ir.types.engagement_type
    import capo_security_ir.types.pending_action
    import capo_security_ir.types.resolver_type


class ListCasesItem(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p/>"""
    last_updated_date: NotRequired["datetime.datetime"]
    """<p/>"""
    title: NotRequired["capo_security_ir.types.case_title.CaseTitle"]
    """<p/>"""
    case_arn: NotRequired["capo_security_ir.types.case_arn.CaseArn"]
    """<p/>"""
    engagement_type: NotRequired[
        "capo_security_ir.types.engagement_type.EngagementType"
    ]
    """<p/>"""
    case_status: NotRequired["capo_security_ir.types.case_status.CaseStatus"]
    """<p/>"""
    created_date: NotRequired["datetime.datetime"]
    """<p/>"""
    closed_date: NotRequired["datetime.datetime"]
    """<p/>"""
    resolver_type: NotRequired["capo_security_ir.types.resolver_type.ResolverType"]
    """<p/>"""
    pending_action: NotRequired["capo_security_ir.types.pending_action.PendingAction"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCasesItem) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    if "last_updated_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["lastUpdatedDate"] = (
            capo_security_ir.types._prelude.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "title" in value:
        out["title"] = value["title"]
    if "case_arn" in value:
        out["caseArn"] = value["case_arn"]
    if "engagement_type" in value:
        import capo_security_ir.types.engagement_type

        out["engagementType"] = capo_security_ir.types.engagement_type.serialize_json(
            value["engagement_type"]
        )
    if "case_status" in value:
        import capo_security_ir.types.case_status

        out["caseStatus"] = capo_security_ir.types.case_status.serialize_json(
            value["case_status"]
        )
    if "created_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["createdDate"] = capo_security_ir.types._prelude.timestamp.serialize_json(
            value["created_date"]
        )
    if "closed_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["closedDate"] = capo_security_ir.types._prelude.timestamp.serialize_json(
            value["closed_date"]
        )
    if "resolver_type" in value:
        import capo_security_ir.types.resolver_type

        out["resolverType"] = capo_security_ir.types.resolver_type.serialize_json(
            value["resolver_type"]
        )
    if "pending_action" in value:
        import capo_security_ir.types.pending_action

        out["pendingAction"] = capo_security_ir.types.pending_action.serialize_json(
            value["pending_action"]
        )
    return out


def deserialize_json(data: dict) -> ListCasesItem:
    out: ListCasesItem = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    else:
        out["case_id"] = ""
    if data.get("lastUpdatedDate") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["last_updated_date"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("caseArn") is not None:
        out["case_arn"] = data["caseArn"]
    if data.get("engagementType") is not None:
        import capo_security_ir.types.engagement_type

        out["engagement_type"] = (
            capo_security_ir.types.engagement_type.deserialize_json(
                data["engagementType"]
            )
        )
    if data.get("caseStatus") is not None:
        import capo_security_ir.types.case_status

        out["case_status"] = capo_security_ir.types.case_status.deserialize_json(
            data["caseStatus"]
        )
    if data.get("createdDate") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["created_date"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if data.get("closedDate") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["closed_date"] = capo_security_ir.types._prelude.timestamp.deserialize_json(
            data["closedDate"]
        )
    if data.get("resolverType") is not None:
        import capo_security_ir.types.resolver_type

        out["resolver_type"] = capo_security_ir.types.resolver_type.deserialize_json(
            data["resolverType"]
        )
    if data.get("pendingAction") is not None:
        import capo_security_ir.types.pending_action

        out["pending_action"] = capo_security_ir.types.pending_action.deserialize_json(
            data["pendingAction"]
        )
    return out


def redact_sensitive(value: ListCasesItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    return out
