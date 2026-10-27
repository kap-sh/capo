"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationResourceNameFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter_value_list
    import capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter_wildcard


class SubsidiaryAuthorizationResourceNameFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter_value_list.SubsidiaryAuthorizationResourceNameFilterValueList"
    ]
    """<p>A list of resource names to filter by. The operation returns subsidiary authorizations for resources with a name that matches any value in this list. You can include up to 10 resource names in this list.</p>"""
    wild_card_value: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter_wildcard.SubsidiaryAuthorizationResourceNameFilterWildcard"
    ]
    """<p>A partial resource name to filter by. The operation returns subsidiary authorizations for resources whose name contains this value. The value must be at least 3 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationResourceNameFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    if "wild_card_value" in value:
        out["WildCardValue"] = value["wild_card_value"]
    return out


def deserialize_json(data: dict) -> SubsidiaryAuthorizationResourceNameFilter:
    out: SubsidiaryAuthorizationResourceNameFilter = {}  # type: ignore[typeddict-item]
    if data.get("ValueList") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_resource_name_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    if data.get("WildCardValue") is not None:
        out["wild_card_value"] = data["WildCardValue"]
    return out
