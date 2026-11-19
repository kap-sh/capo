"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_type

ConformancePackTypeList: TypeAlias = list[
    "capo_config_service.types.conformance_pack_type.ConformancePackType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackTypeList) -> list:
    import capo_config_service.types.conformance_pack_type

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.conformance_pack_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConformancePackTypeList:
    import capo_config_service.types.conformance_pack_type

    out: ConformancePackTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_config_service.types.conformance_pack_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
