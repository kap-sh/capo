"""Generated from Smithy shape ``com.amazonaws.workmail#CreateAvailabilityConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.domain_name
    import capo_workmail.types.ews_availability_provider
    import capo_workmail.types.idempotency_client_token
    import capo_workmail.types.lambda_availability_provider
    import capo_workmail.types.organization_id


class CreateAvailabilityConfigurationRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_workmail.types.idempotency_client_token.IdempotencyClientToken"
    ]
    """<p>An idempotent token that ensures that an API request is executed only once.</p>"""
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which the <code>AvailabilityConfiguration</code> will be created.</p>"""
    domain_name: "capo_workmail.types.domain_name.DomainName"
    """<p>The domain to which the provider applies.</p>"""
    ews_provider: NotRequired[
        "capo_workmail.types.ews_availability_provider.EwsAvailabilityProvider"
    ]
    """<p>Exchange Web Services (EWS) availability provider definition. The request must contain exactly one provider definition, either <code>EwsProvider</code> or <code>LambdaProvider</code>.</p>"""
    lambda_provider: NotRequired[
        "capo_workmail.types.lambda_availability_provider.LambdaAvailabilityProvider"
    ]
    """<p>Lambda availability provider definition. The request must contain exactly one provider definition, either <code>EwsProvider</code> or <code>LambdaProvider</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAvailabilityConfigurationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["OrganizationId"] = value["organization_id"]
    out["DomainName"] = value["domain_name"]
    if "ews_provider" in value:
        import capo_workmail.types.ews_availability_provider

        out["EwsProvider"] = (
            capo_workmail.types.ews_availability_provider.serialize_aws_json_1_1(
                value["ews_provider"]
            )
        )
    if "lambda_provider" in value:
        import capo_workmail.types.lambda_availability_provider

        out["LambdaProvider"] = (
            capo_workmail.types.lambda_availability_provider.serialize_aws_json_1_1(
                value["lambda_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAvailabilityConfigurationRequest:
    out: CreateAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("EwsProvider") is not None:
        import capo_workmail.types.ews_availability_provider

        out["ews_provider"] = (
            capo_workmail.types.ews_availability_provider.deserialize_aws_json_1_1(
                data["EwsProvider"]
            )
        )
    if data.get("LambdaProvider") is not None:
        import capo_workmail.types.lambda_availability_provider

        out["lambda_provider"] = (
            capo_workmail.types.lambda_availability_provider.deserialize_aws_json_1_1(
                data["LambdaProvider"]
            )
        )
    return out


def redact_sensitive(value: CreateAvailabilityConfigurationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ews_provider" in value:
        import capo_workmail.types.ews_availability_provider

        out["ews_provider"] = (
            capo_workmail.types.ews_availability_provider.redact_sensitive(
                value["ews_provider"]
            )
        )
    return out
