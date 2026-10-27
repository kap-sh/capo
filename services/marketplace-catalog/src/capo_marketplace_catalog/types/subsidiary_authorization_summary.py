"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.date_time_iso8601
    import capo_marketplace_catalog.types.subsidiary_authorization_summary_name_string
    import capo_marketplace_catalog.types.subsidiary_authorization_summary_resource_id_string
    import capo_marketplace_catalog.types.subsidiary_authorization_summary_resource_name_string
    import capo_marketplace_catalog.types.subsidiary_authorization_summary_status_string
    import capo_marketplace_catalog.types.subsidiary_authorization_summary_subsidiary_account_id_string


class SubsidiaryAuthorizationSummary(TypedDict, closed=True):
    name: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_summary_name_string.SubsidiaryAuthorizationSummaryNameString"
    ]
    """<p>The name of the subsidiary authorization.</p>"""
    status: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_summary_status_string.SubsidiaryAuthorizationSummaryStatusString"
    ]
    """<p>The status of the subsidiary authorization. Valid values are:</p> <ul> <li> <p> <code>Draft</code> - The subsidiary authorization was created but not yet released. The subsidiary account can't see it.</p> </li> <li> <p> <code>Active</code> - The subsidiary account can use the subsidiary authorization to create offers for the authorized product.</p> </li> <li> <p> <code>Restricted</code> - The subsidiary authorization was discarded while in <code>Draft</code> or revoked while <code>Active</code>. It can't be used to create new offers. This status is final.</p> </li> </ul>"""
    resource_id: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_summary_resource_id_string.SubsidiaryAuthorizationSummaryResourceIdString"
    ]
    """<p>The ID of the resource that the subsidiary authorization applies to. Currently, this is always a product ID, such as <code>prod-example123</code>.</p>"""
    resource_name: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_summary_resource_name_string.SubsidiaryAuthorizationSummaryResourceNameString"
    ]
    """<p>The name of the resource that the subsidiary authorization applies to. Currently, this is always a product name.</p>"""
    subsidiary_account_id: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_summary_subsidiary_account_id_string.SubsidiaryAuthorizationSummarySubsidiaryAccountIdString"
    ]
    """<p>The 12-digit AWS account ID of the subsidiary account.</p>"""
    created_date: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The date the subsidiary authorization was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "subsidiary_account_id" in value:
        out["SubsidiaryAccountId"] = value["subsidiary_account_id"]
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    return out


def deserialize_json(data: dict) -> SubsidiaryAuthorizationSummary:
    out: SubsidiaryAuthorizationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    if data.get("SubsidiaryAccountId") is not None:
        out["subsidiary_account_id"] = data["SubsidiaryAccountId"]
    if data.get("CreatedDate") is not None:
        out["created_date"] = data["CreatedDate"]
    return out
