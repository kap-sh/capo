"""Generated from Smithy shape ``com.amazonaws.acm#RenewalSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm.types.domain_validation_list
    import capo_acm.types.failure_reason
    import capo_acm.types.renewal_status
    import capo_acm.types.t_stamp


class RenewalSummary(TypedDict, closed=True):
    renewal_status: "capo_acm.types.renewal_status.RenewalStatus"
    """<p>The status of ACM's <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html">managed renewal</a> of the certificate.</p>"""
    domain_validation_options: (
        "capo_acm.types.domain_validation_list.DomainValidationList"
    )
    """<p>Contains information about the validation of each domain name in the certificate, as it pertains to ACM's <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html">managed renewal</a>. This is different from the initial validation that occurs as a result of the <a>RequestCertificate</a> request. This field exists only when the certificate type is <code>AMAZON_ISSUED</code>.</p>"""
    renewal_status_reason: NotRequired["capo_acm.types.failure_reason.FailureReason"]
    """<p>The reason that a renewal request was unsuccessful.</p>"""
    updated_at: "capo_acm.types.t_stamp.TStamp"
    """<p>The time at which the renewal summary was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewalSummary) -> dict:
    out: dict = {}
    import capo_acm.types.renewal_status

    out["RenewalStatus"] = capo_acm.types.renewal_status.serialize_aws_json_1_1(
        value["renewal_status"]
    )
    import capo_acm.types.domain_validation_list

    out["DomainValidationOptions"] = (
        capo_acm.types.domain_validation_list.serialize_aws_json_1_1(
            value["domain_validation_options"]
        )
    )
    if "renewal_status_reason" in value:
        import capo_acm.types.failure_reason

        out["RenewalStatusReason"] = (
            capo_acm.types.failure_reason.serialize_aws_json_1_1(
                value["renewal_status_reason"]
            )
        )
    import capo_acm.types.t_stamp

    out["UpdatedAt"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RenewalSummary:
    out: RenewalSummary = {}  # type: ignore[typeddict-item]
    if data.get("RenewalStatus") is not None:
        import capo_acm.types.renewal_status

        out["renewal_status"] = capo_acm.types.renewal_status.deserialize_aws_json_1_1(
            data["RenewalStatus"]
        )
    else:
        raise DeserializationError("RenewalSummary.renewal_status required")
    if data.get("DomainValidationOptions") is not None:
        import capo_acm.types.domain_validation_list

        out["domain_validation_options"] = (
            capo_acm.types.domain_validation_list.deserialize_aws_json_1_1(
                data["DomainValidationOptions"]
            )
        )
    else:
        raise DeserializationError("RenewalSummary.domain_validation_options required")
    if data.get("RenewalStatusReason") is not None:
        import capo_acm.types.failure_reason

        out["renewal_status_reason"] = (
            capo_acm.types.failure_reason.deserialize_aws_json_1_1(
                data["RenewalStatusReason"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_acm.types.t_stamp

        out["updated_at"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("RenewalSummary.updated_at required")
    return out
