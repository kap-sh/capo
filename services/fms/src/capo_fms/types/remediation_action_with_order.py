"""Generated from Smithy shape ``com.amazonaws.fms#RemediationActionWithOrder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.basic_integer
    import capo_fms.types.remediation_action


class RemediationActionWithOrder(TypedDict, closed=True):
    remediation_action: NotRequired[
        "capo_fms.types.remediation_action.RemediationAction"
    ]
    """<p>Information about an action you can take to remediate a violation.</p>"""
    order: "capo_fms.types.basic_integer.BasicInteger"
    """<p>The order of the remediation actions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationActionWithOrder) -> dict:
    out: dict = {}
    if "remediation_action" in value:
        import capo_fms.types.remediation_action

        out["RemediationAction"] = (
            capo_fms.types.remediation_action.serialize_aws_json_1_1(
                value["remediation_action"]
            )
        )
    out["Order"] = value.get("order", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationActionWithOrder:
    out: RemediationActionWithOrder = {}  # type: ignore[typeddict-item]
    if data.get("RemediationAction") is not None:
        import capo_fms.types.remediation_action

        out["remediation_action"] = (
            capo_fms.types.remediation_action.deserialize_aws_json_1_1(
                data["RemediationAction"]
            )
        )
    if data.get("Order") is not None:
        out["order"] = data["Order"]
    else:
        out["order"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RemediationActionWithOrder) -> dict:
    out: dict = {}
    if "remediation_action" in value:
        import capo_fms.types.remediation_action

        out["RemediationAction"] = capo_fms.types.remediation_action.serialize_cbor(
            value["remediation_action"]
        )
    out["Order"] = value.get("order", 0)
    return out


def deserialize_cbor(data: dict) -> RemediationActionWithOrder:
    out: RemediationActionWithOrder = {}  # type: ignore[typeddict-item]
    if data.get("RemediationAction") is not None:
        import capo_fms.types.remediation_action

        out["remediation_action"] = capo_fms.types.remediation_action.deserialize_cbor(
            data["RemediationAction"]
        )
    if data.get("Order") is not None:
        out["order"] = data["Order"]
    else:
        out["order"] = 0
    return out
