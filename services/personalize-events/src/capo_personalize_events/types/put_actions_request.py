"""Generated from Smithy shape ``com.amazonaws.personalizeevents#PutActionsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_personalize_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize_events.types.action_list
    import capo_personalize_events.types.arn


class PutActionsRequest(TypedDict, closed=True):
    dataset_arn: "capo_personalize_events.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Actions dataset you are adding the action or actions to.</p>"""
    actions: "capo_personalize_events.types.action_list.ActionList"
    """<p>A list of action data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutActionsRequest) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    import capo_personalize_events.types.action_list

    out["actions"] = capo_personalize_events.types.action_list.serialize_json(
        value["actions"]
    )
    return out


def deserialize_json(data: dict) -> PutActionsRequest:
    out: PutActionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("PutActionsRequest.dataset_arn required")
    if data.get("actions") is not None:
        import capo_personalize_events.types.action_list

        out["actions"] = capo_personalize_events.types.action_list.deserialize_json(
            data["actions"]
        )
    else:
        raise DeserializationError("PutActionsRequest.actions required")
    return out


def redact_sensitive(value: PutActionsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "actions" in value:
        import capo_personalize_events.types.action_list

        out["actions"] = capo_personalize_events.types.action_list.redact_sensitive(
            value["actions"]
        )
    return out
