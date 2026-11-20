"""Generated from Smithy shape ``aws.iam#ArnOptions``."""

from typing_extensions import NotRequired, TypedDict


class ArnOptions(TypedDict, closed=True):
    cross_account: NotRequired["bool"]
    """Indicates whether the resource bound with the identifier allows cross-account ARN."""
    cross_region: NotRequired["bool"]
    """Indicates whether the resource bound with the identifier allows cross-region ARN."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArnOptions) -> dict:
    out: dict = {}
    if "cross_account" in value:
        out["crossAccount"] = value["cross_account"]
    if "cross_region" in value:
        out["crossRegion"] = value["cross_region"]
    return out


def deserialize_cbor(data: dict) -> ArnOptions:
    out: ArnOptions = {}  # type: ignore[typeddict-item]
    if data.get("crossAccount") is not None:
        out["cross_account"] = data["crossAccount"]
    if data.get("crossRegion") is not None:
        out["cross_region"] = data["crossRegion"]
    return out
