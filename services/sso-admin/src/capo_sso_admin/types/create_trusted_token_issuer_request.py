"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateTrustedTokenIssuerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.client_token
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.tag_list
    import capo_sso_admin.types.trusted_token_issuer_configuration
    import capo_sso_admin.types.trusted_token_issuer_name
    import capo_sso_admin.types.trusted_token_issuer_type


class CreateTrustedTokenIssuerRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>Specifies the ARN of the instance of IAM Identity Center to contain the new trusted token issuer configuration.</p>"""
    name: "capo_sso_admin.types.trusted_token_issuer_name.TrustedTokenIssuerName"
    """<p>Specifies the name of the new trusted token issuer configuration.</p>"""
    trusted_token_issuer_type: (
        "capo_sso_admin.types.trusted_token_issuer_type.TrustedTokenIssuerType"
    )
    """<p>Specifies the type of the new trusted token issuer.</p>"""
    trusted_token_issuer_configuration: "capo_sso_admin.types.trusted_token_issuer_configuration.TrustedTokenIssuerConfiguration"
    """<p>Specifies settings that apply to the new trusted token issuer configuration. The settings that are available depend on what <code>TrustedTokenIssuerType</code> you specify.</p>"""
    client_token: NotRequired["capo_sso_admin.types.client_token.ClientToken"]
    """<p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    tags: NotRequired["capo_sso_admin.types.tag_list.TagList"]
    """<p>Specifies tags to be attached to the new trusted token issuer configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrustedTokenIssuerRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["Name"] = value["name"]
    import capo_sso_admin.types.trusted_token_issuer_type

    out["TrustedTokenIssuerType"] = (
        capo_sso_admin.types.trusted_token_issuer_type.serialize_aws_json_1_1(
            value["trusted_token_issuer_type"]
        )
    )
    import capo_sso_admin.types.trusted_token_issuer_configuration

    out["TrustedTokenIssuerConfiguration"] = (
        capo_sso_admin.types.trusted_token_issuer_configuration.serialize_aws_json_1_1(
            value["trusted_token_issuer_configuration"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_sso_admin.types.tag_list

        out["Tags"] = capo_sso_admin.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrustedTokenIssuerRequest:
    out: CreateTrustedTokenIssuerRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "CreateTrustedTokenIssuerRequest.instance_arn required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateTrustedTokenIssuerRequest.name required")
    if data.get("TrustedTokenIssuerType") is not None:
        import capo_sso_admin.types.trusted_token_issuer_type

        out["trusted_token_issuer_type"] = (
            capo_sso_admin.types.trusted_token_issuer_type.deserialize_aws_json_1_1(
                data["TrustedTokenIssuerType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTrustedTokenIssuerRequest.trusted_token_issuer_type required"
        )
    if data.get("TrustedTokenIssuerConfiguration") is not None:
        import capo_sso_admin.types.trusted_token_issuer_configuration

        out["trusted_token_issuer_configuration"] = (
            capo_sso_admin.types.trusted_token_issuer_configuration.deserialize_aws_json_1_1(
                data["TrustedTokenIssuerConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTrustedTokenIssuerRequest.trusted_token_issuer_configuration required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_sso_admin.types.tag_list

        out["tags"] = capo_sso_admin.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
