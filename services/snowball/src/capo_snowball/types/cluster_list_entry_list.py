"""Generated from Smithy shape ``com.amazonaws.snowball#ClusterListEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.cluster_list_entry

ClusterListEntryList: TypeAlias = list[
    "capo_snowball.types.cluster_list_entry.ClusterListEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterListEntryList) -> list:
    import capo_snowball.types.cluster_list_entry

    out: list = []
    for item in value:
        out.append(capo_snowball.types.cluster_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterListEntryList:
    import capo_snowball.types.cluster_list_entry

    out: ClusterListEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_snowball.types.cluster_list_entry.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClusterListEntryList) -> list:
    import capo_snowball.types.cluster_list_entry

    out: list = []
    for item in value:
        out.append(capo_snowball.types.cluster_list_entry.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ClusterListEntryList:
    import capo_snowball.types.cluster_list_entry

    out: ClusterListEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.cluster_list_entry.deserialize_cbor(item))
    return out
