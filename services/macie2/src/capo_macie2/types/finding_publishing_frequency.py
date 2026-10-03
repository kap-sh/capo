"""Generated from Smithy shape ``com.amazonaws.macie2#FindingPublishingFrequency``."""

from typing import Literal, TypeAlias, cast

"""<p>The frequency with which Amazon Macie publishes updates to policy findings for an account. This includes publishing updates to Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events). For more information, see <a href="https://docs.aws.amazon.com/macie/latest/user/findings-monitor.html">Monitoring and processing findings</a> in the <i>Amazon Macie User Guide</i>. Valid values are:</p>"""
FindingPublishingFrequency: TypeAlias = Literal[
    "FIFTEEN_MINUTES",
    "ONE_HOUR",
    "SIX_HOURS",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingPublishingFrequency) -> str:
    return value


def deserialize_json(data: str) -> FindingPublishingFrequency:
    return cast(FindingPublishingFrequency, data)
