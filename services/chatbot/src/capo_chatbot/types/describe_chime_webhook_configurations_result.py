"""Generated from Smithy shape ``com.amazonaws.chatbot#DescribeChimeWebhookConfigurationsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.chime_webhook_configuration_list
    import capo_chatbot.types.pagination_token


class DescribeChimeWebhookConfigurationsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_chatbot.types.pagination_token.PaginationToken"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>"""
    webhook_configurations: NotRequired[
        "capo_chatbot.types.chime_webhook_configuration_list.ChimeWebhookConfigurationList"
    ]
    """<p>A list of Amazon Chime webhooks associated with the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChimeWebhookConfigurationsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "webhook_configurations" in value:
        import capo_chatbot.types.chime_webhook_configuration_list

        out["WebhookConfigurations"] = (
            capo_chatbot.types.chime_webhook_configuration_list.serialize_json(
                value["webhook_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeChimeWebhookConfigurationsResult:
    out: DescribeChimeWebhookConfigurationsResult = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("WebhookConfigurations") is not None:
        import capo_chatbot.types.chime_webhook_configuration_list

        out["webhook_configurations"] = (
            capo_chatbot.types.chime_webhook_configuration_list.deserialize_json(
                data["WebhookConfigurations"]
            )
        )
    return out


def redact_sensitive(value: DescribeChimeWebhookConfigurationsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "webhook_configurations" in value:
        import capo_chatbot.types.chime_webhook_configuration_list

        out["webhook_configurations"] = (
            capo_chatbot.types.chime_webhook_configuration_list.redact_sensitive(
                value["webhook_configurations"]
            )
        )
    return out
