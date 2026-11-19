"""Generated from Smithy shape ``com.amazonaws.sesv2#DeliverabilityTestStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a predictive inbox placement test. If the status is <code>IN_PROGRESS</code>, then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is <code>COMPLETED</code>, then the test is finished, and you can use the <code>GetDeliverabilityTestReport</code> operation to view the results of the test.</p>"""
DeliverabilityTestStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeliverabilityTestStatus) -> str:
    return value


def deserialize_json(data: str) -> DeliverabilityTestStatus:
    return cast(DeliverabilityTestStatus, data)
