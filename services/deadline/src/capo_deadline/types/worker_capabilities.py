"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.worker_amount_capability_list
    import capo_deadline.types.worker_attribute_capability_list


class WorkerCapabilities(TypedDict, closed=True):
    amounts: (
        "capo_deadline.types.worker_amount_capability_list.WorkerAmountCapabilityList"
    )
    """<p>The worker capabilities amounts on a list of worker capabilities.</p>"""
    attributes: "capo_deadline.types.worker_attribute_capability_list.WorkerAttributeCapabilityList"
    """<p>The worker attribute capabilities in the list of attribute capabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerCapabilities) -> dict:
    out: dict = {}
    import capo_deadline.types.worker_amount_capability_list

    out["amounts"] = capo_deadline.types.worker_amount_capability_list.serialize_json(
        value["amounts"]
    )
    import capo_deadline.types.worker_attribute_capability_list

    out["attributes"] = (
        capo_deadline.types.worker_attribute_capability_list.serialize_json(
            value["attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> WorkerCapabilities:
    out: WorkerCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("amounts") is not None:
        import capo_deadline.types.worker_amount_capability_list

        out["amounts"] = (
            capo_deadline.types.worker_amount_capability_list.deserialize_json(
                data["amounts"]
            )
        )
    else:
        out["amounts"] = []
    if data.get("attributes") is not None:
        import capo_deadline.types.worker_attribute_capability_list

        out["attributes"] = (
            capo_deadline.types.worker_attribute_capability_list.deserialize_json(
                data["attributes"]
            )
        )
    else:
        out["attributes"] = []
    return out
