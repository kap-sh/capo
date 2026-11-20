"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ActivationIssueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.activation_issue

ActivationIssueList: TypeAlias = list[
    "capo_partnercentral_marketing.types.activation_issue.ActivationIssue"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActivationIssueList) -> list:
    import capo_partnercentral_marketing.types.activation_issue

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.activation_issue.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ActivationIssueList:
    import capo_partnercentral_marketing.types.activation_issue

    out: ActivationIssueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.activation_issue.deserialize_cbor(item)
        )
    return out
