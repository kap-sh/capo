"""Generated from Smithy shape ``com.amazonaws.route53domains#TransferDomainToAnotherAwsAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.account_id
    import capo_route_53_domains.types.domain_name


class TransferDomainToAnotherAwsAccountRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to transfer from the current Amazon Web Services account to another account.</p>"""
    account_id: "capo_route_53_domains.types.account_id.AccountId"
    """<p>The account ID of the Amazon Web Services account that you want to transfer the domain to, for example, <code>111122223333</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransferDomainToAnotherAwsAccountRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransferDomainToAnotherAwsAccountRequest:
    out: TransferDomainToAnotherAwsAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    return out
