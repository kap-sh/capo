"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_policy_detail_action_include_resources
    import capo_imagebuilder.types.lifecycle_policy_detail_action_type


class LifecyclePolicyDetailAction(TypedDict, closed=True):
    type: "capo_imagebuilder.types.lifecycle_policy_detail_action_type.LifecyclePolicyDetailActionType"
    """<p>Specifies the lifecycle action to take. <code>DELETE</code> deletes the image resource and, with <code>includeResources</code>, also removes distributed AMIs, snapshots, or container images. <code>DEPRECATE</code> and <code>DISABLE</code> set the corresponding status on the image resource and, if <code>includeResources.amis</code> is set, on its distributed AMIs.</p>"""
    include_resources: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_detail_action_include_resources.LifecyclePolicyDetailActionIncludeResources"
    ]
    """<p>Specifies which underlying resources the action extends to beyond the Image Builder image resource itself: distributed AMIs, their snapshots, or distributed container images. <code>DELETE</code> rules can include all three, <code>DEPRECATE</code> and <code>DISABLE</code> rules can include AMIs only, and you can only include snapshots together with AMIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetailAction) -> dict:
    out: dict = {}
    import capo_imagebuilder.types.lifecycle_policy_detail_action_type

    out["type"] = (
        capo_imagebuilder.types.lifecycle_policy_detail_action_type.serialize_json(
            value["type"]
        )
    )
    if "include_resources" in value:
        import capo_imagebuilder.types.lifecycle_policy_detail_action_include_resources

        out["includeResources"] = (
            capo_imagebuilder.types.lifecycle_policy_detail_action_include_resources.serialize_json(
                value["include_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> LifecyclePolicyDetailAction:
    out: LifecyclePolicyDetailAction = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_imagebuilder.types.lifecycle_policy_detail_action_type

        out["type"] = (
            capo_imagebuilder.types.lifecycle_policy_detail_action_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_imagebuilder.types.lifecycle_policy_detail_action_type.LifecyclePolicyDetailActionType",
            "",
        )
    if data.get("includeResources") is not None:
        import capo_imagebuilder.types.lifecycle_policy_detail_action_include_resources

        out["include_resources"] = (
            capo_imagebuilder.types.lifecycle_policy_detail_action_include_resources.deserialize_json(
                data["includeResources"]
            )
        )
    return out
