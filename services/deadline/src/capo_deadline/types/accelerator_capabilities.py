"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.accelerator_count_range
    import capo_deadline.types.accelerator_selections


class AcceleratorCapabilities(TypedDict, closed=True):
    selections: "capo_deadline.types.accelerator_selections.AcceleratorSelections"
    """<p>A list of accelerator capabilities requested for this fleet. Only Amazon Elastic Compute Cloud instances that provide these capabilities will be used. For example, if you specify both L4 and T4 chips, Amazon Web Services Deadline Cloud will use Amazon EC2 instances that have either the L4 or the T4 chip installed.</p> <important> <ul> <li> <p>You must specify at least one accelerator selection.</p> </li> <li> <p>You cannot specify the same accelerator name multiple times in the selections list.</p> </li> <li> <p>All accelerators in the selections must use the same runtime version.</p> </li> </ul> </important>"""
    count: NotRequired[
        "capo_deadline.types.accelerator_count_range.AcceleratorCountRange"
    ]
    """<p>The number of GPU accelerators specified for worker hosts in this fleet.</p> <important> <p>You must specify either <code>acceleratorCapabilities.count.max</code> or <code>allowedInstanceTypes</code> when using accelerator capabilities. If you don't specify a maximum count, Amazon Web Services Deadline Cloud uses the instance types you specify in <code>allowedInstanceTypes</code> to determine the maximum number of accelerators.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorCapabilities) -> dict:
    out: dict = {}
    import capo_deadline.types.accelerator_selections

    out["selections"] = capo_deadline.types.accelerator_selections.serialize_json(
        value["selections"]
    )
    if "count" in value:
        import capo_deadline.types.accelerator_count_range

        out["count"] = capo_deadline.types.accelerator_count_range.serialize_json(
            value["count"]
        )
    return out


def deserialize_json(data: dict) -> AcceleratorCapabilities:
    out: AcceleratorCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("selections") is not None:
        import capo_deadline.types.accelerator_selections

        out["selections"] = capo_deadline.types.accelerator_selections.deserialize_json(
            data["selections"]
        )
    else:
        out["selections"] = []
    if data.get("count") is not None:
        import capo_deadline.types.accelerator_count_range

        out["count"] = capo_deadline.types.accelerator_count_range.deserialize_json(
            data["count"]
        )
    return out
