"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSPICECapacityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.purchase_mode


class UpdateSPICECapacityConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the SPICE configuration that you want to update.</p>"""
    purchase_mode: "capo_quicksight.types.purchase_mode.PurchaseMode"
    """<p>Determines how SPICE capacity can be purchased. The following options are available. </p> <ul> <li> <p> <code>MANUAL</code>: SPICE capacity can only be purchased manually.</p> </li> <li> <p> <code>AUTO_PURCHASE</code>: Extra SPICE capacity is automatically purchased on your behalf as needed. SPICE capacity can also be purchased manually with this option.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSPICECapacityConfigurationRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.purchase_mode

    out["PurchaseMode"] = capo_quicksight.types.purchase_mode.serialize_json(
        value["purchase_mode"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSPICECapacityConfigurationRequest:
    out: UpdateSPICECapacityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("PurchaseMode") is not None:
        import capo_quicksight.types.purchase_mode

        out["purchase_mode"] = capo_quicksight.types.purchase_mode.deserialize_json(
            data["PurchaseMode"]
        )
    else:
        import typing

        out["purchase_mode"] = typing.cast(
            "capo_quicksight.types.purchase_mode.PurchaseMode", ""
        )
    return out
