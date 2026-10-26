"""Generated from Smithy shape ``com.amazonaws.acm#CreateAcmeDomainValidationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_endpoint_arn
    import capo_acm.types.domain_name
    import capo_acm.types.prevalidation_options
    import capo_acm.types.tag_list


class CreateAcmeDomainValidationRequest(TypedDict, closed=True):
    idempotency_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>"""
    domain_name: "capo_acm.types.domain_name.DomainName"
    """<p>The domain name to validate.</p>"""
    prevalidation_options: "capo_acm.types.prevalidation_options.PrevalidationOptions"
    """<p>The prevalidation options for the domain.</p>"""
    tags: NotRequired["capo_acm.types.tag_list.TagList"]
    """<p>One or more tags to associate with the domain validation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAcmeDomainValidationRequest) -> dict:
    out: dict = {}
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    out["DomainName"] = value["domain_name"]
    import capo_acm.types.prevalidation_options

    out["PrevalidationOptions"] = (
        capo_acm.types.prevalidation_options.serialize_aws_json_1_1(
            value["prevalidation_options"]
        )
    )
    if "tags" in value:
        import capo_acm.types.tag_list

        out["Tags"] = capo_acm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAcmeDomainValidationRequest:
    out: CreateAcmeDomainValidationRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    else:
        out["acme_endpoint_arn"] = ""
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("PrevalidationOptions") is not None:
        import capo_acm.types.prevalidation_options

        out["prevalidation_options"] = (
            capo_acm.types.prevalidation_options.deserialize_aws_json_1_1(
                data["PrevalidationOptions"]
            )
        )
    else:
        out["prevalidation_options"] = {"$unknown": {"name": ""}}
    if data.get("Tags") is not None:
        import capo_acm.types.tag_list

        out["tags"] = capo_acm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
