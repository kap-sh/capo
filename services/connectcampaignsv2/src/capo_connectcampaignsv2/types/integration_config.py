"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#IntegrationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError
from capo_connectcampaignsv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.customer_profiles_integration_config
    import capo_connectcampaignsv2.types.lambda_integration_config
    import capo_connectcampaignsv2.types.q_connect_integration_config


class _IntegrationConfig_customerProfiles(TypedDict, closed=True):
    customerProfiles: "capo_connectcampaignsv2.types.customer_profiles_integration_config.CustomerProfilesIntegrationConfig"


class _IntegrationConfig_qConnect(TypedDict, closed=True):
    qConnect: "capo_connectcampaignsv2.types.q_connect_integration_config.QConnectIntegrationConfig"


_IntegrationConfig_lambda = TypedDict(
    "_IntegrationConfig_lambda",
    {
        "lambda": "capo_connectcampaignsv2.types.lambda_integration_config.LambdaIntegrationConfig",
    },
    closed=True,
)

IntegrationConfig: TypeAlias = (
    _IntegrationConfig_customerProfiles
    | _IntegrationConfig_qConnect
    | _IntegrationConfig_lambda
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"IntegrationConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "customerProfiles" in value:
        import capo_connectcampaignsv2.types.customer_profiles_integration_config

        return {
            "customerProfiles": capo_connectcampaignsv2.types.customer_profiles_integration_config.serialize_json(
                value["customerProfiles"]
            )
        }
    elif "qConnect" in value:
        import capo_connectcampaignsv2.types.q_connect_integration_config

        return {
            "qConnect": capo_connectcampaignsv2.types.q_connect_integration_config.serialize_json(
                value["qConnect"]
            )
        }
    elif "lambda" in value:
        import capo_connectcampaignsv2.types.lambda_integration_config

        return {
            "lambda": capo_connectcampaignsv2.types.lambda_integration_config.serialize_json(
                value["lambda"]
            )
        }
    else:
        raise SerializationError("IntegrationConfig: no variant present")


def deserialize_json(data: dict) -> IntegrationConfig:
    if data.get("customerProfiles") is not None:
        import capo_connectcampaignsv2.types.customer_profiles_integration_config

        return {
            "customerProfiles": capo_connectcampaignsv2.types.customer_profiles_integration_config.deserialize_json(
                data["customerProfiles"]
            )
        }
    elif data.get("qConnect") is not None:
        import capo_connectcampaignsv2.types.q_connect_integration_config

        return {
            "qConnect": capo_connectcampaignsv2.types.q_connect_integration_config.deserialize_json(
                data["qConnect"]
            )
        }
    elif data.get("lambda") is not None:
        import capo_connectcampaignsv2.types.lambda_integration_config

        return {
            "lambda": capo_connectcampaignsv2.types.lambda_integration_config.deserialize_json(
                data["lambda"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("IntegrationConfig: no recognized variant key")
