"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ShareError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.error
    import capo_service_catalog.types.message
    import capo_service_catalog.types.namespaces


class ShareError(TypedDict, closed=True):
    accounts: NotRequired["capo_service_catalog.types.namespaces.Namespaces"]
    """<p>List of accounts impacted by the error.</p>"""
    message: NotRequired["capo_service_catalog.types.message.Message"]
    """<p>Information about the error.</p>"""
    error: NotRequired["capo_service_catalog.types.error.Error"]
    """<p>Error type that happened when processing the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareError) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_service_catalog.types.namespaces

        out["Accounts"] = capo_service_catalog.types.namespaces.serialize_aws_json_1_1(
            value["accounts"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "error" in value:
        out["Error"] = value["error"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ShareError:
    out: ShareError = {}  # type: ignore[typeddict-item]
    if data.get("Accounts") is not None:
        import capo_service_catalog.types.namespaces

        out["accounts"] = (
            capo_service_catalog.types.namespaces.deserialize_aws_json_1_1(
                data["Accounts"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Error") is not None:
        out["error"] = data["Error"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ShareError) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_service_catalog.types.namespaces

        out["Accounts"] = capo_service_catalog.types.namespaces.serialize_cbor(
            value["accounts"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "error" in value:
        out["Error"] = value["error"]
    return out


def deserialize_cbor(data: dict) -> ShareError:
    out: ShareError = {}  # type: ignore[typeddict-item]
    if data.get("Accounts") is not None:
        import capo_service_catalog.types.namespaces

        out["accounts"] = capo_service_catalog.types.namespaces.deserialize_cbor(
            data["Accounts"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Error") is not None:
        out["error"] = data["Error"]
    return out
