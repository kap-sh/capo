"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationResourceIdFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter_value_list


class SubsidiaryAuthorizationResourceIdFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter_value_list.SubsidiaryAuthorizationResourceIdFilterValueList"
    ]
    """<p>A list of resource IDs to filter by. The operation returns subsidiary authorizations for resources with an ID that matches any value in this list. You can include up to 10 resource IDs in this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationResourceIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubsidiaryAuthorizationResourceIdFilter:
    out: SubsidiaryAuthorizationResourceIdFilter = {}  # type: ignore[typeddict-item]
    if data.get("ValueList") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_resource_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
