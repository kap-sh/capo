"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#IntegrationIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError
from capo_connectcampaignsv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.customer_profiles_integration_identifier
    import capo_connectcampaignsv2.types.lambda_integration_identifier
    import capo_connectcampaignsv2.types.q_connect_integration_identifier


class IntegrationIdentifierCustomerProfilesMember(TypedDict, closed=True):
    customerProfiles: "capo_connectcampaignsv2.types.customer_profiles_integration_identifier.CustomerProfilesIntegrationIdentifier"


class IntegrationIdentifierQConnectMember(TypedDict, closed=True):
    qConnect: "capo_connectcampaignsv2.types.q_connect_integration_identifier.QConnectIntegrationIdentifier"


IntegrationIdentifierLambdaMember = TypedDict(
    "IntegrationIdentifierLambdaMember",
    {
        "lambda": "capo_connectcampaignsv2.types.lambda_integration_identifier.LambdaIntegrationIdentifier",
    },
    closed=True,
)

IntegrationIdentifier: TypeAlias = (
    IntegrationIdentifierCustomerProfilesMember
    | IntegrationIdentifierQConnectMember
    | IntegrationIdentifierLambdaMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationIdentifier) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IntegrationIdentifier: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customerProfiles" in value:
        import capo_connectcampaignsv2.types.customer_profiles_integration_identifier

        return {
            "customerProfiles": capo_connectcampaignsv2.types.customer_profiles_integration_identifier.serialize_json(
                value["customerProfiles"]
            )
        }
    elif "qConnect" in value:
        import capo_connectcampaignsv2.types.q_connect_integration_identifier

        return {
            "qConnect": capo_connectcampaignsv2.types.q_connect_integration_identifier.serialize_json(
                value["qConnect"]
            )
        }
    elif "lambda" in value:
        import capo_connectcampaignsv2.types.lambda_integration_identifier

        return {
            "lambda": capo_connectcampaignsv2.types.lambda_integration_identifier.serialize_json(
                value["lambda"]
            )
        }
    else:
        raise SerializationError("IntegrationIdentifier: no variant present")


def deserialize_json(data: dict) -> IntegrationIdentifier:
    if data.get("customerProfiles") is not None:
        import capo_connectcampaignsv2.types.customer_profiles_integration_identifier

        return {
            "customerProfiles": capo_connectcampaignsv2.types.customer_profiles_integration_identifier.deserialize_json(
                data["customerProfiles"]
            )
        }
    elif data.get("qConnect") is not None:
        import capo_connectcampaignsv2.types.q_connect_integration_identifier

        return {
            "qConnect": capo_connectcampaignsv2.types.q_connect_integration_identifier.deserialize_json(
                data["qConnect"]
            )
        }
    elif data.get("lambda") is not None:
        import capo_connectcampaignsv2.types.lambda_integration_identifier

        return {
            "lambda": capo_connectcampaignsv2.types.lambda_integration_identifier.deserialize_json(
                data["lambda"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IntegrationIdentifier: no recognized variant key")
