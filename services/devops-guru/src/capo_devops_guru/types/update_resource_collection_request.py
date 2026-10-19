"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateResourceCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_guru.types.update_resource_collection_action
    import capo_devops_guru.types.update_resource_collection_filter


class UpdateResourceCollectionRequest(TypedDict, closed=True):
    action: "capo_devops_guru.types.update_resource_collection_action.UpdateResourceCollectionAction"
    """<p> Specifies if the resource collection in the request is added or deleted to the resource collection. </p>"""
    resource_collection: "capo_devops_guru.types.update_resource_collection_filter.UpdateResourceCollectionFilter"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceCollectionRequest) -> dict:
    out: dict = {}
    import capo_devops_guru.types.update_resource_collection_action

    out["Action"] = (
        capo_devops_guru.types.update_resource_collection_action.serialize_json(
            value["action"]
        )
    )
    import capo_devops_guru.types.update_resource_collection_filter

    out["ResourceCollection"] = (
        capo_devops_guru.types.update_resource_collection_filter.serialize_json(
            value["resource_collection"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateResourceCollectionRequest:
    out: UpdateResourceCollectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_devops_guru.types.update_resource_collection_action

        out["action"] = (
            capo_devops_guru.types.update_resource_collection_action.deserialize_json(
                data["Action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_devops_guru.types.update_resource_collection_action.UpdateResourceCollectionAction",
            "",
        )
    if data.get("ResourceCollection") is not None:
        import capo_devops_guru.types.update_resource_collection_filter

        out["resource_collection"] = (
            capo_devops_guru.types.update_resource_collection_filter.deserialize_json(
                data["ResourceCollection"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateResourceCollectionRequest.resource_collection required"
        )
    return out
