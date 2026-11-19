"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Tier``."""

from typing import Literal, TypeAlias, cast

Tier: TypeAlias = Literal[
    "CUSTOM",
    "DEFAULT",
    "DOT_NET_CORE",
    "DOT_NET_WORKER",
    "DOT_NET_WEB_TIER",
    "DOT_NET_WEB",
    "SQL_SERVER",
    "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
    "MYSQL",
    "POSTGRESQL",
    "JAVA_JMX",
    "ORACLE",
    "SAP_HANA_MULTI_NODE",
    "SAP_HANA_SINGLE_NODE",
    "SAP_HANA_HIGH_AVAILABILITY",
    "SAP_ASE_SINGLE_NODE",
    "SAP_ASE_HIGH_AVAILABILITY",
    "SQL_SERVER_FAILOVER_CLUSTER_INSTANCE",
    "SHAREPOINT",
    "ACTIVE_DIRECTORY",
    "SAP_NETWEAVER_STANDARD",
    "SAP_NETWEAVER_DISTRIBUTED",
    "SAP_NETWEAVER_HIGH_AVAILABILITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Tier:
    return cast(Tier, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Tier) -> str:
    return value


def deserialize_cbor(data: str) -> Tier:
    return cast(Tier, data)
