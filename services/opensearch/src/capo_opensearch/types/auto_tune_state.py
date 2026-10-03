"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneState``."""

from typing import Literal, TypeAlias, cast

"""<p>The Auto-Tune state for the domain. For valid states see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html">Auto-Tune for Amazon OpenSearch Service</a>. </p>"""
AutoTuneState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLE_IN_PROGRESS",
    "DISABLE_IN_PROGRESS",
    "DISABLED_AND_ROLLBACK_SCHEDULED",
    "DISABLED_AND_ROLLBACK_IN_PROGRESS",
    "DISABLED_AND_ROLLBACK_COMPLETE",
    "DISABLED_AND_ROLLBACK_ERROR",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneState) -> str:
    return value


def deserialize_json(data: str) -> AutoTuneState:
    return cast(AutoTuneState, data)
