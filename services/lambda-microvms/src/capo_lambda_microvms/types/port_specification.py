"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#PortSpecification``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.port_number
    import capo_lambda_microvms.types.port_range


class _PortSpecification_port(TypedDict, closed=True):
    port: "capo_lambda_microvms.types.port_number.PortNumber"


class _PortSpecification_range(TypedDict, closed=True):
    range: "capo_lambda_microvms.types.port_range.PortRange"


class _PortSpecification_allPorts(TypedDict, closed=True):
    allPorts: "None"


PortSpecification: TypeAlias = (
    _PortSpecification_port | _PortSpecification_range | _PortSpecification_allPorts
)


# --- restJson1 ser/de ---
def serialize_json(value: PortSpecification) -> dict:
    if "port" in value:
        return {"port": value["port"]}
    elif "range" in value:
        import capo_lambda_microvms.types.port_range

        return {
            "range": capo_lambda_microvms.types.port_range.serialize_json(
                value["range"]
            )
        }
    elif "allPorts" in value:
        return {"allPorts": {}}
    else:
        raise SerializationError("PortSpecification: no variant present")


def deserialize_json(data: dict) -> PortSpecification:
    if data.get("port") is not None:
        return {"port": data["port"]}
    elif data.get("range") is not None:
        import capo_lambda_microvms.types.port_range

        return {
            "range": capo_lambda_microvms.types.port_range.deserialize_json(
                data["range"]
            )
        }
    elif data.get("allPorts") is not None:
        return {"allPorts": None}
    else:
        raise DeserializationError("PortSpecification: no recognized variant key")
