"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.account_targeting
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.service_owned_arn
    import capo_resiliencehubv2.types.test_run_id
    import capo_resiliencehubv2.types.test_run_status


class TestRunSummary(TypedDict, closed=True):
    test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId"
    """<p>The unique identifier of the test run.</p>"""
    status: "capo_resiliencehubv2.types.test_run_status.TestRunStatus"
    """<p>The current status of the test run.</p>"""
    started_at: "datetime.datetime"
    """<p>The timestamp when the test run started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the test run ended.</p>"""
    test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn"
    """<p>The ARN of the test template the test run was based on.</p>"""
    service_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    """<p>The ARN of the service the test run belongs to.</p>"""
    error_message: NotRequired["str"]
    """<p>A human-readable reason for test run failure. Only present when the status is FAILED or ERROR.</p>"""
    account_targeting: NotRequired[
        "capo_resiliencehubv2.types.account_targeting.AccountTargeting"
    ]
    """<p>Indicates whether the test run targets resources in a single AWS account or across multiple accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSummary) -> dict:
    out: dict = {}
    out["testRunId"] = value["test_run_id"]
    import capo_resiliencehubv2.types.test_run_status

    out["status"] = capo_resiliencehubv2.types.test_run_status.serialize_json(
        value["status"]
    )
    import capo_resiliencehubv2.types._prelude.timestamp

    out["startedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["started_at"]
    )
    if "ended_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["endedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    out["testTemplateArn"] = value["test_template_arn"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "account_targeting" in value:
        import capo_resiliencehubv2.types.account_targeting

        out["accountTargeting"] = (
            capo_resiliencehubv2.types.account_targeting.serialize_json(
                value["account_targeting"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestRunSummary:
    out: TestRunSummary = {}  # type: ignore[typeddict-item]
    if data.get("testRunId") is not None:
        out["test_run_id"] = data["testRunId"]
    else:
        out["test_run_id"] = ""
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.test_run_status

        out["status"] = capo_resiliencehubv2.types.test_run_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_resiliencehubv2.types.test_run_status.TestRunStatus", ""
        )
    if data.get("startedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["started_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["startedAt"]
            )
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["ended_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["endedAt"]
            )
        )
    if data.get("testTemplateArn") is not None:
        out["test_template_arn"] = data["testTemplateArn"]
    else:
        out["test_template_arn"] = ""
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("accountTargeting") is not None:
        import capo_resiliencehubv2.types.account_targeting

        out["account_targeting"] = (
            capo_resiliencehubv2.types.account_targeting.deserialize_json(
                data["accountTargeting"]
            )
        )
    return out
