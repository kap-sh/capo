"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#HealthStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.generic_time_stamp
    import capo_bcm_dashboards.types.health_status_code
    import capo_bcm_dashboards.types.status_reason_list


class HealthStatus(TypedDict, closed=True):
    status_code: "capo_bcm_dashboards.types.health_status_code.HealthStatusCode"
    """<p>The health status code. <code>HEALTHY</code> indicates the scheduled report is configured properly and has all required permissions to execute. <code>UNHEALTHY</code> indicates the scheduled report is unable to deliver the notification to the default Amazon EventBridge EventBus in your account and your action is needed. The reason for the unhealthy state is captured in the health status reasons.</p>"""
    last_refreshed_at: NotRequired[
        "capo_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    ]
    """<p>The timestamp when the health status was last refreshed.</p>"""
    status_reasons: NotRequired[
        "capo_bcm_dashboards.types.status_reason_list.StatusReasonList"
    ]
    """<p>The list of reasons for the current health status. Only present when the status is <code>UNHEALTHY</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HealthStatus) -> dict:
    out: dict = {}
    import capo_bcm_dashboards.types.health_status_code

    out["statusCode"] = (
        capo_bcm_dashboards.types.health_status_code.serialize_aws_json_1_0(
            value["status_code"]
        )
    )
    if "last_refreshed_at" in value:
        import capo_bcm_dashboards.types.generic_time_stamp

        out["lastRefreshedAt"] = (
            capo_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
                value["last_refreshed_at"]
            )
        )
    if "status_reasons" in value:
        import capo_bcm_dashboards.types.status_reason_list

        out["statusReasons"] = (
            capo_bcm_dashboards.types.status_reason_list.serialize_aws_json_1_0(
                value["status_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> HealthStatus:
    out: HealthStatus = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        import capo_bcm_dashboards.types.health_status_code

        out["status_code"] = (
            capo_bcm_dashboards.types.health_status_code.deserialize_aws_json_1_0(
                data["statusCode"]
            )
        )
    else:
        import typing

        out["status_code"] = typing.cast(
            "capo_bcm_dashboards.types.health_status_code.HealthStatusCode", ""
        )
    if data.get("lastRefreshedAt") is not None:
        import capo_bcm_dashboards.types.generic_time_stamp

        out["last_refreshed_at"] = (
            capo_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["lastRefreshedAt"]
            )
        )
    if data.get("statusReasons") is not None:
        import capo_bcm_dashboards.types.status_reason_list

        out["status_reasons"] = (
            capo_bcm_dashboards.types.status_reason_list.deserialize_aws_json_1_0(
                data["statusReasons"]
            )
        )
    return out
