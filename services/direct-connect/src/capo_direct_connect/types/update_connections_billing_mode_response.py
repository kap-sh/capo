"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateConnectionsBillingModeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.billing_mode
    import capo_direct_connect.types.connection_list


class UpdateConnectionsBillingModeResponse(TypedDict, closed=True):
    billing_mode: NotRequired["capo_direct_connect.types.billing_mode.BillingMode"]
    """<p>The billing mode applied to the connections.</p>"""
    connections: NotRequired["capo_direct_connect.types.connection_list.ConnectionList"]
    """<p>The connections with the updated billing mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionsBillingModeResponse) -> dict:
    out: dict = {}
    if "billing_mode" in value:
        import capo_direct_connect.types.billing_mode

        out["billingMode"] = (
            capo_direct_connect.types.billing_mode.serialize_aws_json_1_1(
                value["billing_mode"]
            )
        )
    if "connections" in value:
        import capo_direct_connect.types.connection_list

        out["connections"] = (
            capo_direct_connect.types.connection_list.serialize_aws_json_1_1(
                value["connections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionsBillingModeResponse:
    out: UpdateConnectionsBillingModeResponse = {}  # type: ignore[typeddict-item]
    if data.get("billingMode") is not None:
        import capo_direct_connect.types.billing_mode

        out["billing_mode"] = (
            capo_direct_connect.types.billing_mode.deserialize_aws_json_1_1(
                data["billingMode"]
            )
        )
    if data.get("connections") is not None:
        import capo_direct_connect.types.connection_list

        out["connections"] = (
            capo_direct_connect.types.connection_list.deserialize_aws_json_1_1(
                data["connections"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateConnectionsBillingModeResponse) -> dict:
    out: dict = {}
    if "billing_mode" in value:
        import capo_direct_connect.types.billing_mode

        out["billingMode"] = capo_direct_connect.types.billing_mode.serialize_cbor(
            value["billing_mode"]
        )
    if "connections" in value:
        import capo_direct_connect.types.connection_list

        out["connections"] = capo_direct_connect.types.connection_list.serialize_cbor(
            value["connections"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdateConnectionsBillingModeResponse:
    out: UpdateConnectionsBillingModeResponse = {}  # type: ignore[typeddict-item]
    if data.get("billingMode") is not None:
        import capo_direct_connect.types.billing_mode

        out["billing_mode"] = capo_direct_connect.types.billing_mode.deserialize_cbor(
            data["billingMode"]
        )
    if data.get("connections") is not None:
        import capo_direct_connect.types.connection_list

        out["connections"] = capo_direct_connect.types.connection_list.deserialize_cbor(
            data["connections"]
        )
    return out
