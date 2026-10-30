"""Stand-ins for union variants and events this client doesn't know about.

A service may add a union member or an event after the client was generated.
Smithy asks clients not to fail on those, so deserialization returns one of
these instead of raising.

Both are one more variant of the union, keyed by ``$unknown``: a Smithy member
name can't contain ``$``, so the key never collides with a real member, and
``"$unknown" in value`` narrows like any other variant check.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .._protocol.eventstream import Message


class UnknownUnionMemberValue(TypedDict, closed=True):
    """What is known about a union variant this client has no member for."""

    name: str
    """The variant's name on the wire."""


class UnknownEventValue(TypedDict, closed=True):
    """What is known about an event whose ``:event-type`` this client doesn't know."""

    name: str
    """The event's ``:event-type`` header."""

    message: Message
    """The raw message, headers and undecoded payload."""


UnknownUnionMember = TypedDict(
    "UnknownUnionMember", {"$unknown": UnknownUnionMemberValue}, closed=True
)
"""A union variant the service sent that this client has no member for."""

UnknownEvent = TypedDict("UnknownEvent", {"$unknown": UnknownEventValue}, closed=True)
"""An event-stream event whose ``:event-type`` this client doesn't know."""


__all__ = [
    "UnknownEvent",
    "UnknownEventValue",
    "UnknownUnionMember",
    "UnknownUnionMemberValue",
]
