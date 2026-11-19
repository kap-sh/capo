"""Generated from Smithy shape ``com.amazonaws.pi#DimensionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.string


class DimensionDetail(TypedDict, closed=True):
    identifier: NotRequired["capo_pi.types.string.String"]
    """<p>The identifier of a dimension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionDetail) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DimensionDetail:
    out: DimensionDetail = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DimensionDetail) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    return out


def deserialize_cbor(data: dict) -> DimensionDetail:
    out: DimensionDetail = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    return out
