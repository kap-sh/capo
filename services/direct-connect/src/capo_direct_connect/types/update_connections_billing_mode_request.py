"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateConnectionsBillingModeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id_list
    import capo_direct_connect.types.request_billing_mode


class UpdateConnectionsBillingModeRequest(TypedDict, closed=True):
    connection_ids: "capo_direct_connect.types.connection_id_list.ConnectionIdList"
    """<p>The IDs of the connections to update. You can specify from 1 to 200 connections.</p>"""
    billing_mode: "capo_direct_connect.types.request_billing_mode.RequestBillingMode"
    """<p>The billing mode to apply to the specified connections. The valid values are <code>PayAsYouGo</code>, <code>FlatRateTier1</code>, <code>FlatRateTier2</code>, <code>FlatRateTier3</code>, <code>FlatRateTier4</code>, and <code>FlatRateTier5</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionsBillingModeRequest) -> dict:
    out: dict = {}
    import capo_direct_connect.types.connection_id_list

    out["connectionIds"] = (
        capo_direct_connect.types.connection_id_list.serialize_aws_json_1_1(
            value["connection_ids"]
        )
    )
    import capo_direct_connect.types.request_billing_mode

    out["billingMode"] = (
        capo_direct_connect.types.request_billing_mode.serialize_aws_json_1_1(
            value["billing_mode"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionsBillingModeRequest:
    out: UpdateConnectionsBillingModeRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionIds") is not None:
        import capo_direct_connect.types.connection_id_list

        out["connection_ids"] = (
            capo_direct_connect.types.connection_id_list.deserialize_aws_json_1_1(
                data["connectionIds"]
            )
        )
    else:
        out["connection_ids"] = []
    if data.get("billingMode") is not None:
        import capo_direct_connect.types.request_billing_mode

        out["billing_mode"] = (
            capo_direct_connect.types.request_billing_mode.deserialize_aws_json_1_1(
                data["billingMode"]
            )
        )
    else:
        import typing

        out["billing_mode"] = typing.cast(
            "capo_direct_connect.types.request_billing_mode.RequestBillingMode", ""
        )
    return out
