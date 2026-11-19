"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeAddressesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.address_list
    import capo_snowball.types.string


class DescribeAddressesResult(TypedDict, closed=True):
    addresses: NotRequired["capo_snowball.types.address_list.AddressList"]
    """<p>The Snow device shipping addresses that were created for this account.</p>"""
    next_token: NotRequired["capo_snowball.types.string.String"]
    """<p>HTTP requests are stateless. If you use the automatically generated <code>NextToken</code> value in your next <code>DescribeAddresses</code> call, your list of returned addresses will start from this point in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAddressesResult) -> dict:
    out: dict = {}
    if "addresses" in value:
        import capo_snowball.types.address_list

        out["Addresses"] = capo_snowball.types.address_list.serialize_aws_json_1_1(
            value["addresses"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAddressesResult:
    out: DescribeAddressesResult = {}  # type: ignore[typeddict-item]
    if data.get("Addresses") is not None:
        import capo_snowball.types.address_list

        out["addresses"] = capo_snowball.types.address_list.deserialize_aws_json_1_1(
            data["Addresses"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAddressesResult) -> dict:
    out: dict = {}
    if "addresses" in value:
        import capo_snowball.types.address_list

        out["Addresses"] = capo_snowball.types.address_list.serialize_cbor(
            value["addresses"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAddressesResult:
    out: DescribeAddressesResult = {}  # type: ignore[typeddict-item]
    if data.get("Addresses") is not None:
        import capo_snowball.types.address_list

        out["addresses"] = capo_snowball.types.address_list.deserialize_cbor(
            data["Addresses"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
