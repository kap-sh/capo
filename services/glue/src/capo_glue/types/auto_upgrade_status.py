"""Generated from Smithy shape ``com.amazonaws.glue#AutoUpgradeStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The current phase of the auto-upgrade lifecycle for a job configured with <code>GlueVersion=auto</code>.</p>"""
AutoUpgradeStatus: TypeAlias = Literal[
    "OBSERVING",
    "UPGRADING",
    "UPGRADE_SUCCEEDED",
    "UPGRADE_FAILED",
    "STOPPED",
    "WAITING_FOR_CONSENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoUpgradeStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoUpgradeStatus:
    return cast(AutoUpgradeStatus, data)
