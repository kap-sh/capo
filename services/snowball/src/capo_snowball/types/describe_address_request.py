"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.address_id


class DescribeAddressRequest(TypedDict, closed=True):
    address_id: "capo_snowball.types.address_id.AddressId"
    """<p>The automatically generated ID for a specific address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAddressRequest) -> dict:
    out: dict = {}
    out["AddressId"] = value["address_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAddressRequest:
    out: DescribeAddressRequest = {}  # type: ignore[typeddict-item]
    if data.get("AddressId") is not None:
        out["address_id"] = data["AddressId"]
    else:
        out["address_id"] = ""
    return out
