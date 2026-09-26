"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.resources

ResourcesList: TypeAlias = list["capo_lambda_microvms.types.resources.Resources"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesList) -> list:
    import capo_lambda_microvms.types.resources

    out: list = []
    for item in value:
        out.append(capo_lambda_microvms.types.resources.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourcesList:
    import capo_lambda_microvms.types.resources

    out: ResourcesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_microvms.types.resources.deserialize_json(item))
    return out
