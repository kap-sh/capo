"""Generated from Smithy shape ``com.amazonaws.fms#ExpectedRoutes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.expected_route

ExpectedRoutes: TypeAlias = list["capo_fms.types.expected_route.ExpectedRoute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpectedRoutes) -> list:
    import capo_fms.types.expected_route

    out: list = []
    for item in value:
        out.append(capo_fms.types.expected_route.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExpectedRoutes:
    import capo_fms.types.expected_route

    out: ExpectedRoutes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.expected_route.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpectedRoutes) -> list:
    import capo_fms.types.expected_route

    out: list = []
    for item in value:
        out.append(capo_fms.types.expected_route.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ExpectedRoutes:
    import capo_fms.types.expected_route

    out: ExpectedRoutes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.expected_route.deserialize_cbor(item))
    return out
