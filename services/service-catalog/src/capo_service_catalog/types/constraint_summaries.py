"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ConstraintSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.constraint_summary

ConstraintSummaries: TypeAlias = list[
    "capo_service_catalog.types.constraint_summary.ConstraintSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConstraintSummaries) -> list:
    import capo_service_catalog.types.constraint_summary

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.constraint_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConstraintSummaries:
    import capo_service_catalog.types.constraint_summary

    out: ConstraintSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.constraint_summary.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConstraintSummaries) -> list:
    import capo_service_catalog.types.constraint_summary

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.constraint_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ConstraintSummaries:
    import capo_service_catalog.types.constraint_summary

    out: ConstraintSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_service_catalog.types.constraint_summary.deserialize_cbor(item))
    return out
