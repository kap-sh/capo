"""Generated from Smithy shape ``com.amazonaws.datazone#DomainSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.domain_description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_name
    import capo_datazone.types.domain_status
    import capo_datazone.types.domain_version
    import capo_datazone.types.updated_at


class DomainSummary(TypedDict, closed=True):
    id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain.</p>"""
    name: "capo_datazone.types.domain_name.DomainName"
    """<p>A name of an Amazon DataZone domain.</p>"""
    description: NotRequired["capo_datazone.types.domain_description.DomainDescription"]
    """<p>A description of an Amazon DataZone domain.</p>"""
    arn: "str"
    """<p>The ARN of the Amazon DataZone domain.</p>"""
    managed_account_id: "str"
    """<p>The identifier of the Amazon Web Services account that manages the domain.</p>"""
    status: "capo_datazone.types.domain_status.DomainStatus"
    """<p>The status of the Amazon DataZone domain.</p>"""
    portal_url: NotRequired["str"]
    """<p>The data portal URL for the Amazon DataZone domain.</p>"""
    created_at: "capo_datazone.types.created_at.CreatedAt"
    """<p>A timestamp of when a Amazon DataZone domain was created.</p>"""
    last_updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>A timestamp of when a Amazon DataZone domain was last updated.</p>"""
    domain_version: NotRequired["capo_datazone.types.domain_version.DomainVersion"]
    """<p>The domain version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["arn"] = value["arn"]
    out["managedAccountId"] = value["managed_account_id"]
    import capo_datazone.types.domain_status

    out["status"] = capo_datazone.types.domain_status.serialize_json(value["status"])
    if "portal_url" in value:
        out["portalUrl"] = value["portal_url"]
    import capo_datazone.types.created_at

    out["createdAt"] = capo_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    if "last_updated_at" in value:
        import capo_datazone.types.updated_at

        out["lastUpdatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["last_updated_at"]
        )
    if "domain_version" in value:
        import capo_datazone.types.domain_version

        out["domainVersion"] = capo_datazone.types.domain_version.serialize_json(
            value["domain_version"]
        )
    return out


def deserialize_json(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("managedAccountId") is not None:
        out["managed_account_id"] = data["managedAccountId"]
    else:
        out["managed_account_id"] = ""
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
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUpdatedAt") is not None:
        import capo_datazone.types.updated_at

        out["last_updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["lastUpdatedAt"]
        )
    if data.get("domainVersion") is not None:
        import capo_datazone.types.domain_version

        out["domain_version"] = capo_datazone.types.domain_version.deserialize_json(
            data["domainVersion"]
        )
    return out


def redact_sensitive(value: DomainSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
