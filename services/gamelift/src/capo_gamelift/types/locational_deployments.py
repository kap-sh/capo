"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationalDeployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.locational_deployment
    import capo_gamelift.types.non_zero_and128_max_ascii_string

LocationalDeployments: TypeAlias = dict[
    "capo_gamelift.types.non_zero_and128_max_ascii_string.NonZeroAnd128MaxAsciiString",
    "capo_gamelift.types.locational_deployment.LocationalDeployment",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LocationalDeployments) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_gamelift.types.locational_deployment

        out[key] = capo_gamelift.types.locational_deployment.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationalDeployments:
    out: LocationalDeployments = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_gamelift.types.locational_deployment

        out[key] = capo_gamelift.types.locational_deployment.deserialize_aws_json_1_1(
            value
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: LocationalDeployments) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_gamelift.types.locational_deployment

        out[key] = capo_gamelift.types.locational_deployment.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> LocationalDeployments:
    out: LocationalDeployments = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_gamelift.types.locational_deployment

        out[key] = capo_gamelift.types.locational_deployment.deserialize_cbor(value)
    return out
