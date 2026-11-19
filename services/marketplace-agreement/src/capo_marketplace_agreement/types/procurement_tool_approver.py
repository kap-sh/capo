"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ProcurementToolApprover``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.approver_name


class ProcurementToolApprover(TypedDict, closed=True):
    name: "capo_marketplace_agreement.types.approver_name.ApproverName"
    """<p>The name of the procurement system.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementToolApprover) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProcurementToolApprover:
    out: ProcurementToolApprover = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProcurementToolApprover) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> ProcurementToolApprover:
    out: ProcurementToolApprover = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out


def redact_sensitive(value: ProcurementToolApprover) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
