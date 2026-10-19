"""Generated from Smithy shape ``com.amazonaws.sns#ConfirmSubscriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.authenticate_on_unsubscribe
    import capo_sns.types.token
    import capo_sns.types.topic_arn


class ConfirmSubscriptionInput(TypedDict, closed=True):
    topic_arn: "capo_sns.types.topic_arn.topicARN"
    """<p>The ARN of the topic for which you wish to confirm a subscription.</p>"""
    token: "capo_sns.types.token.token"
    """<p>Short-lived token sent to an endpoint during the <code>Subscribe</code> action.</p>"""
    authenticate_on_unsubscribe: NotRequired[
        "capo_sns.types.authenticate_on_unsubscribe.authenticateOnUnsubscribe"
    ]
    """<p>Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter is <code>true</code> and the request has an Amazon Web Services signature, then only the topic owner and the subscription owner can unsubscribe the endpoint. The unsubscribe action requires Amazon Web Services authentication. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfirmSubscriptionInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    pairs.append((f"{key_prefix}Token", str(value["token"])))
    if "authenticate_on_unsubscribe" in value:
        pairs.append(
            (
                f"{key_prefix}AuthenticateOnUnsubscribe",
                str(value["authenticate_on_unsubscribe"]),
            )
        )


def deserialize_query(el: Element) -> ConfirmSubscriptionInput:
    out: ConfirmSubscriptionInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        out["topic_arn"] = ""
    child_token = el.find("Token")
    if child_token is not None:
        out["token"] = str(child_token.text or "")
    else:
        out["token"] = ""
    child_authenticate_on_unsubscribe = el.find("AuthenticateOnUnsubscribe")
    if child_authenticate_on_unsubscribe is not None:
        out["authenticate_on_unsubscribe"] = str(
            child_authenticate_on_unsubscribe.text or ""
        )
    return out
