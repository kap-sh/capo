"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#BillingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.billing_mode


class BillingConfiguration(TypedDict, closed=True):
    billing_mode: "capo_workspaces_instances.types.billing_mode.BillingMode"
    """<p>Specifies the billing mode for WorkSpace Instances. MONTHLY provides fixed monthly rates for predictable budgeting, while HOURLY enables pay-per-second billing for actual usage.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingConfiguration) -> dict:
    out: dict = {}
    import capo_workspaces_instances.types.billing_mode

    out["BillingMode"] = (
        capo_workspaces_instances.types.billing_mode.serialize_aws_json_1_0(
            value["billing_mode"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingConfiguration:
    out: BillingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("BillingMode") is not None:
        import capo_workspaces_instances.types.billing_mode

        out["billing_mode"] = (
            capo_workspaces_instances.types.billing_mode.deserialize_aws_json_1_0(
                data["BillingMode"]
            )
        )
    else:
        import typing

        out["billing_mode"] = typing.cast(
            "capo_workspaces_instances.types.billing_mode.BillingMode", ""
        )
    return out
