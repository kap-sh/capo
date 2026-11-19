"""Generated from Smithy shape ``com.amazonaws.codedeploy#RevisionLocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.revision_location

RevisionLocationList: TypeAlias = list[
    "capo_codedeploy.types.revision_location.RevisionLocation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionLocationList) -> list:
    import capo_codedeploy.types.revision_location

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.revision_location.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RevisionLocationList:
    import capo_codedeploy.types.revision_location

    out: RevisionLocationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codedeploy.types.revision_location.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevisionLocationList) -> list:
    import capo_codedeploy.types.revision_location

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.revision_location.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RevisionLocationList:
    import capo_codedeploy.types.revision_location

    out: RevisionLocationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.revision_location.deserialize_cbor(item))
    return out
