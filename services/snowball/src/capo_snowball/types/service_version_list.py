"""Generated from Smithy shape ``com.amazonaws.snowball#ServiceVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.service_version

ServiceVersionList: TypeAlias = list[
    "capo_snowball.types.service_version.ServiceVersion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceVersionList) -> list:
    import capo_snowball.types.service_version

    out: list = []
    for item in value:
        out.append(capo_snowball.types.service_version.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceVersionList:
    import capo_snowball.types.service_version

    out: ServiceVersionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.service_version.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceVersionList) -> list:
    import capo_snowball.types.service_version

    out: list = []
    for item in value:
        out.append(capo_snowball.types.service_version.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ServiceVersionList:
    import capo_snowball.types.service_version

    out: ServiceVersionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.service_version.deserialize_cbor(item))
    return out
