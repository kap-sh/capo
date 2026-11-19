"""Generated from Smithy shape ``com.amazonaws.dsql#MetricGroup``."""

from typing import Literal, TypeAlias, cast

"""<p>The name of an advanced monitoring metric group. Advanced monitoring collects detailed, query-level database metrics to help you analyze and resolve performance issues. You choose which metric groups to collect for each cluster.</p> <p>The following metric groups are available:</p> <dl> <dt>STATEMENT_STATISTICS</dt> <dd> <p>Shows which SQL statements run most often or take the most time. Collects execution count, execution time, and rows for each statement.</p> </dd> </dl>"""
MetricGroup: TypeAlias = Literal["STATEMENT_STATISTICS",]


# --- restJson1 ser/de ---
def serialize_json(value: MetricGroup) -> str:
    return value


def deserialize_json(data: str) -> MetricGroup:
    return cast(MetricGroup, data)
