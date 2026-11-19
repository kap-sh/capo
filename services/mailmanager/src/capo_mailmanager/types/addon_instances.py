"""Generated from Smithy shape ``com.amazonaws.mailmanager#AddonInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.addon_instance

AddonInstances: TypeAlias = list["capo_mailmanager.types.addon_instance.AddonInstance"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddonInstances) -> list:
    import capo_mailmanager.types.addon_instance

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.addon_instance.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AddonInstances:
    import capo_mailmanager.types.addon_instance

    out: AddonInstances = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.addon_instance.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AddonInstances) -> list:
    import capo_mailmanager.types.addon_instance

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.addon_instance.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AddonInstances:
    import capo_mailmanager.types.addon_instance

    out: AddonInstances = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.addon_instance.deserialize_cbor(item))
    return out
