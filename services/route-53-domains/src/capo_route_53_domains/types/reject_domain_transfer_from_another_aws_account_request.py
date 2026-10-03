"""Generated from Smithy shape ``com.amazonaws.route53domains#RejectDomainTransferFromAnotherAwsAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name


class RejectDomainTransferFromAnotherAwsAccountRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that was specified when another Amazon Web Services account submitted a <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html">TransferDomainToAnotherAwsAccount</a> request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: RejectDomainTransferFromAnotherAwsAccountRequest,
) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> RejectDomainTransferFromAnotherAwsAccountRequest:
    out: RejectDomainTransferFromAnotherAwsAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "RejectDomainTransferFromAnotherAwsAccountRequest.domain_name required"
        )
    return out
