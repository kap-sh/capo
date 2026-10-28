"""Generated from Smithy shape ``com.amazonaws.bedrock#EndpointConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.sage_maker_endpoint


class EndpointConfigSageMakerMember(TypedDict, closed=True):
    sageMaker: "capo_bedrock.types.sage_maker_endpoint.SageMakerEndpoint"


EndpointConfig: TypeAlias = EndpointConfigSageMakerMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: EndpointConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EndpointConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "sageMaker" in value:
        import capo_bedrock.types.sage_maker_endpoint

        return {
            "sageMaker": capo_bedrock.types.sage_maker_endpoint.serialize_json(
                value["sageMaker"]
            )
        }
    else:
        raise SerializationError("EndpointConfig: no variant present")


def deserialize_json(data: dict) -> EndpointConfig:
    if data.get("sageMaker") is not None:
        import capo_bedrock.types.sage_maker_endpoint

        return {
            "sageMaker": capo_bedrock.types.sage_maker_endpoint.deserialize_json(
                data["sageMaker"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EndpointConfig: no recognized variant key")
