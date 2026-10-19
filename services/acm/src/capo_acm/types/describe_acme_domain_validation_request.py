"""Generated from Smithy shape ``com.amazonaws.acm#DescribeAcmeDomainValidationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_domain_validation_arn


class DescribeAcmeDomainValidationRequest(TypedDict, closed=True):
    acme_domain_validation_arn: (
        "capo_acm.types.acme_domain_validation_arn.AcmeDomainValidationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ACME domain validation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAcmeDomainValidationRequest) -> dict:
    out: dict = {}
    out["AcmeDomainValidationArn"] = value["acme_domain_validation_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAcmeDomainValidationRequest:
    out: DescribeAcmeDomainValidationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcmeDomainValidationArn") is not None:
        out["acme_domain_validation_arn"] = data["AcmeDomainValidationArn"]
    else:
        out["acme_domain_validation_arn"] = ""
    return out
