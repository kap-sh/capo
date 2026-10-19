"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.service_owned_arn
    import capo_resiliencehubv2.types.test_id


class TestSummary(TypedDict, closed=True):
    test_id: "capo_resiliencehubv2.types.test_id.TestId"
    """<p>The unique identifier of the test.</p>"""
    test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn"
    """<p>The ARN of the test template the test was created from.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test belongs to.</p>"""
    total_test_runs: "int"
    """<p>The total number of runs of the test.</p>"""
    successful_test_runs: "int"
    """<p>The number of successful runs of the test.</p>"""
    creation_time: "datetime.datetime"
    """<p>The timestamp when the test was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSummary) -> dict:
    out: dict = {}
    out["testId"] = value["test_id"]
    out["testTemplateArn"] = value["test_template_arn"]
    out["serviceArn"] = value["service_arn"]
    out["totalTestRuns"] = value["total_test_runs"]
    out["successfulTestRuns"] = value["successful_test_runs"]
    import capo_resiliencehubv2.types._prelude.timestamp

    out["creationTime"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> TestSummary:
    out: TestSummary = {}  # type: ignore[typeddict-item]
    if data.get("testId") is not None:
        out["test_id"] = data["testId"]
    else:
        out["test_id"] = ""
    if data.get("testTemplateArn") is not None:
        out["test_template_arn"] = data["testTemplateArn"]
    else:
        out["test_template_arn"] = ""
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("totalTestRuns") is not None:
        out["total_test_runs"] = data["totalTestRuns"]
    else:
        out["total_test_runs"] = 0
    if data.get("successfulTestRuns") is not None:
        out["successful_test_runs"] = data["successfulTestRuns"]
    else:
        out["successful_test_runs"] = 0
    if data.get("creationTime") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["creation_time"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
