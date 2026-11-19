"""Generated from Smithy shape ``com.amazonaws.shield#DescribeProtectionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_shield.errors import DeserializationError

if TYPE_CHECKING:
    import capo_shield.types.protection_group


class DescribeProtectionGroupResponse(TypedDict, closed=True):
    protection_group: "capo_shield.types.protection_group.ProtectionGroup"
    """<p>A grouping of protected resources that you and Shield Advanced can monitor as a collective. This resource grouping improves the accuracy of detection and reduces false positives. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProtectionGroupResponse) -> dict:
    out: dict = {}
    import capo_shield.types.protection_group

    out["ProtectionGroup"] = capo_shield.types.protection_group.serialize_aws_json_1_1(
        value["protection_group"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProtectionGroupResponse:
    out: DescribeProtectionGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionGroup") is not None:
        import capo_shield.types.protection_group

        out["protection_group"] = (
            capo_shield.types.protection_group.deserialize_aws_json_1_1(
                data["ProtectionGroup"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeProtectionGroupResponse.protection_group required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProtectionGroupResponse) -> dict:
    out: dict = {}
    import capo_shield.types.protection_group

    out["ProtectionGroup"] = capo_shield.types.protection_group.serialize_cbor(
        value["protection_group"]
    )
    return out


def deserialize_cbor(data: dict) -> DescribeProtectionGroupResponse:
    out: DescribeProtectionGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionGroup") is not None:
        import capo_shield.types.protection_group

        out["protection_group"] = capo_shield.types.protection_group.deserialize_cbor(
            data["ProtectionGroup"]
        )
    else:
        raise DeserializationError(
            "DescribeProtectionGroupResponse.protection_group required"
        )
    return out
