"""Generated from Smithy shape ``com.amazonaws.lakeformation#RLSPolicyAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.rls_policy_attachment

RLSPolicyAttachmentList: TypeAlias = list[
    "capo_lakeformation.types.rls_policy_attachment.RLSPolicyAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: RLSPolicyAttachmentList) -> list:
    import capo_lakeformation.types.rls_policy_attachment

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.rls_policy_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> RLSPolicyAttachmentList:
    import capo_lakeformation.types.rls_policy_attachment

    out: RLSPolicyAttachmentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lakeformation.types.rls_policy_attachment.deserialize_json(item)
        )
    return out
