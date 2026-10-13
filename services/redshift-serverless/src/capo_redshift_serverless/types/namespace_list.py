"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#NamespaceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace

NamespaceList: TypeAlias = list["capo_redshift_serverless.types.namespace.Namespace"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceList) -> list:
    import capo_redshift_serverless.types.namespace

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types.namespace.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NamespaceList:
    import capo_redshift_serverless.types.namespace

    out: NamespaceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_redshift_serverless.types.namespace.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: NamespaceList) -> list[Any]:
    import capo_redshift_serverless.types.namespace

    return [
        capo_redshift_serverless.types.namespace.redact_sensitive(item)
        for item in value
    ]
