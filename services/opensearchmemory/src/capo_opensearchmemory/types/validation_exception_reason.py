"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

"""<p>Possible reasons a request failed validation. New values can be added, so treat an unknown value as a general validation failure.</p>"""
ValidationExceptionReason: TypeAlias = Literal[
    "disallowedQueryType",
    "nonFilterableField",
    "unknownField",
    "fieldIndexMismatch",
    "queryNestingTooDeep",
    "unboundedPattern",
    "queryBodyTooLarge",
    "malformedQueryBody",
    "invalidNextToken",
    "fieldValidationFailed",
    "unsupportedParameter",
    "unsupportedField",
    "other",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
