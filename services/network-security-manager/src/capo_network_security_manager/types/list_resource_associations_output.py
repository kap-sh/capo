"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ListResourceAssociationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.resource_association_list


class ListResourceAssociationsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_network_security_manager.types.next_token.NextToken"]
    """<p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>"""
    resource_associations: "capo_network_security_manager.types.resource_association_list.ResourceAssociationList"
    """<p>The list of resource associations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceAssociationsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_network_security_manager.types.resource_association_list

    out["resourceAssociations"] = (
        capo_network_security_manager.types.resource_association_list.serialize_json(
            value["resource_associations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListResourceAssociationsOutput:
    out: ListResourceAssociationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("resourceAssociations") is not None:
        import capo_network_security_manager.types.resource_association_list

        out["resource_associations"] = (
            capo_network_security_manager.types.resource_association_list.deserialize_json(
                data["resourceAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "ListResourceAssociationsOutput.resource_associations required"
        )
    return out
