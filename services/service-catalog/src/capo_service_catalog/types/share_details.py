"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ShareDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.share_errors
    import capo_service_catalog.types.successful_shares


class ShareDetails(TypedDict, closed=True):
    successful_shares: NotRequired[
        "capo_service_catalog.types.successful_shares.SuccessfulShares"
    ]
    """<p>List of accounts for whom the operation succeeded.</p>"""
    share_errors: NotRequired["capo_service_catalog.types.share_errors.ShareErrors"]
    """<p>List of errors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareDetails) -> dict:
    out: dict = {}
    if "successful_shares" in value:
        import capo_service_catalog.types.successful_shares

        out["SuccessfulShares"] = (
            capo_service_catalog.types.successful_shares.serialize_aws_json_1_1(
                value["successful_shares"]
            )
        )
    if "share_errors" in value:
        import capo_service_catalog.types.share_errors

        out["ShareErrors"] = (
            capo_service_catalog.types.share_errors.serialize_aws_json_1_1(
                value["share_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShareDetails:
    out: ShareDetails = {}  # type: ignore[typeddict-item]
    if data.get("SuccessfulShares") is not None:
        import capo_service_catalog.types.successful_shares

        out["successful_shares"] = (
            capo_service_catalog.types.successful_shares.deserialize_aws_json_1_1(
                data["SuccessfulShares"]
            )
        )
    if data.get("ShareErrors") is not None:
        import capo_service_catalog.types.share_errors

        out["share_errors"] = (
            capo_service_catalog.types.share_errors.deserialize_aws_json_1_1(
                data["ShareErrors"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ShareDetails) -> dict:
    out: dict = {}
    if "successful_shares" in value:
        import capo_service_catalog.types.successful_shares

        out["SuccessfulShares"] = (
            capo_service_catalog.types.successful_shares.serialize_cbor(
                value["successful_shares"]
            )
        )
    if "share_errors" in value:
        import capo_service_catalog.types.share_errors

        out["ShareErrors"] = capo_service_catalog.types.share_errors.serialize_cbor(
            value["share_errors"]
        )
    return out


def deserialize_cbor(data: dict) -> ShareDetails:
    out: ShareDetails = {}  # type: ignore[typeddict-item]
    if data.get("SuccessfulShares") is not None:
        import capo_service_catalog.types.successful_shares

        out["successful_shares"] = (
            capo_service_catalog.types.successful_shares.deserialize_cbor(
                data["SuccessfulShares"]
            )
        )
    if data.get("ShareErrors") is not None:
        import capo_service_catalog.types.share_errors

        out["share_errors"] = capo_service_catalog.types.share_errors.deserialize_cbor(
            data["ShareErrors"]
        )
    return out
