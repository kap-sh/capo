"""Generated from Smithy shape ``com.amazonaws.snowball#LambdaResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.lambda_resource

LambdaResourceList: TypeAlias = list[
    "capo_snowball.types.lambda_resource.LambdaResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaResourceList) -> list:
    import capo_snowball.types.lambda_resource

    out: list = []
    for item in value:
        out.append(capo_snowball.types.lambda_resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LambdaResourceList:
    import capo_snowball.types.lambda_resource

    out: LambdaResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.lambda_resource.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaResourceList) -> list:
    import capo_snowball.types.lambda_resource

    out: list = []
    for item in value:
        out.append(capo_snowball.types.lambda_resource.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LambdaResourceList:
    import capo_snowball.types.lambda_resource

    out: LambdaResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.lambda_resource.deserialize_cbor(item))
    return out
