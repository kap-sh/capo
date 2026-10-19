"""Stand-ins for union variants and events this client doesn't know about.

A service may add a union member or an event after the client was generated.
Smithy asks clients not to fail on those, so deserialization returns one of
these instead of raising.
"""

from __future__ import annotations

from dataclasses import dataclass

from .._protocol.eventstream import Message


@dataclass(frozen=True)
class UnknownUnionMember:
    """A union variant the service sent that this client has no member for."""

    name: str
    """The variant's name on the wire."""


@dataclass(frozen=True)
class UnknownEvent:
    """An event-stream event whose ``:event-type`` this client doesn't know."""

    event_type: str
    """The event's ``:event-type`` header."""

    message: Message
    """The raw message, headers and undecoded payload."""


__all__ = ["UnknownEvent", "UnknownUnionMember"]
