"""Generated from Smithy shape ``com.amazonaws.fms#IssueInfoMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.dependent_service_name
    import capo_fms.types.detailed_info

IssueInfoMap: TypeAlias = dict[
    "capo_fms.types.dependent_service_name.DependentServiceName",
    "capo_fms.types.detailed_info.DetailedInfo",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: IssueInfoMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fms.types.dependent_service_name

        out[capo_fms.types.dependent_service_name.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> IssueInfoMap:
    out: IssueInfoMap = {}
    for key, value in data.items():
        import capo_fms.types.dependent_service_name

        if value is None:
            continue
        out[capo_fms.types.dependent_service_name.deserialize_aws_json_1_1(key)] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: IssueInfoMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fms.types.dependent_service_name

        out[capo_fms.types.dependent_service_name.serialize_cbor(key)] = value
    return out


def deserialize_cbor(data: dict) -> IssueInfoMap:
    out: IssueInfoMap = {}
    for key, value in data.items():
        import capo_fms.types.dependent_service_name

        if value is None:
            continue
        out[capo_fms.types.dependent_service_name.deserialize_cbor(key)] = value
    return out
