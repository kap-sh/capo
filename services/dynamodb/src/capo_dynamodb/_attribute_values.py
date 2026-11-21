"""Plain Python values to DynamoDB AttributeValues and back.

DynamoDB tags every value with its type: ``{"S": "Ada"}``, ``{"N": "36"}``.
``marshal_item`` writes an item of plain Python values that way, and
``unmarshal_item`` reads one back.

A number comes back as an ``int`` when it is whole and as a ``Decimal``
otherwise. A ``float`` is refused, since it cannot hold every DynamoDB number
exactly.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from collections.abc import Set as AbstractSet
from decimal import Decimal
from typing import Any, TypeAlias, cast

from capo_dynamodb.types.attribute_value import AttributeValue

DynamoValue: TypeAlias = (
    str
    | int
    | Decimal
    | bytes
    | bool
    | None
    | list["DynamoValue"]
    | dict[str, "DynamoValue"]
    | set[str]
    | set[int | Decimal]
    | set[bytes]
)
"""A value as ``unmarshal`` returns it."""
DynamoValueLike: TypeAlias = (
    str
    | int
    | Decimal
    | bytes
    | bytearray
    | bool
    | None
    | Sequence["DynamoValueLike"]
    | Mapping[str, "DynamoValueLike"]
    | AbstractSet[str]
    | AbstractSet[int | Decimal]
    | AbstractSet[bytes]
)
"""A value ``marshal`` takes: any sequence, mapping or set, not only a list, dict or set."""


def marshal(value: DynamoValueLike) -> AttributeValue:
    """One Python value as a DynamoDB AttributeValue.

    Args:
        value: A str, int, Decimal, bytes, bool or None; a sequence or mapping of those; or a non-empty set of only strings, only numbers or only bytes.

    Raises:
        TypeError: For a float, a mixed set, or a type DynamoDB has none for.
        ValueError: For an empty set, or a Decimal that is NaN or infinite.

    Examples:
        A string

        >>> marshal("Ada")  # {"S": "Ada"}
        A set of numbers, sorted

        >>> marshal({3, 1})  # {"NS": ["1", "3"]}
    """
    match value:
        case bool():
            # before int, which bool is a subclass of
            return {"BOOL": value}
        case None:
            return {"NULL": True}
        case str():
            return {"S": value}
        case int() | Decimal():
            return {"N": _format_number(value)}
        case float():
            raise TypeError("float is lossy, use Decimal or int")
        case bytes() | bytearray():
            return {"B": bytes(value)}
        case Mapping():
            # ty narrows a Sequence that is also a Mapping to Mapping[object, object]
            return {"M": marshal_item(cast("Mapping[str, DynamoValueLike]", value))}
        case AbstractSet():
            return _marshal_set(value)
        case Sequence():
            # after str and bytes, which are sequences too
            return {"L": [marshal(v) for v in value]}
        case _:
            raise TypeError(f"unsupported type: {type(value).__name__}")


def _marshal_set(value: AbstractSet[Any]) -> AttributeValue:
    """A set as SS, NS or BS, sorted so the same set always makes the same request."""
    if not value:
        raise ValueError("DynamoDB does not allow empty sets")
    if all(isinstance(v, str) for v in value):
        return {"SS": sorted(value)}
    if all(isinstance(v, (int, Decimal)) and not isinstance(v, bool) for v in value):
        return {"NS": sorted(_format_number(v) for v in value)}
    if all(isinstance(v, bytes) for v in value):
        return {"BS": sorted(value)}
    raise TypeError("sets must contain only str, only numbers, or only bytes")


def _format_number(value: int | Decimal) -> str:
    """A number as DynamoDB spells it, which has no NaN or infinity."""
    if isinstance(value, Decimal) and not value.is_finite():
        raise ValueError(f"DynamoDB numbers must be finite, not {value}")
    return str(value)


def unmarshal(value: AttributeValue) -> DynamoValue:
    """One DynamoDB AttributeValue as a Python value.

    Args:
        value: An AttributeValue, as the client returns it.

    Raises:
        ValueError: For a dict that is not an AttributeValue.

    Examples:
        A whole number

        >>> unmarshal({"N": "36"})  # 36
        A fraction

        >>> unmarshal({"N": "0.5"})  # Decimal("0.5")
    """
    match value:
        case {"S": str(s)}:
            return s
        case {"N": str(n)}:
            return _parse_number(n)
        case {"B": bytes(b)}:
            return b
        case {"BOOL": bool(b)}:
            return b
        case {"NULL": True}:
            return None
        case {"L": list(items)}:
            return [unmarshal(v) for v in items]
        case {"M": dict(members)}:
            return {k: unmarshal(v) for k, v in members.items()}
        case {"SS": list(ss)}:
            return set(ss)
        case {"NS": list(ns)}:
            return {_parse_number(n) for n in ns}
        case {"BS": list(bs)}:
            return set(bs)
        case _:
            raise ValueError(f"not an AttributeValue: {value!r}")


def _parse_number(raw: str) -> int | Decimal:
    """An ``int`` for a whole number, a ``Decimal`` for any other."""
    return int(raw) if raw.lstrip("-").isdigit() else Decimal(raw)


def marshal_item(item: Mapping[str, DynamoValueLike]) -> dict[str, AttributeValue]:
    """An item of Python values as DynamoDB AttributeValues, ready for ``put_item``, a ``key`` or ``expression_attribute_values``.

    Args:
        item: Attribute names and their values, each one ``marshal`` takes.

    Examples:
        An item

        >>> marshal_item({"id": "u1", "age": 36})  # {"id": {"S": "u1"}, "age": {"N": "36"}}
    """
    return {k: marshal(v) for k, v in item.items()}


def unmarshal_item(item: Mapping[str, AttributeValue]) -> dict[str, DynamoValue]:
    """An item DynamoDB returned, from ``get_item``, ``query`` or ``scan``, as Python values.

    Args:
        item: Attribute names and their AttributeValues.

    Examples:
        An item

        >>> unmarshal_item({"id": {"S": "u1"}, "age": {"N": "36"}})  # {"id": "u1", "age": 36}
    """
    return {k: unmarshal(v) for k, v in item.items()}
