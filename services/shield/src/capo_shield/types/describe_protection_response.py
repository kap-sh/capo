"""Generated from Smithy shape ``com.amazonaws.shield#DescribeProtectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.protection


class DescribeProtectionResponse(TypedDict, closed=True):
    protection: NotRequired["capo_shield.types.protection.Protection"]
    """<p>The <a>Protection</a> that you requested. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProtectionResponse) -> dict:
    out: dict = {}
    if "protection" in value:
        import capo_shield.types.protection

        out["Protection"] = capo_shield.types.protection.serialize_aws_json_1_1(
            value["protection"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProtectionResponse:
    out: DescribeProtectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Protection") is not None:
        import capo_shield.types.protection

        out["protection"] = capo_shield.types.protection.deserialize_aws_json_1_1(
            data["Protection"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProtectionResponse) -> dict:
    out: dict = {}
    if "protection" in value:
        import capo_shield.types.protection

        out["Protection"] = capo_shield.types.protection.serialize_cbor(
            value["protection"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeProtectionResponse:
    out: DescribeProtectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Protection") is not None:
        import capo_shield.types.protection

        out["protection"] = capo_shield.types.protection.deserialize_cbor(
            data["Protection"]
        )
    return out
