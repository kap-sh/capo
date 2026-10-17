"""Generated from Smithy shape ``com.amazonaws.deadline#MembershipResourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.membership_resource_type

MembershipResourceTypes: TypeAlias = list[
    "capo_deadline.types.membership_resource_type.MembershipResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipResourceTypes) -> list:
    import capo_deadline.types.membership_resource_type

    out: list = []
    for item in value:
        out.append(capo_deadline.types.membership_resource_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> MembershipResourceTypes:
    import capo_deadline.types.membership_resource_type

    out: MembershipResourceTypes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.membership_resource_type.deserialize_json(item))
    return out
