"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationEntityIdFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter_value_list


class SubsidiaryAuthorizationEntityIdFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter_value_list.SubsidiaryAuthorizationEntityIdFilterValueList"
    ]
    """<p>A list of entity IDs to filter by. The operation returns subsidiary authorizations with an entity ID that matches any value in this list. You can include up to 10 entity IDs in this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationEntityIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubsidiaryAuthorizationEntityIdFilter:
    out: SubsidiaryAuthorizationEntityIdFilter = {}  # type: ignore[typeddict-item]
    if data.get("ValueList") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_entity_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
