"""Generated from Smithy shape ``com.amazonaws.datazone#CreateGlossaryInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.glossary_description
    import capo_datazone.types.glossary_name
    import capo_datazone.types.glossary_status
    import capo_datazone.types.glossary_usage_restrictions
    import capo_datazone.types.project_id


class CreateGlossaryInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this business glossary is created.</p>"""
    name: "capo_datazone.types.glossary_name.GlossaryName"
    """<p>The name of this business glossary.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the project that currently owns business glossary.</p>"""
    description: NotRequired[
        "capo_datazone.types.glossary_description.GlossaryDescription"
    ]
    """<p>The description of this business glossary.</p>"""
    status: NotRequired["capo_datazone.types.glossary_status.GlossaryStatus"]
    """<p>The status of this business glossary.</p>"""
    usage_restrictions: NotRequired[
        "capo_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
    ]
    """<p>The usage restriction of the restricted glossary.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGlossaryInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateGlossaryInput:
    out: CreateGlossaryInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("owningProjectIdentifier") is not None:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        out["owning_project_identifier"] = ""
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateGlossaryInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
