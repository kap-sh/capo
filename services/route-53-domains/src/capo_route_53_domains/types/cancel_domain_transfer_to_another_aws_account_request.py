"""Generated from Smithy shape ``com.amazonaws.route53domains#CancelDomainTransferToAnotherAwsAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name


class CancelDomainTransferToAnotherAwsAccountRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain for which you want to cancel the transfer to another Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CancelDomainTransferToAnotherAwsAccountRequest,
) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CancelDomainTransferToAnotherAwsAccountRequest:
    out: CancelDomainTransferToAnotherAwsAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    return out
