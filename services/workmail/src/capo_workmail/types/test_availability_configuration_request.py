"""Generated from Smithy shape ``com.amazonaws.workmail#TestAvailabilityConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.domain_name
    import capo_workmail.types.ews_availability_provider
    import capo_workmail.types.lambda_availability_provider
    import capo_workmail.types.organization_id


class TestAvailabilityConfigurationRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization where the availability provider will be tested.</p>"""
    domain_name: NotRequired["capo_workmail.types.domain_name.DomainName"]
    """<p>The domain to which the provider applies. If this field is provided, a stored availability provider associated to this domain name will be tested.</p>"""
    ews_provider: NotRequired[
        "capo_workmail.types.ews_availability_provider.EwsAvailabilityProvider"
    ]
    lambda_provider: NotRequired[
        "capo_workmail.types.lambda_availability_provider.LambdaAvailabilityProvider"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestAvailabilityConfigurationRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "domain_name" in value:
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


def deserialize_aws_json_1_1(data: dict) -> TestAvailabilityConfigurationRequest:
    out: TestAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
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


def redact_sensitive(value: TestAvailabilityConfigurationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ews_provider" in value:
        import capo_workmail.types.ews_availability_provider

        out["ews_provider"] = (
            capo_workmail.types.ews_availability_provider.redact_sensitive(
                value["ews_provider"]
            )
        )
    return out
