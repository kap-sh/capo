"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListWebhooksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.webhooks_list


class ListWebhooksOutput(TypedDict, closed=True):
    webhooks: "capo_devops_agent.types.webhooks_list.WebhooksList"
    """<p>The list of association webhooks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebhooksOutput) -> dict:
    out: dict = {}
    import capo_devops_agent.types.webhooks_list

    out["webhooks"] = capo_devops_agent.types.webhooks_list.serialize_json(
        value["webhooks"]
    )
    return out


def deserialize_json(data: dict) -> ListWebhooksOutput:
    out: ListWebhooksOutput = {}  # type: ignore[typeddict-item]
    if data.get("webhooks") is not None:
        import capo_devops_agent.types.webhooks_list

        out["webhooks"] = capo_devops_agent.types.webhooks_list.deserialize_json(
            data["webhooks"]
        )
    else:
        out["webhooks"] = []
    return out
