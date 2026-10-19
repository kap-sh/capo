"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateDomainOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.role_arn
    import capo_datazone.types.single_sign_on
    import capo_datazone.types.updated_at


class UpdateDomainOutput(TypedDict, closed=True):
    id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    root_domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the root domain unit.</p>"""
    description: NotRequired["str"]
    """<p>The description to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    single_sign_on: NotRequired["capo_datazone.types.single_sign_on.SingleSignOn"]
    """<p>The single sign-on option of the Amazon DataZone domain.</p>"""
    domain_execution_role: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>The domain execution role to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    service_role: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>The service role of the domain.</p>"""
    name: NotRequired["str"]
    """<p>The name to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    last_updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>Specifies the timestamp of when the domain was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "root_domain_unit_id" in value:
        out["rootDomainUnitId"] = value["root_domain_unit_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "single_sign_on" in value:
        import capo_datazone.types.single_sign_on

        out["singleSignOn"] = capo_datazone.types.single_sign_on.serialize_json(
            value["single_sign_on"]
        )
    if "domain_execution_role" in value:
        out["domainExecutionRole"] = value["domain_execution_role"]
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "name" in value:
        out["name"] = value["name"]
    if "last_updated_at" in value:
        import capo_datazone.types.updated_at

        out["lastUpdatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDomainOutput:
    out: UpdateDomainOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("rootDomainUnitId") is not None:
        out["root_domain_unit_id"] = data["rootDomainUnitId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("singleSignOn") is not None:
        import capo_datazone.types.single_sign_on

        out["single_sign_on"] = capo_datazone.types.single_sign_on.deserialize_json(
            data["singleSignOn"]
        )
    if data.get("domainExecutionRole") is not None:
        out["domain_execution_role"] = data["domainExecutionRole"]
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("lastUpdatedAt") is not None:
        import capo_datazone.types.updated_at

        out["last_updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
