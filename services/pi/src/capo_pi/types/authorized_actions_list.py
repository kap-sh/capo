"""Generated from Smithy shape ``com.amazonaws.pi#AuthorizedActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.fine_grained_action

AuthorizedActionsList: TypeAlias = list[
    "capo_pi.types.fine_grained_action.FineGrainedAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizedActionsList) -> list:
    import capo_pi.types.fine_grained_action

    out: list = []
    for item in value:
        out.append(capo_pi.types.fine_grained_action.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AuthorizedActionsList:
    import capo_pi.types.fine_grained_action

    out: AuthorizedActionsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.fine_grained_action.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AuthorizedActionsList) -> list:
    import capo_pi.types.fine_grained_action

    out: list = []
    for item in value:
        out.append(capo_pi.types.fine_grained_action.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AuthorizedActionsList:
    import capo_pi.types.fine_grained_action

    out: AuthorizedActionsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.fine_grained_action.deserialize_cbor(item))
    return out
