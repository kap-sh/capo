"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DeadLetterQueueArn``."""

from typing import TypeAlias

"""The ARN of the destination that receives events that could not be delivered. An Amazon SQS queue is the supported destination. The queue-name grammar mirrors SQS's own rule: 1-80 chars of [A-Za-z0-9_-], where a FIFO name's ".fifo" suffix counts toward the 80 (so a FIFO base name is at most 75 chars). Shared: both the subscriber's and the EventSource's OnFailureConfiguration point at it."""
DeadLetterQueueArn: TypeAlias = str
