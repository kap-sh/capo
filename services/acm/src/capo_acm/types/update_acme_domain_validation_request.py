"""Generated from Smithy shape ``com.amazonaws.acm#UpdateAcmeDomainValidationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_domain_validation_arn
    import capo_acm.types.prevalidation_options


class UpdateAcmeDomainValidationRequest(TypedDict, closed=True):
    acme_domain_validation_arn: (
        "capo_acm.types.acme_domain_validation_arn.AcmeDomainValidationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ACME domain validation to update.</p>"""
    prevalidation_options: NotRequired[
        "capo_acm.types.prevalidation_options.PrevalidationOptions"
    ]
    """<p>The updated prevalidation options.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAcmeDomainValidationRequest) -> dict:
    out: dict = {}
    out["AcmeDomainValidationArn"] = value["acme_domain_validation_arn"]
    if "prevalidation_options" in value:
        import capo_acm.types.prevalidation_options

        out["PrevalidationOptions"] = (
            capo_acm.types.prevalidation_options.serialize_aws_json_1_1(
                value["prevalidation_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAcmeDomainValidationRequest:
    out: UpdateAcmeDomainValidationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcmeDomainValidationArn") is not None:
        out["acme_domain_validation_arn"] = data["AcmeDomainValidationArn"]
    else:
        out["acme_domain_validation_arn"] = ""
    if data.get("PrevalidationOptions") is not None:
        import capo_acm.types.prevalidation_options

        out["prevalidation_options"] = (
            capo_acm.types.prevalidation_options.deserialize_aws_json_1_1(
                data["PrevalidationOptions"]
            )
        )
    return out
