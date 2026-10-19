"""Generated from Smithy shape ``com.amazonaws.iot#CreateCertificateProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificate_provider_account_default_for_operations
    import capo_iot.types.certificate_provider_function_arn
    import capo_iot.types.certificate_provider_name
    import capo_iot.types.client_token
    import capo_iot.types.tag_list


class CreateCertificateProviderRequest(TypedDict, closed=True):
    certificate_provider_name: (
        "capo_iot.types.certificate_provider_name.CertificateProviderName"
    )
    """<p>The name of the certificate provider.</p>"""
    lambda_function_arn: "capo_iot.types.certificate_provider_function_arn.CertificateProviderFunctionArn"
    """<p>The ARN of the Lambda function that defines the authentication logic.</p>"""
    account_default_for_operations: "capo_iot.types.certificate_provider_account_default_for_operations.CertificateProviderAccountDefaultForOperations"
    """<p>A list of the operations that the certificate provider will use to generate certificates. Valid value: <code>CreateCertificateFromCsr</code>.</p>"""
    client_token: NotRequired["capo_iot.types.client_token.ClientToken"]
    """<p>A string that you can optionally pass in the <code>CreateCertificateProvider</code> request to make sure the request is idempotent.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the certificate provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCertificateProviderRequest) -> dict:
    out: dict = {}
    out["lambdaFunctionArn"] = value["lambda_function_arn"]
    import capo_iot.types.certificate_provider_account_default_for_operations

    out["accountDefaultForOperations"] = (
        capo_iot.types.certificate_provider_account_default_for_operations.serialize_json(
            value["account_default_for_operations"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCertificateProviderRequest:
    out: CreateCertificateProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("lambdaFunctionArn") is not None:
        out["lambda_function_arn"] = data["lambdaFunctionArn"]
    else:
        out["lambda_function_arn"] = ""
    if data.get("accountDefaultForOperations") is not None:
        import capo_iot.types.certificate_provider_account_default_for_operations

        out["account_default_for_operations"] = (
            capo_iot.types.certificate_provider_account_default_for_operations.deserialize_json(
                data["accountDefaultForOperations"]
            )
        )
    else:
        out["account_default_for_operations"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    return out
