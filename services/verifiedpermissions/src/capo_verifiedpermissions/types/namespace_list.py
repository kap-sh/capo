"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#NamespaceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.namespace

NamespaceList: TypeAlias = list["capo_verifiedpermissions.types.namespace.Namespace"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NamespaceList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NamespaceList:
    return [item for item in data if item is not None]


def redact_sensitive(value: NamespaceList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
