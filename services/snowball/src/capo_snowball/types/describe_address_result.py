"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeAddressResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.address


class DescribeAddressResult(TypedDict, closed=True):
    address: NotRequired["capo_snowball.types.address.Address"]
    """<p>The address that you want the Snow device(s) associated with a specific job to be shipped to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAddressResult) -> dict:
    out: dict = {}
    if "address" in value:
        import capo_snowball.types.address

        out["Address"] = capo_snowball.types.address.serialize_aws_json_1_1(
            value["address"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAddressResult:
    out: DescribeAddressResult = {}  # type: ignore[typeddict-item]
    if data.get("Address") is not None:
        import capo_snowball.types.address

        out["address"] = capo_snowball.types.address.deserialize_aws_json_1_1(
            data["Address"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAddressResult) -> dict:
    out: dict = {}
    if "address" in value:
        import capo_snowball.types.address

        out["Address"] = capo_snowball.types.address.serialize_cbor(value["address"])
    return out


def deserialize_cbor(data: dict) -> DescribeAddressResult:
    out: DescribeAddressResult = {}  # type: ignore[typeddict-item]
    if data.get("Address") is not None:
        import capo_snowball.types.address

        out["address"] = capo_snowball.types.address.deserialize_cbor(data["Address"])
    return out
