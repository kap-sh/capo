"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CustomerSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.account_summary


class CustomerSummary(TypedDict, closed=True):
    account: NotRequired[
        "capo_partnercentral_selling.types.account_summary.AccountSummary"
    ]
    """<p>An object that contains a customer's account details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomerSummary) -> dict:
    out: dict = {}
    if "account" in value:
        import capo_partnercentral_selling.types.account_summary

        out["Account"] = (
            capo_partnercentral_selling.types.account_summary.serialize_aws_json_1_0(
                value["account"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomerSummary:
    out: CustomerSummary = {}  # type: ignore[typeddict-item]
    if data.get("Account") is not None:
        import capo_partnercentral_selling.types.account_summary

        out["account"] = (
            capo_partnercentral_selling.types.account_summary.deserialize_aws_json_1_0(
                data["Account"]
            )
        )
    return out


def redact_sensitive(value: CustomerSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "account" in value:
        import capo_partnercentral_selling.types.account_summary

        out["account"] = (
            capo_partnercentral_selling.types.account_summary.redact_sensitive(
                value["account"]
            )
        )
    return out
