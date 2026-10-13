"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateGlossaryOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_description
    import capo_datazone.types.glossary_id
    import capo_datazone.types.glossary_name
    import capo_datazone.types.glossary_status
    import capo_datazone.types.glossary_usage_restrictions
    import capo_datazone.types.project_id


class UpdateGlossaryOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a business glossary is to be updated.</p>"""
    id: "capo_datazone.types.glossary_id.GlossaryId"
    """<p>The identifier of the business glossary that is to be updated.</p>"""
    name: "capo_datazone.types.glossary_name.GlossaryName"
    """<p>The name to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project in which to update a business glossary.</p>"""
    description: NotRequired[
        "capo_datazone.types.glossary_description.GlossaryDescription"
    ]
    """<p>The description to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    status: NotRequired["capo_datazone.types.glossary_status.GlossaryStatus"]
    """<p>The status to be updated as part of the <code>UpdateGlossary</code> action.</p>"""
    usage_restrictions: NotRequired[
        "capo_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
    ]
    """<p>The usage restriction of the restricted glossary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlossaryOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["owningProjectId"] = value["owning_project_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_datazone.types.glossary_status

        out["status"] = capo_datazone.types.glossary_status.serialize_json(
            value["status"]
        )
    if "usage_restrictions" in value:
        import capo_datazone.types.glossary_usage_restrictions

        out["usageRestrictions"] = (
            capo_datazone.types.glossary_usage_restrictions.serialize_json(
                value["usage_restrictions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGlossaryOutput:
    out: UpdateGlossaryOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("UpdateGlossaryOutput.domain_id required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateGlossaryOutput.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateGlossaryOutput.name required")
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("UpdateGlossaryOutput.owning_project_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_datazone.types.glossary_status

        out["status"] = capo_datazone.types.glossary_status.deserialize_json(
            data["status"]
        )
    if data.get("usageRestrictions") is not None:
        import capo_datazone.types.glossary_usage_restrictions

        out["usage_restrictions"] = (
            capo_datazone.types.glossary_usage_restrictions.deserialize_json(
                data["usageRestrictions"]
            )
        )
    return out


def redact_sensitive(value: UpdateGlossaryOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
