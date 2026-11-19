"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RdsUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

"""<p>The ungraceful behavior for an Amazon RDS switchover read replica, that is, promote the read replica to a standalone primary.</p>"""
RdsUngracefulBehavior: TypeAlias = Literal["promoteReadReplica",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RdsUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RdsUngracefulBehavior:
    return cast(RdsUngracefulBehavior, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RdsUngracefulBehavior) -> str:
    return value


def deserialize_cbor(data: str) -> RdsUngracefulBehavior:
    return cast(RdsUngracefulBehavior, data)
