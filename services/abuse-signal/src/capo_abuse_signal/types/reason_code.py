"""Generated from Smithy shape ``com.amazonaws.abusesignal#ReasonCode``."""

from typing import Literal, TypeAlias, cast

"""<p>A code that explains the resolution outcome of an abuse report, surfaced to the reporter. This value is present only after a report reaches the terminal <code>COMPLETED</code> status; it is absent while the report is <code>QUEUED</code> or <code>PROCESSING</code>. The vocabulary is owned by the service and is append-only, so treat an unrecognized value as opaque rather than as an error.</p> <p>The following values are defined:</p> <ul> <li> <p> <code>ACTIONED</code> – Enforcement action was taken on the reported resource.</p> </li> <li> <p> <code>NOT_RESOLVABLE_TO_AWS</code> – The reported resource could not be attributed to Amazon Web Services.</p> </li> <li> <p> <code>REVIEWED_NO_AWS_ACTION</code> – The report was reviewed and no Amazon Web Services action was warranted.</p> </li> <li> <p> <code>CONTENT_DOWN_OR_INACCESSIBLE</code> – The reported content is already down or inaccessible, so no action was needed.</p> </li> <li> <p> <code>NEED_MORE_INFORMATION</code> – The report did not contain enough information to act on.</p> </li> </ul>"""
ReasonCode: TypeAlias = Literal[
    "ACTIONED",
    "NOT_RESOLVABLE_TO_AWS",
    "REVIEWED_NO_AWS_ACTION",
    "CONTENT_DOWN_OR_INACCESSIBLE",
    "NEED_MORE_INFORMATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReasonCode) -> str:
    return value


def deserialize_json(data: str) -> ReasonCode:
    return cast(ReasonCode, data)
