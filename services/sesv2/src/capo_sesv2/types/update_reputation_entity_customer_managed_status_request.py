"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateReputationEntityCustomerManagedStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.reputation_entity_reference
    import capo_sesv2.types.reputation_entity_type
    import capo_sesv2.types.sending_status


class UpdateReputationEntityCustomerManagedStatusRequest(TypedDict, closed=True):
    reputation_entity_type: (
        "capo_sesv2.types.reputation_entity_type.ReputationEntityType"
    )
    """<p>The type of reputation entity. Currently, only <code>RESOURCE</code> type entities are supported.</p>"""
    reputation_entity_reference: (
        "capo_sesv2.types.reputation_entity_reference.ReputationEntityReference"
    )
    """<p>The unique identifier for the reputation entity. For resource-type entities, this is the Amazon Resource Name (ARN) of the resource.</p>"""
    sending_status: "capo_sesv2.types.sending_status.SendingStatus"
    """<p>The new customer-managed sending status for the reputation entity. This can be one of the following:</p> <ul> <li> <p> <code>ENABLED</code> – Allow sending for this entity.</p> </li> <li> <p> <code>DISABLED</code> – Prevent sending for this entity.</p> </li> <li> <p> <code>REINSTATED</code> – Allow sending even if there are active reputation findings.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReputationEntityCustomerManagedStatusRequest) -> dict:
    out: dict = {}
    import capo_sesv2.types.sending_status

    out["SendingStatus"] = capo_sesv2.types.sending_status.serialize_json(
        value["sending_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateReputationEntityCustomerManagedStatusRequest:
    out: UpdateReputationEntityCustomerManagedStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("SendingStatus") is not None:
        import capo_sesv2.types.sending_status

        out["sending_status"] = capo_sesv2.types.sending_status.deserialize_json(
            data["SendingStatus"]
        )
    else:
        import typing

        out["sending_status"] = typing.cast(
            "capo_sesv2.types.sending_status.SendingStatus", ""
        )
    return out
