"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclCommonPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.network_acl_entry_set


class NetworkAclCommonPolicy(TypedDict, closed=True):
    network_acl_entry_set: "capo_fms.types.network_acl_entry_set.NetworkAclEntrySet"
    """<p>The definition of the first and last rules for the network ACL policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAclCommonPolicy) -> dict:
    out: dict = {}
    import capo_fms.types.network_acl_entry_set

    out["NetworkAclEntrySet"] = (
        capo_fms.types.network_acl_entry_set.serialize_aws_json_1_1(
            value["network_acl_entry_set"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkAclCommonPolicy:
    out: NetworkAclCommonPolicy = {}  # type: ignore[typeddict-item]
    if data.get("NetworkAclEntrySet") is not None:
        import capo_fms.types.network_acl_entry_set

        out["network_acl_entry_set"] = (
            capo_fms.types.network_acl_entry_set.deserialize_aws_json_1_1(
                data["NetworkAclEntrySet"]
            )
        )
    else:
        raise DeserializationError(
            "NetworkAclCommonPolicy.network_acl_entry_set required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkAclCommonPolicy) -> dict:
    out: dict = {}
    import capo_fms.types.network_acl_entry_set

    out["NetworkAclEntrySet"] = capo_fms.types.network_acl_entry_set.serialize_cbor(
        value["network_acl_entry_set"]
    )
    return out


def deserialize_cbor(data: dict) -> NetworkAclCommonPolicy:
    out: NetworkAclCommonPolicy = {}  # type: ignore[typeddict-item]
    if data.get("NetworkAclEntrySet") is not None:
        import capo_fms.types.network_acl_entry_set

        out["network_acl_entry_set"] = (
            capo_fms.types.network_acl_entry_set.deserialize_cbor(
                data["NetworkAclEntrySet"]
            )
        )
    else:
        raise DeserializationError(
            "NetworkAclCommonPolicy.network_acl_entry_set required"
        )
    return out
