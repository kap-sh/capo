"""Generated from Smithy shape ``com.amazonaws.abusesignal#ReportSubmissionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Enumerates the processing states of a submitted abuse report. The reporter-facing lifecycle consists of <code>QUEUED</code>, <code>PROCESSING</code>, and <code>COMPLETED</code>:</p> <ul> <li> <p> <code>QUEUED</code> – The report has been received and queued for processing.</p> </li> <li> <p> <code>PROCESSING</code> – The report has been received and is being processed. Poll for this status to confirm that the report was received.</p> </li> <li> <p> <code>COMPLETED</code> – Downstream resolution is finished. A report in this state carries a <code>reasonCode</code> that describes the outcome. The time to reach <code>COMPLETED</code> may vary and can take up to several days depending on the scope and complexity of the suspected abuse.</p> </li> </ul>"""
ReportSubmissionStatus: TypeAlias = Literal[
    "QUEUED",
    "PROCESSING",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportSubmissionStatus) -> str:
    return value


def deserialize_json(data: str) -> ReportSubmissionStatus:
    return cast(ReportSubmissionStatus, data)
