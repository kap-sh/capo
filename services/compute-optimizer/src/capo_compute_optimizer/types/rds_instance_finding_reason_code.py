"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSInstanceFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

RDSInstanceFindingReasonCode: TypeAlias = Literal[
    "CPUOverprovisioned",
    "NetworkBandwidthOverprovisioned",
    "EBSIOPSOverprovisioned",
    "EBSIOPSUnderprovisioned",
    "EBSThroughputOverprovisioned",
    "CPUUnderprovisioned",
    "NetworkBandwidthUnderprovisioned",
    "EBSThroughputUnderprovisioned",
    "NewGenerationDBInstanceClassAvailable",
    "NewEngineVersionAvailable",
    "DBClusterWriterUnderprovisioned",
    "MemoryUnderprovisioned",
    "InstanceStorageReadIOPSUnderprovisioned",
    "InstanceStorageWriteIOPSUnderprovisioned",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSInstanceFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSInstanceFindingReasonCode:
    return cast(RDSInstanceFindingReasonCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSInstanceFindingReasonCode) -> str:
    return value


def deserialize_cbor(data: str) -> RDSInstanceFindingReasonCode:
    return cast(RDSInstanceFindingReasonCode, data)
