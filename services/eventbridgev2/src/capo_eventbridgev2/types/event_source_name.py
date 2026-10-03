"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventSourceName``."""

from typing import TypeAlias

"""EventSource name. First character alphanumeric; the rest may add '.', '-', '_'. Names may not begin with the reserved "aws." prefix. The grammar matches the ARN local-name segment in EventSourceArn (event-sourcev2/<type>/<name>/<id>), mirroring EventBusName, so a name the ARN cannot represent cannot be created."""
EventSourceName: TypeAlias = str
