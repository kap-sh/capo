"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#IntegrationIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError, SerializationError
from capo_cloudwatchomni.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.integration_arn


class IntegrationIdentifierIntegrationIdMember(TypedDict, closed=True):
    integrationId: "str"


class IntegrationIdentifierIntegrationArnMember(TypedDict, closed=True):
    integrationArn: "capo_cloudwatchomni.types.integration_arn.IntegrationArn"


class IntegrationIdentifierIntegrationNameMember(TypedDict, closed=True):
    integrationName: "str"


IntegrationIdentifier: TypeAlias = (
    IntegrationIdentifierIntegrationIdMember
    | IntegrationIdentifierIntegrationArnMember
    | IntegrationIdentifierIntegrationNameMember
    | UnknownUnionMember
)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IntegrationIdentifier) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IntegrationIdentifier: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "integrationId" in value:
        return {"integrationId": value["integrationId"]}
    elif "integrationArn" in value:
        return {"integrationArn": value["integrationArn"]}
    elif "integrationName" in value:
        return {"integrationName": value["integrationName"]}
    else:
        raise SerializationError("IntegrationIdentifier: no variant present")


def deserialize_cbor(data: dict) -> IntegrationIdentifier:
    if data.get("integrationId") is not None:
        return {"integrationId": data["integrationId"]}
    elif data.get("integrationArn") is not None:
        return {"integrationArn": data["integrationArn"]}
    elif data.get("integrationName") is not None:
        return {"integrationName": data["integrationName"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IntegrationIdentifier: no recognized variant key")
