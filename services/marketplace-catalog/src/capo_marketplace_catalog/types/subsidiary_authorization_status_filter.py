"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SubsidiaryAuthorizationStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.subsidiary_authorization_status_filter_value_list


class SubsidiaryAuthorizationStatusFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.subsidiary_authorization_status_filter_value_list.SubsidiaryAuthorizationStatusFilterValueList"
    ]
    """<p>A list of statuses to filter by. The operation returns subsidiary authorizations with a status that matches a value in this list. Valid values are:</p> <ul> <li> <p> <code>Draft</code> - The subsidiary authorization was created but not yet released. The subsidiary account can't see it.</p> </li> <li> <p> <code>Active</code> - The subsidiary account can use the subsidiary authorization to create offers for the authorized product.</p> </li> <li> <p> <code>Restricted</code> - The subsidiary authorization was discarded while in <code>Draft</code> or revoked while <code>Active</code>. It can't be used to create new offers. This status is final.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubsidiaryAuthorizationStatusFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.subsidiary_authorization_status_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_status_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubsidiaryAuthorizationStatusFilter:
    out: SubsidiaryAuthorizationStatusFilter = {}  # type: ignore[typeddict-item]
    if data.get("ValueList") is not None:
        import capo_marketplace_catalog.types.subsidiary_authorization_status_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.subsidiary_authorization_status_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
