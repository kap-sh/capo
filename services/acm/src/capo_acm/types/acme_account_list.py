"""Generated from Smithy shape ``com.amazonaws.acm#AcmeAccountList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.acme_account_summary

AcmeAccountList: TypeAlias = list[
    "capo_acm.types.acme_account_summary.AcmeAccountSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeAccountList) -> list:
    import capo_acm.types.acme_account_summary

    out: list = []
    for item in value:
        out.append(capo_acm.types.acme_account_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AcmeAccountList:
    import capo_acm.types.acme_account_summary

    out: AcmeAccountList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm.types.acme_account_summary.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: AcmeAccountList) -> list[Any]:
    import capo_acm.types.acme_account_summary

    return [
        capo_acm.types.acme_account_summary.redact_sensitive(item) for item in value
    ]
