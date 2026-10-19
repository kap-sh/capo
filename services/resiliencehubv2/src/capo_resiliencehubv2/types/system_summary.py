"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_name
    import capo_resiliencehubv2.types.organization_id
    import capo_resiliencehubv2.types.ou_id
    import capo_resiliencehubv2.types.system_id


class SystemSummary(TypedDict, closed=True):
    system_id: "capo_resiliencehubv2.types.system_id.SystemId"
    name: "capo_resiliencehubv2.types.entity_name.EntityName"
    system_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    user_journeys_count: NotRequired["int"]
    """<p>The number of user journeys in the system.</p>"""
    services_count: NotRequired["int"]
    """<p>The number of services in the system.</p>"""
    organization_id: NotRequired[
        "capo_resiliencehubv2.types.organization_id.OrganizationId"
    ]
    """<p>Displayed only if caller has access.</p>"""
    ou_id: NotRequired["capo_resiliencehubv2.types.ou_id.OuId"]
    """<p>Displayed only if caller has access.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the system was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the system was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemSummary) -> dict:
    out: dict = {}
    out["systemId"] = value["system_id"]
    out["name"] = value["name"]
    if "system_arn" in value:
        out["systemArn"] = value["system_arn"]
    if "user_journeys_count" in value:
        out["userJourneysCount"] = value["user_journeys_count"]
    if "services_count" in value:
        out["servicesCount"] = value["services_count"]
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    if "ou_id" in value:
        out["ouId"] = value["ou_id"]
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> SystemSummary:
    out: SystemSummary = {}  # type: ignore[typeddict-item]
    if data.get("systemId") is not None:
        out["system_id"] = data["systemId"]
    else:
        out["system_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("systemArn") is not None:
        out["system_arn"] = data["systemArn"]
    if data.get("userJourneysCount") is not None:
        out["user_journeys_count"] = data["userJourneysCount"]
    if data.get("servicesCount") is not None:
        out["services_count"] = data["servicesCount"]
    if data.get("organizationId") is not None:
        out["organization_id"] = data["organizationId"]
    if data.get("ouId") is not None:
        out["ou_id"] = data["ouId"]
    if data.get("createdAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
