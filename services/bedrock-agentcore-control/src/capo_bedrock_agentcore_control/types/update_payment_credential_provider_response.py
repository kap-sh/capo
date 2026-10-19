"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatePaymentCredentialProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.credential_provider_name
    import capo_bedrock_agentcore_control.types.payment_credential_provider_arn_type
    import capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type
    import capo_bedrock_agentcore_control.types.payment_provider_configuration_output


class UpdatePaymentCredentialProviderResponse(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the updated payment credential provider.</p>"""
    credential_provider_vendor: "capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType"
    """<p>The vendor type for the updated payment credential provider.</p>"""
    credential_provider_arn: "capo_bedrock_agentcore_control.types.payment_credential_provider_arn_type.PaymentCredentialProviderArnType"
    """<p>The Amazon Resource Name (ARN) of the updated payment credential provider.</p>"""
    provider_configuration_output: "capo_bedrock_agentcore_control.types.payment_provider_configuration_output.PaymentProviderConfigurationOutput"
    """<p>Output configuration (contains secret ARNs, excludes actual secret values).</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the payment credential provider was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The timestamp when the payment credential provider was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePaymentCredentialProviderResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type

    out["credentialProviderVendor"] = (
        capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.serialize_json(
            value["credential_provider_vendor"]
        )
    )
    out["credentialProviderArn"] = value["credential_provider_arn"]
    import capo_bedrock_agentcore_control.types.payment_provider_configuration_output

    out["providerConfigurationOutput"] = (
        capo_bedrock_agentcore_control.types.payment_provider_configuration_output.serialize_json(
            value["provider_configuration_output"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdTime"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["lastUpdatedTime"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePaymentCredentialProviderResponse:
    out: UpdatePaymentCredentialProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("credentialProviderVendor") is not None:
        import capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type

        out["credential_provider_vendor"] = (
            capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.deserialize_json(
                data["credentialProviderVendor"]
            )
        )
    else:
        import typing

        out["credential_provider_vendor"] = typing.cast(
            "capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType",
            "",
        )
    if data.get("credentialProviderArn") is not None:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        out["credential_provider_arn"] = ""
    if data.get("providerConfigurationOutput") is not None:
        import capo_bedrock_agentcore_control.types.payment_provider_configuration_output

        out["provider_configuration_output"] = (
            capo_bedrock_agentcore_control.types.payment_provider_configuration_output.deserialize_json(
                data["providerConfigurationOutput"]
            )
        )
    else:
        import capo_bedrock_agentcore_control.types._unknown

        out["provider_configuration_output"] = (
            capo_bedrock_agentcore_control.types._unknown.UnknownUnionMember("")
        )
    if data.get("createdTime") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_time"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastUpdatedTime") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["last_updated_time"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
