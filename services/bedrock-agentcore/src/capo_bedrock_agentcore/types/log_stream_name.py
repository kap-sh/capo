"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LogStreamName``."""

from typing import TypeAlias

"""A log stream name. The pattern is CloudWatch Logs' own log stream name pattern, which already admits the empty string; empty is the @default of members relaxed from @required and means "no log stream". No @length is applied, because CloudWatch's min of 1 would reject that default."""
LogStreamName: TypeAlias = str
