"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TagPropagationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.iam_role_arn
    import capo_observabilityadmin.types.tag_conflict_resolution_strategy


class TagPropagationConfiguration(TypedDict, closed=True):
    destination_role_arn: "capo_observabilityadmin.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of a customer-managed IAM role in the destination account. The service assumes this role to propagate tags to destination log groups. You must have <code>iam:PassRole</code> permission on this role.</p>"""
    tag_conflict_resolution_strategy: NotRequired[
        "capo_observabilityadmin.types.tag_conflict_resolution_strategy.TagConflictResolutionStrategy"
    ]
    """<p>The strategy for resolving conflicts when a tag key exists on both the source and destination log groups. If not specified, defaults to <code>UPDATE_SYNC</code>.</p> <ul> <li> <p> <code>ADD_ONLY</code> – Only adds new tags from the source without modifying existing destination tags.</p> </li> <li> <p> <code>UPDATE_SYNC</code> – Adds new tags and updates existing tags from the source. Does not remove destination tags that are absent from the source.</p> </li> <li> <p> <code>IN_SYNC</code> – Keeps destination tags fully synchronized with source tags, including removing destination tags that do not exist on the source.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagPropagationConfiguration) -> dict:
    out: dict = {}
    out["DestinationRoleArn"] = value["destination_role_arn"]
    if "tag_conflict_resolution_strategy" in value:
        import capo_observabilityadmin.types.tag_conflict_resolution_strategy

        out["TagConflictResolutionStrategy"] = (
            capo_observabilityadmin.types.tag_conflict_resolution_strategy.serialize_json(
                value["tag_conflict_resolution_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> TagPropagationConfiguration:
    out: TagPropagationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DestinationRoleArn") is not None:
        out["destination_role_arn"] = data["DestinationRoleArn"]
    else:
        out["destination_role_arn"] = ""
    if data.get("TagConflictResolutionStrategy") is not None:
        import capo_observabilityadmin.types.tag_conflict_resolution_strategy

        out["tag_conflict_resolution_strategy"] = (
            capo_observabilityadmin.types.tag_conflict_resolution_strategy.deserialize_json(
                data["TagConflictResolutionStrategy"]
            )
        )
    return out
