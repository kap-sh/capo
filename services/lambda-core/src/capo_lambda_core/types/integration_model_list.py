"""Generated from Smithy shape ``com.amazonaws.lambdacore#IntegrationModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.integration_model

IntegrationModelList: TypeAlias = list[
    "capo_lambda_core.types.integration_model.IntegrationModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationModelList) -> list:
    import capo_lambda_core.types.integration_model

    out: list = []
    for item in value:
        out.append(capo_lambda_core.types.integration_model.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntegrationModelList:
    import capo_lambda_core.types.integration_model

    out: IntegrationModelList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_core.types.integration_model.deserialize_json(item))
    return out
