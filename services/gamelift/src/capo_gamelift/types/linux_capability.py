"""Generated from Smithy shape ``com.amazonaws.gamelift#LinuxCapability``."""

from typing import Literal, TypeAlias, cast

LinuxCapability: TypeAlias = Literal[
    "AUDIT_CONTROL",
    "AUDIT_WRITE",
    "BLOCK_SUSPEND",
    "CHOWN",
    "DAC_OVERRIDE",
    "DAC_READ_SEARCH",
    "FOWNER",
    "FSETID",
    "IPC_LOCK",
    "IPC_OWNER",
    "KILL",
    "LEASE",
    "LINUX_IMMUTABLE",
    "MAC_ADMIN",
    "MAC_OVERRIDE",
    "MKNOD",
    "NET_ADMIN",
    "NET_BIND_SERVICE",
    "NET_BROADCAST",
    "NET_RAW",
    "SETFCAP",
    "SETGID",
    "SETPCAP",
    "SETUID",
    "SYS_ADMIN",
    "SYS_BOOT",
    "SYS_CHROOT",
    "SYS_MODULE",
    "SYS_NICE",
    "SYS_PACCT",
    "SYS_PTRACE",
    "SYS_RAWIO",
    "SYS_RESOURCE",
    "SYS_TIME",
    "SYS_TTY_CONFIG",
    "SYSLOG",
    "WAKE_ALARM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LinuxCapability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LinuxCapability:
    return cast(LinuxCapability, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LinuxCapability) -> str:
    return value


def deserialize_cbor(data: str) -> LinuxCapability:
    return cast(LinuxCapability, data)
