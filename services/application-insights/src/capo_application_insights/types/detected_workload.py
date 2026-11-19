"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DetectedWorkload``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_insights.types.tier
    import capo_application_insights.types.workload_meta_data

DetectedWorkload: TypeAlias = dict[
    "capo_application_insights.types.tier.Tier",
    "capo_application_insights.types.workload_meta_data.WorkloadMetaData",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DetectedWorkload) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_application_insights.types.tier
        import capo_application_insights.types.workload_meta_data

        out[capo_application_insights.types.tier.serialize_aws_json_1_1(key)] = (
            capo_application_insights.types.workload_meta_data.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectedWorkload:
    out: DetectedWorkload = {}
    for key, value in data.items():
        import capo_application_insights.types.tier

        if value is None:
            continue
        import capo_application_insights.types.workload_meta_data

        out[capo_application_insights.types.tier.deserialize_aws_json_1_1(key)] = (
            capo_application_insights.types.workload_meta_data.deserialize_aws_json_1_1(
                value
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: DetectedWorkload) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_application_insights.types.tier
        import capo_application_insights.types.workload_meta_data

        out[capo_application_insights.types.tier.serialize_cbor(key)] = (
            capo_application_insights.types.workload_meta_data.serialize_cbor(value)
        )
    return out


def deserialize_cbor(data: dict) -> DetectedWorkload:
    out: DetectedWorkload = {}
    for key, value in data.items():
        import capo_application_insights.types.tier

        if value is None:
            continue
        import capo_application_insights.types.workload_meta_data

        out[capo_application_insights.types.tier.deserialize_cbor(key)] = (
            capo_application_insights.types.workload_meta_data.deserialize_cbor(value)
        )
    return out
