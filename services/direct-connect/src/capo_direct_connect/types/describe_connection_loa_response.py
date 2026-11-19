"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeConnectionLoaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.loa


class DescribeConnectionLoaResponse(TypedDict, closed=True):
    loa: NotRequired["capo_direct_connect.types.loa.Loa"]
    """<p>The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionLoaResponse) -> dict:
    out: dict = {}
    if "loa" in value:
        import capo_direct_connect.types.loa

        out["loa"] = capo_direct_connect.types.loa.serialize_aws_json_1_1(value["loa"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionLoaResponse:
    out: DescribeConnectionLoaResponse = {}  # type: ignore[typeddict-item]
    if data.get("loa") is not None:
        import capo_direct_connect.types.loa

        out["loa"] = capo_direct_connect.types.loa.deserialize_aws_json_1_1(data["loa"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeConnectionLoaResponse) -> dict:
    out: dict = {}
    if "loa" in value:
        import capo_direct_connect.types.loa

        out["loa"] = capo_direct_connect.types.loa.serialize_cbor(value["loa"])
    return out


def deserialize_cbor(data: dict) -> DescribeConnectionLoaResponse:
    out: DescribeConnectionLoaResponse = {}  # type: ignore[typeddict-item]
    if data.get("loa") is not None:
        import capo_direct_connect.types.loa

        out["loa"] = capo_direct_connect.types.loa.deserialize_cbor(data["loa"])
    return out
