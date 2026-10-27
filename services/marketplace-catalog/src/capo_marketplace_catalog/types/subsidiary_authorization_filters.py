"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter
    import capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter
    import capo_marketplace_catalog.types.subsidiary_authorization_last_modified_date_filter
    import capo_marketplace_catalog.types.subsidiary_authorization_name_filter
    import capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter
    import capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter
    import capo_marketplace_catalog.types.subsidiary_authorization_status_filter
    import capo_marketplace_catalog.types.subsidiary_authorization_subsidiary_account_id_filter


class SubsidiaryAuthorizationFilters(TypedDict, closed=True):
    entity_id: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter.SubsidiaryAuthorizationEntityIdFilter"
    ]
    """<p>A filter that matches subsidiary authorizations by entity ID.</p>"""
    status: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_status_filter.SubsidiaryAuthorizationStatusFilter"
    ]
    """<p>A filter that matches subsidiary authorizations by status.</p>"""
    resource_id: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter.SubsidiaryAuthorizationResourceIdFilter"
    ]
    """<p>A filter that matches subsidiary authorizations by the ID of the authorized resource.</p>"""
    resource_name: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter.SubsidiaryAuthorizationResourceNameFilter"
    ]
    """<p>A filter that matches subsidiary authorizations by the name of the authorized resource.</p>"""
    name: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_name_filter.SubsidiaryAuthorizationNameFilter"
    ]
    """<p>A filter that matches subsidiary authorizations by name.</p>"""
    subsidiary_account_id: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_subsidiary_account_id_filter.SubsidiaryAuthorizationSubsidiaryAccountIdFilter"
    ]
    """<p>A filter that matches subsidiary authorizations by the AWS account ID of the subsidiary account.</p>"""
    created_date: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter.SubsidiaryAuthorizationCreatedDateFilter"
    ]
    """<p>A filter that matches subsidiary authorizations by creation date.</p>"""
    last_modified_date: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_last_modified_date_filter.SubsidiaryAuthorizationLastModifiedDateFilter"
    ]
    """<p>A filter that matches subsidiary authorizations by last modified date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationFilters) -> dict:
    out: dict = {}
    if "entity_id" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter

        out["EntityId"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter.serialize_json(
                value["entity_id"]
            )
        )
    if "status" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_status_filter

        out["Status"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_status_filter.serialize_json(
                value["status"]
            )
        )
    if "resource_id" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter

        out["ResourceId"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter.serialize_json(
                value["resource_id"]
            )
        )
    if "resource_name" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter

        out["ResourceName"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter.serialize_json(
                value["resource_name"]
            )
        )
    if "name" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_name_filter

        out["Name"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_name_filter.serialize_json(
                value["name"]
            )
        )
    if "subsidiary_account_id" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_subsidiary_account_id_filter

        out["SubsidiaryAccountId"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_subsidiary_account_id_filter.serialize_json(
                value["subsidiary_account_id"]
            )
        )
    if "created_date" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter

        out["CreatedDate"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter.serialize_json(
                value["created_date"]
            )
        )
    if "last_modified_date" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_last_modified_date_filter

        out["LastModifiedDate"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_last_modified_date_filter.serialize_json(
                value["last_modified_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubsidiaryAuthorizationFilters:
    out: SubsidiaryAuthorizationFilters = {}  # type: ignore[typeddict-item]
    if data.get("EntityId") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter

        out["entity_id"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter.deserialize_json(
                data["EntityId"]
            )
        )
    if data.get("Status") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_status_filter

        out["status"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_status_filter.deserialize_json(
                data["Status"]
            )
        )
    if data.get("ResourceId") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter

        out["resource_id"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter.deserialize_json(
                data["ResourceId"]
            )
        )
    if data.get("ResourceName") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter

        out["resource_name"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter.deserialize_json(
                data["ResourceName"]
            )
        )
    if data.get("Name") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_name_filter

        out["name"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_name_filter.deserialize_json(
                data["Name"]
            )
        )
    if data.get("SubsidiaryAccountId") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_subsidiary_account_id_filter

        out["subsidiary_account_id"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_subsidiary_account_id_filter.deserialize_json(
                data["SubsidiaryAccountId"]
            )
        )
    if data.get("CreatedDate") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter

        out["created_date"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_created_date_filter.deserialize_json(
                data["CreatedDate"]
            )
        )
    if data.get("LastModifiedDate") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_last_modified_date_filter

        out["last_modified_date"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_last_modified_date_filter.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    return out
