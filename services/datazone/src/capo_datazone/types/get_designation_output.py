"""Generated from Smithy shape ``com.amazonaws.datazone#GetDesignationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.cedar_designation_policy
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.designation_id
    import capo_datazone.types.designation_name
    import capo_datazone.types.designation_type
    import capo_datazone.types.domain_id


class GetDesignationOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain that contains the designation.</p>"""
    id: "capo_datazone.types.designation_id.DesignationId"
    """<p>The unique ID of the designation.</p>"""
    name: "capo_datazone.types.designation_name.DesignationName"
    """<p>The name of the designation. The name is unique within the domain.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>A human-readable description of the designation and its intended use.</p>"""
    designation_type: "capo_datazone.types.designation_type.DesignationType"
    """The classification of this designation. MANAGED designations are system-defined and cannot be modified or deleted."""
    policy: "capo_datazone.types.cedar_designation_policy.CedarDesignationPolicy"
    """The Cedar permit policy that governs what actions holders of this designation are allowed to perform."""
    deletion_protection: "bool"
    """Whether deletion protection is enabled for this designation. When true, DeleteDesignation is rejected until protection is disabled via UpdateDesignation."""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The identifier of the Amazon DataZone user who created the designation.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the designation was created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the designation was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDesignationOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_datazone.types.designation_type

    out["designationType"] = capo_datazone.types.designation_type.serialize_json(
        value["designation_type"]
    )
    out["policy"] = value["policy"]
    out["deletionProtection"] = value["deletion_protection"]
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone._protocol.serialize

        out["createdAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_datazone._protocol.serialize

        out["lastUpdatedAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetDesignationOutput:
    out: GetDesignationOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
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
    if data.get("designationType") is not None:
        import capo_datazone.types.designation_type

        out["designation_type"] = capo_datazone.types.designation_type.deserialize_json(
            data["designationType"]
        )
    else:
        import typing

        out["designation_type"] = typing.cast(
            "capo_datazone.types.designation_type.DesignationType", ""
        )
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    else:
        out["deletion_protection"] = False
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("lastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["lastUpdatedAt"].replace("Z", "+00:00")
        )
    return out


def redact_sensitive(value: GetDesignationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
