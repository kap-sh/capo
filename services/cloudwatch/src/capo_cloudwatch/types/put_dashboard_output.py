"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutDashboardOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dashboard_validation_messages


class PutDashboardOutput(TypedDict, closed=True):
    dashboard_validation_messages: NotRequired[
        "capo_cloudwatch.types.dashboard_validation_messages.DashboardValidationMessages"
    ]
    """<p>If the input for <code>PutDashboard</code> was correct and the dashboard was successfully created or modified, this result is empty.</p> <p>If this result includes only warning messages, then the input was valid enough for the dashboard to be created or modified, but some elements of the dashboard might not render.</p> <p>If this result includes error messages, the input was not valid and the operation failed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutDashboardOutput) -> dict:
    out: dict = {}
    if "dashboard_validation_messages" in value:
        import capo_cloudwatch.types.dashboard_validation_messages

        out["DashboardValidationMessages"] = (
            capo_cloudwatch.types.dashboard_validation_messages.serialize_aws_json_1_0(
                value["dashboard_validation_messages"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutDashboardOutput:
    out: PutDashboardOutput = {}  # type: ignore[typeddict-item]
    if data.get("DashboardValidationMessages") is not None:
        import capo_cloudwatch.types.dashboard_validation_messages

        out["dashboard_validation_messages"] = (
            capo_cloudwatch.types.dashboard_validation_messages.deserialize_aws_json_1_0(
                data["DashboardValidationMessages"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutDashboardOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dashboard_validation_messages" in value:
        import capo_cloudwatch.types.dashboard_validation_messages

        capo_cloudwatch.types.dashboard_validation_messages.serialize_query(
            value["dashboard_validation_messages"],
            pairs,
            f"{key_prefix}DashboardValidationMessages",
        )


def deserialize_query(el: Element) -> PutDashboardOutput:
    out: PutDashboardOutput = {}  # type: ignore[typeddict-item]
    child_dashboard_validation_messages = el.find("DashboardValidationMessages")
    if child_dashboard_validation_messages is not None:
        import capo_cloudwatch.types.dashboard_validation_messages

        out["dashboard_validation_messages"] = (
            capo_cloudwatch.types.dashboard_validation_messages.deserialize_query(
                child_dashboard_validation_messages
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutDashboardOutput) -> dict:
    out: dict = {}
    if "dashboard_validation_messages" in value:
        import capo_cloudwatch.types.dashboard_validation_messages

        out["DashboardValidationMessages"] = (
            capo_cloudwatch.types.dashboard_validation_messages.serialize_cbor(
                value["dashboard_validation_messages"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PutDashboardOutput:
    out: PutDashboardOutput = {}  # type: ignore[typeddict-item]
    if data.get("DashboardValidationMessages") is not None:
        import capo_cloudwatch.types.dashboard_validation_messages

        out["dashboard_validation_messages"] = (
            capo_cloudwatch.types.dashboard_validation_messages.deserialize_cbor(
                data["DashboardValidationMessages"]
            )
        )
    return out
