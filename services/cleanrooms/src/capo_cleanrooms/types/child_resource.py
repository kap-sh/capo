"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChildResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.child_resource_type
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.resource_status
    import capo_cleanrooms.types.uuid


class ChildResource(TypedDict, closed=True):
    resource_id: NotRequired["capo_cleanrooms.types.uuid.UUID"]
    """<p>The unique identifier of the child resource.</p>"""
    resource_type: "capo_cleanrooms.types.child_resource_type.ChildResourceType"
    """<p>The type of the child resource.</p>"""
    resource_name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The name of the child resource.</p>"""
    owner_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the member who owns the child resource.</p>"""
    resource_status: NotRequired["capo_cleanrooms.types.resource_status.ResourceStatus"]
    """<p>The current status of the child resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChildResource) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    import capo_cleanrooms.types.child_resource_type

    out["resourceType"] = capo_cleanrooms.types.child_resource_type.serialize_json(
        value["resource_type"]
    )
    out["resourceName"] = value["resource_name"]
    out["ownerAccountId"] = value["owner_account_id"]
    if "resource_status" in value:
        import capo_cleanrooms.types.resource_status

        out["resourceStatus"] = capo_cleanrooms.types.resource_status.serialize_json(
            value["resource_status"]
        )
    return out


def deserialize_json(data: dict) -> ChildResource:
    out: ChildResource = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        import capo_cleanrooms.types.child_resource_type

        out["resource_type"] = (
            capo_cleanrooms.types.child_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_cleanrooms.types.child_resource_type.ChildResourceType", ""
        )
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        out["owner_account_id"] = ""
    if data.get("resourceStatus") is not None:
        import capo_cleanrooms.types.resource_status

        out["resource_status"] = capo_cleanrooms.types.resource_status.deserialize_json(
            data["resourceStatus"]
        )
    return out
