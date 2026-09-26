"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListOfPortSpecification``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.port_specification

ListOfPortSpecification: TypeAlias = list[
    "capo_lambda_microvms.types.port_specification.PortSpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfPortSpecification) -> list:
    import capo_lambda_microvms.types.port_specification

    out: list = []
    for item in value:
        out.append(capo_lambda_microvms.types.port_specification.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfPortSpecification:
    import capo_lambda_microvms.types.port_specification

    out: ListOfPortSpecification = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_microvms.types.port_specification.deserialize_json(item))
    return out
