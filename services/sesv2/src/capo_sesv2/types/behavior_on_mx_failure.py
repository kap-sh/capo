"""Generated from Smithy shape ``com.amazonaws.sesv2#BehaviorOnMxFailure``."""

from typing import Literal, TypeAlias, cast

"""<p>The action to take if the required MX record can't be found when you send an email. When you set this value to <code>USE_DEFAULT_VALUE</code>, the mail is sent using <i>amazonses.com</i> as the MAIL FROM domain. When you set this value to <code>REJECT_MESSAGE</code>, the Amazon SES API v2 returns a <code>MailFromDomainNotVerifiedException</code> error, and doesn't attempt to deliver the email.</p> <p>These behaviors are taken when the custom MAIL FROM domain configuration is in the <code>PENDING</code>, <code>FAILED</code>, and <code>TEMPORARY_FAILURE</code> states.</p>"""
BehaviorOnMxFailure: TypeAlias = Literal[
    "USE_DEFAULT_VALUE",
    "REJECT_MESSAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: BehaviorOnMxFailure) -> str:
    return value


def deserialize_json(data: str) -> BehaviorOnMxFailure:
    return cast(BehaviorOnMxFailure, data)
