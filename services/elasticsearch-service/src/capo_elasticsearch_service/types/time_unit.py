"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#TimeUnit``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the unit of a maintenance schedule duration. Valid value is HOUR. See the <a href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html" target="_blank">Developer Guide</a> for more information.</p>"""
TimeUnit: TypeAlias = Literal["HOURS",]


# --- restJson1 ser/de ---
def serialize_json(value: TimeUnit) -> str:
    return value


def deserialize_json(data: str) -> TimeUnit:
    return cast(TimeUnit, data)
