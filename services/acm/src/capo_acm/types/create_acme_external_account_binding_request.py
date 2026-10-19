"""Generated from Smithy shape ``com.amazonaws.acm#CreateAcmeExternalAccountBindingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_endpoint_arn
    import capo_acm.types.expiration
    import capo_acm.types.role_arn
    import capo_acm.types.tag_list


class CreateAcmeExternalAccountBindingRequest(TypedDict, closed=True):
    idempotency_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>"""
    role_arn: "capo_acm.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to associate with the external account binding.</p>"""
    expiration: NotRequired["capo_acm.types.expiration.Expiration"]
    """<p>The expiration configuration for the external account binding.</p>"""
    tags: NotRequired["capo_acm.types.tag_list.TagList"]
    """<p>One or more tags to associate with the external account binding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAcmeExternalAccountBindingRequest) -> dict:
    out: dict = {}
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    out["RoleArn"] = value["role_arn"]
    if "expiration" in value:
        import capo_acm.types.expiration

        out["Expiration"] = capo_acm.types.expiration.serialize_aws_json_1_1(
            value["expiration"]
        )
    if "tags" in value:
        import capo_acm.types.tag_list

        out["Tags"] = capo_acm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAcmeExternalAccountBindingRequest:
    out: CreateAcmeExternalAccountBindingRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    else:
        out["acme_endpoint_arn"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("Expiration") is not None:
        import capo_acm.types.expiration

        out["expiration"] = capo_acm.types.expiration.deserialize_aws_json_1_1(
            data["Expiration"]
        )
    if data.get("Tags") is not None:
        import capo_acm.types.tag_list

        out["tags"] = capo_acm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
