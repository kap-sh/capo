"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RegionalEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_web.types.region
    import capo_lambda_web.types.regional_endpoint

RegionalEndpoints: TypeAlias = dict[
    "capo_lambda_web.types.region.Region",
    "capo_lambda_web.types.regional_endpoint.RegionalEndpoint",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RegionalEndpoints) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lambda_web.types.regional_endpoint

        out[key] = capo_lambda_web.types.regional_endpoint.serialize_json(value)
    return out


def deserialize_json(data: dict) -> RegionalEndpoints:
    out: RegionalEndpoints = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_lambda_web.types.regional_endpoint

        out[key] = capo_lambda_web.types.regional_endpoint.deserialize_json(value)
    return out
