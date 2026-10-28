"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#IntegrationSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError
from capo_connectcampaignsv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.customer_profiles_integration_summary
    import capo_connectcampaignsv2.types.lambda_integration_summary
    import capo_connectcampaignsv2.types.q_connect_integration_summary


class IntegrationSummaryCustomerProfilesMember(TypedDict, closed=True):
    customerProfiles: "capo_connectcampaignsv2.types.customer_profiles_integration_summary.CustomerProfilesIntegrationSummary"


class IntegrationSummaryQConnectMember(TypedDict, closed=True):
    qConnect: "capo_connectcampaignsv2.types.q_connect_integration_summary.QConnectIntegrationSummary"


IntegrationSummaryLambdaMember = TypedDict(
    "IntegrationSummaryLambdaMember",
    {
        "lambda": "capo_connectcampaignsv2.types.lambda_integration_summary.LambdaIntegrationSummary",
    },
    closed=True,
)

IntegrationSummary: TypeAlias = (
    IntegrationSummaryCustomerProfilesMember
    | IntegrationSummaryQConnectMember
    | IntegrationSummaryLambdaMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummary) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IntegrationSummary: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customerProfiles" in value:
        import capo_connectcampaignsv2.types.customer_profiles_integration_summary

        return {
            "customerProfiles": capo_connectcampaignsv2.types.customer_profiles_integration_summary.serialize_json(
                value["customerProfiles"]
            )
        }
    elif "qConnect" in value:
        import capo_connectcampaignsv2.types.q_connect_integration_summary

        return {
            "qConnect": capo_connectcampaignsv2.types.q_connect_integration_summary.serialize_json(
                value["qConnect"]
            )
        }
    elif "lambda" in value:
        import capo_connectcampaignsv2.types.lambda_integration_summary

        return {
            "lambda": capo_connectcampaignsv2.types.lambda_integration_summary.serialize_json(
                value["lambda"]
            )
        }
    else:
        raise SerializationError("IntegrationSummary: no variant present")


def deserialize_json(data: dict) -> IntegrationSummary:
    if data.get("customerProfiles") is not None:
        import capo_connectcampaignsv2.types.customer_profiles_integration_summary

        return {
            "customerProfiles": capo_connectcampaignsv2.types.customer_profiles_integration_summary.deserialize_json(
                data["customerProfiles"]
            )
        }
    elif data.get("qConnect") is not None:
        import capo_connectcampaignsv2.types.q_connect_integration_summary

        return {
            "qConnect": capo_connectcampaignsv2.types.q_connect_integration_summary.deserialize_json(
                data["qConnect"]
            )
        }
    elif data.get("lambda") is not None:
        import capo_connectcampaignsv2.types.lambda_integration_summary

        return {
            "lambda": capo_connectcampaignsv2.types.lambda_integration_summary.deserialize_json(
                data["lambda"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IntegrationSummary: no recognized variant key")
