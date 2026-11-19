"""Generated from Smithy shape ``com.amazonaws.interconnect#Bandwidths``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.bandwidth_list


class Bandwidths(TypedDict, closed=True):
    available: NotRequired["capo_interconnect.types.bandwidth_list.BandwidthList"]
    """<p>The list of currently available bandwidths.</p>"""
    supported: NotRequired["capo_interconnect.types.bandwidth_list.BandwidthList"]
    """<p>The list of all bandwidths that this environment plans to support</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Bandwidths) -> dict:
    out: dict = {}
    if "available" in value:
        import capo_interconnect.types.bandwidth_list

        out["available"] = (
            capo_interconnect.types.bandwidth_list.serialize_aws_json_1_0(
                value["available"]
            )
        )
    if "supported" in value:
        import capo_interconnect.types.bandwidth_list

        out["supported"] = (
            capo_interconnect.types.bandwidth_list.serialize_aws_json_1_0(
                value["supported"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Bandwidths:
    out: Bandwidths = {}  # type: ignore[typeddict-item]
    if data.get("available") is not None:
        import capo_interconnect.types.bandwidth_list

        out["available"] = (
            capo_interconnect.types.bandwidth_list.deserialize_aws_json_1_0(
                data["available"]
            )
        )
    if data.get("supported") is not None:
        import capo_interconnect.types.bandwidth_list

        out["supported"] = (
            capo_interconnect.types.bandwidth_list.deserialize_aws_json_1_0(
                data["supported"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Bandwidths) -> dict:
    out: dict = {}
    if "available" in value:
        import capo_interconnect.types.bandwidth_list

        out["available"] = capo_interconnect.types.bandwidth_list.serialize_cbor(
            value["available"]
        )
    if "supported" in value:
        import capo_interconnect.types.bandwidth_list

        out["supported"] = capo_interconnect.types.bandwidth_list.serialize_cbor(
            value["supported"]
        )
    return out


def deserialize_cbor(data: dict) -> Bandwidths:
    out: Bandwidths = {}  # type: ignore[typeddict-item]
    if data.get("available") is not None:
        import capo_interconnect.types.bandwidth_list

        out["available"] = capo_interconnect.types.bandwidth_list.deserialize_cbor(
            data["available"]
        )
    if data.get("supported") is not None:
        import capo_interconnect.types.bandwidth_list

        out["supported"] = capo_interconnect.types.bandwidth_list.deserialize_cbor(
            data["supported"]
        )
    return out
