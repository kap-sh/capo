"""Generated from Smithy shape ``aws.iam#IdentifierType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.arn_options
    import capo_partnercentral_marketing.types.id_options


class IdentifierType(TypedDict, closed=True):
    id: NotRequired["capo_partnercentral_marketing.types.id_options.IdOptions"]
    """When appears, this identifier allows ID type."""
    arn: NotRequired["capo_partnercentral_marketing.types.arn_options.ArnOptions"]
    """When appears, this identifier allows ARN type."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentifierType) -> dict:
    out: dict = {}
    if "id" in value:
        import capo_partnercentral_marketing.types.id_options

        out["id"] = capo_partnercentral_marketing.types.id_options.serialize_cbor(
            value["id"]
        )
    if "arn" in value:
        import capo_partnercentral_marketing.types.arn_options

        out["arn"] = capo_partnercentral_marketing.types.arn_options.serialize_cbor(
            value["arn"]
        )
    return out


def deserialize_cbor(data: dict) -> IdentifierType:
    out: IdentifierType = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        import capo_partnercentral_marketing.types.id_options

        out["id"] = capo_partnercentral_marketing.types.id_options.deserialize_cbor(
            data["id"]
        )
    if data.get("arn") is not None:
        import capo_partnercentral_marketing.types.arn_options

        out["arn"] = capo_partnercentral_marketing.types.arn_options.deserialize_cbor(
            data["arn"]
        )
    return out
